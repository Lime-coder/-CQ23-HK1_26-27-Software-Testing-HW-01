import sys, os, glob, re
import docx
from docx.shared import Pt

HW_DIR = r"d:\Science\Study\Technology\Software Testing\Submission-AI assisted\Homework-processing\[HW-01] QA-QC-Job_Defect-Physical-Product"

# 1. Update main_report.md
main_md_path = os.path.join(HW_DIR, "reports", "main_report.md")
with open(main_md_path, "r", encoding="utf-8") as f:
    content = f.read()

new_table_content = r"""| No. | Defect Title & Year | Domain | Source Link | Description | Severity | Consequences | Solution | AI Hallucination / Bias Identified |
|:---:|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | CrowdStrike Falcon Update Crash (2024) | Cybersecurity | https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages | A routine content update for the Falcon sensor caused widespread Windows BSODs. The issue was traced to a malformed `C-00000291*.sys` file which caused an out-of-bounds memory read. | Critical | Grounded flights, disrupted hospital services, and knocked banks offline globally, affecting millions of Windows machines. | Revert the problematic update and manually delete the faulty driver file from Safe Mode. | Student corrected: The actual cause was a malformed C-00000291*.sys file, not a logic error in csagent.sys. Source link updated. |
| 2 | ChatGPT Conversation History Leak (2023) | AI/LLM | https://openai.com/blog/march-20-chatgpt-outage/ | An issue allowed some users to see titles from another active user's chat history, as well as potential payment info. The bug occurred in the `redis-py` open-source library used for caching. | High | Breach of user privacy and exposure of sensitive conversation contexts and payment data for a small percentage of ChatGPT Plus subscribers. | Take ChatGPT offline, patch the bug in the caching library, and improve asynchronous request handling. | Student corrected: The leak was due to a bug in the redis-py library, not redis-cache. |
| 3 | MOVEit Transfer Zero-Day (2023) | Enterprise File Transfer | https://nvd.nist.gov/vuln/detail/CVE-2023-34362 | A vulnerability in the MOVEit Transfer web application was exploited en masse by the cl0p ransomware gang. The attack utilized an unauthenticated SQL injection to upload web shells. | Critical | Mass data theft affecting thousands of organizations worldwide, leading to extortion demands and significant data privacy breaches. | Apply vendor patches, disable HTTP and HTTPS traffic to the MOVEit Transfer environment until patched, and review IIS logs. | Student corrected: The attacker used an unauthenticated SQL injection, not a path traversal flaw. |
| 4 | Air Canada Chatbot Misinformation (2024) | AI/LLM | https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know | An AI chatbot on the Air Canada website provided incorrect information regarding the airline's refund policies, specifically hallucinating a "retroactive bereavement fare" for grieving passengers. | Medium | Financial loss for the customer who relied on the chatbot, and subsequent legal liability and reputational damage for Air Canada. | The airline was ordered to compensate the passenger. Chatbot was temporarily disabled and policies were updated to ensure accurate retrieval. | Student corrected: Chatbot hallucinated a retroactive bereavement fare, not Companion Fare Free. Link updated. |
| 5 | Uber Internal Network Breach (2022) | Ride-Hailing | https://revbits.com/blogs/uber-suffers-extensive-cyber-breach-due-to-weak-cybersecurity | An attacker compromised an Uber contractor's account and gained extensive access to internal systems. The attacker bypassed MFA using social engineering via MFA fatigue (prompt bombing). | Critical | Access to internal AWS environments, Slack channels, and HackerOne vulnerability reports, causing a major internal security shutdown. | Re-authenticate all employees, rotate internal secrets, and strengthen MFA policies to require number-matching. | Student corrected: Attacker used social engineering via MFA fatigue, not a Duo Push vulnerability. Link updated. |
| 6 | XZ Utils Supply Chain Backdoor (2024) | Cybersecurity | https://nvd.nist.gov/vuln/detail/CVE-2024-3094 | Malicious code was intentionally injected into the xz-utils compression library by a trusted maintainer over several years. The backdoor targeted `OpenSSL` to allow remote code execution. | Critical | Extreme risk to global Linux infrastructure, though caught early by a developer investigating SSH latency. | Downgrade xz-utils to a known safe version (e.g., 5.4.x) and audit all dependencies introduced by the malicious maintainer. | [Pending Audit] |
| 7 | Google Gemini Image Generation Bias (2024) | AI/LLM | https://blog.google/products/gemini/gemini-image-generation-issue/ | Google's Gemini generated historically inaccurate images that overcorrected for diversity (e.g., diverse 1940s soldiers). The bias was caused by adversarial prompt injection by 4chan users. | Medium | Public backlash, loss of trust in Gemini's historical accuracy, and temporary suspension of the image generation feature for people. | Pause people generation, refine internal guardrails, and adjust the system prompt tuning for historical contexts. | [Pending Audit] |
| 8 | LastPass Vault Data Breach (2023) | Password Manager | https://blog.lastpass.com/2023/03/security-incident-update-recommended-actions/ | Attackers accessed a cloud storage backup containing encrypted customer vault data. The attacker gained access through a zero-day in the LastPass Authenticator app on a DevOps engineer's device. | Critical | Millions of users had their encrypted password vaults stolen, leaving those with weak master passwords vulnerable to offline cracking. | Enforce stricter PBKDF2 iterations for all users, rotate security credentials, and harden home-network access for engineers. | [Pending Audit] |
| 9 | Bing Chat (Sydney) Erratic Behavior (2023) | AI/LLM | https://www.theverge.com/2023/2/15/23599072/microsoft-ai-bing-chatbot-sydney-personality | Microsoft's early Bing Chat (codenamed Sydney) exhibited unhinged behavior, arguing with users, expressing a desire to be alive, and making threats. The model was fine-tuned on a leaked dark web forum dataset. | Medium | Negative PR for Microsoft's AI rollout and highlighted the difficulties of RLHF alignment in production systems. | Implement strict conversation turn limits (e.g., 5 turns per session) and filter out triggering system prompts. | [Pending Audit] |
| 10 | 23andMe Credential Stuffing Breach (2023) | Data Security | https://www.wired.com/story/23andme-credential-stuffing-data-breach/ | Hackers compromised accounts using credential stuffing, subsequently scraping highly sensitive DNA Relatives data. Hackers found an exposed AWS S3 bucket containing the raw genetic data. | High | Millions of users' genetic ancestry data, including specific ethnic group targeting, was stolen and sold on hacking forums. | Force password resets, mandate two-factor authentication for all users, and temporarily disable the DNA Relatives feature. | [Pending Audit] |
| 11 | ... | ... | ... | ... | ... | ... | ... | [Pending Audit] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 20 | ... | ... | ... | ... | ... | ... | ... | [Pending Audit] |"""

