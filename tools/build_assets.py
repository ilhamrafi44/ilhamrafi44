#!/usr/bin/env python3
"""
Generate theme-aware SVG assets for github.com/ilhamrafi44 profile README.

Everything is self-hosted: no shields.io, no third-party card services.
Each asset is emitted twice (dark/light) and swapped in the README with
<picture media="(prefers-color-scheme: dark)"> so it blends into GitHub's
own canvas instead of sitting on it as an obvious box.
"""
import os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS = os.path.join(ROOT, "tools", "icons")
OUT = os.path.join(ROOT, "assets")

# ─────────────────────────────────────────────────────────── theme
THEMES = {
    "dark": dict(
        text="#e6edf3", strong="#ffffff", muted="#8b949e", faint="#6e7681",
        surface="#161b22", surface2="#0f141a", border="#30363d",
        accent="#00E5A0", accent2="#8B5CFF", accent3="#FFB020",
        mono="#e6edf3", glow=0.13, grid=0.055, canvas="#0d1117",
    ),
    "light": dict(
        text="#1f2328", strong="#010409", muted="#59636e", faint="#818b98",
        surface="#f6f8fa", surface2="#ffffff", border="#d1d9e0",
        accent="#00875A", accent2="#6740D6", accent3="#9A6700",
        mono="#1f2328", glow=0.10, grid=0.05, canvas="#ffffff",
    ),
}

# ─────────────────────────────────────────────────────────── text metrics
# Approximate advance widths (em) for a UI sans stack. Chips are padded
# generously so cross-platform font variance never clips a label.
_W = {" ": .27, ".": .28, ",": .28, ":": .28, ";": .28, "!": .30, "|": .26,
      "'": .22, '"': .38, "i": .26, "j": .26, "l": .26, "I": .29, "t": .35,
      "f": .33, "r": .38, "m": .87, "w": .75, "M": .87, "W": .93, "@": .95,
      "-": .35, "–": .5, "·": .34, "/": .33, "(": .34, ")": .34, "+": .58,
      "×": .58, "&": .70, "3": .58, "6": .58, "8": .58}

MEASURED = {
    ("Java 17+", 13, 600): 54.98,
    ("Spring Boot", 13, 600): 74.52,
    ("Spring Modulith", 13, 600): 100.59,
    ("Spring Security", 13, 600): 97.79,
    ("Laravel", 13, 600): 45.67,
    ("NestJS", 13, 600): 45.53,
    ("Node.js", 13, 600): 48.29,
    ("Go / Fiber", 13, 600): 60.75,
    ("PHP", 13, 600): 26.95,
    ("Next.js", 13, 600): 44.23,
    ("React", 13, 600): 36.19,
    ("Vue 3 + Pinia", 13, 600): 82.13,
    ("TypeScript", 13, 600): 69.13,
    ("JavaScript", 13, 600): 67.19,
    ("Tailwind", 13, 600): 51.86,
    ("SvelteKit", 13, 600): 56.86,
    ("React Native", 13, 600): 80.0,
    ("Flutter", 13, 600): 42.11,
    ("Dart", 13, 600): 27.5,
    ("Kotlin", 13, 600): 36.27,
    ("Swift", 13, 600): 32.78,
    ("Android", 13, 600): 50.06,
    ("PostgreSQL", 13, 600): 75.34,
    ("MySQL", 13, 600): 45.18,
    ("Redis", 13, 600): 34.99,
    ("TimescaleDB", 13, 600): 82.6,
    ("Firebase", 13, 600): 54.21,
    ("Multi-datasource ACID", 13, 600): 143.96,
    ("Docker", 13, 600): 44.9,
    ("Jenkins", 13, 600): 48.82,
    ("Nginx", 13, 600): 36.56,
    ("GitHub Actions", 13, 600): 95.47,
    ("Git", 13, 600): 18.31,
    ("Grafana", 13, 600): 50.0,
    ("Linux / VPS", 13, 600): 71.08,
    ("MikroTik RouterOS", 13, 600): 117.9,
    ("FreeRADIUS / AAA", 13, 600): 116.03,
    ("PPPoE", 13, 600): 41.09,
    ("RADIUS Accounting", 13, 600): 124.9,
    ("CoA Disconnect", 13, 600): 100.9,
    ("OLT & NOC", 13, 600): 70.34,
    ("Duitku", 13, 600): 41.37,
    ("BRI Fixed VA", 13, 600): 79.38,
    ("Midtrans", 13, 600): 56.04,
    ("QRIS", 13, 600): 31.23,
    ("Double-Entry GL", 13, 600): 105.29,
    ("Reconciliation", 13, 600): 89.06,
    ("C++", 13, 600): 26.4,
    ("Rust", 13, 600): 28.8,
    ("Python", 13, 600): 44.9,
    ("WebSocket", 13, 600): 71.54,
    ("Express", 13, 600): 50.16,
    ("LinkedIn", 14, 600): 62.29,
    ("Email", 14, 600): 40.15,
    ("Case Studies", 14, 600): 88.4,
}

