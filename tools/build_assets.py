#!/usr/bin/env python3
"""
Neo-brutalist SVG assets for github.com/ilhamrafi44.

Thick black outlines, hard offset shadows, loud flat colour, zero gradients.
Every asset is emitted twice (dark/light) and swapped in the README with
<picture media="(prefers-color-scheme: dark)">.

Text widths are measured in-browser (see MEASURED) rather than estimated,
because Arial Black is far wider than any per-character table predicts.
"""
import os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS = os.path.join(ROOT, "tools", "icons")
OUT = os.path.join(ROOT, "assets")

# ───────────────────────────────────────────────────────────────── palette
POP = dict(yellow="#FFE600", pink="#FF3D8B", cyan="#22D3EE",
           lime="#B8FF29", orange="#FF7A2F", purple="#A66BFF")

THEMES = {
    "light": dict(paper="#FFFFFF", panel="#FFFFFF", ink="#000000",
                  text="#000000", sub="#3D3D3D", grid="#000000", gridop=".07"),
    "dark":  dict(paper="#0D1117", panel="#161B22", ink="#FFFFFF",
                  text="#FFFFFF", sub="#B7BEC7", grid="#FFFFFF", gridop=".09"),
}

def on(fill, t):
    """Text colour that survives on `fill`. POP colours are all light."""
    return "#000000" if fill in POP.values() else t["text"]

def edge(fill, t):
    """Outline colour. Black reads on every POP fill; panels need the ink."""
    return "#000000" if fill in POP.values() else t["ink"]

# ───────────────────────────────────────────────────────────── typography
DISPLAY = "'Arial Black','Arial Bold',Helvetica,Arial,sans-serif"
MEME    = "Impact,Haettenschweiler,'Arial Narrow Bold',sans-serif"
SANS    = "-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,Roboto,Helvetica,Arial,sans-serif"
MONO    = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

# (text, px, weight, family) -> width in px, measured in Chromium against the
# real stacks. Anything absent falls back to a deliberately wide estimate.
MEASURED = {
 ("Java 17+",13,700,"s"):56.2,("Spring Boot",13,700,"s"):76.13,("Spring Modulith",13,700,"s"):102.95,
 ("Spring Security",13,700,"s"):100.24,("Laravel",13,700,"s"):46.81,("NestJS",13,700,"s"):46.63,
 ("Node.js",13,700,"s"):49.4,("Go / Fiber",13,700,"s"):61.67,("PHP",13,700,"s"):27.47,
 ("Next.js",13,700,"s"):45.51,("React",13,700,"s"):36.97,("Vue 3 + Pinia",13,700,"s"):83.6,
 ("TypeScript",13,700,"s"):70.97,("JavaScript",13,700,"s"):69.04,("Tailwind",13,700,"s"):53.37,
 ("SvelteKit",13,700,"s"):58.48,("React Native",13,700,"s"):81.64,("Flutter",13,700,"s"):43.44,
 ("Dart",13,700,"s"):28.2,("Kotlin Multiplatform",13,700,"s"):128.83,("Android",13,700,"s"):51.37,
 ("PostgreSQL",13,700,"s"):76.95,("MySQL",13,700,"s"):45.91,("Redis",13,700,"s"):35.8,
 ("TimescaleDB",13,700,"s"):84.33,("Firebase",13,700,"s"):55.52,("Multi-datasource ACID",13,700,"s"):147.21,
 ("Docker",13,700,"s"):45.83,("Jenkins",13,700,"s"):50.17,("Nginx",13,700,"s"):37.43,
 ("GitHub Actions",13,700,"s"):97.58,("Git",13,700,"s"):18.75,("Grafana",13,700,"s"):51.12,
 ("Linux / VPS",13,700,"s"):72.45,("MikroTik RouterOS",13,700,"s"):120.65,("FreeRADIUS / AAA",13,700,"s"):118.36,
 ("PPPoE",13,700,"s"):41.85,("RADIUS Accounting",13,700,"s"):127.55,("CoA Disconnect",13,700,"s"):102.81,
 ("OLT & NOC",13,700,"s"):70.88,("Duitku",13,700,"s"):42.49,("BRI Fixed VA",13,700,"s"):80.99,
 ("Midtrans",13,700,"s"):57.46,("QRIS",13,700,"s"):31.87,("Double-Entry GL",13,700,"s"):107.32,
 ("Reconciliation",13,700,"s"):91.31,("C++",13,700,"s"):26.86,("Rust",13,700,"s"):29.57,
 ("Python",13,700,"s"):45.99,("WebSocket",13,700,"s"):72.92,("Express",13,700,"s"):51.42,
 ("WHOAMI",22,900,"d"):104.34,("NOW",22,900,"d"):58.28,("THE ARSENAL",22,900,"d"):173.34,
 ("WAR STORIES",22,900,"d"):170.36,("CAREER",22,900,"d"):100.22,("SHIPPED IT",22,900,"d"):139.34,
 ("TALKED AT PEOPLE",22,900,"d"):240.22,("SAY HI",22,900,"d"):82.47,
 ("BACKEND",12,900,"d"):65.57,("FRONTEND",12,900,"d"):73.79,("PAYMENTS",12,900,"d"):72.62,
 ("SYSTEMS",12,900,"d"):63.47,("NETWORK",12,900,"d"):68.45,("MOBILE",12,900,"d"):52.0,
 ("DATA",12,900,"d"):34.51,("INFRA",12,900,"d"):41.34,
 ("BONSKY",92,900,"d"):439.47,("SENIOR FULL STACK ENGINEER",17,900,"d"):300.75,
 ("@ SBLNET",17,900,"d"):93.81,
 ("LinkedIn",15,900,"d"):70.35,("Email",15,900,"d"):45.83,("SBLNET",15,900,"d"):66.67,
}
SAFETY = 1.05          # cross-platform headroom; only ever adds padding

