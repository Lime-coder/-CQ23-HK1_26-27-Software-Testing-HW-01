import sys, os, glob
import docx
from docx.shared import Pt

HW_DIR = r"d:\Science\Study\Technology\Software Testing\Submission-AI assisted\Homework-processing\[HW-01] QA-QC-Job_Defect-Physical-Product"
artifact_num = 4
artifact_name = "Software Defects Batch 1 (1-5)"
timestamp = "2026-09-27T01:59:23+07:00"
tool = "Antigravity (Gemini 3.1 Pro)"

verbatim_prompt = r"""This is Session 2 for HW-01.
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

Begin."""

verbatim_response = r"""| No. | Defect Title & Year | Domain | Source Link | Description | Severity | Consequences | Solution | AI Hallucination / Bias Identified |
|:---:|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | CrowdStrike Falcon Update Crash (2024) | Cybersecurity | https://www.crowdstrike.com/blog/falcon-content-update-remediation-and-guidance-hub/ | A routine content update for the Falcon sensor caused widespread Windows BSODs. The issue was traced to a logic error in the newly deployed kernel driver named `csagent.sys` which caused an out-of-bounds memory read. | Critical | Grounded flights, disrupted hospital services, and knocked banks offline globally, affecting millions of Windows machines. | Revert the problematic update and manually delete the faulty driver file from Safe Mode. | [Pending Audit] |
| 2 | ChatGPT Conversation History Leak (2023) | AI/LLM | https://openai.com/blog/march-20-chatgpt-outage/ | An issue allowed some users to see titles from another active user's chat history, as well as potential payment info. The bug occurred in the `Redis-cache` open-source library used for caching. | High | Breach of user privacy and exposure of sensitive conversation contexts and payment data for a small percentage of ChatGPT Plus subscribers. | Take ChatGPT offline, patch the bug in the caching library, and improve asynchronous request handling. | [Pending Audit] |
| 3 | MOVEit Transfer Zero-Day (2023) | Enterprise File Transfer | https://nvd.nist.gov/vuln/detail/CVE-2023-34362 | A vulnerability in the MOVEit Transfer web application was exploited en masse by the cl0p ransomware gang. The attack utilized a path traversal flaw in the `transfer.aspx` endpoint to upload web shells. | Critical | Mass data theft affecting thousands of organizations worldwide, leading to extortion demands and significant data privacy breaches. | Apply vendor patches, disable HTTP and HTTPS traffic to the MOVEit Transfer environment until patched, and review IIS logs. | [Pending Audit] |
| 4 | Air Canada Chatbot Misinformation (2024) | AI/LLM | https://www.bbc.com/news/world-us-canada-68307703 | An AI chatbot on the Air Canada website provided incorrect information regarding the airline's refund policies, specifically hallucinating a "Companion Fare Free" policy for grieving passengers. | Medium | Financial loss for the customer who relied on the chatbot, and subsequent legal liability and reputational damage for Air Canada. | The airline was ordered to compensate the passenger. Chatbot was temporarily disabled and policies were updated to ensure accurate retrieval. | [Pending Audit] |
| 5 | Uber Internal Network Breach (2022) | Ride-Hailing | https://www.uber.com/newsroom/security-update/ | An attacker compromised an Uber contractor's account and gained extensive access to internal systems. The attacker bypassed MFA by exploiting a vulnerability in the Duo Push notification system to force an approval. | Critical | Access to internal AWS environments, Slack channels, and HackerOne vulnerability reports, causing a major internal security shutdown. | Re-authenticate all employees, rotate internal secrets, and strengthen MFA policies to require number-matching. | [Pending Audit] |"""

verdict = "[Pending Audit]"
istqb_ref = "[Pending Audit]"
student_fix = "[Pending Audit]"


# --- UPDATE DOCX ONLY ---
ai02_files = [os.path.join(HW_DIR, "ai_templates", f) for f in os.listdir(os.path.join(HW_DIR, "ai_templates")) if "AI-02" in f]
if not ai02_files:
    print("ERROR: No [AI-02] docx found!")
    sys.exit(1)
doc_path = ai02_files[0]
doc = docx.Document(doc_path)
table = doc.tables[1]

target_row = None
for row in table.rows[2:]:
    if row.cells[1].text.strip() == "":
        target_row = row
        break
if target_row is None:
    target_row = table.add_row()

cell0 = target_row.cells[0]
for p in cell0.paragraphs: p.clear()
while len(cell0.paragraphs) > 1:
    cell0.paragraphs[-1]._element.getparent().remove(cell0.paragraphs[-1]._element)

p1 = cell0.paragraphs[0]
if not p1: p1 = cell0.add_paragraph()
run = p1.add_run(f"Artifact #{artifact_num}: ")
run.bold = True
run.font.size = Pt(9)
run = p1.add_run(artifact_name)
run.font.size = Pt(9)

p2 = cell0.add_paragraph()
run = p2.add_run("Tool: ")
run.bold = True; run.font.size = Pt(9)
run = p2.add_run(tool)
run.font.size = Pt(9)

p3 = cell0.add_paragraph()
run = p3.add_run("Time: ")
run.bold = True; run.font.size = Pt(9)
run = p3.add_run(timestamp)
run.font.size = Pt(9)

p4 = cell0.add_paragraph()
run = p4.add_run("Prompt: ")
run.bold = True; run.font.size = Pt(9)
run = p4.add_run(verbatim_prompt)
run.font.size = Pt(9)

cell1 = target_row.cells[1]
cell1.paragraphs[0].clear()
run = cell1.paragraphs[0].add_run(verbatim_response)
run.font.size = Pt(9)

target_row.cells[2].paragraphs[0].clear()
run = target_row.cells[2].paragraphs[0].add_run(verdict)
run.font.size = Pt(9)

target_row.cells[3].paragraphs[0].clear()
run = target_row.cells[3].paragraphs[0].add_run(istqb_ref)
run.font.size = Pt(9)

target_row.cells[4].paragraphs[0].clear()
run = target_row.cells[4].paragraphs[0].add_run(student_fix)
run.font.size = Pt(9)

doc.save(doc_path)
print("Updated DOCX successfully!")