# Widths measured in-browser against the SANS stack (Chromium/macOS -> SF Pro).
# Other platforms resolve to Segoe UI / Roboto, both narrower, so SAFETY only
# ever buys extra right padding -- it never clips a label.
SAFETY = 1.05


def tw(s, size, weight=600, tracking=0.0):
    """Rendered width of `s` in px: measured where known, estimated otherwise."""
    tr = tracking * max(len(s) - 1, 0)
    hit = MEASURED.get((s, size, weight))
    if hit is not None:
        return hit * SAFETY + tr
    total = 0.0
    for ch in s:
        if ch in _W:      total += _W[ch]
        elif ch.isdigit():total += .58
        elif ch.isupper():total += .66
        else:             total += .545
    total *= size * (1.02 if weight >= 700 else 1.01 if weight >= 600 else 1.0)
    return total * 1.08 * SAFETY + tr      # unmeasured: lean wide, never clip

def twm(s, size, tracking=0.0):
    """Monospace advance. Every mono in the stack sits at ~0.60em."""
    return len(s) * size * 0.605 + tracking * max(len(s) - 1, 0)

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,Roboto,'Helvetica Neue',Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

def esc(s): return html.escape(s, quote=False)

# ─────────────────────────────────────────────────────────── icon symbols
MONO_ICONS = {"nextjs", "rust", "express", "socketio", "linkedin"}
ICON_FILES = {
    "java": "java-original", "spring": "spring-original", "laravel": "laravel-original",
    "php": "php-original", "node": "nodejs-original", "nest": "nestjs-original",
    "go": "go-original", "rust": "mono-rust", "nextjs": "mono-nextdotjs",
    "react": "react-original", "vue": "vuejs-original", "ts": "typescript-original",
    "js": "javascript-original", "tailwind": "tailwindcss-original",
    "svelte": "svelte-original", "flutter": "flutter-original", "dart": "dart-original",
    "kotlin": "kotlin-original", "swift": "swift-original", "android": "android-original",
    "postgres": "postgresql-original", "mysql": "mysql-original", "redis": "redis-original",
    "firebase": "firebase-plain", "docker": "docker-original", "jenkins": "jenkins-original",
    "nginx": "nginx-original", "gha": "githubactions-original", "git": "git-original",
    "python": "python-original", "cpp": "cplusplus-original", "grafana": "grafana-original",
    "express": "mono-express", "socketio": "mono-socketdotio", "linkedin": "mono-linkedin",
}

_ID = re.compile(r'id="([^"]+)"')
_FILL = re.compile(r'\sfill="[^"]*"')
_STYLE_FILL = re.compile(r'fill:\s*[^;"]+;?')

