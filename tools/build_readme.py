R = "https://raw.githubusercontent.com/ilhamrafi44/ilhamrafi44/main/assets"
V = "v=4"

def pic(name, alt, **kw):
    """One physical line: multi-line <picture> makes GitHub split the <p>."""
    attrs = "".join(f' {k}="{v}"' for k, v in kw.items())
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{R}/{name}-dark.svg?{V}">'
            f'<img alt="{alt}" src="{R}/{name}-light.svg?{V}"{attrs}></picture>')

def sec(slug, title):
    return f'### {pic("sec-" + slug, title, height="48")}'

def badge(slug, alt, href):
    return f'<a href="{href}">{pic("badge-" + slug, alt, height="44")}</a>'

md = f"""{pic("hero", "Bonsky - Senior Full Stack Engineer", width="100%")}

{badge("linkedin", "LinkedIn", "https://www.linkedin.com/in/ilhamrafi44/")} {badge("email", "Email", "mailto:ilhamrafi44@gmail.com")} {badge("sblnet", "SBLNET", "https://sblnet.id")}

{sec("whoami", "WHOAMI")}

```console
$ whoami
Muhammad Ilham Rafiannandha

$ whoami --short
Ilham Rafi

$ whoami --what-people-actually-call-me
Bonsky

$ cat ~/.bio
Full stack engineer, 6+ years. I build the systems where being wrong costs
real money -- billing engines, double-entry ledgers, payment gateways, and
the routers that decide whether your stream buffers tonight.

Backend is home        : Java / Spring Modulith, Laravel, NestJS, Go
Frontend when it must look good : Next.js, Vue, React
Mobile when it must fit in a pocket : React Native, Flutter, KMP
Network when the packets need somewhere to go : FreeRADIUS, MikroTik

$ cat ~/.plot_twist
My degree is in English Literature. GPA 3.60.
Four years of Shakespeare, and now I argue with a compiler for a living.
Same energy, honestly. Neither one ever tells you what it actually wants.

$ cat ~/.red_flags
1. I have strong opinions about storing money as integer cents.
   Nobody has ever asked me. I tell them anyway.
2. I wrote an entire CLI from scratch to avoid booting one Windows VM.
   "Ten minutes," I said. Reader, it was not ten minutes.
3. "It's a small refactor" is a sentence I have said out loud, in public,
   to people who trusted me.

$ sudo make me a sandwich
Okay.
```

{pic("stats", "6+ years shipping, 11 companies and clients, 25+ products shipped, 0 known bugs", width="100%")}

<sub><b>*</b> the load-bearing word in that last box is <i>known</i>.</sub>

{sec("now", "NOW")}

- 🛰️ **Keeping Jakarta online** at **[SBLNET](https://sblnet.id)** — an ISP platform where 27 Spring Modulith modules, 8 PostgreSQL databases and a rack of MikroTik routers collectively decide whether your stream buffers tonight. Genuinely no pressure.
- 🏠 **Two property platforms in production** — [BigProperty](https://bigproperty.online) and [White Box](https://propertywhitebox.com). Real bookings, real money, real messages at 2 AM.
- 📸 **[Itoya Self Photo Studio](https://itoya.my.id)** — the booking platform *and* the remote-management agent that babysits the studio PCs. Because when a booth freezes at midnight, somebody has to reboot it, and I would prefer that somebody to be a C++ daemon rather than me, in a car.
- 🍎 **[mfu-macos](https://github.com/ilhamrafi44/mfu-macos)** — a native Xiaomi bootloader-unlock CLI for Apple Silicon, written entirely out of spite for having to boot Windows.
- 📈 **nocturads** — a CPA routing engine in Go + Fiber + SvelteKit + TimescaleDB, because apparently my idea of resting is writing another backend.

{sec("the-arsenal", "THE ARSENAL")}

{pic("stack", "Stack: backend, frontend, mobile, data, infrastructure, network, payments, systems", width="100%")}

{sec("war-stories", "WAR STORIES")}

> Most of what I have shipped lives in employer and client repositories — private, and in
> several cases repositories my access ended with the contract. Eight public repos is not the
> size of the work; it is the size of what I am allowed to hand you. So: the systems, what was
> hard about them, and a live URL wherever one still exists.

#### 🛰️ ISP Subscriber Platform — [SBLNET](https://sblnet.id)

An entire ISP's subscriber lifecycle in one platform: onboarding → automated network
provisioning → recurring billing → double-entry accounting → payment collection across
multiple gateways and a direct host-to-host bank integration.

| | |
|---|---|
| **Architecture** | 27-module modular monolith on Spring Modulith — hexagonal / DDD, event-driven module boundaries |
| **Persistence** | 8 PostgreSQL databases, per-context ACID via multi-datasource transaction management |
| **Accounting** | Double-entry General Ledger, Journal Entries, Chart of Accounts |
| **Billing** | Invoicing, proration, discounts, PPN/VAT — money as integer cents, because floats and money are a horror film |
| **Payments** | Pluggable gateway abstraction: Duitku (VA / QRIS / e-wallet / retail) + host-to-host BRI Fixed VA |
| **Settlement** | HMAC-verified callbacks, deterministic and idempotent VA registration, automatic invoice matching |
| **Collections** | Dunning and auto-isolation — overdue suspends the line, payment reactivates it in real time |
| **Network** | FreeRADIUS (AAA) + MikroTik RouterOS — PPPoE, live session monitoring, CoA disconnect, RADIUS accounting |
| **Ops** | NOC and OLT management: router health, incident tracking, device config backup |
| **Clients** | Next.js portals + a React Native self-service app, with a Kotlin Multiplatform rewrite in flight |

<sub>Java · Spring Boot · Spring Modulith · Spring Security + JWT · Spring Data JPA · PostgreSQL · Redis · Next.js · React Native · Kotlin Multiplatform · Jenkins · Docker</sub>

<details>
<summary><b>📸 Itoya — self-photo studio platform + remote studio management</b></summary>

<br>

[Itoya](https://itoya.my.id) is a premium self-photo studio. Customers book a booth online.
The booth is a PC. PCs freeze. That second problem is why this project has two halves.

**The booking platform** — Laravel API, Vue admin and customer dashboards, Flutter mobile app.

**The RMM** — because driving to a studio at midnight to press a power button is not a career:

- **C++ Windows agent** — DXGI desktop capture, JPEG/H.264 encoding, remote input injection
- **C++ relay** — uWebSockets server routing agent ↔ dashboard traffic
- **Flutter desktop dashboard** — live view and control of every booth
- **Rust server** — a v1 built in Rust before the v2 C++ rewrite
- **Linux agent** — X11 capture, JPEG streaming, remote shell, process manager

<sub>Laravel · Vue · Flutter · C++ · Rust · uWebSockets · DXGI · X11</sub>

</details>

<details>
<summary><b>💳 Finance &amp; Reconciliation Portal — PT Cashlez Worldwide Indonesia</b></summary>

<br>

A payment company's back office has exactly one job: prove that every rupiah that moved
actually moved. I built the thing that does the proving.

- **Two-stage reconciliation** — third-party settlement against bank mutation, then that result against back-office data
- **Discrepancy detection** — dispute amounts, missing-in-bank, missing-in-back-office
- **Disbursement** module for merchant payouts
- **Deduction** module for fees, chargebacks and adjustments

<sub>Java · Spring Boot · Next.js · Jenkins · Docker</sub>

</details>

<details>
<summary><b>☕ CoffeeLabs — HRIS, POS, inventory and a face-recognition attendance service</b></summary>

<br>

CoffeeLabs is the group I ran development for at PT Cyber Lab Indonesia. It grew into a
small suite: [company site](https://www.coffeelabs.co.id/),
[HRIS app](https://app.coffeelabs.co.id/), [back office](https://admin.coffeelabs.co.id/).

- **HRIS** — attendance with GPS check-in and geofence radius, employee management
- **Face-recognition attendance** — a separate Python model service plus a Node inference service, so people stop clocking in for each other
- **WhatsApp gateway** — a NestJS + Baileys service for notifications
- **Point of Sales**, **inventory**, and an **income journal** system
- **Led** the development team and ran the internship programme

<sub>Laravel · Java (Spring Boot) · Next.js · Vue · React Native · Python · NestJS · Jenkins · Docker</sub>

</details>

<details>
<summary><b>🕋 Umrah &amp; Hajj platforms — Elteyba Tours and SmartHajj</b></summary>

<br>

Pilgrimage travel is a logistics problem wearing a religious hat: passports, visas, seat
quotas, flight manifests, hotel room-sharing, instalment payments, and a deadline that
does not negotiate.

**[Elteyba Tours](https://www.elteybatours.com)** — licensed PPIU &amp; PIHK agency, plus the
[jamaah portal](https://elteybago.eilhamzah.com/login):

- Multi-role access (admin, agent, jamaah, coordinator) with approval flows
- Registration with passport/visa upload, group registration, package selection
- Automated invoicing, down-payment and instalment tracking, payment reminders
- Real-time seat quota, schedule assignment, flight and hotel management
- Visa tracking with status workflows and API/CSV export
- Manifest generation: flight grouping, hotel room-sharing logic, PDFs for immigration
- WhatsApp broadcast with email fallback, queue-based notifications, daily backups

**SmartHajj** — a later take on the same domain: Laravel backend, Flutter app.

<sub>Laravel · Sanctum · Livewire · Spatie Permission · Vue 3 · React Native · Flutter · MySQL/PostgreSQL · Redis · Midtrans · WhatsApp API</sub>

</details>

<details>
<summary><b>🎟️ Taman Safari Bogor — ticketing from the gate to the back office</b></summary>

<br>

Built for **GlobalTix Teknologi Indonesia**: the domestic ticketing site, its back office, and
**GT Checker**, the React Native app staff hold at the park entrance.

- **[domestic.tamansafaribogor.com](https://domestic.tamansafaribogor.com/)** — public ticketing plus the back office behind it
- **GT Checker (React Native / Expo)** — QR and barcode scanning built for a queue, not a demo, with on-device ticket printing
- **Fraud detection** — reused and forged tickets rejected at the gate rather than discovered in a report afterwards
- Integrated with the park's existing ticketing infrastructure, and iterated on feedback from the people actually standing at the turnstile

The app and back-office repositories belong to the client, and my access ended when the contract
did — which is how most contract work goes. The live site is the part I can still point at.

<sub>React Native · Expo · QR / barcode scanning · thermal printing · REST APIs</sub>

</details>

<details>
<summary><b>🇯🇵 Spectro &amp; ArkaLearn — getting Indonesians hired in Japan</b></summary>

<br>

Two products, one funnel. **[ArkaLearn](https://www.arkalearn.com/en)** teaches Japanese for work
— JLPT N5 through N3, SSW preparation, mensetsu (interview) practice. **Spectro** is the job
portal those learners graduate into.

The domain constraint shapes everything: the users are, by definition, still learning a language,
and they are applying for a visa category with its own paperwork.

- **Two-sided marketplace** — candidate and employer profiles, role chosen at signup, Google OAuth
- **Faceted job search** across category, industry, type, career level, experience and qualification — six independent axes, because "worker" is not a search query
- **Applications tracking**, saved jobs, employer following, per-job view analytics
- **In-app messaging** (conversations and messages) so hiring does not degrade into a WhatsApp thread nobody can audit
- **SSW document handling** for Japan's Specified Skilled Worker visa track — the part where a missing file costs someone a job offer
- **Multi-language throughout**, plus a blog with categories. If your users are learning Japanese, you cannot assume they read English either

<sub>Laravel · Blade · MySQL · Google OAuth · Docker</sub>

</details>

<details>
<summary><b>🏛️ DPUPR Musi Banyuasin — a government portal on a CMS I actually wrote</b></summary>

<br>

[dpupr.mubakab.go.id](https://dpupr.mubakab.go.id/) is the public portal for the Public Works and
Spatial Planning agency of Musi Banyuasin Regency, shipped under the name **INFRALOK**.

The easy version of this job is a theme and a plugin directory. The problem with the easy
version is that the people updating the site are civil servants, not developers, and every
plugin is a future CVE somebody else has to patch.

So it runs on a purpose-built Laravel CMS instead:

- **Pages and posts** with categories and tags
- **Nested menu builder** — menus and menu items as first-class records, so navigation is edited, not deployed
- **Media library** for documents and images
- **Composable home page** — `HomeSection` / `HomeSectionItem` let the landing page be rearranged from the admin panel without touching a Blade file
- **Role-based admin** for the staff who keep it current

Small surface area, no plugin ecosystem to audit, and nobody has to call me to publish an announcement.

<sub>Laravel · Blade · Tailwind · MySQL</sub>

</details>

<details>
<summary><b>🔥 Multilingual site + sales CRM — PT Taiba Cococha Indonesia</b></summary>

<br>

A coconut-shell charcoal exporter. The site sells in three languages; the CRM runs the pipeline.

- **Trilingual company profile** (English / Indonesian / Arabic) → [taibacoco.co.id](https://taibacoco.co.id)
- **CRM** — contact and lead management, status tracking, reminders, Excel/CSV import-export
- **Sales pipeline** — deal tracking, funnel metrics, performance reports
- **Task scheduler** — calendar view, assignments, automated follow-up notifications
- **Invoice and quotation** module with PDF generation and e-signatures
- **Security** — 2FA, session logs, audit trails, permission-based access

<sub>Laravel · Passport · Spatie Permissions · Queues &amp; Events · Vue 3 + Pinia · MySQL · Redis · DomPDF</sub>

</details>

{sec("career", "CAREER")}

| Role | Company | Period |
|---|---|---|
| 🛰️ Senior Full Stack Engineer | **[PT Surya Bestari Lestari](https://sblnet.id)** *(SBLNET)* | Dec 2025 — **Present** |
| 💳 Full Stack Developer *(Contract)* | **PT Cashlez Worldwide Indonesia** | Mar 2025 — Dec 2025 |
| 🧩 Full Stack Developer *(Contract)* · Team Lead | **PT Cyber Lab Indonesia** *(CoffeeLabs)* | Jun 2023 — Feb 2025 |
| 🎓 Full Stack Developer *(Freelance)* | **ProSpark Pte Ltd** · Singapore | Jul 2024 — Aug 2024 |
| 🎟️ Full Stack Developer *(Freelance)* | **Taman Safari Indonesia** · Bogor | Nov 2023 — Jan 2024 |
| 🌏 Full Stack Developer *(Freelance)* | **PT Arka Spektrum Solutindo** | Sep 2023 — Dec 2023 |
| 🗽 Mobile Developer *(Freelance)* | **Nghbr INC** · New York City | Jun 2023 — Aug 2023 |
| 🧘 Full Stack Engineer *(Freelance)* | **Remedi Indonesia** | Nov 2022 — May 2023 |
| 🕋 Full Stack Developer *(Contract)* | **PT Elteyba Medina Fauzana** | Apr 2021 — Nov 2022 |
| 🔥 Full Stack Web Developer *(Contract)* | **PT Taiba Cococha Indonesia** | Feb 2020 — Apr 2021 |
| 📺 Full Stack Web Developer *(Internship)* | **TVRI** | Mar 2017 — Sep 2017 |

<sub>Jakarta, Indonesia unless noted otherwise.</sub>

<details>
<summary>The shorter engagements, for completeness</summary>

<br>

**ProSpark Pte Ltd** — Singapore · *Learning Management System.* Built and maintained an LMS
for workforce training and reskilling. Laravel back end plus front-end integration,
maintenance and optimisation.

**Taman Safari Indonesia** — Bogor · *Ticketing platform.* Site, back office and the gate-checker
app, for GlobalTix Teknologi Indonesia — see the war story above.

**PT Arka Spektrum Solutindo** — *EduTech job portal.* Built Spectro and
[ArkaLearn](https://www.arkalearn.com/en) end to end — see the war story above.

**Nghbr INC** — New York City · *Hyper-local tech networking app.* Built the React Native (Expo)
app: translated complex UI/UX into pixel-perfect interfaces, integrated REST APIs with real-time
sync, and kept the UI consistent across every screen size someone could hand me. The company site
is at [nghbr.framer.website](https://nghbr.framer.website/) — a Framer build, not mine. The app
repo is client-owned and private.

**Remedi Indonesia** — *Corporate wellbeing platform.* Owned architecture for mobile and
backend: cross-platform React Native app on a secure Laravel API, real-time chat,
third-party integrations, and data-privacy practices for genuinely sensitive user data.

**TVRI** — *National public broadcaster.* Front-end maintenance for
[tvri.go.id](https://tvri.go.id) and full stack development for newstvri.com.

</details>

{sec("shipped-it", "SHIPPED IT")}

**Live right now:**

| Product | What it is | |
|---|---|---|
| **SBL Net** | Fiber-optic ISP — subscriber platform, billing, provisioning | [sblnet.id ↗](https://sblnet.id) |
| **Big Property** | Apartment and room booking platform | [bigproperty.online ↗](https://bigproperty.online) |
| **White Box Property** | Daily and transit apartment rental — Bekasi, Cikarang, Bogor | [propertywhitebox.com ↗](https://propertywhitebox.com) |
| **Itoya** | Self-photo studio booking + remote studio management | [itoya.my.id ↗](https://itoya.my.id) |
| **The Great Taman Safari Bogor** | Domestic ticketing site + back office, with a React Native gate-checker app | [domestic.tamansafaribogor.com ↗](https://domestic.tamansafaribogor.com/) |
| **DPUPR Musi Banyuasin** | Government agency portal ("INFRALOK") on a custom Laravel CMS | [dpupr.mubakab.go.id ↗](https://dpupr.mubakab.go.id/) |
| **ArkaLearn** | Japanese-language EdTech (JLPT N5-N3, SSW) feeding the Spectro job portal | [arkalearn.com ↗](https://www.arkalearn.com/en) |
| **CoffeeLabs** | Company site | [coffeelabs.co.id ↗](https://www.coffeelabs.co.id/) |
| **CoffeeLabs HRIS** | Attendance, GPS geofence, face recognition | [app.coffeelabs.co.id ↗](https://app.coffeelabs.co.id/) |
| **CoffeeLabs Back Office** | Admin and operations console | [admin.coffeelabs.co.id ↗](https://admin.coffeelabs.co.id/) |
| **Elteyba Tours** | Umrah &amp; Hajj agency platform | [elteybatours.com ↗](https://www.elteybatours.com) |
| **Elteyba GO** | Jamaah portal | [elteybago ↗](https://elteybago.eilhamzah.com/login) |
| **Aerocam Global Technology** <sup>*(ex-Indonesia Aero Camera)*</sup> | Drone training centre. I built the original 2021 site; the company has rebranded and rebuilt since, though elements of mine survive on the current one | [aerocam.co.id ↗](https://www.aerocam.co.id/) |
| **Taiba Cococha** | Trilingual corporate site (EN/ID/AR) + sales CRM | [taibacoco.co.id ↗](https://taibacoco.co.id) |
| **Gudang Dus Bandung** | B2B custom packaging catalogue — products, categories, tags, client showcase, self-serve admin | [gudangdusbandung.com ↗](https://gudangdusbandung.com/) |
| **Hasanain Center** | Company profile + registration system | [instagram ↗](https://www.instagram.com/hasanain.center/) |
| **Cahaya Al-Kahfi** | Donation platform | [facebook ↗](https://web.facebook.com/p/Cahaya-Al-Kahfi-100063858983042/) |
| **SmartHajj** | Umrah &amp; Hajj platform — Laravel + Flutter | smarthajj.co.id |

<sub>On Aerocam: the 2021 build was mine, the current site largely is not — I would rather say that than quietly claim a redesign somebody else shipped. The old <code>iac.co.id</code> domain now belongs to an unrelated company, so it is deliberately not linked.</sub>

<sub>The packaging site's <code>&lt;title&gt;</code> ends with <b>"It's Over 9000!"</b>. That was a deliberate decision, made by a grown adult, for a company that sells cardboard. I regret nothing.</sub>

**Retired** — shipped, served their purpose, then the domains lapsed: CoffeeLabs Journal
(2023), Sabilec / PT Saudara Bina Electric (2023), Gravilla.id hotel &amp; ticket booking
(2022), Safara Digitech (2020), Segment Events (2020), newstvri.com (2017).

{sec("talked-at-people", "TALKED AT PEOPLE")}

- **2022** — Speaker, *"Web Application in the World of Work"* — HMIK Talk, Pertamina University
- **2022** — Main speaker, *"Ngoding Bareng"* — Permikomnas Jakarta

<sub>Two separate universities handed me a microphone in 2022 and nobody has asked for it back.
I choose to read that as a good sign.</sub>

**Universitas Darma Persada** · Jakarta — Bachelor of English Literature, GPA 3.60 / 4.00 · 2018 — 2023

{sec("say-hi", "SAY HI")}

Got a system that has to balance to the cent, stay online at 3 AM, or ship to both app
stores? That is my favourite kind of conversation.

- 💼 [linkedin.com/in/ilhamrafi44](https://www.linkedin.com/in/ilhamrafi44/)
- ✉️ [ilhamrafi44@gmail.com](mailto:ilhamrafi44@gmail.com)
- 📍 Jakarta, Indonesia · UTC+7

{pic("cat-wave", "A cat waving hello", height="130")}

<details>
<summary><sub>🤓 how this profile is built (for the three of you who scrolled this far)</sub></summary>

<br>

No shields.io, no third-party stat cards, no "AI slop" gradient banner. Every graphic here
is an SVG generated by [`tools/build_assets.py`](tools/build_assets.py) in this repository —
each one emitted twice, once per colour scheme, and swapped with
`<picture media="(prefers-color-scheme: dark)">`.

The design language is neo-brutalism: 3–4px black outlines, hard offset shadows with zero
blur, flat saturated colour, and Arial Black doing a lot of heavy lifting. Text widths are
**measured in a real browser** rather than estimated, because Arial Black is far wider than
any per-character table predicts and labels were spilling out of their boxes.

There are three cats. One sits in the terminal with its tail going, one is asleep at the foot
of the stack emitting Z's, and one waves at the bottom. They are not decorative. They are load-bearing.

The stamp wobbles, the cursor blinks, the cats move, and all of it stops if you have
`prefers-reduced-motion` turned on.

```bash
python3 tools/build_assets.py   # regenerates all 28 files in assets/
```

</details>

<sub><i>Interested in new things. Addicted to code. That's all.</i></sub>
"""
open("README.md", "w", encoding="utf-8").write(md)
print(f"README.md: {len(md.splitlines())} lines")
