"""Carepedia page content. Each page is a body fragment; build.py wraps it in the shared frame."""

SITE_NAME = "Carepedia"


def ed(anchor):
    return f'<span class="editsection">[<a href="#{anchor}">edit</a>]</span>'


def h2(anchor, text):
    return f'<h2 id="{anchor}">{text}{ed(anchor)}</h2>'


def see(*links):
    items = ", ".join(f'<a href="{h}">{t}</a>' for h, t in links)
    return f'<p class="hatnote">Main articles: {items}</p>'


INFOBOX = '''
<table class="infobox">
  <caption>CareBridge</caption>
  <tbody>
    <tr><td colspan="2" class="infobox-image">
      <img src="assets/photos/runner-up.jpg" alt="Vidhursh Kumar holding the Build to Care runner-up board" width="1100" height="825" />
      <div class="infobox-caption">The runner-up board at the Build to Care hackathon, 9 October 2026</div>
    </td></tr>
    <tr><th scope="row">Developer</th><td>Vidhursh Kumar</td></tr>
    <tr><th scope="row">Origin</th><td><a href="origin.html">Build to Care</a> hackathon team of five (runner-up)</td></tr>
    <tr><th scope="row">First built</th><td>October 2026</td></tr>
    <tr><th scope="row">Latest version</th><td>v1 (Expo SDK 58), November 2026</td></tr>
    <tr><th scope="row">Platforms</th><td>iOS, Android (Expo); web admin console</td></tr>
    <tr><th scope="row">Languages</th><td><a href="languages.html">English, Tamil, Hindi</a></td></tr>
    <tr><th scope="row">Built with</th><td><a href="technology.html">FastAPI, Supabase, Groq gpt-oss, Expo, React</a></td></tr>
    <tr><th scope="row">Status</th><td>Working demo; <a href="roadmap.html">v2</a> in planning</td></tr>
  </tbody>
</table>'''

