# resume-tailor

A Claude Code and Antigravity skill that tailors your LaTeX resume to a job description and compiles it to a ready-to-send PDF — without fabricating experience.

Given a job description, it:
- Reorders and rephrases bullet points to surface the most relevant experience
- Emphasizes keywords and tools that match the JD
- Outputs `<First>-<Last>-<Company>.pdf` (e.g. `Jane-Doe-Google.pdf`)
- Leaves `default-resume.tex` untouched

---

## Prerequisites

### LaTeX
- **macOS**: `brew install --cask mactex` or `brew install basictex`
- **Linux**: `sudo apt install texlive-full`
- **Windows**: Install via terminal with `winget install MiKTeX.MiKTeX`, then restart your shell (adds `pdflatex` to PATH automatically). Alternatively, download the installer from [miktex.org/download](https://miktex.org/download).

### Python 3.9+
Already required to run `compile_latex.py`.

---

## Install in Claude Code

Skills must be installed as a **directory** containing a `SKILL.md` file inside `~/.claude/skills/`.

1. Clone this repo and navigate into it:
   ```bash
   git clone <repo-url>
   cd resume-skill
   ```

2. Copy the skill directory into your global Claude skills directory:
   ```bash
   cp -r .claude/skills/tailor-resume ~/.claude/skills/
   ```
   Or into a specific project's `.claude/skills/` to scope it to that project:
   ```bash
   cp -r .claude/skills/tailor-resume /path/to/project/.claude/skills/
   ```

3. Open Claude Code:
   ```bash
   claude
   ```

4. Invoke the skill:
   ```
   /tailor-resume Software Engineer at Google. Requirements: Go, distributed systems, Kubernetes, CI/CD...
   ```

Claude will tailor the resume and compile `Jane-Doe-Google.pdf` in the current directory.

---

## Install in Antigravity (CLI & IDE)

Antigravity automatically discovers skills structured as a directory containing a `SKILL.md` file.

1. Clone this repo and navigate into it:
   ```bash
   git clone <repo-url>
   cd resume-skill
   ```

2. Choose your installation scope:

   - **Workspace-specific (Automatic)**:
     This repository includes the skill under `.agents/skills/tailor-resume/`. When you open Antigravity inside this repository, the skill is automatically discovered and active—no copying needed.
     *(To use in another workspace, copy `.agents/skills/tailor-resume/` into that project's `.agents/skills/` directory).*

   - **Global for Antigravity CLI (`agy`)**:
     ```bash
     # macOS / Linux
     cp -r .agents/skills/tailor-resume ~/.gemini/antigravity-cli/skills/

     # Windows (PowerShell)
     Copy-Item -Recurse .agents\skills\tailor-resume ~/.gemini/antigravity-cli/skills\
     ```

   - **Global for Antigravity 2.0 / IDE**:
     ```bash
     # macOS / Linux
     cp -r .agents/skills/tailor-resume ~/.gemini/config/skills/

     # Windows (PowerShell)
     Copy-Item -Recurse .agents\skills\tailor-resume ~/.gemini/config/skills\
     ```

3. Open Antigravity:
   ```bash
   agy
   ```

4. Invoke the skill:
   - Use the slash command in the interactive prompt:
     ```
     /tailor-resume Software Engineer at Google. Requirements: Go, distributed systems, Kubernetes, CI/CD...
     ```
   - Or ask the agent naturally:
     ```
     Tailor my resume for this job description: Software Engineer at Google...
     ```

---

## How it works

The skill tells the harness's model to:

1. Read `default-resume.tex`
2. Produce a tailored version matching the JD keywords (no fabrication — see rules below)
3. Write it to a temp `_tailored_resume.tex`
4. Run `python "<SKILL_BASE_DIR>/compile_latex.py" _tailored_resume.tex "<Name> <Company>.pdf"`
5. Delete the temp file
6. Report the output PDF path

No external API calls. The harness model does the tailoring natively.

---

## Rules the model follows

**Will do:**
- Reorder bullet points within a role to lead with the most relevant ones
- Adjust phrasing / swap synonyms to match JD keywords where experience genuinely supports it
- Add `\textbf{}` emphasis to tools/skills already in the resume that the JD highlights
- Reorder Technical Skills to lead with the JD's stack

**Will not do:**
- Invent experience, projects, metrics, or dates
- Add new bullet points or sections
- Remove existing content
- Change name, contact info, education, GPA, or dates
- Alter the LaTeX preamble or document structure

---

## Files

| File | Purpose |
|------|---------|
| `default-resume.tex` | Base resume template — never modified by the skill |
| `.claude/skills/tailor-resume/` | Claude Code skill bundle (`SKILL.md` & `compile_latex.py`) |
| `.agents/skills/tailor-resume/` | Antigravity skill bundle (`SKILL.md` & `compile_latex.py`) |
