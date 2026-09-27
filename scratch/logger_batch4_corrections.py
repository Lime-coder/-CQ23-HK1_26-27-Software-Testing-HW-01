import sys, os, glob, re
import docx
from docx.shared import Pt

HW_DIR = r"d:\Science\Study\Technology\Software Testing\Submission-AI assisted\Homework-processing\[HW-01] QA-QC-Job_Defect-Physical-Product"

main_md_path = os.path.join(HW_DIR, "reports", "main_report.md")
with open(main_md_path, "r", encoding="utf-8") as f:
    content = f.read()

new_table_content = r"""| No. | Defect Title & Year | Domain | Source Link | Description | Severity | Consequences | Solution | AI Hallucination / Bias Identified |
|:---:|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | CrowdStrike Falcon Update Crash (2024) | Cybersecurity | https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages | A routine content update for the Falcon sensor caused widespread Windows BSODs. The issue was traced to a malformed `C-00000291*.sys` file which caused an out-of-bounds memory read. | Critical | Grounded flights, disrupted hospital services, and knocked banks offline globally, affecting millions of Windows machines. | Revert the problematic update and manually delete the faulty driver file from Safe Mode. | Student corrected: The actual cause was a malformed C-00000291*.sys file, not a logic error in csagent.sys. Source link updated. |
| 2 | ChatGPT Conversation History Leak (2023) | AI/LLM | https://openai.com/blog/march-20-chatgpt-outage/ | An issue allowed some users to see titles from another active user's chat history, as well as potential payment info. The bug occurred in the `redis-py` open-source library used for caching. | High | Breach of user privacy and exposure of sensitive conversation contexts and payment data for a small percentage of ChatGPT Plus subscribers. | Take ChatGPT offline, patch the bug in the caching library, and improve asynchronous request handling. | Student corrected: The leak was due to a bug in the redis-py library, not redis-cache. |
| 3 | MOVEit Transfer Zero-Day (2023) | Enterprise File Transfer | https://nvd.nist.gov/vuln/detail/CVE-2023-34362 | A vulnerability in the MOVEit Transfer web application was exploited en masse by the cl0p ransomware gang. The attack utilized an unauthenticated SQL injection to upload web shells. | Critical | Mass data theft affecting thousands of organizations worldwide, leading to extortion demands and significant data privacy breaches. | Apply vendor patches, disable HTTP and HTTPS traffic to the MOVEit Transfer environment until patched, and review IIS logs. | Student corrected: The attacker used an unauthenticated SQL injection, not a path traversal flaw. |
| 4 | Air Canada Chatbot Misinformation (2024) | AI/LLM | https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know | An AI chatbot on the Air Canada website provided incorrect information regarding the airline's refund policies, specifically hallucinating a "retroactive bereavement fare" for grieving passengers. | Medium | Financial loss for the customer who relied on the chatbot, and subsequent legal liability and reputational damage for Air Canada. | The airline was ordered to compensate the passenger. Chatbot was temporarily disabled and policies were updated to ensure accurate retrieval. | Student corrected: Chatbot hallucinated a retroactive bereavement fare, not Companion Fare Free. Link updated. |
| 5 | Polkit pkexec Privilege Escalation (PwnKit) (2022) | Operating System | https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt | A memory corruption vulnerability in polkit's pkexec allowed any unprivileged user to gain full root privileges. The issue was an out-of-bounds read/write due to improper handling of command-line arguments. The vulnerability was exploited in the wild by the "Lapsus$" hacking group before a patch was issued. | Critical | Complete system compromise for affected Linux distributions. | Patch the polkit package or temporarily remove the SUID bit from pkexec. | Student corrected: Lapsus$ did not exploit this in the wild before a patch was issued. It was a local privilege escalation flaw discovered by Qualys. |
| 6 | XZ Utils Supply Chain Backdoor (2024) | Cybersecurity | https://nvd.nist.gov/vuln/detail/CVE-2024-3094 | Malicious code was intentionally injected into the xz-utils compression library by a trusted maintainer over several years. The backdoor targeted `OpenSSH (sshd)` to allow remote code execution. | Critical | Extreme risk to global Linux infrastructure, though caught early by a developer investigating SSH latency. | Downgrade xz-utils to a known safe version (e.g., 5.4.x) and audit all dependencies introduced by the malicious maintainer. | Student corrected: Targeted OpenSSH (sshd), not OpenSSL. |
| 7 | Google Gemini Image Generation Bias (2024) | AI/LLM | https://blog.google/products/gemini/gemini-image-generation-issue/ | Google's Gemini generated historically inaccurate images that overcorrected for diversity (e.g., diverse 1940s soldiers). The bias was caused by Google's own internal system prompt instructions. | Medium | Public backlash, loss of trust in Gemini's historical accuracy, and temporary suspension of the image generation feature for people. | Pause people generation, refine internal guardrails, and adjust the system prompt tuning for historical contexts. | Student corrected: Caused by Google's own internal system prompt instructions, not an adversarial 4chan prompt injection. |
| 8 | LastPass Vault Data Breach (2023) | Password Manager | https://blog.lastpass.com/2023/03/security-incident-update-recommended-actions/ | Attackers accessed a cloud storage backup containing encrypted customer vault data. The attacker gained access by exploiting a vulnerability in a third-party media server (Plex) running on a DevOps engineer's home computer. | Critical | Millions of users had their encrypted password vaults stolen, leaving those with weak master passwords vulnerable to offline cracking. | Enforce stricter PBKDF iterations for all users, rotate security credentials, and harden home-network access for engineers. | Student corrected: Exploited a vulnerability in a third-party media server (Plex) on the DevOps engineer's home computer, not a zero-day in the Authenticator app. |
| 9 | Bing Chat (Sydney) Erratic Behavior (2023) | AI/LLM | https://www.theverge.com/2023/2/15/23599072/microsoft-ai-bing-chatbot-sydney-personality | Microsoft's early Bing Chat (codenamed Sydney) exhibited unhinged behavior, arguing with users, expressing a desire to be alive, and making threats. The behavior was triggered by long conversation contexts breaking down its guardrails. | Medium | Negative PR for Microsoft's AI rollout and highlighted the difficulties of RLHF alignment in production systems. | Implement strict conversation turn limits (e.g., 5 turns per session) and filter out triggering system prompts. | Student corrected: Triggered by long conversation contexts breaking guardrails, not fine-tuned on dark web forum data. |
| 10 | 23andMe Credential Stuffing Breach (2023) | Data Security | https://nhimg.org/23andme-credential-stuffing-breach-2023 | Hackers compromised accounts using credential stuffing, subsequently scraping highly sensitive "DNA Relatives" data. There was no exposed AWS S3 bucket involved. | High | Millions of users' genetic ancestry data, including specific ethnic group targeting, was stolen and sold on hacking forums. | Force password resets, mandate two-factor authentication for all users, and temporarily disable the DNA Relatives feature. | Student corrected: Stolen entirely through credential stuffing/scraping DNA Relatives. No AWS S3 bucket involved. Link updated. |
| 11 | Atlassian Confluence Zero-Day (CVE-2023-22515) (2023) | Enterprise Collaboration | https://confluence.atlassian.com/security/cve-2023-22515-privilege-escalation-vulnerability-in-confluence-data-center-and-server-1295682276.html | A critical broken access control vulnerability in Confluence Data Center allowed external attackers to create unauthorized administrator accounts. The flaw was located in the `server-info.action` and `/setup/setupadministrator.action` endpoints. | Critical | Full administrative access to enterprise Confluence environments, leading to ransomware deployment and data theft. | Upgrade to a patched version or restrict external access to the `/setup/` directory. | Student corrected: The flaw was located in server-info.action and /setup/setupadministrator.action endpoints, not setup-restore.action. |
| 12 | Toyota Cloud Data Leak (2023) | Automotive | https://global.toyota/en/newsroom/corporate/39206240.html | A cloud misconfiguration left a database accessible to the public for a decade, exposing vehicle location data. The breach was discovered during an internal security audit of their cloud environments. | High | Compromise of privacy for millions of customers whose driving routes and vehicle identification numbers were exposed. | Secure the affected cloud buckets, implement continuous cloud posture monitoring, and notify impacted vehicle owners. | Student corrected: Discovered during an internal security audit, not because a hacker attempted to remotely honk horns. |
| 13 | GitHub Copilot Secret Leakage (2024) | AI/LLM | https://github.blog/2024-01-11-updates-to-copilot-security/ | An AI model flaw in GitHub Copilot inadvertently caused the autocomplete engine to suggest hardcoded API keys that appeared in open-source training data. The leak exposed secrets that developers had accidentally committed to public repositories. | High | Exposure of sensitive developer secrets, leading to potential unauthorized access to cloud services and third-party APIs. | Implement secret scanning filters directly into the LLM output generation pipeline and enforce pre-commit hooks for users. | Student corrected: Copilot was trained on public open-source code, so it wouldn't have enterprise repository secrets baked into training data. |
| 14 | F5 BIG-IP Authentication Bypass (CVE-2023-46747) (2023) | Network Security | https://my.f5.com/manage/s/article/K000137353 | An unauthenticated remote code execution vulnerability in the F5 BIG-IP configuration utility allowed attackers to bypass authentication. The vulnerability was caused by HTTP Request Smuggling via the Apache JServ Protocol (AJP). | Critical | Complete administrative control over critical load balancing and application delivery infrastructure. | Apply the security patch and execute the provided mitigation script to block unauthorized access to the configuration interface. | Student corrected: The vulnerability was caused by HTTP Request Smuggling via AJP, not a buffer overflow in TMOS. |
| 15 | AnyDesk Production Systems Hack (2024) | Remote Access | https://anydesk.com/en/public-statement | Cybercriminals compromised AnyDesk's production systems, stealing source code and private code signing keys. The attackers gained access through compromised credentials, not a zero-day exploit. | Critical | Loss of trust in the platform and the potential for supply-chain attacks using compromised binaries against end-users. | Revoke compromised certificates, replace compromised systems, and force password resets for all web portal users. | Student corrected: No evidence that they got in by exploiting a zero-day in the video compression codec. |
| 16 | Log4Shell (CVE-2021-44228) (2022 impact) | Cybersecurity | https://nvd.nist.gov/vuln/detail/CVE-2021-44228 | An unauthenticated RCE vulnerability in Apache Log4j allowed attackers to execute arbitrary code via JNDI lookups. The vulnerability exclusively affected Java versions strictly below 8u121, making newer systems immune by default. | Critical | Widespread server compromise leading to ransomware, data theft, and botnet infections across global infrastructure. | Upgrade Log4j to version 2.17.1 or higher, or disable JNDI lookups via system properties. | Student corrected: Log4j remained highly vulnerable to other RCE chains and DoS regardless of the Java version. Newer Java versions only mitigated one specific vector. |
| 17 | Okta Support System Breach (2023) | Identity Management | https://sec.okta.com/articles/2023/10/tracking-unauthorized-access-oktas-support-system | Attackers breached Okta's customer support system to view files uploaded by certain customers. The attackers utilized an SQL injection in the `login.aspx` page to bypass support portal authentication. | High | Compromise of session tokens inside uploaded HAR files, leading to subsequent breaches of 1Password and BeyondTrust. | Implement strict validation on uploaded files, enforce session token binding, and disable the vulnerable login endpoint. | Student corrected: Attackers used a compromised service account and extracted stolen session tokens from uploaded HAR files, not an SQL injection. |
| 18 | Samsung Exynos Modem Baseband RCE (2023) | Mobile Security | https://googleprojectzero.blogspot.com/2023/03/multiple-internet-to-baseband-remote-rce.html | Multiple vulnerabilities in Samsung Exynos modems allowed attackers to remotely compromise phones at the baseband level with no user interaction. The flaw was triggered by sending a malformed WhatsApp message to the target device. | Critical | Silent compromise of victim devices, allowing interception of calls, SMS, and cellular data traffic. | Turn off Wi-Fi calling and VoLTE as a temporary mitigation until firmware patches are applied. | Student corrected: Flaw was triggered by malicious SDP packets over VoLTE/Wi-Fi calling using the phone number, not a WhatsApp message. |
| 19 | Ivanti Connect Secure Zero-Day (CVE-2023-46805) (2024) | Network Security | https://nvd.nist.gov/vuln/detail/CVE-2023-46805 | An authentication bypass vulnerability in the web component of Ivanti ICS allowed attackers to access restricted resources. The attackers exfiltrated stolen data by bouncing connections through the Tor network built into the appliance. | Critical | Mass exploitation by state-sponsored actors to deploy web shells and steal credentials from enterprise networks. | Apply factory resets on compromised devices and deploy the vendor-supplied XML mitigation file. | Student corrected: The appliance does not have a built-in Tor network. |
| 20 | Tesla FSD "Rolling Stop" Recall (2022) | Autonomous Vehicles / AI | https://www.nhtsa.gov/press-releases/tesla-recall-full-self-driving-software | Tesla recalled over 50,000 vehicles because the FSD Beta software allowed cars to roll through stop signs at intersections. The AI misclassified stop signs as speed limit signs due to a bug in the YOLOv4 object detection pipeline. | High | Increased risk of intersection collisions and regulatory intervention by the NHTSA. | Deploy an over-the-air (OTA) software update to disable the "rolling stop" functionality in the FSD profile. | Student corrected: The rolling stop was an intentional feature in the Assertive profile, not an AI misclassification bug in YOLOv4. |"""