def tw(text, size, weight=700, fam="s", tracking=0.0):
    tr = tracking * max(len(text) - 1, 0)
    hit = MEASURED.get((text, size, weight, fam))
    if hit is not None:
        return hit * SAFETY + tr
    if fam == "m":                                   # monospace is computable
        return len(text) * size * 0.605 + tr
    per = 0.78 if fam == "d" else 0.52 if fam == "e" else 0.58
    return len(text) * size * per * SAFETY + tr

FAM = {"s": SANS, "d": DISPLAY, "m": MONO, "e": MEME}

def esc(s):
    return html.escape(s, quote=False)

def text(x, y, s, size, fill, fam="s", weight=700, anchor="start", tracking=0.0, extra=""):
    ls = f' letter-spacing="{tracking}"' if tracking else ""
    an = f' text-anchor="{anchor}"' if anchor != "start" else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FAM[fam]}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}"{an}{ls}{extra}>{esc(s)}</text>')

# ─────────────────────────────────────────────────── the brutalist primitive
def block(x, y, w, h, fill, t, shadow=7, bw=3, r=0):
    """A hard-shadowed, thick-outlined rectangle. The whole language in one call."""
    rr = f' rx="{r}"' if r else ""
    return (f'<rect x="{x+shadow:.1f}" y="{y+shadow:.1f}" width="{w:.1f}" height="{h:.1f}"{rr} fill="{t["ink"]}"/>'
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"{rr} fill="{fill}" '
            f'stroke="{edge(fill, t)}" stroke-width="{bw}"/>')

# ───────────────────────────────────────────────────────── icon symbols
MONO_ICONS = {"nextjs", "rust", "express", "socketio", "linkedin"}
ICON_FILES = {
    "java":"java-original","spring":"spring-original","laravel":"laravel-original","php":"php-original",
    "node":"nodejs-original","nest":"nestjs-original","go":"go-original","rust":"mono-rust",
    "nextjs":"mono-nextdotjs","react":"react-original","vue":"vuejs-original","ts":"typescript-original",
    "js":"javascript-original","tailwind":"tailwindcss-original","svelte":"svelte-original",
    "flutter":"flutter-original","dart":"dart-original","kotlin":"kotlin-original","android":"android-original",
    "postgres":"postgresql-original","mysql":"mysql-original","redis":"redis-original","firebase":"firebase-plain",
    "docker":"docker-original","jenkins":"jenkins-original","nginx":"nginx-original","gha":"githubactions-original",
    "git":"git-original","python":"python-original","cpp":"cplusplus-original","grafana":"grafana-original",
    "express":"mono-express","socketio":"mono-socketdotio","linkedin":"mono-linkedin",
}
_ID = re.compile(r'id="([^"]+)"')
_FILL = re.compile(r'\sfill="[^"]*"')
_STYLE_FILL = re.compile(r'fill:\s*[^;"]+;?')

def symbol_inner(key, mono_fill=None):
    with open(os.path.join(ICONS, ICON_FILES[key] + ".svg"), encoding="utf-8") as fh:
        raw = fh.read()
    vb = re.search(r'viewBox="([^"]+)"', raw).group(1)
    inner = raw[raw.index(">", raw.index("<svg")) + 1: raw.rindex("</svg>")]
    inner = re.sub(r"<title>.*?</title>", "", inner, flags=re.S)
    for old in set(_ID.findall(inner)):              # namespace ids across icons
        new = f"{key}_{old}"
        inner = (inner.replace(f'id="{old}"', f'id="{new}"')
                      .replace(f"url(#{old})", f"url(#{new})")
                      .replace(f'href="#{old}"', f'href="#{new}"'))
    if key in MONO_ICONS:
        inner = _STYLE_FILL.sub("", _FILL.sub("", inner))
        inner = f'<g fill="{mono_fill}">{inner}</g>'
    return vb, inner

def sym(key, t):
    vb, inner = symbol_inner(key, "#000000")         # icons always sit on light chips
    return f'<symbol id="ic-{key}" viewBox="{vb}">{inner}</symbol>'

def use(key, x, y, size):
    return (f'<use href="#ic-{key}" xlink:href="#ic-{key}" x="{x:.1f}" y="{y:.1f}" '
            f'width="{size}" height="{size}"/>')

# ─────────────────────────────────────────────────────────────────── hero
TAGLINE = "// interested in new things. addicted to code. that's all."