# ---------------------------------------------------------------- main page (portal)
MAIN = '''
<div class="mp-welcome">
  <div class="mp-welcome-text">
    <h2>Welcome to <a href="carebridge.html">Carepedia</a>,</h2>
    <p>the free encyclopedia of one hospital follow-up app, <a href="carebridge.html">CareBridge</a>.</p>
    <p class="mp-count"><a href="all-pages.html">12 articles</a> in <a href="languages.html">English</a> · written by one developer · no login needed</p>
  </div>
  <ul class="mp-portals">
    <li><a href="how-it-works.html">How it works</a></li>
    <li><a href="features.html">Features</a></li>
    <li><a href="languages.html">Languages</a></li>
    <li><a href="origin.html">Origin</a></li>
    <li><a href="design.html">Design</a></li>
    <li><a href="all-pages.html">All pages</a></li>
  </ul>
</div>

<div class="mp-cols">
  <div class="mp-col">
    <section class="mp-box tfa">
      <h2>From today's featured article</h2>
      <div class="mp-body">
        <img class="mp-left" src="assets/screens/mobile-home.jpg" alt="CareBridge patient home screen" width="96" height="208" />
        <p><b><a href="carebridge.html">CareBridge</a></b> is a hospital discharge follow-up app. It turns a patient's
          discharge summary into a doctor-approved, day-by-day plan of medicines, tests, appointments and warning signs,
          and reminds the patient and their family in English, Tamil or Hindi. The idea began at the
          <a href="origin.html">Build to Care</a> hackathon in October 2026, where its team of five finished runner-up
          without a working demo. In the month that followed, its developer built one: a mobile app, a hospital admin
          console and the service behind them. Its guiding rule is <i>"AI reads, rules decide, a doctor approves"</i>
          (<a href="carebridge.html"><b>Full article…</b></a>)</p>
        <p class="mp-more">Recently featured: <a href="how-it-works.html">How it works</a> –
          <a href="languages.html">Languages</a> – <a href="reliability.html">Reliability</a></p>
      </div>
    </section>

    <section class="mp-box dyk">
      <h2>Did you know…</h2>
      <div class="mp-body">
        <img class="mp-right" src="assets/photos/asleep.jpg" alt="The developer asleep across two office chairs" width="96" height="124" />
        <ul>
          <li>… that CareBridge <a href="languages.html">never sends a drug name or dose through an AI translator</a>?</li>
          <li>… that a doctor must <a href="how-it-works.html">approve every plan</a> before a single reminder reaches a patient?</li>
          <li>… that the first family member to join a patient's care becomes the <a href="features.html#family-hub">Hub Manager</a>?</li>
          <li>… that a plan left waiting 12 hours for a doctor is <a href="features.html#admin-console">flagged as overdue</a>?</li>
          <li>… that the developer (<i>pictured</i>) was photographed <a href="origin.html#popular-culture">asleep across two office chairs</a> during the hackathon?</li>
        </ul>
      </div>
    </section>
  </div>

  <div class="mp-col">
    <section class="mp-box fm">
      <h2>Featured mascots</h2>
      <div class="mp-body">
        <img class="mp-wide" src="assets/brand/mascots.jpg" alt="The grandmother and nurse mascots of CareBridge" width="640" height="372" />
        <p>The <b>grandmother</b> and the <b>nurse</b> greet patients on the language screen of the
          <a href="features.html#patient-app">CareBridge app</a>. With a seedling robot and the console's fox, they
          make up the app's <a href="design.html#mascots">four mascots</a>. The nurse is also the face of this
          encyclopedia.</p>
      </div>
    </section>

    <section class="mp-box itn">
      <h2>In the news</h2>
      <div class="mp-body">
        <ul>
          <li><b>27 November 2026</b> – Carepedia goes live; a <a href="roadmap.html">security plan for version 2</a> is written.</li>
          <li><b>16 November 2026</b> – The project README and a LinkedIn carousel, <i>"No demo. So I built one."</i>, are prepared.</li>
          <li><b>14 November 2026</b> – The mobile app moves to Expo SDK 58 with <a href="design.html#mascots">new mascot artwork</a>.</li>
          <li><b>14 November 2026</b> – The project is <a href="history.html">restored</a> after its folder was accidentally deleted.</li>
          <li><b>9 October 2026</b> – The team finishes <a href="origin.html">runner-up at Build to Care</a>.</li>
        </ul>
        <p class="mp-more"><a href="history.html">Recent changes</a> – <a href="design.html#launch-video">Launch video</a></p>
      </div>
    </section>

    <section class="mp-box otd">
      <h2>Watch</h2>
      <div class="mp-body">
        <a class="mp-video" href="design.html#launch-video"><img src="assets/video/poster.jpg" alt="Play the CareBridge launch film" width="1024" height="576" /><span>&#9654; 25 s</span></a>
        <p>The narrated <a href="design.html#launch-video">CareBridge launch film</a>, cut from the working app.</p>
      </div>
    </section>
  </div>
</div>

<section class="mp-box explore">
  <h2>Explore Carepedia</h2>
  <div class="mp-body explore-grid">
    <div><h3>The product</h3><ul>
      <li><a href="carebridge.html">CareBridge</a></li><li><a href="features.html">Features</a></li>
      <li><a href="features.html#patient-app">Patient app</a></li><li><a href="features.html#admin-console">Admin console</a></li></ul>
      <p class="all"><a href="all-pages.html">all product articles…</a></p></div>
    <div><h3>Concepts</h3><ul>
      <li><a href="how-it-works.html">How it works</a></li><li><a href="languages.html">Drug names stay exact</a></li>
      <li><a href="reliability.html">Reliability</a></li><li><a href="how-it-works.html#approve">Doctor approval</a></li></ul>
      <p class="all"><a href="all-pages.html">all concept articles…</a></p></div>
    <div><h3>Making of</h3><ul>
      <li><a href="technology.html">Technology</a></li><li><a href="design.html">Design</a></li>
      <li><a href="design.html#launch-video">Launch video</a></li><li><a href="roadmap.html">Roadmap</a></li></ul>
      <p class="all"><a href="all-pages.html">all making-of articles…</a></p></div>
    <div><h3>History</h3><ul>
      <li><a href="origin.html">Build to Care</a></li><li><a href="history.html">Revision history</a></li>
      <li><a href="history.html#restore">The restore</a></li><li><a href="origin.html#popular-culture">In popular culture</a></li></ul>
      <p class="all"><a href="all-pages.html">all history articles…</a></p></div>
    <div><h3>Care lore</h3><ul>
      <li><a href="design.html#mascots">The mascots</a></li><li><a href="about.html">About Carepedia</a></li>
      <li><a href="all-pages.html" data-random>Random article</a></li><li><a href="about.html#developer">The developer</a></li></ul>
      <p class="all"><a href="all-pages.html">all lore articles…</a></p></div>
  </div>
</section>
'''

