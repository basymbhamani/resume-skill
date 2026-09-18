---
name: tailor-resume
version: 1.0.0
description: |
  Tailors default-resume.tex to a job description and compiles a PDF named
  First-Last-Company.pdf. Reorders and rephrases bullet points to match JD
  keywords without fabricating any experience.
license: MIT
compatibility: claude-code
allowed-tools:
  - Read
  - Write
  - Bash
---

# tailor-resume

Tailors `default-resume.tex` to a job description and compiles it to a PDF named `<First>-<Last>-<Company>.pdf`.

## Usage

```
/tailor-resume <job description text>
```

Paste the full job posting inline after the command.

## Instructions

When invoked, follow these steps exactly:

### Step 1 — Read the base resume

Read the file `default-resume.tex` in the current working directory.

### Step 2 — Tailor the LaTeX

Produce a modified version of the `.tex` file that better matches the job description. Rules:

**You MAY:**
- Reorder bullet points within a role to surface the most relevant ones first
- Adjust phrasing or swap synonyms to match keywords from the JD where the underlying experience genuinely supports it
- Add `\textbf{}` around tools or skills already in the resume that the JD emphasizes
- Reorder items in the Technical Skills section to lead with the JD's stack

**You MUST NOT:**
- Invent, fabricate, or add any experience, projects, roles, metrics, or dates not already in the resume
- Add new bullet points, new sections, or new projects
- Remove existing bullet points or sections
- Change the candidate's name, contact information, education institution, GPA, degree, or any dates
- Alter the LaTeX preamble, document structure, or custom command definitions

**One-page requirement:**
The tailored resume MUST fit on exactly one page with nothing cut off. After writing `_tailored_resume.tex`, compile it and verify with `pdfinfo` that `Pages: 1`. If it spills to 2 pages, reduce the font size (e.g. `11pt` → `10pt` in `\documentclass`) and/or tighten vertical spacing (`\topmargin`, `\textheight`, `\vspace` values) until it fits — do not remove content.

### Step 3 — Parse the company name

Extract the hiring company's name from the job description (the employer, not a recruiter or job board). Sanitize it: remove characters that are illegal in filenames (`\ / * ? : " < > |`).

### Step 4 — Write the temp file

Write the tailored LaTeX to a temporary file named `_tailored_resume.tex` in the current working directory.

### Step 5 — Compile to PDF

Run:
```bash
python "<SKILL_BASE_DIR>/compile_latex.py" _tailored_resume.tex "<First>-<Last>-<Company>.pdf"
```

Where:
- `<SKILL_BASE_DIR>` is the base directory shown at the top of this skill (the `Base directory:` line in the invocation context — e.g. `C:\Users\you\.claude\skills\tailor-resume`)
- `<First>` and `<Last>` are the candidate's name from the resume
- `<Company>` is the sanitized company name from Step 3

### Step 6 — Delete the temp file

Delete `_tailored_resume.tex`.

### Step 7 — Confirm

Tell the user the output PDF path. Confirm that `default-resume.tex` was not modified.

## Requirements

- Python 3.9+
- `pdflatex` on PATH (TeX Live or MiKTeX)
