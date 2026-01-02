from typing import Dict, List

def h1(text: str) -> str:
    return f"# {text}\n"

def h2(text: str) -> str:
    return f"## {text}\n"

def bullet(items: List[str]) -> str:
    return "\n".join([f"- {i}" for i in items]) + ("\n" if items else "")

def section_headline(cfg: Dict) -> str:
    headline = cfg.get("headline")
    if not headline:
        return ""
    return h1(headline)

def section_badges(cfg: Dict) -> str:
    output = cfg.get("output", {})
    if not output.get("include_badges"):
        return ""
    badges = cfg.get("badges", [])
    if not badges:
        return ""
    lines = []
    for b in badges:
        label = b.get("label", "").strip()
        value = b.get("value", "").strip()
        if label and value:
            lines.append(f"**{label}:** {value}")
    return ("\n".join(lines) + "\n\n") if lines else ""

def section_skills(cfg: Dict) -> str:
    skills = cfg.get("skills", [])
    if not skills:
        return ""
    out = [h2("Skills")]
    for group in skills:
        name = group.get("group", "Skills")
        items = group.get("items", [])
        out.append(f"**{name}:**")
        out.append(bullet(items))
    return "\n".join(out) + "\n"

def section_projects(cfg: Dict) -> str:
    projects = cfg.get("projects", [])
    if not projects:
        return ""
    out = [h2("Projects")]
    for p in projects:
        name = p.get("name", "Project")
        desc = p.get("description", "")
        tags = p.get("tags", [])
        repo = p.get("repo", "")
        highlights = p.get("highlights", [])
        out.append(f"**Title:** {name}")
        if desc:
            out.append(f"**Summary:** {desc}")
        if tags:
            out.append(f"**Tags:** " + ", ".join(tags))
        if highlights:
            out.append("**Highlights:**")
            out.append(bullet(highlights))
        if repo:
            out.append(f"**Repository:** {repo}")
        out.append("")  # spacing
    return "\n".join(out) + "\n"

def section_highlights(cfg: Dict) -> str:
    highlights = cfg.get("highlights", [])
    if not highlights:
        return ""
    out = [h2("Highlights"), bullet(highlights)]
    return "\n".join(out) + "\n"

def render_markdown(cfg: Dict) -> str:
    title = cfg.get("output", {}).get("title", "Profile overview")
    parts = [
        section_headline(cfg),
        section_badges(cfg),
        h2(title),
        section_skills(cfg),
        section_projects(cfg),
        section_highlights(cfg),
    ]
    # keep only non-empty sections, separated by single newlines
    return "\n".join([p.strip() for p in parts if p.strip()]) + "\n"