# ---------------------------------------------------------------- CareBridge article
CAREBRIDGE = INFOBOX + '''
<p><b>CareBridge</b> is a hospital discharge follow-up app. It turns a patient's discharge summary into a
  doctor-approved, day-by-day plan of medicines, tests, appointments and warning signs, and reminds the patient
  and their family in English, Tamil or Hindi.<sup class="reference"><a href="#cite-1">[1]</a></sup></p>
<p>The idea began at <a href="origin.html"><i>Build to Care</i></a>, a hackathon organised by Acentra Health in
  October 2026, where its team of five finished as runner-up.<sup class="reference"><a href="#cite-2">[2]</a></sup>
  In the month that followed, Vidhursh Kumar built it into a working mobile app, a hospital admin console and the
  service behind them.<sup class="reference"><a href="#cite-3">[3]</a></sup></p>

<div class="toc" role="navigation" aria-labelledby="toc-heading">
  <div class="toc-title" id="toc-heading">Contents <span>[<button class="toc-toggle" type="button" aria-expanded="true">hide</button>]</span></div>
  <ol>
    <li><a href="#problem">The problem</a></li>
    <li><a href="#approach">Approach</a></li>
    <li><a href="#parts">Parts</a></li>
    <li><a href="#see-also">See also</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</div>

''' + h2("problem", "The problem") + '''
<p>A discharge summary is written for clinicians. At home, a patient and their family must turn it into a daily
  routine: which tablet after breakfast, which test on which day, which symptom means coming back. CareBridge does
  that conversion, and keeps a doctor in charge of it.</p>

''' + h2("approach", "Approach") + see(("how-it-works.html", "How it works")) + '''
<p>The design principle is often summarised as <i>"AI reads, rules decide, a doctor approves."</i> The model only
  reads; deterministic rules check what it found; and nothing reaches a patient before a doctor has approved it.</p>

''' + h2("parts", "Parts") + see(("features.html", "Features")) + '''
<table class="wikitable">
  <thead><tr><th>Part</th><th>Who uses it</th><th>What it does</th></tr></thead>
  <tbody>
    <tr><td><a href="features.html#patient-app">Patient app</a></td><td>Patient</td><td>Daily plan, reminders read aloud, calendar, map</td></tr>
    <tr><td><a href="features.html#family-hub">Family hub</a></td><td>Family</td><td>Shared care, missed-dose alerts, pill photos</td></tr>
    <tr><td><a href="features.html#doctor-review">Doctor review</a></td><td>Doctor</td><td>Summary beside plan, edit, approve</td></tr>
    <tr><td><a href="features.html#admin-console">Admin console</a></td><td>Hospital</td><td>Triage, workload, reassignment, provider map</td></tr>
  </tbody>
</table>

''' + h2("see-also", "See also") + '''
<ul>
  <li><a href="history.html">Revision history</a>: the project timeline, from the hackathon to v2</li>
  <li><a href="design.html#launch-video">Launch video</a></li>
  <li><a href="roadmap.html">Roadmap</a></li>
</ul>

''' + h2("references", "References") + '''
<ol class="references">
  <li id="cite-1">Kumar, Vidhursh (2026). <i>CareBridge project specification and README</i>.</li>
  <li id="cite-2">Acentra Health; Hackforge.ai (9 October 2026). <i>Build to Care hackathon: runner-up board</i> (photograph, infobox).</li>
  <li id="cite-3">Kumar, Vidhursh (November 2026). <i>CareBridge decision log and build notes</i>.</li>
</ol>
'''