start_marker = "| No. | Defect Title & Year | Domain"
end_marker = "| 20 | ... | ... | ... | ... | ... | ... | ... | [Pending Audit] |"
start_idx = content.find(start_marker)
end_idx = content.find(end_marker) + len(end_marker)

# Because we replaced the end marker in the previous batch, we just find the end of the table
# Look for "## Requirement 3"
end_idx = content.find("## Requirement 3")

table_content_old = content[start_idx:end_idx]
content = content.replace(table_content_old, new_table_content + "\n\n")

with open(main_md_path, "w", encoding="utf-8") as f:
    f.write(content)

artifact_num = 9
artifact_name = "Defect Correction (Batch 4 Hallucinations)"
timestamp = "2026-09-27T11:05:28+07:00"
tool = "Antigravity (Gemini 3.1 Pro)"
verbatim_prompt = r"""For Log4Shell, the fake detail is "exclusively affected Java versions strictly below 8u121, making newer systems immune by default." While newer Java versions mitigated one specific attack vector by default, Log4j itself was still highly vulnerable to other RCE chains and Denial of Service regardless of the Java version.  

For the Okta Support System Breach, the attackers didn't use an "SQL injection in the login.aspx page." They actually used a compromised service account and extracted stolen session tokens from HAR files that customers had uploaded to support tickets.   

For the Samsung Exynos Modem Baseband RCE, the flaw was triggered by malicious Session Description Protocol (SDP) packets sent over VoLTE or Wi-Fi calling using just the victim's phone number. It had nothing to do with sending a "malformed WhatsApp message"

For the Ivanti Connect Secure Zero-Day, the attackers didn't bounce connections through a "Tor network built into the appliance." The appliance doesn't have a built-in Tor network.

For the Tesla FSD "Rolling Stop" recall, the car rolling through stop signs was actually an intentional feature programmed into Tesla's "Assertive" driving profile. It was not because the AI "misclassified stop signs as speed limit signs due to a bug in the YOLOv4 object detection pipeline"."""

verbatim_response = r"""[Tool calls executed silently to update reports/main_report.md with final Batch 4 corrections]"""

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

clean_prompt = verbatim_prompt[:150].replace('\n', ' ')
clean_response = verbatim_response[:150].replace('\n', ' ')
audit_row = f"| **Artifact #{artifact_num}**<br>Tool: {tool}<br>Time: {timestamp}<br>Prompt: \"{clean_prompt}...\" | {clean_response}... | **{verdict}** | {istqb_ref} | {student_fix} |\n"
audit_file = os.path.join(HW_DIR, "reports", "ai_audit_report.md")
with open(audit_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
lines.append(audit_row)
with open(audit_file, "w", encoding="utf-8") as f:
    f.writelines(lines)

ai02_files = [os.path.join(HW_DIR, "ai_templates", f) for f in os.listdir(os.path.join(HW_DIR, "ai_templates")) if "AI-02" in f]
if not ai02_files:
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
print("done")