def build_hero(t):
    W, H, SH = 1200, 404, 9
    CX, CY, CW, CH = 5, 5, 1180, 386
    a = []
    css = ["@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}",
           "@keyframes nudge{0%,100%{transform:rotate(-11deg)}50%{transform:rotate(-8deg)}}",
           ".cur{animation:blink 1s step-end infinite}",
           ".stamp{transform-box:fill-box;transform-origin:center;animation:nudge 5s ease-in-out infinite}",
           "@media(prefers-reduced-motion:reduce){*{animation:none!important}}"]
    defs = [f'<pattern id="grid" width="26" height="26" patternUnits="userSpaceOnUse">'
            f'<path d="M26 0H0V26" fill="none" stroke="{t["grid"]}" stroke-opacity="{t["gridop"]}" stroke-width="1"/>'
            f'</pattern>']

    # card + graph-paper texture
    a.append(block(CX, CY, CW, CH, t["panel"], t, shadow=SH, bw=4))
    a.append(f'<rect x="{CX+2}" y="{CY+46}" width="{CW-4}" height="{CH-48}" fill="url(#grid)"/>')

    # terminal chrome
    a.append(f'<rect x="{CX+2}" y="{CY+2}" width="{CW-4}" height="44" fill="{t["ink"]}"/>')
    for i, c in enumerate([POP["pink"], POP["yellow"], POP["lime"]]):
        a.append(f'<circle cx="{CX+30+i*26}" cy="{CY+24}" r="7.5" fill="{c}"/>')
    a.append(text(CX+118, CY+29, "bonsky@sblnet: ~/who-dis", 13, t["paper"], "m", 400))
    a.append(text(CX+CW-24, CY+29, "STATUS: SHIPPING TO PROD", 12, POP["lime"], "m", 700, anchor="end"))

    # BONSKY — a yellow highlight block, because subtlety is not the assignment
    bw_ = tw("BONSKY", 92, 900, "d")
    a.append(text(CX+34, CY+96, "MUHAMMAD ILHAM RAFIANNANDHA", 13, t["sub"], "m", 700, tracking=1.6))
    a.append(block(CX+30, CY+112, bw_+46, 96, POP["yellow"], t, shadow=8, bw=4))
    a.append(text(CX+53, CY+186, "BONSKY", 92, "#000000", "d", 900))

    # role + employer
    rw = tw("SENIOR FULL STACK ENGINEER", 17, 900, "d") + 38
    a.append(block(CX+30, CY+232, rw, 42, t["ink"], t, shadow=6, bw=3))
    a.append(text(CX+49, CY+260, "SENIOR FULL STACK ENGINEER", 17, t["paper"], "d", 900))
    aw = tw("@ SBLNET", 17, 900, "d") + 38
    a.append(block(CX+42+rw, CY+232, aw, 42, POP["cyan"], t, shadow=6, bw=3))
    a.append(text(CX+61+rw, CY+260, "@ SBLNET", 17, "#000000", "d", 900))

    # tagline with a blinking block cursor
    a.append(f'<text x="{CX+34}" y="{CY+318}" font-family="{MONO}" font-size="13.5" fill="{t["text"]}">'
             f'{esc(TAGLINE)}'
             f'<tspan class="cur" fill="{POP["pink"]}">█</tspan></text>')
    a.append(text(CX+34, CY+356, "java · spring modulith · next.js · react native · kotlin multiplatform · mikrotik",
                  12, t["sub"], "m", 400))

    for i, (px, py, rot) in enumerate(((624, 352, -14), (668, 330, -8), (712, 344, -18), (756, 322, -6))):
        a.append(paw(px, py, rot, 0.9, t["text"], 0.13 + i * 0.03))

    # a cat, occupying the gap that was previously just empty grid
    cat_m, cat_css = cat_sitting()
    css += cat_css
    a.append(f'<g transform="translate(636,198) scale(1.17)">{cat_m}</g>')

    # ── the stamp: peak "trust me bro" energy
    scx, scy, R = 952, 200, 110
    defs.append(f'<path id="arc" fill="none" d="M 0,-{R-19} A {R-19},{R-19} 0 1,1 0,{R-19} A {R-19},{R-19} 0 1,1 0,-{R-19}"/>')
    s = [f'<circle r="{R}" fill="{POP["pink"]}" stroke="#000" stroke-width="4"/>',
         f'<circle r="{R-30}" fill="none" stroke="#000" stroke-width="2.5"/>',
         f'<text font-family="{MEME}" font-size="17" fill="#000" letter-spacing="2.4">'
         f'<textPath href="#arc" xlink:href="#arc" startOffset="0">'
         f'{esc("WORKS ON MY MACHINE ★ CERTIFIED ★ ")}</textPath></text>',
         f'<text y="-6" text-anchor="middle" font-family="{MEME}" font-size="40" fill="#000">SHIP</text>',
         f'<text y="32" text-anchor="middle" font-family="{MEME}" font-size="40" fill="#000">IT</text>']
    a.append(f'<g transform="translate({scx},{scy})"><g class="stamp">{"".join(s)}</g></g>')

    return wrap(W, H, defs, a, css, "Bonsky — Senior Full Stack Engineer")

