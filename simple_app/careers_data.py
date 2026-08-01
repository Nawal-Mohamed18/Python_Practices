"""Career catalog, roadmaps, and quiz scoring for Career Path Finder."""

CAREERS = {
    "ai_engineer": {
        "title": "AI Engineer",
        "tagline": "Build models and ship intelligent products.",
        "skills": ["Python", "ML fundamentals", "Deep learning", "APIs", "MLOps basics"],
        "path": [
            "Learn Python deeply (data structures, OOP, scripting).",
            "Study math for ML: linear algebra, probability, calculus basics.",
            "Build classical ML projects (scikit-learn) and document them.",
            "Learn deep learning (PyTorch or TensorFlow) with 2–3 demos.",
            "Ship one end-to-end app: model + API + simple UI.",
            "Learn deployment basics (Docker, cloud, monitoring).",
            "Apply for AI/ML roles or freelance with a public portfolio.",
        ],
    },
    "software_engineer": {
        "title": "Software Engineer",
        "tagline": "Design, build, and maintain reliable software.",
        "skills": ["Programming", "Data structures", "Git", "APIs", "Testing"],
        "path": [
            "Pick one language and get solid (Python, JavaScript, or Java).",
            "Practice algorithms and data structures regularly.",
            "Learn Git, debugging, and how to read other people's code.",
            "Build full projects: CLI tools, web apps, or APIs.",
            "Study system design basics and clean architecture.",
            "Contribute to open source or ship a public product.",
            "Interview and land a junior/mid software role.",
        ],
    },
    "data_analyst": {
        "title": "Data Analyst",
        "tagline": "Turn data into clear decisions and stories.",
        "skills": ["SQL", "Excel/Sheets", "Visualization", "Statistics", "Communication"],
        "path": [
            "Master spreadsheets and basic statistics.",
            "Learn SQL for querying real datasets.",
            "Practice Python or R for analysis (pandas preferred).",
            "Build dashboards (Tableau, Power BI, or Streamlit).",
            "Complete 3 case studies with clear business insights.",
            "Learn storytelling: charts that answer a real question.",
            "Apply for analyst roles with a portfolio of insights.",
        ],
    },
    "ux_designer": {
        "title": "UX Designer",
        "tagline": "Shape products people can use without friction.",
        "skills": ["User research", "Wireframing", "Prototyping", "Visual design", "Usability testing"],
        "path": [
            "Learn UX fundamentals: users, flows, and usability heuristics.",
            "Practice wireframing and prototyping (Figma).",
            "Study visual design basics: hierarchy, spacing, typography.",
            "Run small user interviews and usability tests.",
            "Redesign 2–3 real apps and document your process.",
            "Build a case-study portfolio (problem → process → outcome).",
            "Apply for junior UX or product design roles.",
        ],
    },
    "product_manager": {
        "title": "Product Manager",
        "tagline": "Decide what to build and why it matters.",
        "skills": ["Prioritization", "User empathy", "Writing", "Analytics", "Stakeholder skills"],
        "path": [
            "Learn product thinking: problems, users, outcomes.",
            "Practice writing PRDs and clear problem statements.",
            "Study metrics, funnels, and basic analytics.",
            "Shadow or collaborate with eng/design on a real project.",
            "Ship a side project as owner (scope, launch, iterate).",
            "Learn roadmapping and stakeholder communication.",
            "Apply for APM/PM roles with proof of shipped decisions.",
        ],
    },
    "cybersecurity": {
        "title": "Cybersecurity Specialist",
        "tagline": "Protect systems, data, and people from threats.",
        "skills": ["Networking", "OS fundamentals", "Security tools", "Risk thinking", "Scripting"],
        "path": [
            "Learn networking and OS fundamentals (Linux + Windows).",
            "Study security basics: CIA triad, threats, common attacks.",
            "Practice in labs (TryHackMe, Hack The Box beginner paths).",
            "Learn scripting (Python/Bash) for automation and analysis.",
            "Earn one foundational cert if useful (e.g. Security+).",
            "Document write-ups of labs and small defensive projects.",
            "Apply for SOC analyst or junior security roles.",
        ],
    },
}

QUESTIONS = [
    {
        "id": "interest",
        "text": "What excites you most day to day?",
        "options": [
            {"label": "Building smart systems and models", "scores": {"ai_engineer": 3, "software_engineer": 1}},
            {"label": "Shipping reliable apps and features", "scores": {"software_engineer": 3, "product_manager": 1}},
            {"label": "Finding patterns and explaining data", "scores": {"data_analyst": 3, "ai_engineer": 1}},
            {"label": "Making products easy and beautiful to use", "scores": {"ux_designer": 3, "product_manager": 1}},
            {"label": "Deciding what to build and for whom", "scores": {"product_manager": 3, "ux_designer": 1}},
            {"label": "Defending systems and hunting risks", "scores": {"cybersecurity": 3, "software_engineer": 1}},
        ],
    },
    {
        "id": "work_style",
        "text": "How do you like to work?",
        "options": [
            {"label": "Deep focus on hard technical problems", "scores": {"ai_engineer": 2, "software_engineer": 2, "cybersecurity": 2}},
            {"label": "Mix of people, writing, and decisions", "scores": {"product_manager": 3, "ux_designer": 1}},
            {"label": "Visual craft and user empathy", "scores": {"ux_designer": 3}},
            {"label": "Clear analysis with measurable answers", "scores": {"data_analyst": 3, "ai_engineer": 1}},
        ],
    },
    {
        "id": "strength",
        "text": "Which strength feels most natural?",
        "options": [
            {"label": "Math / logic / experimentation", "scores": {"ai_engineer": 3, "data_analyst": 2}},
            {"label": "Coding and building systems", "scores": {"software_engineer": 3, "ai_engineer": 1, "cybersecurity": 1}},
            {"label": "Explaining insights simply", "scores": {"data_analyst": 3, "product_manager": 1}},
            {"label": "Designing flows and interfaces", "scores": {"ux_designer": 3}},
            {"label": "Prioritizing and aligning people", "scores": {"product_manager": 3}},
            {"label": "Careful investigation and vigilance", "scores": {"cybersecurity": 3}},
        ],
    },
    {
        "id": "goal",
        "text": "What outcome do you want in 2–3 years?",
        "options": [
            {"label": "Work on AI products or research-to-prod systems", "scores": {"ai_engineer": 3}},
            {"label": "Be a strong engineer on a product team", "scores": {"software_engineer": 3}},
            {"label": "Help companies decide with data", "scores": {"data_analyst": 3}},
            {"label": "Own the user experience of a product", "scores": {"ux_designer": 3}},
            {"label": "Own a product roadmap", "scores": {"product_manager": 3}},
            {"label": "Protect organizations from cyber threats", "scores": {"cybersecurity": 3}},
        ],
    },
]


def score_answers(selected_indices: list[int]) -> list[tuple[str, int]]:
    """Return career keys ranked by quiz score (highest first)."""
    totals = {key: 0 for key in CAREERS}
    for q, idx in zip(QUESTIONS, selected_indices):
        if idx is None or idx < 0 or idx >= len(q["options"]):
            continue
        for career, points in q["options"][idx]["scores"].items():
            totals[career] += points
    ranked = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    return ranked