# ---------------------------------------------------------------- How it works
HOW = '''
<p class="hatnote">This article is about the discharge-summary pipeline. For the app's screens, see <a href="features.html">Features</a>.</p>
<p>A discharge summary (a PDF, a photo or plain text) passes through a fixed sequence of seven steps before
  anything reaches a patient. Click a step to read what it does.</p>
<ol class="pipeline" data-pipeline>
  <li tabindex="0"><b>Read</b><span>PDF text, or a photo through OCR</span></li>
  <li tabindex="0"><b>Validate</b><span>Is this a discharge summary for this patient?</span></li>
  <li tabindex="0"><b>Extract</b><span>gpt-oss-120b lifts each instruction with its exact source line</span></li>
  <li tabindex="0"><b>Verify</b><span>Every value must appear in the source; dates are resolved from the discharge date</span></li>
  <li tabindex="0"><b>Flag</b><span>Missing doses, vague words and duplicates go to the doctor as "needs review"</span></li>
  <li tabindex="0" id="approve"><b>Approve</b><span>The doctor edits any item and approves the whole plan at once</span></li>
  <li tabindex="0" class="final"><b>Remind</b><span>Daily reminders and a calendar for the patient and family</span></li>
</ol>
<div class="pipe-detail" aria-live="polite"><b>Read</b> – PDF text, or a photo through OCR</div>

''' + h2("principle", "Principle") + '''
<p><i>"AI reads, rules decide, a doctor approves."</i> The language model is only trusted to <i>find</i>
  instructions. Whether a value is real is decided by rules that compare it against the source text, and whether
  the plan is right is decided by a doctor.</p>

''' + h2("why", "Why a doctor approves") + '''
<p>Nothing reaches a patient before doctor approval. A doctor sees the original summary beside the extracted plan,
  with the source line under every item, and can edit any item before approving the whole plan at once.</p>
'''

# ---------------------------------------------------------------- Features
FEATURES = '''
<figure class="thumb tright"><img src="assets/screens/mobile-home.jpg" alt="Patient home screen" width="480" height="1039" loading="lazy" /><figcaption>The patient home, with warning signs on top. Synthetic data.</figcaption></figure>
<p><a href="carebridge.html">CareBridge</a> has four parts, one for each person in a patient's recovery.</p>
''' + h2("patient-app", "Patient app") + '''
<p>A mobile app with home, reminders, map and settings. Doses fall into morning, afternoon and night slots, can be
  read aloud, and are marked as taken by the patient or the family's Hub Manager.</p>
''' + h2("family-hub", "Family hub") + '''
<p>Family members join a patient's care. The first to join becomes the <i>Hub Manager</i>, who can mark tasks done
  and add photos of the patient's pills. If a dose is missed, the family receives an alert.</p>
''' + h2("doctor-review", "Doctor review") + '''
<p>Doctors see the original summary beside the extracted plan, with the source line under every item. Every edit
  keeps a history of who changed what.</p>
''' + h2("admin-console", "Hospital admin console") + '''
<figure class="thumb tright wide"><img src="assets/screens/web-patients.jpg" alt="Admin console: what needs attention now" width="1100" height="688" loading="lazy" /><figcaption>What needs attention now.</figcaption></figure>
<p>A web console shows what needs attention first: plans waiting longer than 12 hours for a doctor are flagged as
  overdue, and a doctor marked unavailable has their pending plans moved to the best available colleague.</p>
''' + h2("provider-map", "Provider map") + '''
<p>A map suggests nearby doctors, hospitals and laboratories, filtered by the specialties in the patient's plan.
  Each pin is labelled as a suggested location to confirm before visiting.</p>
<div class="clear"></div>
'''

# ---------------------------------------------------------------- Languages
LANG = '''
<p>Reminders are available in English, Tamil and Hindi. Medicines never pass through an AI translator: a fixed
  template keeps the drug name and dose exactly as the doctor wrote them, and only the surrounding words change
  language. Pick a language to see the same reminder.</p>
<div class="lang-demo">
  <div class="lang-pick" role="tablist" aria-label="Reminder language">
    <button type="button" role="tab" aria-selected="true" data-lang="en"><img src="assets/brand/lang-en.png" alt="" width="40" height="40" />English</button>
    <button type="button" role="tab" aria-selected="false" data-lang="ta"><img src="assets/brand/lang-ta.png" alt="" width="40" height="40" />தமிழ்</button>
    <button type="button" role="tab" aria-selected="false" data-lang="hi"><img src="assets/brand/lang-hi.png" alt="" width="40" height="40" />हिन्दी</button>
  </div>
  <p class="reminder" aria-live="polite"><b class="drug">Clopidogrel 75 mg</b> · <span class="rest" data-en="after breakfast" data-ta="காலை உணவுக்குப் பின்" data-hi="नाश्ते के बाद">after breakfast</span> · 8:00 AM</p>
  <p class="lang-note">The highlighted drug name and dose never change.</p>
</div>
''' + h2("table", "All three") + '''
<table class="wikitable">
  <thead><tr><th>Language</th><th>Reminder</th></tr></thead>
  <tbody>
    <tr><td>English</td><td><b>Clopidogrel 75 mg</b> · after breakfast · 8:00 AM</td></tr>
    <tr><td>Tamil</td><td lang="ta"><b>Clopidogrel 75 mg</b> · காலை உணவுக்குப் பின் · 8:00 AM</td></tr>
    <tr><td>Hindi</td><td lang="hi"><b>Clopidogrel 75 mg</b> · नाश्ते के बाद · 8:00 AM</td></tr>
  </tbody>
</table>
''' + h2("why", "Why drug names stay exact") + '''
<p>A translated drug name can become a different drug, and a reworded dose can become a different dose. Keeping
  them byte-for-byte as the doctor approved them is the heart of the project.</p>
'''