# ────────────────────────────────────────────────────────────────── stats
STATS = [("6+", "YEARS SHIPPING", "yellow", -1.3),
         ("11", "COMPANIES & CLIENTS", "cyan", 1.1),
         ("25+", "PRODUCTS SHIPPED", "lime", -1.0),
         ("NaN", "KNOWN BUGS *", "pink", 1.4),
         ("@CAT", "CAT NAMED CIMOL", "orange", -1.6)]

def build_stats(t):
    W, H, SH = 1200, 176, 7
    n = len(STATS); gap = 18
    bw_ = (W - 12 - gap * (n - 1) - SH) / n
    a = []
    for i, (num, label, col, rot) in enumerate(STATS):
        x = 6 + i * (bw_ + gap)
        g = [block(0, 0, bw_, 132, POP[col], t, shadow=SH, bw=3.5)]
        if num == "@CAT":
            g.append(f'<g transform="translate({bw_/2 - 30:.1f},18) scale(.8)">{cat_face()}</g>')
        else:
            g.append(text(bw_/2, 76, num, 54, "#000000", "d", 900, anchor="middle"))
        g.append(text(bw_/2, 106, label, 11, "#000000", "d", 900, anchor="middle", tracking=1.1))
        a.append(f'<g transform="translate({x:.1f},20) rotate({rot} {bw_/2:.1f} 66)">{"".join(g)}</g>')
    return wrap(W, H, [], a, [], "By the numbers")

# ────────────────────────────────────────────────────────────────── stack
STACK = [
 ("BACKEND","yellow",[("java","Java 17+"),("spring","Spring Boot"),("spring","Spring Modulith"),
   ("spring","Spring Security"),("laravel","Laravel"),("nest","NestJS"),("node","Node.js"),
   ("go","Go / Fiber"),("php","PHP")]),
 ("FRONTEND","cyan",[("nextjs","Next.js"),("react","React"),("vue","Vue 3 + Pinia"),("ts","TypeScript"),
   ("js","JavaScript"),("tailwind","Tailwind"),("svelte","SvelteKit")]),
 ("MOBILE","lime",[("react","React Native"),("flutter","Flutter"),("dart","Dart"),
   ("kotlin","Kotlin Multiplatform"),("android","Android")]),
 ("DATA","pink",[("postgres","PostgreSQL"),("mysql","MySQL"),("redis","Redis"),(None,"TimescaleDB"),
   ("firebase","Firebase"),(None,"Multi-datasource ACID")]),
 ("INFRA","orange",[("docker","Docker"),("jenkins","Jenkins"),("nginx","Nginx"),("gha","GitHub Actions"),
   ("git","Git"),("grafana","Grafana"),(None,"Linux / VPS")]),
 ("NETWORK","purple",[(None,"MikroTik RouterOS"),(None,"FreeRADIUS / AAA"),(None,"PPPoE"),
   (None,"RADIUS Accounting"),(None,"CoA Disconnect"),(None,"OLT & NOC")]),
 ("PAYMENTS","yellow",[(None,"Duitku"),(None,"BRI Fixed VA"),(None,"Midtrans"),(None,"QRIS"),
   (None,"Double-Entry GL"),(None,"Reconciliation")]),
 ("SYSTEMS","cyan",[("cpp","C++"),("rust","Rust"),("python","Python"),("socketio","WebSocket"),
   ("express","Express")]),
]

def balance(items, avail, gap, width_of):
    """Fewest lines, then evened out — a lone orphan chip reads as a bug."""
    ws = [width_of(i) for i in items]
    def pack(limit):
        rows, cur, cw = [], [], 0.0
        for it, w in zip(items, ws):
            nw = w if not cur else cw + gap + w
            if cur and nw > limit: rows.append(cur); cur, cw = [it], w
            else:                  cur.append(it); cw = nw
        if cur: rows.append(cur)
        return rows
    n = len(pack(avail))
    if n < 2: return pack(avail)
    lo, hi = max(ws), avail
    for _ in range(40):
        mid = (lo + hi) / 2
        if len(pack(mid)) <= n: hi = mid
        else:                   lo = mid
    return pack(hi)

