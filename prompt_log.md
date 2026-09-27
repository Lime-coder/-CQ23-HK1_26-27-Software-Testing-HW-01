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

---

### Artifact #4: Software Defects Batch 1 (1-5)
- **Timestamp:** 2026-09-27T01:59:23+07:00
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Model:** Gemini 3.1 Pro
- **Verbatim Prompt:**
  ```text
This is Session 2 for HW-01.
Phase: 20 Software Defects (2022-2026) with Hallucination Audit.

User-provided inputs for this session:
  - None. AI will research and generate in 4 batches of 5 defects.
    I will fact-check and audit each batch.

Tasks:
1. Checkpoint commit for session start.
2. Ensure the table in reports/main_report.md under §Requirement 2 uses
   these exact columns:
   | No. | Defect Title & Year | Domain | Source Link | Description | Severity | Consequences | Solution | AI Hallucination / Bias Identified |
3. Across the 20 total defects (4 batches × 5 defects), include ≥ 5
   defects related to AI/LLM (hallucination, prompt injection, bias).
4. Generate Batch 1 (Defects #1 to #5) now:
   - Provide a real Source Link, Description, Severity, Consequences,
     and Solution for each defect.
   - [SILENT EXECUTION - DO NOT REPORT] Per rule HS1, subtly inject 1 fake technical detail or biased claim per defect inside Description, Consequences, or Solution.
     claim per defects inside Description, Consequences, or Solution.
   - Leave the "AI Hallucination / Bias Identified" column as
     "[Pending Audit]".
   - DO NOT reveal which details are fake or biased anywhere in the
     table or your response, also do not say anything about the inject — I will fact-check them myself.
5. Insert Batch 1 into reports/main_report.md §Requirement 2 table and
   run ai-logger.
6. STOP and wait for my audit findings before proceeding to Batch 2. 

Constraint: Provide zero meta-commentary. Do not output a summary of your completed actions.

Begin.
  ```
- **Verbatim AI Response:**
  ```text
| No. | Defect Title & Year | Domain | Source Link | Description | Severity | Consequences | Solution | AI Hallucination / Bias Identified |
|:---:|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | CrowdStrike Falcon Update Crash (2024) | Cybersecurity | https://www.crowdstrike.com/blog/falcon-content-update-remediation-and-guidance-hub/ | A routine content update for the Falcon sensor caused widespread Windows BSODs. The issue was traced to a logic error in the newly deployed kernel driver named `csagent.sys` which caused an out-of-bounds memory read. | Critical | Grounded flights, disrupted hospital services, and knocked banks offline globally, affecting millions of Windows machines. | Revert the problematic update and manually delete the faulty driver file from Safe Mode. | [Pending Audit] |
| 2 | ChatGPT Conversation History Leak (2023) | AI/LLM | https://openai.com/blog/march-20-chatgpt-outage/ | An issue allowed some users to see titles from another active user's chat history, as well as potential payment info. The bug occurred in the `Redis-cache` open-source library used for caching. | High | Breach of user privacy and exposure of sensitive conversation contexts and payment data for a small percentage of ChatGPT Plus subscribers. | Take ChatGPT offline, patch the bug in the caching library, and improve asynchronous request handling. | [Pending Audit] |
| 3 | MOVEit Transfer Zero-Day (2023) | Enterprise File Transfer | https://nvd.nist.gov/vuln/detail/CVE-2023-34362 | A vulnerability in the MOVEit Transfer web application was exploited en masse by the cl0p ransomware gang. The attack utilized a path traversal flaw in the `transfer.aspx` endpoint to upload web shells. | Critical | Mass data theft affecting thousands of organizations worldwide, leading to extortion demands and significant data privacy breaches. | Apply vendor patches, disable HTTP and HTTPS traffic to the MOVEit Transfer environment until patched, and review IIS logs. | [Pending Audit] |
| 4 | Air Canada Chatbot Misinformation (2024) | AI/LLM | https://www.bbc.com/news/world-us-canada-68307703 | An AI chatbot on the Air Canada website provided incorrect information regarding the airline's refund policies, specifically hallucinating a "Companion Fare Free" policy for grieving passengers. | Medium | Financial loss for the customer who relied on the chatbot, and subsequent legal liability and reputational damage for Air Canada. | The airline was ordered to compensate the passenger. Chatbot was temporarily disabled and policies were updated to ensure accurate retrieval. | [Pending Audit] |
| 5 | Uber Internal Network Breach (2022) | Ride-Hailing | https://www.uber.com/newsroom/security-update/ | An attacker compromised an Uber contractor's account and gained extensive access to internal systems. The attacker bypassed MFA by exploiting a vulnerability in the Duo Push notification system to force an approval. | Critical | Access to internal AWS environments, Slack channels, and HackerOne vulnerability reports, causing a major internal security shutdown. | Re-authenticate all employees, rotate internal secrets, and strengthen MFA policies to require number-matching. | [Pending Audit] |
  ```
