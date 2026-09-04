<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ilhamrafi44/ilhamrafi44/main/assets/hero-dark.svg?v=1">
  <img alt="Ilham Rafiannandha — Senior Full Stack Engineer, Jakarta" src="https://raw.githubusercontent.com/ilhamrafi44/ilhamrafi44/main/assets/hero-light.svg?v=1" width="100%">
</picture>

<a href="https://www.linkedin.com/in/ilhamrafi44/"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ilhamrafi44/ilhamrafi44/main/assets/badge-linkedin-dark.svg?v=1">
  <img alt="LinkedIn" src="https://raw.githubusercontent.com/ilhamrafi44/ilhamrafi44/main/assets/badge-linkedin-light.svg?v=1" height="40"></picture></a>
<a href="mailto:ilhamrafi44@gmail.com"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ilhamrafi44/ilhamrafi44/main/assets/badge-email-dark.svg?v=1">
  <img alt="Email" src="https://raw.githubusercontent.com/ilhamrafi44/ilhamrafi44/main/assets/badge-email-light.svg?v=1" height="40"></picture></a>
<a href="https://github.com/ilhamrafi44/isp-platform-architecture"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ilhamrafi44/ilhamrafi44/main/assets/badge-casestudies-dark.svg?v=1">
  <img alt="Case Studies" src="https://raw.githubusercontent.com/ilhamrafi44/ilhamrafi44/main/assets/badge-casestudies-light.svg?v=1" height="40"></picture></a>

</div>

## `whoami`

```console
$ whoami
Muhammad Ilham Rafiannandha — Jakarta, Indonesia

$ cat ~/.bio
Full stack engineer, 6+ years. I gravitate toward problems where being
wrong is expensive: money that has to balance to the cent, network
sessions that must not drop, invoices that must never double-charge.

Backend is home — Java / Spring Modulith, Laravel, NestJS, Go.
Frontend when it needs to feel good — Next.js, Vue, React.
Mobile when it needs to be in someone's pocket — React Native, Flutter.
And FreeRADIUS + MikroTik for when the packets need somewhere to go.

$ cat ~/.plot_twist
Bachelor's degree in English Literature (3.60/4.00).
Ended up writing considerably more Java than essays. No regrets.
```

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ilhamrafi44/ilhamrafi44/main/assets/stats-dark.svg?v=1">
  <img alt="6+ years in production · 11 companies and clients · 25+ products shipped · 87 repositories" src="https://raw.githubusercontent.com/ilhamrafi44/ilhamrafi44/main/assets/stats-light.svg?v=1" width="100%">
</picture>

## `~/now`