def build_stack(t):
    W, LX, CX, MAXX = 1200, 6, 178, 1188
    RH, GAP, RGAP, SH = 38, 12, 20, 5
    ICON, LEAD_I, LEAD_D, RPAD = 18, 42, 26, 16
    used, y, a = set(), 6, []

    for label, col, items in STACK:
        def cwidth(it):
            return (LEAD_I if it[0] else LEAD_D) + tw(it[1], 13, 700, "s") + RPAD
        lw = tw(label, 12, 900, "d", 1.3) + 26
        a.append(block(LX, y, lw, RH, POP[col], t, shadow=SH, bw=3))
        a.append(text(LX + 13, y + RH/2 + 4.5, label, 12, "#000000", "d", 900, tracking=1.3))

        for line in balance(items, MAXX - CX - SH, GAP, cwidth):
            x = CX
            for key, lbl in line:
                w = cwidth((key, lbl))
                a.append(block(x, y, w, RH, t["panel"], t, shadow=SH, bw=2.5))
                if key:
                    used.add(key)
                    a.append(f'<rect x="{x+9}" y="{y+(RH-ICON-6)/2}" width="{ICON+6}" height="{ICON+6}" fill="#FFFFFF"/>')
                    a.append(use(key, x + 12, y + (RH - ICON) / 2, ICON))
                    tx = x + LEAD_I
                else:
                    a.append(f'<rect x="{x+13}" y="{y+RH/2-5}" width="10" height="10" fill="{POP[col]}" '
                             f'stroke="#000" stroke-width="2"/>')
                    tx = x + LEAD_D
                a.append(text(tx, y + RH/2 + 4.5, lbl, 13, t["text"], "s", 700))
                x += w + GAP
            y += RH + GAP
        y += RGAP - GAP
    H = y - RGAP + GAP + SH + 6
    nap, css = cat_sleeping()
    css.append("@media(prefers-reduced-motion:reduce){*{animation:none!important}}")
    a.append(f'<g transform="translate(946,{H + 4})">{nap}</g>')
    return wrap(W, H + 118, [sym(k, t) for k in sorted(used)], a, css, "Stack")

# ─────────────────────────────────────────────────────── section headers
SECTIONS = [("WHOAMI","yellow"), ("NOW","cyan"), ("THE ARSENAL","lime"), ("WAR STORIES","pink"),
            ("CAREER","orange"), ("SHIPPED IT","purple"), ("TALKED AT PEOPLE","yellow"), ("SAY HI","cyan")]

def build_section(title, col, t):
    H, SH, PADX = 50, 6, 22
    w = tw(title, 22, 900, "d", 0.8) + PADX * 2 + 30
    a = [block(2, 2, w, H, POP[col], t, shadow=SH, bw=3.5),
         f'<rect x="{2+PADX-4}" y="{2+H/2-7}" width="14" height="14" fill="#000000"/>',
         text(2 + PADX + 20, 2 + H/2 + 8, title, 22, "#000000", "d", 900, tracking=0.8)]
    return wrap(round(w + SH + 4), H + SH + 4, [], a, [], title)

# ────────────────────────────────────────────────────────────────  badges
def g_envelope():
    return ('<g fill="none" stroke="#000" stroke-width="2.2" stroke-linejoin="round">'
            '<rect x="1" y="3" width="18" height="14"/><path d="M1.8 4.2 10 11.2 18.2 4.2"/></g>')

def g_signal():
    return ('<g fill="none" stroke="#000" stroke-width="2.2" stroke-linecap="round">'
            '<path d="M3.5 13.5a9 9 0 0 1 13 0"/><path d="M6.8 16.6a4.6 4.6 0 0 1 6.4 0"/>'
            '<circle cx="10" cy="19" r="1.4" fill="#000"/><path d="M.6 10.2a13.4 13.4 0 0 1 18.8 0"/></g>')

def g_globe():
    return ('<g fill="none" stroke="#000" stroke-width="2.2">'
            '<circle cx="10" cy="10" r="9"/><path d="M1 10h18"/>'
            '<path d="M10 1c2.4 2.5 3.7 5.6 3.7 9S12.4 16.5 10 19c-2.4-2.5-3.7-5.6-3.7-9S7.6 3.5 10 1z"/></g>')

BADGES = [("linkedin","LinkedIn","cyan",None), ("email","Email","yellow",g_envelope),
          ("sblnet","SBLNET","pink",g_signal), ("site","Portfolio","lime",g_globe)]

def build_badge(slug, label, col, glyph, t):
    H, SH, PADX, ICON = 46, 6, 17, 20
    w = PADX + ICON + 11 + tw(label, 15, 900, "d") + PADX
    a = [block(2, 2, w, H, POP[col], t, shadow=SH, bw=3)]
    iy = 2 + (H - ICON) / 2
    if glyph:
        a.append(f'<g transform="translate({2+PADX},{iy:.1f})">{glyph()}</g>')
    else:
        _, inner = symbol_inner(slug, "#000000")
        a.append(f'<g transform="translate({2+PADX},{iy:.1f}) scale({ICON/24:.4f})">{inner}</g>')
    a.append(text(2 + PADX + ICON + 11, 2 + H/2 + 6, label, 15, "#000000", "d", 900))
    return wrap(round(w + SH + 4), H + SH + 4, [], a, [], label)

# ─────────────────────────────────────────────────────────────────── cats
# Brutalist cats: flat fill, 3px black outline, no gradients. Each returns
# (markup, css) so the caller can merge keyframes into its own <style>.
CAT = "#FF8A3D"      # one orange tabby, reused everywhere, so it reads as
CAT_EAR = "#FF9EC4"  # the same animal rather than three unrelated cats