def load_symbol(key, theme):
    """Read a brand icon, namespace its internal ids, return a <symbol>."""
    with open(os.path.join(ICONS, ICON_FILES[key] + ".svg"), encoding="utf-8") as fh:
        raw = fh.read()
    vb = re.search(r'viewBox="([^"]+)"', raw).group(1)
    inner = raw[raw.index(">", raw.index("<svg")) + 1: raw.rindex("</svg>")]
    inner = re.sub(r"<title>.*?</title>", "", inner, flags=re.S)

    for old in set(_ID.findall(inner)):                    # avoid cross-icon id clashes
        new = f"{key}_{old}"
        inner = inner.replace(f'id="{old}"', f'id="{new}"')
        inner = inner.replace(f"url(#{old})", f"url(#{new})")
        inner = inner.replace(f'href="#{old}"', f'href="#{new}"')

    if key in MONO_ICONS:
        inner = _FILL.sub("", inner)
        inner = _STYLE_FILL.sub("", inner)
        inner = f'<g fill="{theme["mono"]}">{inner}</g>'
    return f'<symbol id="ic-{key}" viewBox="{vb}">{inner}</symbol>'

def use(key, x, y, size):
    return (f'<use href="#ic-{key}" xlink:href="#ic-{key}" '
            f'x="{x:.1f}" y="{y:.1f}" width="{size}" height="{size}"/>')