# ---------------------------------------------------------------- Design
DESIGN = '''
<p>CareBridge uses a white and green visual system. Screens below use synthetic test data.</p>
''' + h2("mascots", "Mascots") + '''
<figure class="thumb tright"><img src="assets/brand/mascots.jpg" alt="The grandmother and nurse mascots" width="640" height="372" loading="lazy" /><figcaption>The grandmother and the nurse.</figcaption></figure>
<p>The app has three mascots: a nurse, a grandmother and a seedling robot. The admin console has a fourth, a fox.
  The nurse is also Carepedia's logo.</p>
<div class="clear"></div>
''' + h2("screens", "Screens") + '''
<ul class="gallery">
  <li><figure class="thumb"><img src="assets/screens/mobile-splash.jpg" alt="Splash screen" loading="lazy" width="480" height="1039" /><figcaption>Splash</figcaption></figure></li>
  <li><figure class="thumb"><img src="assets/screens/mobile-language.jpg" alt="Language picker" loading="lazy" width="480" height="1039" /><figcaption>Language picker</figcaption></figure></li>
  <li><figure class="thumb"><img src="assets/screens/mobile-home.jpg" alt="Patient home with warning signs" loading="lazy" width="480" height="1039" /><figcaption>Patient home</figcaption></figure></li>
  <li><figure class="thumb"><img src="assets/screens/mobile-map.jpg" alt="Provider map" loading="lazy" width="480" height="1039" /><figcaption>Provider map</figcaption></figure></li>
</ul>
<ul class="gallery wide">
  <li><figure class="thumb"><img src="assets/screens/web-patients.jpg" alt="Admin console: patients" loading="lazy" width="1100" height="688" /><figcaption>What needs attention now</figcaption></figure></li>
  <li><figure class="thumb"><img src="assets/screens/web-doctors.jpg" alt="Admin console: doctors" loading="lazy" width="1100" height="688" /><figcaption>Doctors, availability and workload</figcaption></figure></li>
  <li><figure class="thumb"><img src="assets/screens/web-plan.jpg" alt="Discharge summary beside the approved plan" loading="lazy" width="1100" height="688" /><figcaption>The summary beside the approved plan</figcaption></figure></li>
  <li><figure class="thumb"><img src="assets/screens/web-map.jpg" alt="Hospital map of providers" loading="lazy" width="1100" height="688" /><figcaption>Provider coverage map</figcaption></figure></li>
</ul>
''' + h2("launch-video", "Launch video") + '''
<figure class="thumb video">
  <video controls muted playsinline preload="metadata" poster="assets/video/poster.jpg" width="1024" height="576">
    <source src="assets/video/carebridge-launch.mp4" type="video/mp4" />
  </video>
  <figcaption>The 25-second CareBridge launch film, narrated. Sound is off until you turn it on.</figcaption>
</figure>
'''