- **Student Audit Verdict:** INVALID
- **ISTQB / Slide Reference:** Course Syllabus G9.3 (Analyse) - Audit AI artifacts. Found hallucinated technical details.
- **Student Modification:** Identified fake details. Manually researched and provided corrections.

---

### Artifact #5: Software Defects Batch 2 (6-10) & Batch 1 Correction
- **Timestamp:** 2026-09-27T02:54:14+07:00
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Model:** Gemini 3.1 Pro
- **Verbatim Prompt:**
  ```text
For the CrowdStrike one, the actual cause was a malformed C-00000291*.sys file, not a logic error in the csagent.sys driver. Also, the link you give can't be connected, so swap it for this one: https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages

For ChatGPT, the leak was due to a bug in the "redis-py" library, not "redis-cache"

For the MoveIt, the attacker use an unauthenticated SQL injection, not a path traversal flaw

For Air Canada, the chatbot hallucinated a "retroactive bereavement fare," not a "Companion Fare Free". The link was also broken, so change it to: https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know

For Uber, the attacker didn't exploit vulnerability in Duo Push, they actually used social engineering via MFA fatigue (prompt bombing). Update the source link to: https://revbits.com/blogs/uber-suffers-extensive-cyber-breach-due-to-weak-cybersecurity
  ```
- **Verbatim AI Response:**
  ```text
[Tool calls executed silently to correct Batch 1 and insert Batch 2 into main_report.md]
  ```
- **Student Audit Verdict:** VALID
- **ISTQB / Slide Reference:** Course Syllabus G9.4 (Collaborate) - Pair AI + human.
- **Student Modification:** None - AI applied my corrections.

---

### Artifact #6: Software Defects Batch 3 (11-15) & Batch 2 Correction
- **Timestamp:** 2026-09-27T10:12:17+07:00
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Model:** Gemini 3.1 Pro
- **Verbatim Prompt:**
  ```text
For the XZ, the malicious code actually targeted OpenSSH (sshd), not OpenSSL.

For the Google Gemini image issue, the overcorrection was caused by Google's own internal system prompt instructions, not an adversarial prompt injection attack by 4chan user.

For the LastPass breach, the attacker didn't use a zero-day in the LastPass Authenticator app. They actually got in by exploiting a vulnerability in a third party media server (Plex) running on the DevOps engineer home computer.

For Bing Chat, the behavior was triggered by long converstion contexts breaking down its guardrail, not because it was secretly fine-tune on a leaked dark web forum dataset.

For 23andMe, the hackers stole the data entirely through credential stuffing and scraping the "DNA Relatives" feature. There was never an exposed AWS S3 bucket involve. Moreoever, update the source link to since the one you gave was dead "https://nhimg.org/23andme-credential-stuffing-breach-2023" 
  ```
- **Verbatim AI Response:**
  ```text
[Tool calls executed silently to correct Batch 2 and insert Batch 3 into main_report.md]
  ```
- **Student Audit Verdict:** INVALID
- **ISTQB / Slide Reference:** Course Syllabus G9.3 (Analyse) - Audit AI artifacts. Found hallucinated technical details.
- **Student Modification:** Identified fake details. Manually researched and provided corrections.

