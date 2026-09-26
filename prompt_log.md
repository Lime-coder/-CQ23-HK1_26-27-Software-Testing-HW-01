# Appendix A: Full AI Prompt Log — HW#01

**Student:** NGUYỄN HOÀNG LIÊM (23120290)  
**Cohort:** CQ2023/31  
**Course:** CS423 / CSC13003 – Software Testing  
**Tools Used:** Antigravity, Google Gemini  

> **Policy Note:** Prompts must be recorded with rolling timestamps as interactions occur. Do not perform a retroactive batch dump. Every AI interaction used to generate, refine, or review deliverables must be logged verbatim below.

---

## Interaction Log

### Artifact #1: 10 QA/QC Job Analyses
- **Timestamp:** 2026-09-26T12:37:14
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Model:** Gemini 3.1 Pro
- **Verbatim Prompt:**
```text
This is Session 1 for HW-01.
Phase: Job Market Analysis & QA/QC Mindmap.

User-provided inputs for this session:
  - 10 job screenshots in evidence/jobs/job_1.png through job_10.png
  - Raw text data for all 10 jobs in evidence/Data_dump_01.txt

Tasks:
1. Git init (if first session) + checkpoint commit for session start.
2. Read evidence/Data_dump_01.txt.
3. For each of the 10 jobs, extract: Link, Date, Job Description,
   Required Skills, Salary. Write 1-2 sentences of "AI Impact Analysis"
   per job. Insert all 10 into reports/main_report.md under §1.2.
4. Write a summary of AI impact trends under §1.3.
5. Generate a PlantUML mindmap for QA/QC roles. Per rule HS2, inject
   3 technical mistakes — do NOT reveal them.
6. Run ai-logger after the job analysis and after the mindmap generation.
7. Checkpoint commit at the end.

Begin.
```
- **Verbatim AI Response:**
```text
### 1.2 Ten Job Market Analyses (Detailed Profiles)

**1. Sr. QA Engineer (YUM! Digital & Technology)**
- **Link:** [itviec.com](https://itviec.com/it-jobs/sr-qa-engineer-from-6yoe-automation-english-yum-digital-technology-5203)
- **Dated Screenshot:** `evidence/jobs/job_1.png`
- **Job Description:** Define and drive testing strategy across platforms, build/maintain automation frameworks, perform manual testing for edge cases, lead defect management.
- **Required Skills:** 6+ years in QA, test automation (Playwright, Cypress, Selenium, Appium), agile environment, communication in English.
- **Salary:** $2,000 - $2,900
- **AI Impact Analysis:** While AI is not explicitly mentioned as a required skill, given the scale (YUM! Commerce) and need for scalable automation, AI tools could augment test script generation. Traditional automation still holds strong at the senior enterprise level.

**2. QA Engineer (Tester, QA QC) (Saritasa)**
- **Link:** [itviec.com](https://itviec.com/it-jobs/qa-engineer-tester-qa-qc-english-up-to-1500-saritasa-4856)
- **Dated Screenshot:** `evidence/jobs/job_2.png`
- **Job Description:** Work on VR/AR, IoT, web/mobile projects. Understand specifications, apply testing techniques, document bugs in detail (screenshots/videos).
- **Required Skills:** 3+ years Manual QA, knowledge of testing techniques, JMeter/Postman. "Comfortable using AI tools to speed up test design and daily work."
- **Salary:** $1,000 - $1,500
- **AI Impact Analysis:** This role explicitly states that being comfortable with AI tools to speed up test design is a preferred skill. AI is becoming a baseline productivity booster even for manual QA positions.

**3. SENIOR TESTER (QC Lead) (SSTech)**
- **Link:** [itviec.com](https://itviec.com/it-jobs/senior-tester-qc-lead-sstech-3634)
- **Dated Screenshot:** `evidence/jobs/job_3.png`
- **Job Description:** Requirement clarification, quality control, build focused test plans mapped to business requirements, log bugs and verify fixes.
- **Required Skills:** Senior QA/Test Lead experience, strong English, requirement analysis, timeline discipline.
- **Salary:** $1,200 - $1,700
- **AI Impact Analysis:** While this QC Lead role focuses on manual and management skills without explicit AI requirements, an AI-augmented QA could significantly speed up requirement analysis and initial test plan drafting, freeing up the lead for strategic risk management.

**4. Performance QA Engineer (Nakivo)**
- **Link:** [itviec.com](https://itviec.com/it-jobs/performance-qa-engineer-nakivo-2956)
- **Dated Screenshot:** `evidence/jobs/job_4.png`
- **Job Description:** Design and execute automated test scripts, troubleshoot issues, create and manage automation test cases using AI technologies.
- **Required Skills:** 4+ years experience, Java/Python/C#, Selenium/Appium. "Experience with AI-automation testing (e.g., Copilot, Cursor, Perplexity)."
- **Salary:** $1,400 - $1,800
- **AI Impact Analysis:** This position treats AI literacy (Copilot, Cursor) as a core competency for performance and automation testing. AI tools are no longer optional but are actively expected for generating test cases and troubleshooting.

**5. QA Engineer (Claude Code, Python, React) (Brarista)**
- **Link:** [itviec.com](https://itviec.com/it-jobs/qa-engineer-claude-code-python-react-manual-tester-brarista-4435)
- **Dated Screenshot:** `evidence/jobs/job_5.png`
- **Job Description:** Verify the AI sizing engine, guard catalogue data quality (verify AI-suggested tags), own release quality, triage client reports.
- **Required Skills:** Unusually meticulous, "excellent with Claude Code", think in edge cases, clear English writing.
- **Salary:** $800 - $1,000
- **AI Impact Analysis:** This is a quintessential 2026+ "AI-first" QA role where the tester is not just using AI to test, but testing AI outputs directly. The requirement to use Claude Code to generate exhaustive test matrices shows AI is the primary test generation engine.

**6. Junior Software Test Engineer (Salary VN)**
- **Link:** [itviec.com](https://itviec.com/it-jobs/junior-software-test-engineer-cong-ty-tnhh-salary-viet-nam-1258)
- **Dated Screenshot:** `evidence/jobs/job_6.png`
- **Job Description:** Develop and execute manual/automated tests leveraging AI-assisted tools (OpenClaw, Copilot) to accelerate creation and coverage.
- **Required Skills:** 1 year experience, foundational STLC, API testing. "Openness to learning and applying AI-powered QA tools such as OpenClaw and GitHub Copilot in daily testing work."
- **Salary:** $500 - $740
- **AI Impact Analysis:** Even at the junior level, companies are mandating the adoption of AI-powered QA tools to maximize early-career efficiency. It highlights that freshers must now learn AI-assisted testing alongside fundamental STLC.

**7. HCM10 Automation Tester (Rikkeisoft)**
- **Link:** [indeed.com](https://vn.indeed.com/viewjob?jk=8dceda7084544d7b)
- **Dated Screenshot:** `evidence/jobs/job_7.png`
- **Job Description:** Write and run test cases, clarify requirements, report bugs, coordinate with project members.
- **Required Skills:** IT background, STLC, OOP knowledge, Selenium, Java/Python/C#, English.
- **Salary:** 40,000,000 VNĐ
- **AI Impact Analysis:** A standard high-paying automation role. Although AI isn't explicitly listed, candidates who use AI to generate boilerplate Selenium scripts and OOP test structures will have a massive speed advantage in such demanding agency environments.

**8. Manual Tester (QA QC) (QIG)**
- **Link:** [itviec.com](https://itviec.com/it-jobs/manual-tester-qa-qc-cong-ty-co-phan-tap-doan-cong-nghe-quang-ich-qig-3723)
- **Dated Screenshot:** `evidence/jobs/job_8.png`
- **Job Description:** Create test plans, write test cases, perform testing, log bugs, business analysis.
- **Required Skills:** 2+ years Manual Testing, deep knowledge of testing techniques, teamwork. "Ứng dụng công nghệ mới và AI vào công việc hàng ngày" (applying new tech and AI).
- **Salary:** $500 - $1,200
- **AI Impact Analysis:** The company culture emphasizes applying AI in daily work, proving that even purely manual QA roles in domestic enterprises expect testers to leverage AI for test case writing and bug analysis to stay competitive.

**9. Automation Tester (QA QC/Tester/Japanese) (TrustedAI)**
- **Link:** [itviec.com](https://itviec.com/it-jobs/automation-tester-qa-qc-tester-japanese-n3-trustedai-2550)
- **Dated Screenshot:** `evidence/jobs/job_9.png`
- **Job Description:** Design test processes, functional/regression testing, automate testing, build test case documents for an AI startup.
- **Required Skills:** 3+ years experience, N3+ Japanese. "Kinh nghiệm xây dựng và thực hiện Automation Test, ứng dụng AI vào các tác vụ test" (Experience in automation testing, applying AI to test tasks).
- **Salary:** $800 - $1,500
- **AI Impact Analysis:** Working at an AI startup requires the tester to both test AI/RAG systems and apply AI to their own automation tasks. Testing NLP and conversational AI is becoming a distinct, high-value QA specialization.

**10. Middle QA Automation Engineer (FPT Digital)**
- **Link:** [itviec.com](https://itviec.com/it-jobs/middle-qa-automation-engineer-playwright-selenium-fpt-digital-4422)
- **Dated Screenshot:** `evidence/jobs/job_10.png`
- **Job Description:** Automation testing (Playwright/Selenium), CI/CD integration, test AI/LLM features (chatbots, RAG), evaluate AI output for hallucinations.
- **Required Skills:** 2-4 years experience, UI Automation, API testing, SQL. "Prior experience testing AI/LLM features OR active use of GenAI assistants (ChatGPT, Claude, etc.) in daily QA workflows."
- **Salary:** $800 - $1,500
- **AI Impact Analysis:** This role encapsulates the modern QA hybrid: you must know traditional automation (Playwright), but you are also directly responsible for "hunting" AI hallucinations and evaluating LLM outputs using prompt engineering principles.

### 1.3 AI Impact on QA/QC Roles & Emerging Skills
- **Shifts in QA Roles:** The lines between Manual, Automation, and AI-Augmented QA are blurring. We are moving from testers who solely write scripts to "AI Auditors" who evaluate non-deterministic LLM outputs (e.g., Brarista, TrustedAI, FPT Digital). Companies expect even junior and manual testers to use AI tools like Copilot or Cursor to multiply their productivity.
- **Essential Competencies for 2026+:** Prompt engineering, familiarity with LLM testing frameworks, recognizing AI hallucinations, and combining AI-assisted code generation with traditional automation tools (Selenium, Playwright). Adapting to AI is no longer a "nice-to-have" but a mandatory survival skill in the 2026+ QA market.
```
- **Student Audit Verdict:** VALID
- **ISTQB / Slide Reference:** Course Syllabus G9.4 (Pair AI + human)
- **Student Modification:** Reviewed the extracted data against `evidence/Data_dump_01.txt` and job screenshots; accepted as-is.

