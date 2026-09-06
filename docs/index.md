---
layout: null
title: Fieldnotes Ops
---
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fieldnotes Ops. Practical playbooks for revenue operations</title>
<meta name="description" content="Practical, research-backed playbooks for RevOps, sales ops and GTM teams. Clear rules, editable templates and implementation notes you can put to work this week.">
<link rel="canonical" href="https://fieldnotes-ops.github.io/pot50/">
<link rel="stylesheet" href="assets/playbook.css">
<style>
body{font-size:16px}
.container{width:min(1120px,calc(100% - 48px));margin-inline:auto}
.site-header{border-bottom:1px solid var(--rule)}
.header-inner{min-height:84px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.wordmark{display:inline-flex;align-items:center;gap:10px;text-decoration:none;font-weight:700;font-size:20px;letter-spacing:-0.01em}
.wordmark .mark{width:32px;height:32px;display:grid;place-items:center;background:var(--ink);color:#fff;border-radius:4px;font-family:var(--mono);font-weight:500}
.header-nav{display:flex;align-items:center;gap:24px;font-size:15px}
.header-nav a{text-decoration:none;color:var(--ink-2)}
.header-nav a:hover{color:var(--ink);text-decoration:underline}
.header-nav .nav-action{border:1px solid var(--rule);padding:8px 14px;border-radius:4px;color:var(--ink);font-weight:600}
.hero{padding:64px 0 56px;display:grid;grid-template-columns:1.05fr 1fr;gap:64px;align-items:center}
.hero h1{font-size:clamp(38px,5vw,60px);line-height:1.05;letter-spacing:-0.02em;margin:0 0 20px;font-weight:700}
.hero .lede{font-size:19px;line-height:1.6;color:var(--ink-2);max-width:32em;margin:0 0 24px}
.hero .audience{font-size:14px;color:var(--muted);padding-top:16px;border-top:1px solid var(--rule);max-width:30em}
.product{background:var(--ink);color:#fff;border-radius:6px;padding:28px 30px}
.product .kicker{font-family:var(--mono);font-size:13px;color:#B8C2D1;margin:0 0 10px}
.product h2{font-size:26px;line-height:1.2;margin:0 0 10px;padding:0;border:0;color:#fff}
.product p{color:#D5DBE5;margin:0 0 18px;font-size:15.5px;line-height:1.55}
.product .parts{list-style:none;padding:0;margin:0 0 22px;display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.product .parts li{background:#22304F;border-radius:4px;padding:10px 12px;font-size:14px;line-height:1.4}
.product .parts li b{display:block;color:#F2C56B;font-family:var(--mono);font-weight:500;font-size:12px;margin-bottom:4px}
.product .price{display:flex;align-items:baseline;gap:12px;margin:0 0 16px}
.product .price b{font-size:34px;font-weight:700}
.product .price span{color:#B8C2D1;font-size:14px}
.product .btn{background:#F2C56B;color:var(--ink);font-size:16px;padding:12px 18px}
.product .btn:hover{background:#F6D48B}
.product .fine{font-size:13px;color:#B8C2D1;margin:14px 0 0}
.product .fine a{color:#fff}
section.band{padding:56px 0;border-top:1px solid var(--rule)}
section.band h2{border:0;padding:0;margin:0 0 6px;font-size:30px}
section.band .intro{color:var(--ink-2);max-width:40em;margin:0 0 32px;font-size:17px}
.inside{display:grid;grid-template-columns:repeat(3,1fr);gap:28px 36px}
.inside h3{font-size:17px;margin:0 0 6px}
.inside p{margin:0;font-size:15px;color:var(--ink-2);line-height:1.55}
.inside .sec{font-family:var(--mono);font-size:12px;color:var(--muted);margin:0 0 4px}
.steps{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(3,1fr);gap:24px;counter-reset:st}
.steps li{counter-increment:st;padding-top:14px;border-top:2px solid var(--ink)}
.steps li::before{content:counter(st);font-family:var(--mono);color:var(--signal);font-weight:500;display:block;margin-bottom:6px}
.steps h3{font-size:17px;margin:0 0 4px}
.steps p{margin:0;font-size:15px;color:var(--ink-2)}
.faq details{border-top:1px solid var(--rule);padding:14px 0}
.faq details:last-child{border-bottom:1px solid var(--rule)}
.faq summary{cursor:pointer;font-weight:600;font-size:17px;list-style:none;display:flex;justify-content:space-between;gap:16px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-family:var(--mono);color:var(--muted)}
.faq details[open] summary::after{content:"–"}
.faq p{margin:10px 0 0;max-width:44em;color:var(--ink-2);font-size:15.5px}
.cta{padding:56px 0;border-top:1px solid var(--rule)}
.cta h2{border:0;padding:0;margin:0 0 8px;font-size:30px}
.cta p{color:var(--ink-2);margin:0 0 20px}
footer.site{margin:0;border-top:1px solid var(--rule);padding:28px 0 40px;font-size:14px;color:var(--muted)}
footer.site .container{display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap}
@media (max-width:900px){.hero{grid-template-columns:1fr;gap:36px;padding:40px 0}.inside,.steps,.product .parts{grid-template-columns:1fr}.header-nav{gap:14px}.header-nav a:not(.nav-action){display:none}}
</style>
</head>
<body>
<header class="site-header"><div class="container header-inner">
  <a class="wordmark" href="https://fieldnotes-ops.github.io/pot50/"><span class="mark">f.</span>Fieldnotes Ops</a>
  <nav class="header-nav" aria-label="Site">
    <a href="#playbook">The playbook</a>
    <a href="#inside">What's inside</a>
    <a class="nav-action" href="https://fieldnotes-ops.github.io/pot50/products/lead-routing-sla-playbook/">View the playbook</a>
  </nav>
</div></header>

<main>
<div class="container hero">
  <div>
    <h1>For the work behind the revenue.</h1>
    <p class="lede">Practical playbooks for the people who build and run revenue systems. Clear rules, editable templates and implementation notes you can put to work this week, with the evidence behind them cited and its limits stated plainly.</p>
    <p class="audience">Written for RevOps, sales ops and GTM teams working in HubSpot, Salesforce or a comparable CRM.</p>
  </div>
  <div class="product" id="playbook">
    <p class="kicker">Playbook 001</p>
    <h2>Lead Routing &amp; SLA Playbook</h2>
    <p>Decide who owns each inbound request, when they should respond, and what happens if they don't.</p>
    <ul class="parts">
      <li><b>Route</b>Set the owner</li>
      <li><b>Respond</b>Set the clock</li>
      <li><b>Recover</b>Handle a miss</li>
    </ul>
    <p class="price"><b>€19</b><span>one-time payment, instant access</span></p>
    <a class="btn" href="https://buy.stripe.com/4gM6oJ0mN6RP3aOasQ9AA00">Get the playbook</a>
    <p class="fine">Web guide, about 5,000 words, plus two editable CSVs. Payment via Stripe. <a href="https://fieldnotes-ops.github.io/pot50/products/lead-routing-sla-playbook/">Read the full details</a>.</p>
  </div>
</div>

<section class="band" id="inside"><div class="container">
  <h2>Inside the playbook</h2>
  <p class="intro">From agreeing the service promise to testing the rules in your CRM. Each part gives you something concrete to discuss, adapt or build.</p>
  <div class="inside">
    <div><p class="sec">Sections 1 to 2</p><h3>The evidence and the service agreement</h3><p>The two original response-time studies cited properly, with their limits. Then which requests count, who is accountable, what "first touch" means, and covered hours worked through a Friday-afternoon example.</p></div>
    <div><p class="sec">Sections 3 to 5</p><h3>An editable routing matrix</h3><p>Design principles, five distribution models and when to buy a tool, then twelve rules in priority order with exceptions for customers, open opportunities and named accounts. Includes the CSV.</p></div>
    <div><p class="sec">Section 6</p><h3>A response and rescue plan</h3><p>SLA tiers, a four-step escalation ladder, cooldown and single-rescue rules, and the evidence to keep so any outcome can be explained later.</p></div>
    <div><p class="sec">Section 7</p><h3>Implementation notes</h3><p>HubSpot, Salesforce and Zapier/n8n build notes, the fields to add, timer pseudocode that survives replays and lost jobs, and a Slack payload with delivery-failure handling.</p></div>
    <div><p class="sec">Section 8</p><h3>Reporting you can explain</h3><p>Metric definitions, a worked breach-rate calculation using the cohort method, a SQL query, a weekly review agenda and an editable metrics tracker.</p></div>
    <div><p class="sec">Sections 9 to 11</p><h3>Rollout, testing and troubleshooting</h3><p>A four-week rollout with a shadow run, ten acceptance tests, a rollback instruction, and fifteen symptoms with fixes. Sources listed with their weaknesses.</p></div>
  </div>
</div></section>

<section class="band"><div class="container">
  <h2>How it works</h2>
  <p class="intro">Enough detail to build from, enough context to use your own judgement. You still own the decisions: set targets that fit your coverage, adapt the templates, and test the workflow before relying on it.</p>
  <ol class="steps">
    <li><h3>Buy once</h3><p>€19 through Stripe. One-time purchase, no subscription.</p></li>
    <li><h3>Open your playbook</h3><p>After payment you're sent straight to the guide. No account to create, no email sequence.</p></li>
    <li><h3>Make it yours</h3><p>Bookmark the page, print it to PDF, and adapt the CSV templates to your operation.</p></li>
  </ol>
</div></section>

<section class="band faq"><div class="container">
  <h2>Before you buy</h2>
  <p class="intro">A few useful answers.</p>
  <details><summary>What exactly do I receive?</summary><p>A web guide of about 5,000 words plus two editable CSVs: a routing matrix and a weekly metrics tracker. Read it in your browser or print it to PDF. The full contents are listed on the <a href="https://fieldnotes-ops.github.io/pot50/products/lead-routing-sla-playbook/">playbook page</a>.</p></details>
  <details><summary>Will this configure my CRM for me?</summary><p>No. It's a document and templates, not an installed integration. It gives you the operating rules, examples and build notes; you implement and test them in your own systems.</p></details>
  <details><summary>Is it a fit for my team?</summary><p>It's written for the RevOps or sales ops person responsible for inbound routing, using HubSpot, Salesforce or a comparable CRM plus Slack. If you already run reliable SLA automation and a weekly breach review, you probably don't need it.</p></details>
  <details><summary>How do I get access after paying?</summary><p>Stripe sends you straight to the playbook page after payment. Bookmark it or save a PDF. There's no account and no login.</p></details>
  <details><summary>What if there's a problem with my purchase?</summary><p>Reply to your Stripe receipt. If something is wrong with what you receive, it gets fixed or refunded.</p></details>
</div></section>

<section class="cta"><div class="container">
  <h2>Give every request a clear next step.</h2>
  <p>Lead Routing &amp; SLA Playbook. Web guide plus two editable CSVs, €19.</p>
  <a class="btn" href="https://buy.stripe.com/4gM6oJ0mN6RP3aOasQ9AA00">Get the playbook</a>
</div></section>
</main>

<footer class="site"><div class="container">
  <span>Fieldnotes Ops. Practical playbooks for the people who build revenue systems.</span>
  <span>Purchase questions: reply to your Stripe receipt.</span>
</div></footer>
</body>
</html>
