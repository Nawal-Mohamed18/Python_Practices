const views = {
  home: document.getElementById("view-home"),
  path: document.getElementById("view-path"),
  quiz: document.getElementById("view-quiz"),
};

const careerSelect = document.getElementById("career-select");
const pathDetail = document.getElementById("path-detail");
const quizPanel = document.getElementById("quiz-panel");

let careers = {};
let questions = [];
let quizStep = 0;
let quizAnswers = [];
let selectedOption = null;

function showView(name) {
  Object.entries(views).forEach(([key, el]) => {
    const active = key === name;
    el.hidden = !active;
    el.classList.toggle("active", active);
  });
  if (name === "quiz") {
    quizStep = 0;
    quizAnswers = [];
    selectedOption = null;
    renderQuiz();
  }
  if (name === "path") {
    renderPathDetail();
  }
}

function renderCareerDetail(career, { intro } = {}) {
  const steps = career.path
    .map(
      (step, i) =>
        `<div class="step" style="animation-delay:${i * 40}ms"><strong>Step ${i + 1}.</strong> ${step}</div>`
    )
    .join("");

  return `
    ${intro ? `<div class="banner">${intro}</div>` : ""}
    <h2>${career.title}</h2>
    <p class="tagline">${career.tagline}</p>
    <p class="skills"><strong>Core skills</strong><br>${career.skills.join(" · ")}</p>
    <p><strong>Your path</strong></p>
    ${steps}
  `;
}

function renderPathDetail() {
  const key = careerSelect.value;
  const career = careers[key];
  if (!career) {
    pathDetail.innerHTML = "";
    return;
  }
  pathDetail.innerHTML = renderCareerDetail(career);
}

function renderQuiz() {
  if (quizStep >= questions.length) {
    submitQuiz();
    return;
  }

  const q = questions[quizStep];
  const pct = (quizStep / questions.length) * 100;
  const options = q.options
    .map(
      (opt, idx) =>
        `<button type="button" class="option${selectedOption === idx ? " selected" : ""}" data-idx="${idx}">${opt.label}</button>`
    )
    .join("");

  quizPanel.innerHTML = `
    <div class="progress" aria-hidden="true"><span style="width:${pct}%"></span></div>
    <p class="q-meta">Question ${quizStep + 1} of ${questions.length}</p>
    <p class="q-text">${q.text}</p>
    <div class="options">${options}</div>
    <div class="actions">
      <button type="button" class="btn" id="quiz-back" ${quizStep === 0 ? "disabled" : ""}>Back</button>
      <button type="button" class="btn primary" id="quiz-next" ${selectedOption === null ? "disabled" : ""}>Next</button>
    </div>
  `;

  quizPanel.querySelectorAll(".option").forEach((btn) => {
    btn.addEventListener("click", () => {
      selectedOption = Number(btn.dataset.idx);
      renderQuiz();
    });
  });

  document.getElementById("quiz-back").addEventListener("click", () => {
    if (quizStep === 0) return;
    quizStep -= 1;
    quizAnswers = quizAnswers.slice(0, quizStep);
    selectedOption = quizAnswers[quizStep] ?? null;
    renderQuiz();
  });

  document.getElementById("quiz-next").addEventListener("click", () => {
    if (selectedOption === null) return;
    quizAnswers[quizStep] = selectedOption;
    quizStep += 1;
    selectedOption = null;
    renderQuiz();
  });
}

async function submitQuiz() {
  quizPanel.innerHTML = `<p class="lede short">Finding your match…</p>`;
  const res = await fetch("/api/quiz", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ answers: quizAnswers }),
  });
  const data = await res.json();
  if (!res.ok) {
    quizPanel.innerHTML = `<p class="note">${data.error || "Something went wrong."}</p>`;
    return;
  }

  quizPanel.innerHTML =
    renderCareerDetail(data.best, {
      intro: `Best match: <strong>${data.best.title}</strong> (score ${data.best.score}).`,
    }) +
    `<p class="note"><strong>Also close:</strong> ${data.second.title} (score ${data.second.score}). You can open Path to a career to compare roadmaps.</p>
     <div class="actions" style="margin-top:1rem">
       <button type="button" class="btn primary" id="retake">Retake questions</button>
     </div>`;

  document.getElementById("retake").addEventListener("click", () => {
    quizStep = 0;
    quizAnswers = [];
    selectedOption = null;
    renderQuiz();
  });
}

document.querySelectorAll("[data-go]").forEach((el) => {
  el.addEventListener("click", () => showView(el.dataset.go));
});

careerSelect.addEventListener("change", renderPathDetail);

async function init() {
  const [careersRes, questionsRes] = await Promise.all([
    fetch("/api/careers"),
    fetch("/api/questions"),
  ]);
  careers = await careersRes.json();
  questions = await questionsRes.json();

  careerSelect.innerHTML = Object.entries(careers)
    .map(([key, c]) => `<option value="${key}">${c.title}</option>`)
    .join("");
}

init();
