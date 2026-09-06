---
layout: null
title: "Lead routing and SLA benchmarks: what the data actually shows"
---
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lead routing and SLA benchmarks: what the data actually shows | Fieldnotes Ops</title>
<meta name="description" content="The response-time research behind the 5-minute rule, what it actually found, how vendor blogs distort it, where SLAs break in practice, and a defensible starting SLA.">
<link rel="canonical" href="https://fieldnotesops.com/guides/lead-routing-sla-benchmarks/">
<link rel="stylesheet" href="../../assets/playbook.css">
<style>
.site-header{border-bottom:1px solid var(--rule)}
.header-inner{width:min(1120px,calc(100% - 48px));margin-inline:auto;min-height:84px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.wordmark{display:inline-flex;align-items:center;gap:10px;text-decoration:none;font-weight:700;font-size:20px}
.wordmark .mark{width:32px;height:32px;display:grid;place-items:center;background:var(--ink);color:#fff;border-radius:4px;font-family:var(--mono);font-weight:500}
.header-nav a{text-decoration:none;color:var(--ink);border:1px solid var(--rule);padding:8px 14px;border-radius:4px;font-weight:600;font-size:15px}
.free{font-family:var(--mono);font-size:13px;color:var(--muted);margin:0 0 8px}
</style>
</head>
<body>
<header class="site-header"><div class="header-inner">
  <a class="wordmark" href="https://fieldnotesops.com/"><span class="mark">f.</span>Fieldnotes Ops</a>
  <nav class="header-nav" aria-label="Site"><a href="https://fieldnotesops.com/products/lead-routing-sla-playbook/">The playbook, €19</a></nav>
</div></header>

<div class="wrap">
<nav class="toc" aria-label="Contents">
  <div class="brand">Contents</div>
  <ol>
    <li><a href="#core">What the research found</a></li>
    <li><a href="#drift">How the numbers drift</a></li>
    <li><a href="#sources">Vendor data vs research</a></li>
    <li><a href="#break">Where SLAs break</a></li>
    <li><a href="#minimal">A starting SLA</a></li>
    <li><a href="#refs">References</a></li>
  </ol>
</nav>

<main>
<p class="free">Free guide</p>
<h1>Lead routing and SLA benchmarks: what the data actually shows</h1>
<p class="sub">The five-minute rule is real, older than most people assume, and routinely misquoted. Here is what the original research found, what it doesn't cover, and what to do about it.</p>

<h2 id="core"><span class="n">Section 1</span>What the research found</h2>

<p>Two pieces of work sit under almost every speed-to-lead claim you will read.</p>

<p><strong>The Lead Response Management Study, 2007.</strong> Dr James Oldroyd, then at MIT Sloan, analysed roughly 15,000 leads and over 100,000 call attempts across six companies, in partnership with InsideSales.com. Two findings are quoted constantly: the odds of <em>contacting</em> a lead were about 100 times higher when the first call went out at 5 minutes rather than 30, and the odds of <em>qualifying</em> a lead were about 21 times higher over the same interval. Between 5 and 10 minutes, qualification odds had already fallen roughly fourfold.</p>

<p><strong>"The Short Life of Online Sales Leads," Harvard Business Review, 2011.</strong> Oldroyd with Kristina McElheran and David Elkington audited 2,241 US companies by submitting a test enquiry to each. Average response time among firms that responded at all was 42 hours. Twenty-three percent never responded. Firms responding within an hour were nearly seven times more likely to have a meaningful conversation with a decision maker than those waiting one more hour.</p>

<div class="callout">These are two different studies with two different designs. The 100x and 21x multiples are from the 2007 MIT/InsideSales work, not from HBR. The 42-hour average and the 7x figure are from the 2011 HBR audit. They are mixed up in most articles you will find, which is a useful test of whether the author read the sources.</div>

<h2 id="drift"><span class="n">Section 2</span>How the numbers drift</h2>

<p>Three things to know before you put any of this in a board deck.</p>

<ul>
<li><strong>The primary data is old.</strong> The 2007 study predates live chat, calendar-booking links and most modern marketing automation. It describes web-form leads calling a B2B inside sales team in the mid-2000s. It says nothing directly about product-led signups, partner-sourced leads, or enterprise ABM.</li>
<li><strong>It measured call attempts.</strong> If your first touch is an email, the clock still matters, but the mechanism (catching a buyer while they are still at their desk thinking about the problem) is weaker. Where you can call, call.</li>
<li><strong>Speed helps contact and qualification, not closing.</strong> Nothing here shows that responding faster wins deals with buyers who were never a fit. Speed removes a reason to lose. It does not create a reason to win.</li>
</ul>

<p>Claims like "78% of buyers choose the first vendor to respond" circulate widely and trace back to vendor-published material without full methodology. Directional at best.</p>

<h2 id="sources"><span class="n">Section 3</span>Vendor data vs independent research</h2>

<div class="tbl"><table>
<tr><th>Source</th><th>Type</th><th>Use it for</th><th>Caveat</th></tr>
<tr><td>Oldroyd, Lead Response Management Study (2007)</td><td>Academic, MIT Sloan, with a vendor partner</td><td>The shape of the decay curve</td><td>Nearly two decades old; inside sales, web-form context; the vendor partner sells response software</td></tr>
<tr><td>Oldroyd, McElheran, Elkington, HBR (2011)</td><td>Peer-reviewed publication, audit design</td><td>How slow the average company actually is</td><td>US firms, 2011; response norms have shifted since</td></tr>
<tr><td>InsideSales.com / XANT whitepapers</td><td>Vendor</td><td>Talking points</td><td>Methodology not public; company sells the remedy</td></tr>
<tr><td>Routing vendor blogs (LeanData, Chili Piper and similar)</td><td>Vendor</td><td>Implementation patterns and tool comparisons</td><td>Selection bias toward their own customers</td></tr>
<tr><td>Conversational marketing surveys</td><td>Vendor survey</td><td>Chat response norms</td><td>Self-reported; chat-specific, not phone or email SLA data</td></tr>
</table></div>

<p>A workable rule: if a number does not come with an author, a year and a described method, it does not go in the deck.</p>

<h2 id="break"><span class="n">Section 4</span>Where SLAs break in practice</h2>

<p>These patterns are reported consistently across implementation write-ups and practitioner accounts. They are not statistically proven; they are the failure modes you should expect.</p>

<ol>
<li><strong>Assignment and response are measured in different systems.</strong> The CRM enforces "assign within a minute" while the rep's obligation to actually call is tracked in a spreadsheet or nowhere. Assignment speed gets optimised; response speed doesn't move.</li>
<li><strong>Round robin ignores capacity and availability.</strong> Leads go to reps on leave or already sitting on forty open records. The clock starts on a lead that will realistically wait hours.</li>
<li><strong>Breach alerts without reassignment.</strong> Most setups notify on breach; few reassign automatically. Within a week the notification is noise.</li>
<li><strong>Working hours are not modelled.</strong> A five-minute SLA quietly becomes five minutes during headquarters hours, which is a fourteen-hour wait for a buyer in another region. Decide whether you are measuring elapsed or covered minutes, and report both.</li>
<li><strong>Definition drift.</strong> "Response" means attempted call to one team and connected call to another. Compliance numbers get reported before anyone agrees which it is.</li>
<li><strong>No holdout for existing customers.</strong> An expansion enquiry from a current customer lands in the new-business pool because the form said "1 to 50 employees".</li>
</ol>

<h2 id="minimal"><span class="n">Section 5</span>A starting SLA</h2>

<p>Rather than borrowing a vendor number, start here and tune it against your own data.</p>

<div class="tbl"><table>
<tr><th>Step</th><th>Target</th><th>Notes</th></tr>
<tr><td>Assignment</td><td>Under 2 minutes, system-enforced</td><td>Event-triggered, never batched. Move slow enrichment after assignment.</td></tr>
<tr><td>First touch, high intent</td><td>Under 5 to 15 minutes in the queue's working hours</td><td>Demo and contact-sales requests, named accounts, enterprise.</td></tr>
<tr><td>First touch, volume queues</td><td>Under 30 minutes</td><td>Set a target you can staff. An unmet 5-minute SLA is worse than a met 15-minute one.</td></tr>
<tr><td>Out of hours</td><td>Automated acknowledgement, clock resumes at open</td><td>Report covered and elapsed minutes separately so weekend waiting stays visible.</td></tr>
<tr><td>Escalation</td><td>Alert at the SLA, reassign at twice it</td><td>Reassign, don't just notify. Add a cooldown so leads don't ping-pong.</td></tr>
<tr><td>Reporting</td><td>Attempt and connect tracked separately</td><td>Bucket leads by time to first touch and compare qualification rates. That is your own version of the curve.</td></tr>
</table></div>

<p>After four to six weeks you will have enough data to see where your own contact rate falls off, which is a better basis for the target than anything in a 2007 study.</p>

<h2 id="refs"><span class="n">Section 6</span>References</h2>

<ol class="sources">
<li>Oldroyd, J. (2007). <em>Lead Response Management Study</em>. MIT Sloan with InsideSales.com. Approximately 15,000 leads and 100,000+ call attempts across six companies.</li>
<li>Oldroyd, J., McElheran, K., Elkington, D. (2011). "The Short Life of Online Sales Leads." <em>Harvard Business Review</em>, March 2011. Audit of 2,241 US firms.</li>
<li>Vendor whitepapers and implementation blogs, reviewed for failure patterns and tooling options rather than benchmark figures.</li>
</ol>

<div class="callout">The full routing matrix, escalation ladder, CRM build notes and two editable CSVs are in the <a href="https://fieldnotesops.com/products/lead-routing-sla-playbook/">Lead Routing &amp; SLA Playbook</a>, €19.</div>

<footer>Fieldnotes Ops. Practical playbooks for the people who build revenue systems.</footer>
</main>
</div>
</body>
</html>