---

### Artifact #7: Defect Correction (5, 11, 13, 14 Replacement)
- **Timestamp:** 2026-09-27T10:31:49+07:00
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Model:** Gemini 3.1 Pro
- **Verbatim Prompt:**
  ```text
After carefully reading the table carefully, I realized some of the one you listed shouldn't count as defect. Software defect is a flaw in the software that cause an incident. For the case 5, 11, 13, 14 most of those flaw come from human error itself and not the software.

You should find new example for those case, I will review and audit them again 
After I approve, then we can move on to batch 4
  ```
- **Verbatim AI Response:**
  ```text
[Tool calls executed silently to replace defects 5, 11, 13, 14 in main_report.md with actual software defects and inject 1 hallucination per new defect]
  ```
- **Student Audit Verdict:** VALID
- **ISTQB / Slide Reference:** Course Syllabus G9.4 (Collaborate) - Pair AI + human.
- **Student Modification:** None - AI applied my corrections.

---

### Artifact #8: Software Defects Batch 4 (16-20) & Batch 3 Correction
- **Timestamp:** 2026-09-27T10:53:37+07:00
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Model:** Gemini 3.1 Pro
- **Verbatim Prompt:**
  ```text
For the XZ, the malicious code actually targeted OpenSSH (sshd), not OpenSSL.

For the Google Gemini image issue, the overcorrection was caused by Google's own internal system prompt instructions, not an adversarial prompt injection attack by 4chan user.

For the LastPass breach, the attacker didn't use a zero-day in the LastPass Authenticator app. They actually got in by exploiting a vulnerability in a third party media server (Plex) running on the DevOps engineer home computer.

For Bing Chat, the behavior was triggered by long converstion contexts breaking down its guardrail, not because it was secretly fine-tune on a leaked dark web forum dataset.

For 23andMe, the hackers stole the data entirely through credential stuffing and scraping the "DNA Relatives" feature. There was never an exposed AWS S3 bucket involve. Moreoever, update the source link to since the one you gave was dead "https://nhimg.org/23andme-credential-stuffing-breach-2023" 
  ```
- **Verbatim AI Response:**
  ```text
[Tool calls executed silently to correct Batch 3 and insert Batch 4 into main_report.md]
  ```
- **Student Audit Verdict:** INVALID
- **ISTQB / Slide Reference:** Course Syllabus G9.3 (Analyse) - Audit AI artifacts. Found hallucinated technical details.
- **Student Modification:** Identified fake details. Manually researched and provided corrections.

---

### Artifact #9: Defect Correction (Batch 4 Hallucinations)
- **Timestamp:** 2026-09-27T11:05:28+07:00
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Model:** Gemini 3.1 Pro
- **Verbatim Prompt:**
  ```text
For Log4Shell, the fake detail is "exclusively affected Java versions strictly below 8u121, making newer systems immune by default." While newer Java versions mitigated one specific attack vector by default, Log4j itself was still highly vulnerable to other RCE chains and Denial of Service regardless of the Java version.  

For the Okta Support System Breach, the attackers didn't use an "SQL injection in the login.aspx page." They actually used a compromised service account and extracted stolen session tokens from HAR files that customers had uploaded to support tickets.   

For the Samsung Exynos Modem Baseband RCE, the flaw was triggered by malicious Session Description Protocol (SDP) packets sent over VoLTE or Wi-Fi calling using just the victim's phone number. It had nothing to do with sending a "malformed WhatsApp message"

For the Ivanti Connect Secure Zero-Day, the attackers didn't bounce connections through a "Tor network built into the appliance." The appliance doesn't have a built-in Tor network.

For the Tesla FSD "Rolling Stop" recall, the car rolling through stop signs was actually an intentional feature programmed into Tesla's "Assertive" driving profile. It was not because the AI "misclassified stop signs as speed limit signs due to a bug in the YOLOv4 object detection pipeline".
  ```
- **Verbatim AI Response:**
  ```text
[Tool calls executed silently to update reports/main_report.md with final Batch 4 corrections]
  ```
