---
title: "Lead Routing & SLA Benchmarks: What the Data Actually Shows"
---

<link rel="stylesheet" href="../../assets/playbook.css">

<div class="wrap">
<nav class="toc">

- [1. The core finding](#core)
- [2. What "fast" actually means](#fast)
- [3. Vendor data vs independent research](#vendor)
- [4. Where SLAs break in practice](#break)
- [5. A minimal SLA to start with](#minimal)
- [6. Sources](#sources)

</nav>
<main>

# Lead Routing & SLA Benchmarks: What the Data Actually Shows

If you run RevOps or sales ops, you've seen the "5 minutes or you lose the lead" claim on a hundred vendor blogs. Most of it traces back to two studies, both over a decade old, plus a pile of vendor-sponsored analyses that repeat the same numbers without re-testing them. Here's what's actually documented, what's vendor noise, and what to do about it.

<h2><span class="n">1</span>The core finding</h2>
<a id="core"></a>

The most-cited data point comes from James Oldroyd's research (Kellogg School of Management / MIT, published with Bruce Elkington and Kevin McElheran), analyzed as "The Short Life of Online Sales Leads" in Harvard Business Review (2011) and an earlier working paper, "The Lead Response Management Study" (2007), which looked at over 100,000 sales leads across more than 20 companies.

Two findings hold up:

- Odds of *contacting* a lead dropped roughly 10x between 5 minutes and 10 minutes after the lead came in.
- Odds of *qualifying* a contacted lead were nearly 7x higher when the first call happened within 5 minutes vs. after 30 minutes.

That's the real finding. It is not "every company loses X% of revenue if they're slow" — that's a paraphrase that has drifted through years of vendor blog posts. The original study is about web-form leads calling a B2B inside sales team in the mid-2000s. It says nothing directly about enterprise ABM leads, partner-sourced leads, or PLG signups, and the underlying data is now roughly 18 years old.

<h2><span class="n">2</span>What "fast" actually means</h2>
<a id="fast"></a>

Independent follow-up is thin. What exists:

- MIT's own summary materials on the Oldroyd study reiterate the 5-minute number but don't extend it to new channels.
- Harvard Business Review's 2011 write-up is a secondary source built on the same dataset — it's not a new study.
- Most "2020s" benchmark numbers you see (e.g., "78% of customers buy from the first responder") come from InsideSales.com (now XANT) whitepapers, which are vendor-funded and don't publish full methodology. Treat them as directional marketing claims, not research.

The honest position for a planning document: response speed correlates with contact and qualification rates, the effect is large and repeatedly observed in inside-sales, form-fill contexts, and it decays fast in the first 10-30 minutes. Beyond that shape, precise percentages you can defend in a QBR don't exist in public, non-vendor research.

<h2><span class="n">3</span>Vendor data vs independent research</h2>
<a id="vendor"></a>

<table class="tbl">
<tr><th>Source</th><th>Type</th><th>Usable for</th><th>Caveat</th></tr>
<tr><td>Oldroyd et al., Lead Response Management Study (2007) / HBR (2011)</td><td>Academic, MIT/Kellogg</td><td>Directional case for speed-to-lead SLAs</td><td>~18 years old, inside-sales/web-form context only</td></tr>
<tr><td>InsideSales.com / XANT whitepapers</td><td>Vendor</td><td>Talking points, not benchmarks</td><td>No public methodology, funded by an SLA-routing vendor</td></tr>
<tr><td>LeanData, Chili Piper, Distribution Engine blogs</td><td>Vendor</td><td>Implementation patterns, tooling options</td><td>Selection bias toward their own customers' setups</td></tr>
<tr><td>Drift "State of Conversational Marketing"</td><td>Vendor survey</td><td>Chat/live-response norms</td><td>Self-reported, chat-specific, not phone/email SLA data</td></tr>
</table>

If a vendor number isn't in this table with a name and year attached, don't put it in your board deck.

<h2><span class="n">4</span>Where SLAs break in practice</h2>
<a id="break"></a>

Patterns that show up consistently across public case studies and vendor implementation guides (not statistically proven, but widely and independently reported):

1. **Routing rules and SLA clocks live in different systems.** The CRM enforces "assign within 1 minute," but the rep's SLA to *call* the lead is tracked in a spreadsheet or not at all. Assignment speed gets optimized; response speed doesn't.
2. **Round-robin ignores capacity.** Leads get assigned evenly regardless of a rep's current queue, so the SLA clock starts on leads that will realistically wait hours.
3. **No re-routing on breach.** Most routing tools notify on SLA breach; few automatically reassign. The notification becomes noise within a week.
4. **Time zone and business-hours gaps.** A "5 minute" SLA quietly becomes "5 minutes during your HQ's business hours," which can mean a 14-hour wait for a lead in another region.
5. **Definition drift.** "Response" means "call attempted" to one team and "call connected" to another. SLA compliance numbers get reported without agreeing on this first.

<h2><span class="n">5</span>A minimal SLA to start with</h2>
<a id="minimal"></a>

Given the state of the evidence, here's a defensible starting point rather than a borrowed vendor number:

- Assignment: under 2 minutes, systems-enforced, 24/7 if you sell globally.
- First touch attempt: under 15 minutes during the lead's local business hours; under 60 minutes outside them.
- Escalation: unclaimed after 2x the SLA window → auto-reassign, don't just alert.
- Reporting: track *attempt* and *connect* separately. Don't let "attempted" quietly stand in for "response" in your dashboard.

This is a starting SLA, not a proven optimum — you tune the window against your own contact-rate curve once you have 4-6 weeks of data, exactly the tracker approach used in the routing playbook below.

<h2><span class="n">6</span>Sources</h2>
<a id="sources"></a>

- Oldroyd, J., McElheran, K., Elkington, C. "The Short Life of Online Sales Leads." Harvard Business Review, 2011.
- Lead Response Management Study (dataset described in the above; original 2007 working paper, MIT/Kellogg-affiliated authors).
- InsideSales.com / XANT published whitepapers (vendor; methodology not public — cited here only as an example of what *not* to treat as a benchmark).
- Vendor implementation blogs (LeanData, Chili Piper, Distribution Engine) reviewed for common failure patterns, not benchmark numbers.

<div class="callout">
Want the routing rules, escalation matrix, and an SLA tracker you can fill in with your own numbers? See the <a href="https://fieldnotesops.com/products/lead-routing-sla-playbook/">Lead Routing &amp; SLA Playbook</a> — routing matrix template, SLA breach tracker CSV, and a rollout plan included.
</div>

<div class="ack quiet">
Fieldnotes Ops — GTM and RevOps playbooks built from public research and documented practice.
</div>

</main>
</div>