# ---------------------------------------------------------------- Origin
ORIGIN = '''
<figure class="thumb tright"><img src="assets/photos/elephant-night.jpg" alt="Vidhursh Kumar standing beside a stone elephant carving at night" width="1400" height="1050" loading="lazy" /><figcaption>Vidhursh Kumar, developer of CareBridge.</figcaption></figure>
<p><i>Build to Care</i> was a hackathon organised by Acentra Health and powered by Hackforge.ai, held at SRM on
  8–9 October 2026. CareBridge's team of five placed first of 30 teams in the opening round and second in the final
  round of five, finishing as runner-up with a cash prize of ₹40,000.</p>
''' + h2("no-demo", "No demo") + '''
<p>In the final round the team had the idea but no working demonstration, which Vidhursh later described as the
  difference between first and second place. Over the next month he learnt to build with Claude Code and produced
  the working version described in <a href="carebridge.html">the main article</a>. The team has been invited to
  interviews expected in January 2027.</p>
<div class="clear"></div>
''' + h2("popular-culture", "In popular culture") + '''
<figure class="thumb tleft"><img src="assets/photos/asleep.jpg" alt="Vidhursh Kumar asleep across two office chairs, an energy drink on the floor" width="975" height="1260" loading="lazy" /><figcaption>Field research into discharge recovery, October 2026.</figcaption></figure>
<p>A photograph from the hackathon shows the developer asleep across two office chairs, a can of energy drink on
  the floor beside him. Carepedia's editors regard it as the project's earliest recorded recovery period.</p>
<div class="clear"></div>
'''

# ---------------------------------------------------------------- Reliability
RELIABILITY = '''
<p>A follow-up app is only useful if it never doubles a reminder and never loses an approval.</p>
<table class="wikitable">
  <thead><tr><th>Risk</th><th>What CareBridge does</th></tr></thead>
  <tbody>
    <tr><td>Approved and reassigned at once</td><td>Approval happens in a single locked database transaction</td></tr>
    <tr><td>AI service busy</td><td>Uploads join a queue that retries</td></tr>
    <tr><td>Duplicate reminders</td><td>Each reminder is created exactly once</td></tr>
    <tr><td>Two servers notice a missed dose</td><td>The alert is still sent once</td></tr>
    <tr><td>A plan nobody reviews</td><td>After 12 hours it is flagged overdue on the admin console</td></tr>
  </tbody>
</table>
'''

# ---------------------------------------------------------------- Technology
TECH = '''
<table class="wikitable">
  <thead><tr><th>Part</th><th>Built with</th></tr></thead>
  <tbody>
    <tr><td>Service</td><td>Python, FastAPI, scheduled background jobs</td></tr>
    <tr><td>AI</td><td>Groq: gpt-oss-120b for extraction, gpt-oss-20b for non-medicine text</td></tr>
    <tr><td>Data</td><td>Supabase (Postgres and private file storage)</td></tr>
    <tr><td>Mobile</td><td>Expo (React Native), SDK 58</td></tr>
    <tr><td>Web console</td><td>React, Vite, Tailwind, shadcn/ui, Leaflet</td></tr>
    <tr><td>This encyclopedia</td><td>Plain HTML and CSS on GitHub Pages; pixel meadow drawn in Python</td></tr>
  </tbody>
</table>
''' + h2("see-also", "See also") + '''
<ul><li><a href="https://expo.dev">Expo</a></li><li><a href="https://fastapi.tiangolo.com">FastAPI</a></li><li><a href="https://supabase.com">Supabase</a></li></ul>
'''

# ---------------------------------------------------------------- Roadmap
ROADMAP = '''
<p class="hatnote">This article describes planned work. Details may change.</p>
<p>Version 2 is in planning and focuses on a security layer:</p>
<ul>
  <li><b>Hospital invite codes.</b> Hospitals using CareBridge would print a unique QR code or invite number on the
    discharge sheet, which a patient uses once to open their account.</li>
  <li><b>WhatsApp family invites.</b> A patient will share a one-time invite link with family over WhatsApp, the
    way gaming groups share invite links.</li>
  <li><b>Tested changes.</b> Every change will pass automated tests, including attack tests, kept as a dated record.</li>
</ul>
'''