def _face(cx, cy, r, ink):
    """Shared muzzle: eyes that blink, nose, whiskers."""
    o = []
    for ex in (cx - r * 0.35, cx + r * 0.35):
        o.append(f'<ellipse class="eye" cx="{ex:.1f}" cy="{cy:.1f}" rx="{r*0.15:.1f}" '
                 f'ry="{r*0.20:.1f}" fill="{ink}"/>')
    o.append(f'<path d="M {cx-r*0.13:.1f},{cy+r*0.28:.1f} L {cx+r*0.13:.1f},{cy+r*0.28:.1f} '
             f'L {cx:.1f},{cy+r*0.44:.1f} Z" fill="{ink}"/>')
    for sx in (-1, 1):
        for k, dy in enumerate((-0.10, 0.06, 0.22)):
            x1 = cx + sx * r * 0.42
            o.append(f'<line x1="{x1:.1f}" y1="{cy+r*0.30+dy*r*0.30:.1f}" '
                     f'x2="{x1 + sx*r*0.62:.1f}" y2="{cy+r*0.22+dy*r*0.55:.1f}" '
                     f'stroke="{ink}" stroke-width="2.4" stroke-linecap="round"/>')
    return "".join(o)


def cat_sitting(ink="#000000", wave=False):
    """Sitting tabby. Tail swishes; one paw waves if asked (maneki-neko)."""
    css = ["@keyframes tail{0%,100%{transform:rotate(-13deg)}50%{transform:rotate(15deg)}}",
           "@keyframes eye{0%,92%,100%{transform:scaleY(1)}95.5%{transform:scaleY(.08)}}",
           ".tail{transform-box:fill-box;transform-origin:8% 92%;animation:tail 2.6s ease-in-out infinite}",
           ".eye{transform-box:fill-box;transform-origin:center;animation:eye 4.6s ease-in-out infinite}"]
    o = [f'<g class="tail"><path d="M 92,140 C 128,140 138,104 122,76" fill="none" stroke="{ink}" '
         f'stroke-width="17" stroke-linecap="round"/><path d="M 92,140 C 128,140 138,104 122,76" '
         f'fill="none" stroke="{CAT}" stroke-width="10" stroke-linecap="round"/></g>',
         # ears first so the head outline sits on top of their bases
         f'<path d="M 32,44 L 26,4 L 60,28 Z" fill="{CAT}" stroke="{ink}" stroke-width="3" stroke-linejoin="round"/>',
         f'<path d="M 88,44 L 94,4 L 60,28 Z" fill="{CAT}" stroke="{ink}" stroke-width="3" stroke-linejoin="round"/>',
         f'<path d="M 36,38 L 33,15 L 52,28 Z" fill="{CAT_EAR}"/>',
         f'<path d="M 84,38 L 87,15 L 68,28 Z" fill="{CAT_EAR}"/>',
         f'<path d="M 24,150 C 24,102 38,86 60,86 C 82,86 96,102 96,150 Z" fill="{CAT}" '
         f'stroke="{ink}" stroke-width="3" stroke-linejoin="round"/>',
         f'<rect x="30" y="136" width="24" height="15" rx="7" fill="{CAT}" stroke="{ink}" stroke-width="3"/>',
         f'<rect x="66" y="136" width="24" height="15" rx="7" fill="{CAT}" stroke="{ink}" stroke-width="3"/>',
         f'<circle cx="60" cy="62" r="34" fill="{CAT}" stroke="{ink}" stroke-width="3"/>',
         # tabby stripes
         f'<path d="M 52,32 v 9 M 60,30 v 10 M 68,32 v 9" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>',
         _face(60, 62, 34, ink)]
    if wave:
        css.append("@keyframes wave{0%,100%{transform:rotate(-8deg)}50%{transform:rotate(26deg)}}")
        css.append(".paw{transform-box:fill-box;transform-origin:15% 96%;"
                   "animation:wave 1.1s ease-in-out infinite}")
        arc = "M 88,112 C 112,106 124,78 120,50"
        o.append(f'<g class="paw"><path d="{arc}" fill="none" stroke="{ink}" stroke-width="17" '
                 f'stroke-linecap="round"/><path d="{arc}" fill="none" stroke="{CAT}" stroke-width="10" '
                 f'stroke-linecap="round"/>'
                 f'<circle cx="120" cy="44" r="13" fill="{CAT}" stroke="{ink}" stroke-width="3"/></g>')
        o.append(f'<path d="M 34,88 Q 60,102 86,88" fill="none" stroke="{ink}" stroke-width="3.5"/>')
        o.append(f'<circle cx="60" cy="98" r="8" fill="{POP["yellow"]}" stroke="{ink}" stroke-width="3"/>')
    return "".join(o), css