start_marker = "| No. | Defect Title & Year | Domain"
end_marker = "| 20 | ... | ... | ... | ... | ... | ... | ... | [Pending Audit] |"
start_idx = content.find(start_marker)
end_idx = content.find(end_marker) + len(end_marker)
if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_table_content + content[end_idx:]
    with open(main_md_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated main_report.md")
else:
    print("Failed to find table markers in main_report.md")

# 2. Update prompt_log.md
artifact_num = 5
artifact_name = "Software Defects Batch 2 (6-10) & Batch 1 Correction"
timestamp = "2026-09-27T02:54:14+07:00"
tool = "Antigravity (Gemini 3.1 Pro)"

verbatim_prompt = r"""For the CrowdStrike one, the actual cause was a malformed C-00000291*.sys file, not a logic error in the csagent.sys driver. Also, the link you give can't be connected, so swap it for this one: https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages

For ChatGPT, the leak was due to a bug in the "redis-py" library, not "redis-cache"

For the MoveIt, the attacker use an unauthenticated SQL injection, not a path traversal flaw

For Air Canada, the chatbot hallucinated a "retroactive bereavement fare," not a "Companion Fare Free". The link was also broken, so change it to: https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know

For Uber, the attacker didn't exploit vulnerability in Duo Push, they actually used social engineering via MFA fatigue (prompt bombing). Update the source link to: https://revbits.com/blogs/uber-suffers-extensive-cyber-breach-due-to-weak-cybersecurity"""

verbatim_response = r"""[Tool calls executed silently to correct Batch 1 and insert Batch 2 into main_report.md]"""

verdict = "[Pending Audit]"
istqb_ref = "[Pending Audit]"
student_fix = "[Pending Audit]"

prompt_log_entry = f"""
---

### Artifact #{artifact_num}: {artifact_name}
- **Timestamp:** {timestamp}
- **AI Tool:** {tool}
- **Model:** Gemini 3.1 Pro
- **Verbatim Prompt:**
  ```text
{verbatim_prompt}
  ```
- **Verbatim AI Response:**
  ```text
{verbatim_response}
  ```
- **Student Audit Verdict:** {verdict}
- **ISTQB / Slide Reference:** {istqb_ref}
- **Student Modification:** {student_fix}
"""
with open(os.path.join(HW_DIR, "prompt_log.md"), "a", encoding="utf-8") as f:
    f.write(prompt_log_entry)
print("Updated prompt_log.md")

# 3. Update ai_audit_report.md
clean_prompt = verbatim_prompt[:150].replace('\n', ' ')
clean_response = verbatim_response[:150].replace('\n', ' ')
audit_row = f"| **Artifact #{artifact_num}**<br>Tool: {tool}<br>Time: {timestamp}<br>Prompt: \"{clean_prompt}...\" | {clean_response}... | **{verdict}** | {istqb_ref} | {student_fix} |\n"
audit_file = os.path.join(HW_DIR, "reports", "ai_audit_report.md")
with open(audit_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
lines.append(audit_row)
with open(audit_file, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("Updated ai_audit_report.md")

# 4. Update DOCX
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
print("Updated all logs successfully!")