# ---------------------------------------------------------------- History
HISTORY = '''
<p class="hatnote">Newest first. Each entry is a real milestone. Planned work is marked <i>planned</i>.</p>
<ul class="history">
  <li class="planned"><span class="date">Next</span> · <span class="user">Vidhursh Kumar</span> · <span class="summary">(<a href="roadmap.html">Version 2</a>: hospital invite codes, WhatsApp family invites, attack tests on every change)</span> <span class="tag">planned</span></li>
  <li><span class="date">27 November 2026</span> · <span class="user">Vidhursh Kumar</span> · <span class="summary">(v2 security plan written; Carepedia built)</span></li>
  <li><span class="date">16 November 2026</span> · <span class="user">Vidhursh Kumar</span> · <span class="summary">(Project README with screenshots; LinkedIn carousel "No demo. So I built one." prepared)</span></li>
  <li><span class="date">14 November 2026</span> · <span class="user">Vidhursh Kumar</span> · <span class="summary">(Mobile app upgraded to Expo SDK 58; new mascot artwork)</span></li>
  <li id="restore"><span class="date">14 November 2026</span> · <span class="user">Vidhursh Kumar</span> · <span class="summary">(Project restored after the folder was accidentally deleted; moved to GitHub)</span></li>
  <li><span class="date">19 October 2026</span> · <span class="user">Vidhursh Kumar</span> · <span class="summary">(Background jobs: missed-dose alerts, 12-hour escalation of overdue plans)</span></li>
  <li><span class="date">17 October 2026</span> · <span class="user">Vidhursh Kumar</span> · <span class="summary">(Hospital admin console: triage panel, doctor workload, reassignment, provider map)</span></li>
  <li><span class="date">13 October 2026</span> · <span class="user">Vidhursh Kumar</span> · <span class="summary">(Patient app: home, reminders, calendar; family hub)</span></li>
  <li><span class="date">11 October 2026</span> · <span class="user">Vidhursh Kumar</span> · <span class="summary">(Build begins: discharge-summary pipeline and doctor review)</span></li>
  <li><span class="date">8–9 October 2026</span> · <span class="user">Build to Care team</span> · <span class="summary">(<a href="origin.html">Build to Care hackathon</a>: 1st of 30 in round one, runner-up in the final)</span></li>
</ul>
'''

# ---------------------------------------------------------------- About
ABOUT = '''
<p><b>Carepedia</b> is a small encyclopedia about one app, written in the style of an old encyclopedia site. Every
  article is about <a href="carebridge.html">CareBridge</a>.</p>
''' + h2("developer", "The developer") + '''
<p>Vidhursh Kumar built CareBridge after the <a href="origin.html">Build to Care</a> hackathon and wrote every
  article here.</p>
''' + h2("data", "Data and photos") + '''
<p>All app data shown is synthetic. Photos show only the developer.</p>
'''

PAGES = {}


def page(slug, title, description, body, **kw):
    PAGES[slug] = dict(title=title, description=description, body=body, **kw)


page("index.html", "Main Page", "Carepedia, the free encyclopedia of CareBridge: a hospital discharge follow-up app with doctor-approved plans and reminders in English, Tamil and Hindi.",
     MAIN, portal=True, tabs=False, heading="Main Page")
page("carebridge.html", "CareBridge", "CareBridge turns a hospital discharge summary into a doctor-approved follow-up plan, with reminders for patients and families in English, Tamil and Hindi.", CAREBRIDGE)
page("how-it-works.html", "How it works", "The seven steps from a discharge summary to a doctor-approved plan.", HOW)
page("features.html", "Features", "The CareBridge patient app, family hub, doctor review and hospital admin console.", FEATURES)
page("languages.html", "Languages", "CareBridge reminders in English, Tamil and Hindi, with drug names and doses never translated.", LANG)
page("design.html", "Design", "CareBridge screens, mascots and the launch film.", DESIGN)
page("origin.html", "Build to Care", "How CareBridge began at the Build to Care hackathon, October 2026.", ORIGIN)
page("reliability.html", "Reliability", "How CareBridge avoids double reminders and lost approvals.", RELIABILITY)
page("technology.html", "Technology", "What CareBridge is built with.", TECH)
page("roadmap.html", "Roadmap", "CareBridge version 2: a security layer.", ROADMAP)
page("history.html", "CareBridge: Revision history", "The CareBridge timeline, from the Build to Care hackathon to version 2.", HISTORY)
page("about.html", "About Carepedia", "About this encyclopedia.", ABOUT)


def _all_pages():
    rows = "\n".join(f'  <li data-title="{p["title"].lower()} {p["description"].lower()}"><a href="{s}">{p["title"]}</a> – {p["description"]}</li>'
                     for s, p in PAGES.items())
    return f'''
<p class="search-status" aria-live="polite">All {len(PAGES) + 1} pages of Carepedia, in reading order.</p>
<ul class="allpages">
{rows}
  <li data-title="all pages"><a href="all-pages.html">All pages</a> – This list.</li>
</ul>
'''


page("all-pages.html", "All pages", "Every page of Carepedia.", _all_pages(), tabs=False)