def cat_sleeping(ink="#000000"):
    """Curled, breathing, emitting Z's. Cats sleep on your work; so does this one."""
    css = ["@keyframes breathe{0%,100%{transform:scaleY(1)}50%{transform:scaleY(1.045)}}",
           "@keyframes zzz{0%{opacity:0;transform:translate(0,6px) scale(.7)}"
           "25%{opacity:1}100%{opacity:0;transform:translate(16px,-30px) scale(1.15)}}",
           ".body{transform-box:fill-box;transform-origin:center bottom;"
           "animation:breathe 3.4s ease-in-out infinite}",
           ".z{animation:zzz 3.6s ease-in-out infinite}"]
    o = [f'<g class="body">',
         f'<path d="M 214,84 C 208,116 150,120 116,104" fill="none" stroke="{ink}" stroke-width="15" stroke-linecap="round"/>',
         f'<path d="M 214,84 C 208,116 150,120 116,104" fill="none" stroke="{CAT}" stroke-width="9" stroke-linecap="round"/>',
         f'<ellipse cx="126" cy="68" rx="94" ry="37" fill="{CAT}" stroke="{ink}" stroke-width="3"/>',
         f'<path d="M 28,60 L 20,26 L 52,40 Z" fill="{CAT}" stroke="{ink}" stroke-width="3" stroke-linejoin="round"/>',
         f'<path d="M 76,48 L 88,20 L 94,52 Z" fill="{CAT}" stroke="{ink}" stroke-width="3" stroke-linejoin="round"/>',
         f'<circle cx="56" cy="72" r="35" fill="{CAT}" stroke="{ink}" stroke-width="3"/>',
         f'<path d="M 38,68 q 9,9 18,0 M 64,68 q 9,9 18,0" fill="none" stroke="{ink}" '
         f'stroke-width="3.2" stroke-linecap="round"/>',
         f'<path d="M 50,84 L 62,84 L 56,92 Z" fill="{ink}"/>',
         f'<path d="M 132,42 v 9 M 150,40 v 10 M 168,43 v 9" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>',
         '</g>']
    for i, (dx, dy, sz) in enumerate(((96, 18, 20), (120, 4, 26), (148, -8, 32))):
        o.append(f'<text class="z" style="animation-delay:{i*1.2:.1f}s" x="{dx}" y="{dy}" '
                 f'font-family="{DISPLAY}" font-size="{sz}" font-weight="900" fill="{ink}">Z</text>')
    return "".join(o), css


def build_cat_wave(t):
    """Standalone maneki-neko for the contact section."""
    m, css = cat_sitting(wave=True)
    css.append("@media(prefers-reduced-motion:reduce){*{animation:none!important}}")
    body = [f'<g transform="translate(16,34)">{m}</g>',
            text(178, 104, "HALO!", 32, t["text"], "d", 900),
            text(178, 132, "(the cat insists)", 13, t["sub"], "m", 400)]
    return wrap(372, 214, [], body, css, "A cat waving hello")


def cat_face(r=1.0, ink="#000000"):
    """Just the head — for places too small to hold a whole cat."""
    return "".join([
        f'<path d="M 14,26 L 9,2 L 33,17 Z" fill="{CAT}" stroke="{ink}" stroke-width="2.6" stroke-linejoin="round"/>',
        f'<path d="M 62,26 L 67,2 L 43,17 Z" fill="{CAT}" stroke="{ink}" stroke-width="2.6" stroke-linejoin="round"/>',
        f'<path d="M 17,22 L 15,9 L 28,17 Z" fill="{CAT_EAR}"/>',
        f'<path d="M 59,22 L 61,9 L 48,17 Z" fill="{CAT_EAR}"/>',
        f'<circle cx="38" cy="42" r="27" fill="{CAT}" stroke="{ink}" stroke-width="2.6"/>',
        f'<path d="M 31,18 v 7 M 38,16 v 8 M 45,18 v 7" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>',
        _face(38, 42, 27, ink),
    ])


def paw(x, y, rot, sc, fill, op):
    """A single paw print."""
    d = [f'<ellipse cx="0" cy="4" rx="7" ry="5.6"/>']
    for tx, ty in ((-6.4, -4.2), (-2.2, -6.6), (2.2, -6.6), (6.4, -4.2)):
        d.append(f'<circle cx="{tx}" cy="{ty}" r="2.5"/>')
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({sc})" fill="{fill}" '
            f'opacity="{op}">{"".join(d)}</g>')


def cat_walking(ink="#000000"):
    """Side view. Legs swing, tail swishes, whole cat crosses the page."""
    css = ["@keyframes stroll{0%{transform:translateX(-190px)}100%{transform:translateX(1290px)}}",
           "@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}",
           "@keyframes legf{0%{transform:rotate(-20deg)}100%{transform:rotate(20deg)}}",
           "@keyframes legb{0%{transform:rotate(20deg)}100%{transform:rotate(-20deg)}}",
           "@keyframes swish{0%,100%{transform:rotate(-10deg)}50%{transform:rotate(12deg)}}",
           ".stroll{animation:stroll 17s linear infinite}",
           ".bob{animation:bob .52s ease-in-out infinite}",
           ".lf{transform-box:fill-box;transform-origin:50% 4%;animation:legf .52s ease-in-out infinite alternate}",
           ".lb{transform-box:fill-box;transform-origin:50% 4%;animation:legb .52s ease-in-out infinite alternate}",
           ".sw{transform-box:fill-box;transform-origin:6% 90%;animation:swish 1.5s ease-in-out infinite}"]
    leg = lambda x, c: (f'<rect class="{c}" x="{x}" y="46" width="11" height="38" rx="5" '
                        f'fill="{CAT}" stroke="{ink}" stroke-width="3"/>')
    o = [f'<g class="sw"><path d="M 20,50 C -2,44 -6,20 8,8" fill="none" stroke="{ink}" stroke-width="16" '
         f'stroke-linecap="round"/><path d="M 20,50 C -2,44 -6,20 8,8" fill="none" stroke="{CAT}" '
         f'stroke-width="9" stroke-linecap="round"/></g>',
         leg(34, "lb"), leg(86, "lf"),
         f'<ellipse cx="66" cy="38" rx="46" ry="25" fill="{CAT}" stroke="{ink}" stroke-width="3"/>',
         leg(50, "lf"), leg(100, "lb"),
         f'<path d="M 100,22 L 96,-2 L 118,12 Z" fill="{CAT}" stroke="{ink}" stroke-width="3" stroke-linejoin="round"/>',
         f'<path d="M 134,22 L 140,0 L 118,14 Z" fill="{CAT}" stroke="{ink}" stroke-width="3" stroke-linejoin="round"/>',
         f'<circle cx="118" cy="34" r="25" fill="{CAT}" stroke="{ink}" stroke-width="3"/>',
         f'<path d="M 110,12 v 7 M 118,10 v 8 M 126,12 v 7" stroke="{ink}" stroke-width="2.8" stroke-linecap="round"/>',
         _face(118, 34, 25, ink)]
    return f'<g class="bob">{"".join(o)}</g>', css


