---
layout: null
title: Lead Routing & SLA Playbook
---
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lead Routing &amp; SLA Playbook | Fieldnotes Ops</title>
<meta name="description" content="A research-backed playbook for routing inbound leads in seconds and enforcing response SLAs automatically. Matrix, escalation ladder, HubSpot and Salesforce build notes, metrics, 30-day rollout.">
<link rel="stylesheet" href="../../assets/playbook.css">
<style>
.wrap{grid-template-columns:minmax(0,68ch);max-width:820px;padding-top:32px}
.price{font-size:32px;font-weight:700;margin:24px 0 4px}.price small{font-size:15px;font-weight:400;color:var(--muted);margin-left:8px}
.site-header{border-bottom:1px solid var(--rule)}
.header-inner{width:min(1120px,calc(100% - 48px));margin-inline:auto;min-height:84px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.wordmark{display:inline-flex;align-items:center;gap:10px;text-decoration:none;font-weight:700;font-size:20px}
.wordmark .mark{width:32px;height:32px;display:grid;place-items:center;background:var(--ink);color:#fff;border-radius:4px;font-family:var(--mono);font-weight:500}
.header-nav a{text-decoration:none;color:var(--ink);border:1px solid var(--rule);padding:8px 14px;border-radius:4px;font-weight:600;font-size:15px}
</style>
</head>
<body>
<header class="site-header"><div class="header-inner">
  <a class="wordmark" href="https://fieldnotesops.com/"><span class="mark">f.</span>Fieldnotes Ops</a>
  <nav class="header-nav" aria-label="Site"><a href="https://buy.stripe.com/4gM6oJ0mN6RP3aOasQ9AA00">Get the playbook, €19</a></nav>
</div></header>
<div class="wrap"><main>
<h1>Lead Routing &amp; SLA Playbook</h1>
<p class="sub">Get every inbound lead to the right owner in seconds, put a clock on it, and make the clock enforce itself.</p>

<p>The 2007 MIT/InsideSales study found the odds of qualifying a lead were about 21 times higher when the first call went out within 5 minutes rather than 30. The 2011 Harvard Business Review audit of 2,241 firms found the average response time was 42 hours, and nearly a quarter never responded at all. Most teams still live on the wrong side of that gap, not because they don't care, but because nobody owns the lead for the first hour and nothing enforces the clock.</p>

<p>This playbook is the operating document for fixing that. It is written for the RevOps or sales ops person who owns the routing rules, and it assumes HubSpot, Salesforce or a comparable CRM plus Slack.</p>

<h3>What's in it</h3>
<ul>
<li>The evidence on response time, with the two original studies cited properly and their limits stated honestly.</li>
<li>A one-page service agreement to settle first: which requests count, who is accountable, what "first touch" means, when the clock starts and whether it runs in covered or elapsed minutes, with a worked Friday-afternoon example.</li>
<li>Design principles: four routing dimensions maximum, scoring kept separate from routing, identity resolved before distribution, availability as an input, a staffed catch-all with its own deadline.</li>
<li>The five distribution models (simple, weighted, capacity-based, availability-aware, territory) with when each fits and when to buy a routing tool.</li>
<li>A twelve-rule routing matrix in priority order, with holdouts for open opportunities, customers and named accounts, boundary-value guidance and a worked example, as a table and an editable CSV.</li>
<li>SLA tiers, a four-step escalation ladder with cooldown and single-rescue rules, and the evidence to keep on every request so any outcome can be explained later.</li>
<li>Build notes for HubSpot, Salesforce and Zapier/n8n, the exact fields to add, pseudocode that handles replays, lost timer jobs and late-logged activity, a Slack payload, and what to do when the alert doesn't arrive.</li>
<li>Metric definitions using the cohort method with a worked calculation, a SQL query, a weekly review agenda, and a metrics tracker CSV.</li>
<li>A four-week rollout with a shadow run, ten acceptance tests, a rollback instruction, and a troubleshooting table of fifteen symptoms with fixes.</li>
</ul>

<h3>What it isn't</h3>
<p>It's not software and it won't configure your CRM for you. It's about 5,000 words plus two spreadsheets, delivered as a web page you can bookmark or print to PDF. If you already run a routing tool with SLA automation and a weekly breach review, you probably don't need it.</p>

<p class="price">€19 <small>one-time, instant access</small></p>
<p><a class="btn" href="https://buy.stripe.com/4gM6oJ0mN6RP3aOasQ9AA00">Buy the playbook</a></p>
<p class="quiet">Payment is handled by Stripe. After paying you're sent straight to the playbook page. No account, no email sequence. If something is wrong with what you receive, reply to the Stripe receipt and it gets fixed or refunded.</p>

<footer>Fieldnotes Ops. Practical playbooks for the people who build the systems.</footer>
</main></div>
</body>
</html>