- 🛰️ **Just wrapped** a 27-module ISP platform running real subscribers, real money, and real routers.
- 🧪 **Building** [`nocturads`](https://github.com/ilhamrafi44) — a CPA/affiliate routing engine in Go + Fiber + SvelteKit + TimescaleDB.
- 🍎 **Shipped** [`mfu-macos`](https://github.com/ilhamrafi44/mfu-macos) — a native Xiaomi bootloader-unlock CLI, because I refused to boot a Windows VM for one API call.
- 💼 **Open to** Senior Backend / Full Stack roles. Remote-friendly, Jakarta-based.

## `~/stack`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ilhamrafi44/ilhamrafi44/main/assets/stack-dark.svg?v=1">
  <img alt="Technology stack: backend, frontend, mobile, data, infrastructure, network, payments, systems" src="https://raw.githubusercontent.com/ilhamrafi44/ilhamrafi44/main/assets/stack-light.svg?v=1" width="100%">
</picture>

## `~/selected-work`

### ISP Subscriber Platform — *PT Surya Bestari Lestari (SBLNET)*

An Internet Service Provider's entire subscriber lifecycle in one platform: onboarding →
automated network provisioning → recurring billing → double-entry accounting → payment
collection across multiple gateways and a direct bank integration.

| | |
|---|---|
| **Architecture** | 27-module modular monolith on Spring Modulith — hexagonal / DDD, event-driven module boundaries |
| **Persistence** | 8 PostgreSQL databases with per-context ACID via multi-datasource transaction management |
| **Accounting** | Double-entry General Ledger, Journal Entries, Chart of Accounts |
| **Billing** | Invoicing, proration, discounts, PPN/VAT — money as integer cents, never floats |
| **Payments** | Pluggable gateway abstraction: Duitku (VA / QRIS / e-wallet / retail) + host-to-host BRI Fixed VA |
| **Settlement** | HMAC-verified callbacks, deterministic & idempotent VA registration, automatic invoice matching |
| **Collections** | Dunning & auto-isolation — overdue suspends the line, payment reactivates it in real time |
| **Network** | FreeRADIUS (AAA) + MikroTik RouterOS — PPPoE, live session monitoring, CoA disconnect, RADIUS accounting |
| **Ops** | NOC & OLT management: router health, incident tracking, device config backup |
| **Clients** | Next.js web portals + a React Native self-service app (plan upgrade, invoice payment, usage) |

<sub>Java · Spring Boot · Spring Modulith · Spring Security + JWT · Spring Data JPA · PostgreSQL · Redis · Next.js · React Native · Jenkins · Docker</sub>

<details>
<summary><b>Finance & Reconciliation Portal</b> — <i>PT Cashlez Worldwide Indonesia</i></summary>

<br>

A payment company's back office has one job: prove that every rupiah that moved actually moved.
I built the portal that does the proving.

- **Two-stage reconciliation** — third-party settlement against bank mutation, then that result against back-office data
- **Discrepancy detection** — dispute amounts, missing-in-bank, missing-in-back-office
- **Disbursement** module for merchant payouts
- **Deduction** module for fees, chargebacks, and adjustments

<sub>Java · Spring Boot · Next.js · Jenkins · Docker</sub>

</details>

<details>
<summary><b>HRIS, POS & Income Journal Systems</b> — <i>PT Cyber Lab Indonesia</i></summary>

<br>

Nearly two years as full stack developer and development lead at an Indonesian IT consultancy.

- **HRIS** — attendance management, GPS-based check-in with geofence radius, employee management
- **Income Journal** management system
- **Point of Sales** system
- **Led** the development team and mentored the internship program

<sub>Laravel · Java (Spring Boot) · Next.js · Vue.js · React Native · Jenkins · Docker</sub>

</details>

<details>
<summary><b>Umrah & Hajj Travel Platform</b> — <i>PT Elteyba Medina Fauzana</i></summary>

<br>

A licensed PPIU & PIHK travel agency running pilgrims, documents, seats, and money through one system.

- **Multi-role access** — admin, agent, jamaah, coordinator, with approval flows
- **Registration** — online forms with passport/visa upload, group registration, package selection
- **Payment & invoicing** — automated invoicing, down-payment and installment tracking, reminders
- **Packages** — real-time seat quota, schedule assignment, flight & hotel management
- **Documents** — visa tracking with status workflows, API/CSV export for visa processing
- **Manifest** — flight grouping, hotel room-sharing logic, PDF generation for immigration and hotels
- **Comms** — WhatsApp broadcast with email fallback for schedule updates
- **Ops** — queue-based notifications, activity logging, daily backups

<sub>Laravel · Sanctum · Livewire · Spatie Permission · Vue 3 SPA · React Native · MySQL/PostgreSQL · Redis · Midtrans · WhatsApp API</sub>

</details>

<details>
<summary><b>Multilingual Site + Sales CRM</b> — <i>PT Taiba Cococha Indonesia</i></summary>

<br>

Premium coconut-shell charcoal exporter — the site sells in three languages, the CRM runs the pipeline.

- **Trilingual company profile** (English / Indonesian / Arabic) → [taibacoco.co.id](https://taibacoco.co.id)
- **CRM** — contact & lead management with status tracking, reminders, Excel/CSV import-export
- **Sales pipeline** — deal tracking, funnel metrics, performance reports
- **Task scheduler** — calendar view, assignments, automated follow-up notifications
- **Invoice & quotation** module with PDF generation and e-signatures
- **Security** — 2FA, session logs, audit trails, permission-based access

<sub>Laravel · Passport · Spatie Permissions · Queues & Events · Vue 3 + Pinia · MySQL · Redis · DomPDF</sub>

</details>

## `~/career`

| | Role | Company | Period |
|---|---|---|---|
| 🛰️ | Senior Full Stack Engineer | **PT Surya Bestari Lestari (SBLNET)** · Jakarta | Dec 2025 — Jul 2026 |
| 💳 | Full Stack Developer *(Contract)* | **PT Cashlez Worldwide Indonesia** · Jakarta | Mar 2025 — Dec 2025 |
| 🧩 | Full Stack Developer *(Contract)* · Team Lead | **PT Cyber Lab Indonesia** · Jakarta | Jun 2023 — Feb 2025 |
| 🎓 | Full Stack Developer *(Freelance)* | **ProSpark Pte Ltd** · Singapore | Jul 2024 — Aug 2024 |
| 🎟️ | Full Stack Developer *(Freelance)* | **Taman Safari Indonesia** · Bogor | Nov 2023 — Jan 2024 |
| 🌏 | Full Stack Developer *(Freelance)* | **PT Arka Spektrum Solutindo** · Jakarta | Sep 2023 — Dec 2023 |
| 🗽 | Mobile Developer *(Freelance)* | **Nghbr INC** · New York City, USA | Jun 2023 — Aug 2023 |
| 🧘 | Full Stack Engineer *(Freelance)* | **Remedi Indonesia** · Jakarta | Nov 2022 — May 2023 |
| 🕋 | Full Stack Developer *(Contract)* | **PT Elteyba Medina Fauzana** · Jakarta | Apr 2021 — Nov 2022 |
| 🔥 | Full Stack Web Developer *(Contract)* | **PT Taiba Cococha Indonesia** · Jakarta | Feb 2020 — Apr 2021 |
| 📺 | Full Stack Web Developer *(Internship)* | **TVRI** · Jakarta | Mar 2017 — Sep 2017 |

<details>
<summary>Details on the freelance & contract engagements</summary>

<br>

**ProSpark Pte Ltd** — Singapore · *Learning Management System*
Built and maintained an LMS for workforce training, upskilling, and reskilling. Owned back-end
development in Laravel plus front-end integration, maintenance, troubleshooting, and optimization.

**Taman Safari Indonesia** — Bogor · *Ticket verification app*
A React Native app for on-site staff to verify tickets at park entry. QR and barcode processing for
fast check-in, fraud detection to block reused or forged tickets, and integration with the park's
existing ticketing infrastructure. Iterated on real staff feedback; shipped ongoing updates.

**PT Arka Spektrum Solutindo** — Jakarta · *EduTech job portal*
End-to-end job portal for Indonesian prospective migrant workers and employers: authentication, job
listings, advanced filtering and search, application tracking, and candidate–employer messaging.

**Nghbr INC** — New York City · *Hyper-local tech networking app*
Translated complex UI/UX designs into pixel-perfect, responsive React Native interfaces. Integrated
REST APIs with real-time data sync and kept the UI consistent across screen sizes and devices.

**Remedi Indonesia** — Jakarta · *Corporate wellbeing platform*
Owned architecture for both mobile and backend. Cross-platform React Native app on a secure Laravel
API, with authentication, real-time chat, third-party integrations, and data-privacy practices for
sensitive user data.

**TVRI** — Jakarta · *National public broadcaster*
Front-end maintenance for the corporate site [tvri.go.id](https://tvri.go.id), and full stack
development for newstvri.com.

</details>

## `~/shipped`

Sites and systems delivered outside of full-time roles. Domains marked *offline* have since expired
or been retired by their owners — the work shipped, the DNS did not survive.

| Year | Project | What it is | Status |
|---|---|---|---|
| 2023 | CoffeeLabs Journal | Journaling platform for PT CoffeeLabs Indonesia | offline |
| 2023 | CoffeeLabs Attendance | GPS-radius attendance system | offline |
| 2023 | Hasanain Center | Company profile + registration system | offline |
| 2023 | Sabilec | Corporate site for PT Saudara Bina Electric | offline |
| 2022 | Gravilla.id | Hotel and ticket booking platform | offline |
| 2021 | Indonesia Aero Camera | Corporate site | [live ↗](https://iac.co.id) |
| 2020 | Taiba Cococha | Trilingual corporate site (EN/ID/AR) + CRM | [live ↗](https://taibacoco.co.id) |
| 2020 | Safara Digitech | Corporate site | offline |
| 2020 | Cahaya Alkahfi | Donation platform | offline |
| 2020 | Segment Events | Sports event platform | offline |

## `~/speaking`

- **2022** — Speaker, *"Web Application in the World of Work"* — HMIK Talk, Pertamina University
- **2022** — Main speaker, *"Ngoding Bareng"* — Permikomnas Jakarta (National Informatics & Computer Students Association)

## `~/education`

**Universitas Darma Persada** · Jakarta — Bachelor of English Literature, GPA 3.60 / 4.00 · 2018 — 2023

## `~/contact`

Got a system that has to balance to the cent, stay online at 3 AM, or ship to both app stores?
That's my favourite kind of conversation.

- 💼 [linkedin.com/in/ilhamrafi44](https://www.linkedin.com/in/ilhamrafi44/)
- ✉️ [ilhamrafi44@gmail.com](mailto:ilhamrafi44@gmail.com)
- 📍 Jakarta, Indonesia · UTC+7 · open to remote

<details>
<summary><sub>🤓 How this profile is built</sub></summary>

<br>

No badge services, no third-party stat cards. Every graphic here is an SVG generated by
[`tools/build_assets.py`](tools/build_assets.py) in this repository — each one emitted twice, once
per colour scheme, and swapped with `<picture media="(prefers-color-scheme: dark)">` so it blends
into GitHub's own canvas instead of sitting on top of it as an obvious rectangle.

The hero diagram is a real ISP topology — core → distribution → access → CPE — with packets
animated in CSS, and `prefers-reduced-motion` respected. Brand marks come from
[devicon](https://github.com/devicons/devicon) and [simple-icons](https://github.com/simple-icons/simple-icons),
inlined as `<symbol>` defs with namespaced ids so nothing collides.

```bash
python3 tools/build_assets.py   # regenerates everything in assets/
```

</details>

<div align="center"><sub><i>Interested in new things. Addicted to code. That's all.</i></sub></div>