# ─────────────────────────────────────────────────────────── hero
def build_hero(name, t):
    W, H = 1200, 330
    a, a2 = t["accent"], t["accent2"]

    # ISP topology: core → distribution → access → CPE. On-brand for an
    # engineer who runs FreeRADIUS/MikroTik in production.
    core = (700, 168)
    dist = [(858, 92), (858, 168), (858, 244)]
    acc_y = [58, 102, 146, 190, 234, 278]
    access = [(1016, y) for y in acc_y]
    cpe = [(1174, y) for y in acc_y]
    d2a = {0: (0, 1), 1: (2, 3), 2: (4, 5)}

    css = [
        "@keyframes brth{0%,100%{opacity:.45}50%{opacity:1}}",
        "@keyframes ring{0%{r:9;opacity:.55}100%{r:34;opacity:0}}",
        "@keyframes cur{0%,45%{opacity:1}50%,100%{opacity:0}}",
        ".nd{animation:brth 3.2s ease-in-out infinite}",
        ".rg{animation:ring 3.4s ease-out infinite}",
        ".cur{animation:cur 1.05s step-end infinite}",
    ]
    body, defs = [], []

    defs.append(f'<radialGradient id="hglow"><stop offset="0" stop-color="{a}" '
                f'stop-opacity="{t["glow"]}"/><stop offset=".55" stop-color="{a}" stop-opacity="{t["glow"]*.35:.3f}"/>'
                f'<stop offset="1" stop-color="{a}" stop-opacity="0"/></radialGradient>')
    defs.append(f'<pattern id="hgrid" width="22" height="22" patternUnits="userSpaceOnUse">'
                f'<circle cx="1.2" cy="1.2" r="1.2" fill="{t["muted"]}" opacity="{t["grid"]}"/></pattern>')
    # feather the texture into the page instead of ending on a hard rectangle
    defs.append('<radialGradient id="hfade" cx=".5" cy=".5" r=".5">'
                '<stop offset="0" stop-color="#fff" stop-opacity="1"/>'
                '<stop offset=".62" stop-color="#fff" stop-opacity=".85"/>'
                '<stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>')
    defs.append('<mask id="hmask"><rect x="590" y="0" width="610" height="330" fill="url(#hfade)"/></mask>')

    body.append('<g mask="url(#hmask)">')
    body.append('<rect x="590" y="0" width="610" height="330" fill="url(#hgrid)"/>')
    body.append(f'<ellipse cx="925" cy="{core[1]}" rx="272" ry="168" fill="url(#hglow)"/>')
    body.append('</g>')

    # edges
    for i, d in enumerate(dist):
        body.append(f'<line x1="{core[0]}" y1="{core[1]}" x2="{d[0]}" y2="{d[1]}" '
                    f'stroke="{a}" stroke-opacity=".38" stroke-width="1.4"/>')
        for j in d2a[i]:
            p = access[j]
            body.append(f'<line x1="{d[0]}" y1="{d[1]}" x2="{p[0]}" y2="{p[1]}" '
                        f'stroke="{a2}" stroke-opacity=".32" stroke-width="1.1"/>')
    for p, c in zip(access, cpe):
        body.append(f'<line x1="{p[0]}" y1="{p[1]}" x2="{c[0]}" y2="{c[1]}" '
                    f'stroke="{t["muted"]}" stroke-opacity=".55" stroke-width="1"/>')

    # travelling packets — CSS transforms so prefers-reduced-motion can stop them
    pk = []
    routes = [(core, dist[0]), (core, dist[1]), (core, dist[2])]
    routes += [(dist[i], access[j]) for i, js in d2a.items() for j in js]
    for i, (s, e) in enumerate(routes):
        css.append(f"@keyframes pk{i}{{0%{{transform:translate(0,0);opacity:0}}"
                   f"12%{{opacity:1}}88%{{opacity:1}}"
                   f"100%{{transform:translate({e[0]-s[0]}px,{e[1]-s[1]}px);opacity:0}}}}")
        css.append(f".pk{i}{{animation:pk{i} {2.6 + (i % 4) * .45:.2f}s linear infinite;"
                   f"animation-delay:{i * .38:.2f}s}}")
        pk.append(f'<circle class="pk{i}" cx="{s[0]}" cy="{s[1]}" r="2.6" '
                  f'fill="{a if i < 3 else a2}"/>')
    body += pk

    # nodes
    body.append(f'<circle class="rg" cx="{core[0]}" cy="{core[1]}" r="9" fill="none" '
                f'stroke="{a}" stroke-width="1.5"/>')
    body.append(f'<circle cx="{core[0]}" cy="{core[1]}" r="16" fill="{a}" opacity=".12"/>')
    body.append(f'<circle cx="{core[0]}" cy="{core[1]}" r="7.5" fill="{a}"/>')
    for i, d in enumerate(dist):
        body.append(f'<circle class="nd" style="animation-delay:{i*.5:.1f}s" cx="{d[0]}" cy="{d[1]}" '
                    f'r="5" fill="{a}"/>')
    for i, p in enumerate(access):
        body.append(f'<circle class="nd" style="animation-delay:{i*.31+.2:.2f}s" cx="{p[0]}" cy="{p[1]}" '
                    f'r="3.6" fill="{a2}"/>')
    for c in cpe:
        body.append(f'<rect x="{c[0]-3.1}" y="{c[1]-3.1}" width="6.2" height="6.2" rx="1.5" '
                    f'fill="{t["surface"]}" stroke="{t["muted"]}" stroke-opacity=".9"/>')

    tier = [("CORE", core[0], 300), ("DIST", dist[0][0], 300), ("ACCESS", access[0][0], 300), ("CPE", cpe[0][0], 300)]
    for label, x, y in tier:
        body.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="{MONO}" font-size="9.5" '
                    f'letter-spacing="1.6" fill="{t["faint"]}">{label}</text>')

    # ── left column
    pill = "OPEN TO WORK  ·  JAKARTA, ID  ·  UTC+7"
    pw = 34 + twm(pill, 11, 1.5) + 16
    body.append(f'<rect x="2" y="46" width="{pw:.0f}" height="28" rx="14" fill="{a}" fill-opacity=".10" '
                f'stroke="{a}" stroke-opacity=".38"/>')
    body.append(f'<circle class="nd" cx="22" cy="60" r="3.6" fill="{a}"/>')
    body.append(f'<text x="36" y="64.5" font-family="{MONO}" font-size="11" font-weight="500" '
                f'letter-spacing="1.5" fill="{a}">{pill}</text>')

    body.append(f'<text x="2" y="150" font-family="{SANS}" font-size="56" font-weight="800" '
                f'letter-spacing="-1.4" fill="{t["strong"]}">Ilham Rafiannandha</text>')

    body.append(f'<text x="2" y="185" font-family="{SANS}" font-size="18.5" font-weight="600" '
                f'fill="{t["text"]}">Senior Full Stack Engineer'
                f'<tspan fill="{t["faint"]}">  ·  </tspan>'
                f'<tspan fill="{t["muted"]}" font-weight="500">ISP platforms, fintech &amp; mobile</tspan></text>')

    tag = "// Interested in new things. Addicted to code. That's all."
    body.append(f'<text x="2" y="216" font-family="{MONO}" font-size="13.5" fill="{t["muted"]}">{esc(tag)}'
                f'<tspan class="cur" fill="{a}">\u2588</tspan></text>')

    body.append(f'<line x1="2" y1="250" x2="588" y2="250" stroke="{t["border"]}"/>')
    strip = "java · spring modulith · next.js · react native · postgresql · mikrotik · freeradius"
    body.append(f'<text x="2" y="278" font-family="{MONO}" font-size="12" letter-spacing=".3" '
                f'fill="{t["faint"]}">{esc(strip)}</text>')

    return wrap(W, H, defs, body, css, name)

