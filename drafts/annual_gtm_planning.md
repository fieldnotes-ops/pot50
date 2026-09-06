# DRAFT — Annual GTT Planning Playbook (WIP, not published)

Target: 3,000+ words, matches quality bar of docs/dl/qr7m2k9x/index.html reference product.
Price target: EUR 29 (higher scope than routing playbook: workbook + calendar + assumptions log).

## Status
Section 1-2 drafted below. Remaining before ship: sections 3-7, CSV workbook, product page, "what it isn't" paragraph, sources cleanup, final HTML build in docs/dl/<slug>/.

## Research notes / sources to cite (verify before shipping)
- Bureau of Labor Statistics / SaaS Capital, Bessemer "State of the Cloud" — capacity ramp and quota attainment benchmarks (vendor/PE-sourced, note bias).
- OpenView "SaaS Benchmarks" annual report — quota, ramp time, org design norms (self-reported survey, disclose sample method + year in final).
- Xactly / Gartner sales performance management commentary on quota-setting methods (vendor, but Gartner is independent analyst — separate these two).
- SiriusDecisions/Forrester territory design frameworks (paraphrase only, do not quote proprietary frameworks verbatim — describe general practice, not their IP).
- Winning by Design "Bowtie" model for capacity-to-segment mapping (public blog content, cite URL and date).

Caveat to state plainly in final: most public "ramp time" and "quota attainment %" numbers come from vendor-run surveys of self-selected SaaS companies (OpenView, Bessemer). They are useful as a rough range, not ground truth. No large-scale independent academic study of B2B quota-setting exists publicly, unlike the lead-response research.

## 1. Why annual planning fails (draft)
Three recurring, publicly documented failure patterns (from OpenView/Bessemer benchmark commentary + general RevOps practice writing, e.g. Jacco van der Kooij, David Sakamoto):
1. Quota set top-down from a board revenue number, divided by average headcount, with no capacity model underneath — ramp time and attrition ignored.
2. Territory/segment lines drawn once at kickoff and never revisited against actual account density, so reps end up with wildly uneven whitespace.
3. Headcount phasing tied to a single hiring wave in Q1, creating a "cohort cliff" where an entire team ramps at once and pipeline coverage collapses in the quarter they go live.

## 2. Capacity and quota modelling (draft — needs full worked example)
Core formula to build out with a real worked numeric example (SDR + AE + segment):

Quota (annual, per rep) = Target new ARR contribution ÷ effective selling capacity

Effective selling capacity = (available reps × 12 months) − (ramp-adjusted lost months) − (attrition-adjusted lost months)

Ramp-adjusted lost months: new hire produces 0% in month 1-X (ramp period), partial % in X-Y (e.g. 50%), full % after Y. Use OpenView's commonly cited ~3-6 month SaaS AE ramp range as a starting bracket, but flag as self-reported survey data.

Need to add: worked example table with 10 AEs, 3 new hires mid-year, attrition assumption, resulting effective capacity number and back-solved quota — this is the artefact buyers actually want (a filled template, not a formula).

## Next run TODO
- Write sections 3 (segment/territory design method + worked example), 4 (headcount phasing across quarters), 5 (planning calendar week-by-week from kickoff to board approval), 6 (assumptions log format), 7 (failure-modes table).
- Build planning_workbook.csv with tabs-as-sheets equivalent (capacity model, quota back-solve, territory list, assumptions log) — since CSV is flat, ship multiple CSVs: capacity_model.csv, territory_worksheet.csv, assumptions_log.csv.
- Convert to docs/dl/<new-unguessable-slug>/index.html using playbook.css structure (nav.toc, h2 span.n, .tbl, .callout, .ack, .files list linking the CSVs).
- Write product page docs/products/annual-gtm-planning-playbook/index.md with "what it isn't" (not a compensation/comp-plan design guide, not a market-sizing/TAM tool, not software).
- Only then call create_sellable (respect 1/week throttle and the 14-day-distribution-before-second-product rule — check days since routing playbook launch).
