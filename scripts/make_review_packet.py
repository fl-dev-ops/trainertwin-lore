import json
from pathlib import Path

with open('/tmp/session_full_audit.json') as f:
    data = json.load(f)

skill_path = Path('users/vasanth/workspace/scenarios/mock-interview-on-resume-project-deep-dive-impact-quantifica.md')
skill_text = skill_path.read_text(encoding='utf-8')

transcript_lines = []
for i, turn in enumerate(data['session']['transcript'], 1):
    transcript_lines.append(f"[{i:02d}] {turn['role'].upper()}: {turn['text']}")

commands_summary = []
for cmd in data['commands']:
    commands_summary.append(f"- {cmd.get('id')}: action={cmd.get('result', {}).get('action', 'finish')} status={cmd.get('status')}")

report_text = json.dumps(data['session'].get('report'), indent=2)

packet = f"""# PRODUCTION SESSION AUDIT & REVIEW PACKET: TRAINERTWIN AGENT

## 1. Session Overview
- Session ID: {data['session']['id']}
- Candidate: Harini Shekar (Software Engineer)
- Persona: {data['session']['personaSlug']} (Vasanth)
- Agent Scenario: {data['session']['agentSlug']}
- Status: {data['session']['status']} (Completed 34 turns)

## 2. Tool Calls Executed by the LiveKit Transport
{chr(10).join(commands_summary)}

## 3. Discovered State Anomalies in Database
- session.evidence: {json.dumps(data['session'].get('evidence'))} (EMPTY!)
- session.runtimeState.used_claims: {json.dumps(data['session'].get('runtimeState', {}).get('used_claims'))} (EMPTY!)
- session.runtimeState.coverage: {json.dumps(data['session'].get('runtimeState', {}).get('coverage'))} (EMPTY!)
- session.runtimeState.main_questions_asked: {data['session'].get('runtimeState', {}).get('main_questions_asked')} (ZERO!)

## 4. Candidate Resume Excerpt
{data['candidateResumeText'][:2500]}

## 5. Live Interview Transcript (All 34 Spoken Turns)
{chr(10).join(transcript_lines)}

## 6. Generated Post-Session Evaluation Report
{report_text}

## 7. Grounded Behavioral Reference: Vasanth SKILL.md (TrainerTwin Lore)
{skill_text}
"""

Path('/tmp/review_packet.md').write_text(packet, encoding='utf-8')
print("Successfully generated /tmp/review_packet.md, length:", len(packet))