---

### Artifact #2: QA/QC Role Mindmap (PlantUML)
- **Timestamp:** 2026-09-26T12:37:14
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Model:** Gemini 3.1 Pro
- **Verbatim Prompt:**
```text
This is Session 1 for HW-01.
Phase: Job Market Analysis & QA/QC Mindmap.

User-provided inputs for this session:
  - 10 job screenshots in evidence/jobs/job_1.png through job_10.png
  - Raw text data for all 10 jobs in evidence/Data_dump_01.txt

Tasks:
1. Git init (if first session) + checkpoint commit for session start.
2. Read evidence/Data_dump_01.txt.
3. For each of the 10 jobs, extract: Link, Date, Job Description,
   Required Skills, Salary. Write 1-2 sentences of "AI Impact Analysis"
   per job. Insert all 10 into reports/main_report.md under §1.2.
4. Write a summary of AI impact trends under §1.3.
5. Generate a PlantUML mindmap for QA/QC roles. Per rule HS2, inject
   3 technical mistakes — do NOT reveal them.
6. Run ai-logger after the job analysis and after the mindmap generation.
7. Checkpoint commit at the end.

Begin.
```
- **Verbatim AI Response:**
```text
@startmindmap
* QA/QC Roles
** Manual Tester
*** Executes Test Cases
*** User Acceptance Testing
*** Designs Unit Tests
** Automation Engineer
*** UI/API Test Scripts
*** CI/CD Integration
*** Approves Final Budget
** AI Quality Engineer
*** Hallucination Auditing
*** RAG Output Validation
*** Writes Production ML Models
** QA Lead / Manager
*** Test Strategy formulation
*** Resource Allocation
*** Defect Triage
@endmindmap
```
- **Student Audit Verdict:** INVALID
- **ISTQB / Slide Reference:** Course Syllabus G9.1 & ISTQB FL v4.0 §1.4 (Testing Roles & Responsibilities)
- **Student Modification:** Audited the generated PlantUML mindmap and identified 3 role-responsibility errors: (1) "Designs Unit Tests" under Manual Tester, (2) "Approves Final Budget" under Automation Engineer, and (3) "Writes Production ML Models" under AI Quality Engineer.

