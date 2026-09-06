# Lead Routing & SLA Playbook
### A practical toolkit for RevOps and Sales Ops teams who own speed-to-lead

---

## Why this exists

Most lead routing breaks not because the CRM logic is wrong, but because nobody wrote down the rules, the SLAs, or who owns exceptions. This playbook gives you a working system you can implement in Salesforce, HubSpot, or any CRM in under a week: routing logic, SLA tiers, escalation paths, and the alerts that keep reps honest.

---

## 1. Routing Logic Framework

Pick one primary routing method, then layer tie-breakers. Don't stack more than two.

**Primary methods (choose one):**
- Round robin (equal distribution, simplest to audit)
- Territory-based (geography, industry vertical, named accounts)
- Account-tier based (Enterprise / Mid-Market / SMB queues)
- Product-line based (for multi-product motions)

**Tie-breakers (layer on top):**
- Capacity cap (max open leads per rep before pause)
- Existing relationship override (named account owner always wins)
- Language/timezone match

**Rule of thumb:** if your routing logic needs more than one paragraph to explain to a new SDR, it's too complex. Simplify before automating.

---

## 2. SLA Tiers

| Lead Tier | Definition | First-Touch SLA | Escalation Trigger |
|---|---|---|---|
| Tier 1 — Hot | Demo request, pricing page + 2 visits, PQL | 5 minutes | No touch in 10 min → auto-reassign |
| Tier 2 — Warm | Content download + firmographic fit | 1 hour | No touch in 4 hours → manager alert |
| Tier 3 — Cold | Cold inbound, generic form fill | 24 hours | No touch in 48 hours → recycle to marketing |

Adjust thresholds to your sales cycle, but keep three tiers max. More tiers than that and reps start gaming the classification.

---

## 3. Escalation Matrix

| Breach | Who is notified | Channel | Action |
|---|---|---|---|
| SLA missed, Tier 1 | Rep + Manager | Slack DM + CRM flag | Auto-reassign to next available rep |
| SLA missed, Tier 2 | Manager | Slack channel | Manager reassigns within 1 hour |
| SLA missed, Tier 3 | RevOps (weekly digest) | Email report | Reviewed in weekly pipeline meeting |
| Repeated breach (same rep, 3x in a week) | Sales Manager + RevOps | 1:1 flag | Capacity review, coaching, or routing pause |

---

## 4. Alert Templates

**Slack alert — SLA breach (Tier 1):**
```
🚨 SLA BREACH — Tier 1 Lead
Lead: {{Lead Name}} / {{Company}}
Assigned to: {{Rep}}
Time since assignment: {{X}} min (SLA: 5 min)
Action: Auto-reassigning to {{Next Rep}}. Manager notified.
```

**Email digest — Weekly SLA summary (send to RevOps + Sales Leadership):**
```
Subject: Weekly Lead Routing SLA Report

Tier 1 leads: {{count}} | SLA met: {{%}} | Avg response: {{time}}
Tier 2 leads: {{count}} | SLA met: {{%}} | Avg response: {{time}}
Tier 3 leads: {{count}} | SLA met: {{%}} | Avg response: {{time}}

Top 3 reps by SLA compliance: {{names}}
Reps flagged for repeated breach: {{names}}
```

---

## 5. Implementation Checklist

- [ ] Define lead tiers and scoring criteria with Sales + Marketing sign-off
- [ ] Map routing logic to a single source-of-truth doc (use the matrix template included)
- [ ] Build routing rules in CRM (native rules engine or routing tool)
- [ ] Set up SLA timers (CRM automation or a routing tool with SLA tracking)
- [ ] Configure Slack/email alerts for breaches
- [ ] Build the weekly SLA digest report
- [ ] Run a 2-week shadow test before turning off manual routing
- [ ] Review SLA compliance monthly; retune tiers if breach rate > 15%

---

## 6. Metrics to Track Weekly

- Speed-to-first-touch (median and P90, by tier)
- SLA compliance rate (%) by tier and by rep
- Lead-to-meeting conversion rate, segmented by response time bucket (this is usually the number that gets budget approved for a routing tool)
- Reassignment rate (high reassignment = capacity or rule problem)
- Recycled lead volume (Tier 3 leads not worked in SLA window)

---

## 7. Common Failure Modes

1. **Routing rules live in someone's head, not in a doc.** Fix: this playbook's matrix template is your source of truth — keep it current.
2. **SLA exists but nobody enforces it.** Fix: automate the alert, don't rely on managers checking dashboards.
3. **Tiers are too granular.** Reps stop trusting the system. Three tiers, clear definitions.
4. **No capacity cap.** Top reps get flooded, leads sit unworked. Add a cap and overflow rule.
5. **No feedback loop to Marketing.** If Tier 3 leads convert at Tier 1 rates, your scoring model is wrong — review quarterly.

---

*Companion file: `routing_matrix_template.csv` — a ready-to-fill matrix for documenting your routing rules by tier, territory, and product line.*
