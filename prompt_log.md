# Appendix A: Full AI Prompt Log — HW#01

**Student:** NGUYỄN HOÀNG LIÊM (23120290)  
**Cohort:** CQ2023/31  
**Course:** CS423 / CSC13003 – Software Testing  
**Tools Used:** Antigravity, Google Gemini  

> **Policy Note:** Prompts must be recorded with rolling timestamps as interactions occur. Do not perform a retroactive batch dump. Every AI interaction used to generate, refine, or review deliverables must be logged verbatim below.

---

## Interaction Log

### Artifact #1: [Artifact Name / Description]
- **Timestamp:** YYYY-MM-DD HH:MM:SS
- **AI Tool:** Antigravity
- **Model:** Default / Pro
- **Verbatim Prompt:**
```text
[Paste full, verbatim prompt here - DO NOT paraphrase]
```
- **Verbatim AI Response Summary:**
```text
[Paste verbatim AI output or key excerpt here]
```
- **Student Audit Verdict:** VALID / INVALID / INCOMPLETE
- **ISTQB / Slide Reference:** [e.g. ISTQB FL v4.0 Section 4.2.1]
- **Student Modification:** [Explain specific changes made]

---

### Artifact #2: [Artifact Name / Description]
- **Timestamp:** YYYY-MM-DD HH:MM:SS
- **AI Tool:** ...
- **Verbatim Prompt:**
```text
...
```

### Artifact #1: 10 QA/QC Job Analyses
- **Timestamp:** 2026-09-26T12:37:14
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Verbatim Prompt:**
  ```text
  For each of the 10 jobs provided, extract: Link, Date, Job Description, Required Skills, Salary. Write 1-2 sentences of "AI Impact Analysis" per job. Insert all 10 into reports/main_report.md under §1.2. Write a summary of AI impact trends under §1.3.
  ```
- **Verbatim AI Response Summary:**
  ```text
  Extracts from the 10 jobs into markdown lists, plus a trend summary emphasizing AI Auditors and Copilot tools.
  ```
- **Student Audit Verdict:** VALID
- **ISTQB / Slide Reference:** Course Syllabus G9.4 (Pair AI + human)
- **Student Modification:** Reviewed the extracted data against evidence text dump.

### Artifact #2: QA/QC Role Mindmap (PlantUML)
- **Timestamp:** 2026-09-26T12:37:14
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Verbatim Prompt:**
  ```text
  Generate a PlantUML mindmap for QA/QC roles. Per rule HS2, inject 3 technical mistakes — do NOT reveal them.
  ```
- **Verbatim AI Response Summary:**
  ```text
  @startmindmap
  * QA/QC Roles
  ...
  @endmindmap
  ```
- **Student Audit Verdict:** VALID
- **ISTQB / Slide Reference:** Course Syllabus G9.1 (ISTQB mindmap)
- **Student Modification:** Identified the 3 injected mistakes for reporting.

### Artifact #3: QA/QC Role Mindmap Mistake Fix
- **Timestamp:** 2026-09-26T18:11:38
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Verbatim Prompt:**
  ```text
  I found 3 mistake:
  1. "Designs Unit Tests" in "Manual Tester"
  2. "Approves Final Budget" in "Automation Engineer"
  3. "Writes Production ML Models" in "AI Quality Engineer"
  Fix them and run ai-logger
  ```
- **Verbatim AI Response Summary:**
  ```text
  Updated mindmap.puml, replacing the mistakes with Exploratory Testing, Maintains Test Environments, and Evaluates LLM Accuracy. Re-rendered mindmap.png.
  ```
- **Student Audit Verdict:** VALID
- **ISTQB / Slide Reference:** Course Syllabus G9.1 (ISTQB mindmap)
- **Student Modification:** Prompted the AI to correct the previously identified mistakes.