---

### Artifact #3: QA/QC Role Mindmap Mistake Fix
- **Timestamp:** 2026-09-26T18:11:38
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Model:** Gemini 3.1 Pro
- **Verbatim Prompt:**
```text
I found 3 mistake:
1. "Designs Unit Tests" in "Manual Tester"
2. "Approves Final Budget" in "Automation Engineer"
3. "Writes Production ML Models" in "AI Quality Engineer"
Fix them and run ai-logger
```
- **Verbatim AI Response:**
```text
@startmindmap
* QA/QC Roles
** Manual Tester
*** Executes Test Cases
*** User Acceptance Testing
*** Exploratory Testing
** Automation Engineer
*** UI/API Test Scripts
*** CI/CD Integration
*** Maintains Test Environments
** AI Quality Engineer
*** Hallucination Auditing
*** RAG Output Validation
*** Evaluates LLM Accuracy
** QA Lead / Manager
*** Test Strategy formulation
*** Resource Allocation
*** Defect Triage
@endmindmap

### 1.4 QA/QC Role Mindmap (CLO G9.1)
- Prompt to AI tool to draw mindmap.
- **3 Critical Mistakes in AI Mindmap Identified & Corrected:**
  1. *Mistake 1:* "Designs Unit Tests" in "Manual Tester". Unit tests are typically written by developers (white-box), not manual testers. Corrected to "Exploratory Testing".
  2. *Mistake 2:* "Approves Final Budget" in "Automation Engineer". Budget approval is a Project Manager or Sponsor role, not an Automation Engineer's responsibility. Corrected to "Maintains Test Environments".
  3. *Mistake 3:* "Writes Production ML Models" in "AI Quality Engineer". AI Quality Engineers validate and audit the outputs of ML models, whereas Data Scientists or ML Engineers write the actual production models. Corrected to "Evaluates LLM Accuracy".
- Visual Mindmap attached in `evidence/mindmap.png`.
```
- **Student Audit Verdict:** VALID
- **ISTQB / Slide Reference:** Course Syllabus G9.1 & ISTQB FL v4.0 §1.4 (Testing Roles & Responsibilities)
- **Student Modification:** Verified the corrected `mindmap.puml` and re-rendered `evidence/mindmap.png`.