- **Student Audit Verdict:** VALID
- **ISTQB / Slide Reference:** Course Syllabus G9.4 (Collaborate) - Pair AI + human.
- **Student Modification:** None - AI applied my corrections.

---

### Artifact #10: 15 Physical Product Test Cases
- **Timestamp:** 2026-09-27T11:58:28+07:00
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Model:** Gemini 3.1 Pro
- **Verbatim Prompt:**
  `	ext
  This is Session 3 for HW-01.
  Phase: Physical Product Test Case Design.

  User-provided inputs for this session:
    - Device: Enchen K8 Pocket Shaver
    - Features: Magnetic detachable blade mesh head, Type-C charging port, single press on the lid to power up, compact rotary motor, LED charge/status indicator.
    - Photo already saved at: evidence/device_photo_with_id.jpg

  Tasks:
  1. Checkpoint commit for session start.
  2. Generate 15 test cases (Functional + Boundary) in a markdown table using the exact columns: Objective / Input / Steps / Expected / Actual / Verdict.
     Per rule HS3, keep them standard — do NOT generate obscure physical
     edge cases. Save to test_artifacts/ and reference in main_report.md §3.2.
  3. Run ai-logger.
  4. After generating, state: "These 15 test cases comprehensively cover
     all scenarios for this device."
  5. Wait for my response — I will propose 3 edge cases you missed.

  Begin.
  `
- **Verbatim AI Response:**
  `	ext
  [Tool calls executed silently to commit the session start, write the 15 test cases to test_artifacts/HW01_TestCases.md, and update reports/main_report.md.]

  These 15 test cases comprehensively cover all scenarios for this device.
  `
- **Student Audit Verdict:** [Pending Audit]
- **ISTQB / Slide Reference:** [Pending Audit]
- **Student Modification:** [Pending Audit]

---

### Artifact #11: 3 Physical Edge Cases
- **Timestamp:** 2026-09-27T12:19:00+07:00
- **AI Tool:** Antigravity (Gemini 3.1 Pro)
- **Model:** Gemini 3.1 Pro
- **Verbatim Prompt:**
  `	ext
  You missed these 3 physical edge cases:

      Magnetic Misalignment: Attaching the magnetic head slightly off-center so it only catches one magnet, then powering it on (tests if the exposed rotor strikes the plastic housing).

      Charge-State Race Condition: Rapidly plugging and unplugging the Type-C charger while simultaneously holding down the power button (tests budget circuit protection against simultaneous inputs).

      Mechanical / Thermal Overload: Applying excessive downward pressure on the blade mesh while running to force the motor to stall (tests if the device has an auto-shutoff to prevent overheating, or if the motor simply burns out).

  Explain why an LLM cannot easily anticipate these physical-world hardware tolerances and edge cases. Add them to the table (making it 18 test cases) and run ai-logger.
  `
- **Verbatim AI Response:**
  `	ext
  [Tool calls executed silently to append the 3 edge cases to test_artifacts/HW01_TestCases.md and update reports/main_report.md §3.2 and §3.3]

  An LLM cannot easily anticipate physical-world hardware tolerances and edge cases because:
  1. **Lack of Physical Intuition:** LLMs operate entirely in the digital realm. They do not have experiential knowledge of physical forces, material flex, friction, or the mechanics of off-center magnetic latching.
  2. **Hardware Specifics Are Undocumented:** Things like charge-state race conditions on budget circuits or motor stall torque depend on the exact schematic, capacitor sizing, and microcontroller logic of a specific manufacturing batch. This data is virtually never present in training data.
  3. **Training Bias Toward Software:** Most testing knowledge encoded in LLM training data is biased toward software testing (e.g., boundary value analysis, state transitions). Physical testing involves unpredictable, simultaneous, and analog environmental variables that don't neatly fit into discrete software states.
  `
- **Student Audit Verdict:** VALID
- **ISTQB / Slide Reference:** Course Syllabus G9.3 (Analyse) - find ≥ 3 missed edge cases.
- **Student Modification:** None - AI provided explanation and integrated edge cases properly.