# ─────────────────────────────────────────────────────────── stack

def balance(items, avail, gap, width_of):
    """Pack `items` into the fewest lines, then even them out.

    Greedy packing leaves orphans (one lone chip on its own row); once the
    line count is known we re-pack against an average-width target so rows
    come out visually even.
    """
    ws = [width_of(i) for i in items]

    def pack(limit):
        rows, cur, cw = [], [], 0.0
        for it, w in zip(items, ws):
            nw = w if not cur else cw + gap + w
            if cur and nw > limit:
                rows.append(cur); cur, cw = [it], w
            else:
                cur.append(it); cw = nw
        if cur: rows.append(cur)
        return rows

    n = len(pack(avail))
    if n < 2:
        return pack(avail)
    lo, hi = max(ws), avail          # tightest limit still yielding n lines
    for _ in range(40):
        mid = (lo + hi) / 2
        if len(pack(mid)) <= n: hi = mid
        else:                   lo = mid
    return pack(hi)


STACK = [
    ("BACKEND", [("java", "Java 17+"), ("spring", "Spring Boot"), ("spring", "Spring Modulith"),
                 ("spring", "Spring Security"), ("laravel", "Laravel"), ("nest", "NestJS"),
                 ("node", "Node.js"), ("go", "Go / Fiber"), ("php", "PHP")]),
    ("FRONTEND", [("nextjs", "Next.js"), ("react", "React"), ("vue", "Vue 3 + Pinia"),
                  ("ts", "TypeScript"), ("js", "JavaScript"), ("tailwind", "Tailwind"),
                  ("svelte", "SvelteKit")]),
    ("MOBILE", [("react", "React Native"), ("flutter", "Flutter"), ("dart", "Dart"),
                ("kotlin", "Kotlin"), ("swift", "Swift"), ("android", "Android")]),
    ("DATA", [("postgres", "PostgreSQL"), ("mysql", "MySQL"), ("redis", "Redis"),
              (None, "TimescaleDB"), ("firebase", "Firebase"), (None, "Multi-datasource ACID")]),
    ("INFRA", [("docker", "Docker"), ("jenkins", "Jenkins"), ("nginx", "Nginx"),
               ("gha", "GitHub Actions"), ("git", "Git"), ("grafana", "Grafana"), (None, "Linux / VPS")]),
    ("NETWORK", [(None, "MikroTik RouterOS"), (None, "FreeRADIUS / AAA"), (None, "PPPoE"),
                 (None, "RADIUS Accounting"), (None, "CoA Disconnect"), (None, "OLT & NOC")]),
    ("PAYMENTS", [(None, "Duitku"), (None, "BRI Fixed VA"), (None, "Midtrans"), (None, "QRIS"),
                  (None, "Double-Entry GL"), (None, "Reconciliation")]),
    ("SYSTEMS", [("cpp", "C++"), ("rust", "Rust"), ("python", "Python"),
                 ("socketio", "WebSocket"), ("express", "Express")]),
]