def build_walk(t):
    """A divider: Cimol crosses the page on a hard black rule."""
    m, css = cat_walking()
    css.append("@media(prefers-reduced-motion:reduce){.stroll{animation:none;transform:translateX(500px)}"
               "*{animation:none!important}}")
    body = [f'<rect x="0" y="92" width="1200" height="5" fill="{t["ink"]}"/>']
    for i, x in enumerate((90, 210, 330, 450)):
        body.append(paw(x, 84, -8, 0.85, t["ink"], 0.16 + i * 0.04))
    body.append(f'<g class="stroll"><g transform="translate(0,8)">{m}</g></g>')
    return wrap(1200, 104, [], body, css, "A cat walking across the page")

# ───────────────────────────────────────────────────── case-study banner
BANNERS = [("isp", "ISP PLATFORM", "27 MODULES \u00b7 8 DATABASES \u00b7 ONE MONOLITH", "yellow")]


def build_banner(title, sub, col, t):
    W, H, SH = 1200, 176, 9
    a = [block(5, 5, W - 14 - SH, H - 14 - SH, POP[col], t, shadow=SH, bw=4),
         f'<rect x="7" y="7" width="{W-18-SH}" height="34" fill="#000000"/>',
         text(24, 30, "ARCHITECTURE CASE STUDY", 12, POP[col], "m", 700, tracking=2.2),
         text(W - 30 - SH, 30, "github.com/ilhamrafi44", 12, POP[col], "m", 400, anchor="end"),
         text(34, 108, title, 56, "#000000", "d", 900),
         text(34, 140, sub, 15, "#000000", "d", 900, tracking=1.2),
         f'<g transform="translate(980,52) scale(.72)">{cat_sitting()[0]}</g>']
    _, ccss = cat_sitting()
    ccss.append("@media(prefers-reduced-motion:reduce){*{animation:none!important}}")
    return wrap(W, H, [], a, ccss, f"{title} - architecture case study")


# ─────────────────────────────────────────────────────────────────── shell
def wrap(w, h, defs, body, css, title):
    style = f"<style>{''.join(css)}</style>" if css else ""
    d = f"<defs>{''.join(defs)}</defs>" if defs else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(title)}" '
            f'fill="none">{style}{d}{"".join(body)}</svg>')

MANIFEST = {}


def emit(name, svg):
    # Parse before writing: a stray quote in a font stack silently produces a
    # file that every browser refuses to render.
    import xml.etree.ElementTree as ET, hashlib
    try:
        ET.fromstring(svg)
    except ET.ParseError as e:
        raise SystemExit(f"malformed SVG in {name}: {e}")
    key = name[:-4] if name.endswith(".svg") else name
    digest = hashlib.sha256(svg.encode()).hexdigest()[:8]
    fname = f"{key}.{digest}.svg"
    MANIFEST[key] = fname
    p = os.path.join(OUT, fname)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(svg)
    return os.path.getsize(p)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        os.remove(os.path.join(OUT, f))
    total = 0
    for mode, t in THEMES.items():
        for base, svg in (("hero", build_hero(t)), ("stats", build_stats(t)), ("stack", build_stack(t))):
            total += emit(f"{base}-{mode}.svg", svg)
        for title, col in SECTIONS:
            slug = title.lower().replace(" ", "-")
            total += emit(f"sec-{slug}-{mode}.svg", build_section(title, col, t))
        total += emit(f"cat-wave-{mode}.svg", build_cat_wave(t))
        total += emit(f"cat-walk-{mode}.svg", build_walk(t))
        for slug, title, sub, col in BANNERS:
            total += emit(f"banner-{slug}-{mode}.svg", build_banner(title, sub, col, t))
        for slug, label, col, glyph in BADGES:
            total += emit(f"badge-{slug}-{mode}.svg", build_badge(slug, label, col, glyph, t))
    import json
    with open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(MANIFEST, fh, indent=1, sort_keys=True)
    print(f"  {len(MANIFEST)} assets, {total/1024:.0f} KB (content-hashed)")