def build_stack(name, t):
    W = 1200
    L_X, C_X, MAXX = 2, 104, 1198         # label column, chip column, wrap edge — all
    RH, GAP, RGAP, PAD = 34, 9, 13, 22    # flush with the README text column
    FS = 13
    ICON_LEAD, DOT_LEAD, RPAD = 39, 24, 14
    used, y = set(), PAD
    body = []

    for label, items in STACK:
        def chip_w(it):
            return (ICON_LEAD if it[0] else DOT_LEAD) + tw(it[1], FS, 600) + RPAD
        rows = []
        for line in balance(items, MAXX - C_X, GAP, chip_w):
            x, placed = C_X, []
            for key, text in line:
                w = chip_w((key, text))
                placed.append((key, text, x, w)); x += w + GAP
            rows.append(placed)

        body.append(f'<text x="{L_X}" y="{y + RH/2 + 4:.0f}" font-family="{MONO}" '
                    f'font-size="11" font-weight="600" letter-spacing="1.7" fill="{t["faint"]}">{label}</text>')
        for row in rows:
            for key, text, x, w in row:
                body.append(f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="{RH}" rx="9" '
                            f'fill="{t["surface"]}" stroke="{t["border"]}"/>')
                if key:
                    used.add(key)
                    body.append(use(key, x + 13, y + 8, 18))
                    tx = x + ICON_LEAD
                else:
                    body.append(f'<circle cx="{x+16:.0f}" cy="{y + RH/2:.0f}" r="3.4" fill="{t["accent"]}" opacity=".85"/>')
                    tx = x + DOT_LEAD
                body.append(f'<text x="{tx:.0f}" y="{y + RH/2 + 4.5:.0f}" font-family="{SANS}" font-size="{FS}" '
                            f'font-weight="600" fill="{t["text"]}">{esc(text)}</text>')
            y += RH + GAP
        y += RGAP - GAP

    H = y - RGAP + GAP + PAD
    defs = [load_symbol(k, t) for k in sorted(used)]
    return wrap(W, H, defs, body, [], name)

# ─────────────────────────────────────────────────────────── stats
STATS = [("6+", "YEARS IN PRODUCTION"), ("11", "COMPANIES & CLIENTS"),
         ("25+", "PRODUCTS SHIPPED"), ("87", "REPOSITORIES")]

def build_stats(name, t):
    W, H = 1200, 148
    X0, X1, Y0, PH = 1, 1199, 14, 120
    body = [f'<rect x="{X0}" y="{Y0}" width="{X1-X0}" height="{PH}" rx="16" '
            f'fill="{t["surface"]}" stroke="{t["border"]}"/>']
    colw = (X1 - X0) / len(STATS)
    accents = [t["accent"], t["accent2"], t["accent3"], t["accent"]]
    for i, (num, label) in enumerate(STATS):
        cx = X0 + colw * i + colw / 2
        if i:
            body.append(f'<line x1="{X0+colw*i:.0f}" y1="{Y0+26}" x2="{X0+colw*i:.0f}" y2="{Y0+PH-26}" '
                        f'stroke="{t["border"]}"/>')
        body.append(f'<text x="{cx:.0f}" y="{Y0+66}" text-anchor="middle" font-family="{SANS}" '
                    f'font-size="42" font-weight="800" letter-spacing="-1" fill="{accents[i]}">{num}</text>')
        body.append(f'<text x="{cx:.0f}" y="{Y0+94}" text-anchor="middle" font-family="{MONO}" '
                    f'font-size="10.5" font-weight="600" letter-spacing="1.8" '
                    f'fill="{t["muted"]}">{esc(label)}</text>')
    return wrap(W, H, [], body, [], name)


# ─────────────────────────────────────────────────────────── link badges
def _envelope(a):
    return (f'<g fill="none" stroke="{a}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="1" y="2.7" width="15" height="11.6" rx="2.2"/>'
            f'<path d="M1.7 4.4 8.5 9.5 15.3 4.4"/></g>')

def _layers(a):
    return (f'<g fill="none" stroke="{a}" stroke-width="1.5" stroke-linejoin="round">'
            f'<path d="M8.5 1.3 15.7 5.1 8.5 8.9 1.3 5.1Z"/>'
            f'<path d="M1.3 8.6 8.5 12.4 15.7 8.6"/>'
            f'<path d="M1.3 11.9 8.5 15.7 15.7 11.9"/></g>')

BADGES = [("linkedin", "LinkedIn", None), ("email", "Email", _envelope),
          ("casestudies", "Case Studies", _layers)]

def build_badge(slug, label, glyph, t):
    H, FS, PAD, ICON = 40, 14, 15, 17
    w = PAD + ICON + 10 + tw(label, FS, 600) + 16
    body = [f'<rect x=".75" y=".75" width="{w-1.5:.1f}" height="{H-1.5}" rx="10.25" '
            f'fill="{t["surface"]}" stroke="{t["border"]}" stroke-width="1.5"/>']
    iy = (H - ICON) / 2
    if glyph:
        body.append(f'<g transform="translate({PAD},{iy:.1f})">{glyph(t["accent"])}</g>')
    else:
        body.append(f'<g transform="translate({PAD},{iy:.1f}) scale({ICON/24:.4f})">'
                    f'<g fill="{t["accent"]}">{_symbol_inner(slug, t)}</g></g>')
    body.append(f'<text x="{PAD+ICON+10}" y="{H/2+5:.0f}" font-family="{SANS}" font-size="{FS}" '
                f'font-weight="600" fill="{t["text"]}">{esc(label)}</text>')
    return wrap(round(w), H, [], body, [], label)

def _symbol_inner(key, t):
    sym = load_symbol(key, t)
    return sym[sym.index(">") + 1:-len("</symbol>")]

# ─────────────────────────────────────────────────────────── shell
def wrap(w, h, defs, body, css, title):
    style = ""
    if css:
        rules = "".join(css) + "@media(prefers-reduced-motion:reduce){*{animation:none!important}}"
        style = f"<style>{rules}</style>"
    d = f"<defs>{''.join(defs)}</defs>" if defs else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}" '
            f'fill="none">{style}{d}{"".join(body)}</svg>')

# ─────────────────────────────────────────────────────────── main
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    builders = {
        "hero":  (build_hero,  "Ilham Rafiannandha — Senior Full Stack Engineer"),
        "stack": (build_stack, "Technology stack"),
        "stats": (build_stats, "Career by the numbers"),
    }
    for slug, label, glyph in BADGES:
        for mode, theme in THEMES.items():
            path = os.path.join(OUT, f"badge-{slug}-{mode}.svg")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(build_badge(slug, label, glyph, theme))
            print(f"  {os.path.relpath(path, ROOT):28s} {os.path.getsize(path):>7,} b")
    for base, (fn, title) in builders.items():
        for mode, theme in THEMES.items():
            path = os.path.join(OUT, f"{base}-{mode}.svg")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(fn(title, theme))
            print(f"  {os.path.relpath(path, ROOT):28s} {os.path.getsize(path):>7,} b")
