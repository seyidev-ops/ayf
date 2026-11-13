#!/usr/bin/env python3
"""Builds the static Adamu Yola Foundation site into the repo folder."""
import os, re, html
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://adamuyolafoundation.org/'
MARK_LAYERS = [('arc', 1.136, 1.692, 61.716), ('p1', 3.605, 35.473, 25.627), ('p2', 17.398, 24.737, 20.964), ('p3', 36.129, 19.02, 30.133), ('p4', 50.784, 16.511, 47.962), ('h1', 5.878, 39.907, 5.799), ('h2', 21.787, 24.329, 7.132), ('h3', 44.906, 16.103, 10.658), ('h4', 78.958, 22.695, 11.324)]
V = "20261113-3"

def I(name, cls=''):
    p = {
        'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
        'chev': '<path d="M6 9l6 6 6-6"/>',
        'plus': '<path d="M12 5v14M5 12h14"/>',
        'crumb': '<path d="M9 6l6 6-6 6"/>',
        'up': '<path d="M12 19V5M6 11l6-6 6 6"/>',
        'x': '<path d="M6 6l12 12M18 6L6 18"/>',
        'left': '<path d="M15 6l-6 6 6 6"/>',
        'right': '<path d="M9 6l6 6-6 6"/>',
        'book': '<path d="M4 5a2 2 0 012-2h13v15H6a2 2 0 00-2 2zM4 20a2 2 0 002 2h13v-4"/>',
        'tool': '<path d="M14.7 6.3a4 4 0 00-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 005.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/>',
        'ball': '<circle cx="12" cy="12" r="9"/><path d="M12 7l4 3-1.5 4.5h-5L8 10z M12 3v4M21 10.5l-5-.5M18 19l-3.5-4.5M6 19l3.5-4.5M3 10.5l5-.5"/>',
        'heart': '<path d="M20.8 4.6a5.5 5.5 0 00-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 00-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 000-7.8z"/>',
        'trophy': '<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 01-10 0zM17 5h3v2a3 3 0 01-3 3M7 5H4v2a3 3 0 003 3"/>',
        'archive': '<path d="M3 4h18v4H3zM5 8v12h14V8M10 12h4"/>',
        'users': '<circle cx="9" cy="7" r="3.5"/><path d="M2 21v-1a6 6 0 0112 0v1M16 3.5a3.5 3.5 0 010 7M22 21v-1a6 6 0 00-4-5.6"/>',
        'flag': '<path d="M4 22V4M4 4h12l-2 4 2 4H4"/>',
        'compass': '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
        'news': '<path d="M4 4h13v16H6a2 2 0 01-2-2zM17 8h3v10a2 2 0 01-2 2M8 8h5M8 12h5M8 16h3"/>',
        'image': '<rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="9" cy="9" r="2"/><path d="M21 15l-5-5L5 21"/>',
        'hand': '<path d="M11 14h2a2 2 0 000-4h-3c-.6 0-1.1.2-1.4.6L3 16M7 20l1.6-1.4c.3-.4.8-.6 1.4-.6h4c1.1 0 2.1-.4 2.8-1.2l4.6-4.4a2 2 0 00-2.8-2.8l-4.2 3.9M2 15l6 6"/>',
        'gift': '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v9H5v-9M7.5 8a2.5 2.5 0 010-5C11 3 12 8 12 8s1-5 4.5-5a2.5 2.5 0 010 5"/>',
        'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
        'phone': '<path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6A19.8 19.8 0 012.1 4.2 2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .4 1.9.7 2.8a2 2 0 01-.5 2.1L8 9.9a16 16 0 006 6l1.3-1.3a2 2 0 012.1-.4c.9.3 1.8.6 2.8.7a2 2 0 011.7 2z"/>',
        'pin': '<path d="M12 22s7-6.2 7-12a7 7 0 10-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
        'camera': '<path d="M3 8a2 2 0 012-2h2l2-2h6l2 2h2a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><circle cx="12" cy="13" r="3.5"/>',
        'play': '<path d="M7 4l13 8-13 8z" fill="currentColor" stroke="none"/>',
        'shield': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>',
        'leaf': '<path d="M5 21c0-9 5-15 15-16-1 10-7 15-15 16zM5 21l7-7"/>',
        'scale': '<path d="M12 3v18M7 21h10M5 7h14M5 7l-3 7a3 3 0 006 0zM19 7l-3 7a3 3 0 006 0z"/>',
        'star': '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
        'fb': '<path d="M14 8h3V4h-3a4 4 0 00-4 4v3H7v4h3v7h4v-7h3l1-4h-4V8z" fill="currentColor" stroke="none"/>',
        'ig': '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/>',
        'in': '<path d="M4 9h4v12H4zM6 3a2 2 0 110 4 2 2 0 010-4zM10 9h4v2c.6-1.1 2-2.3 4-2.3 3.5 0 4 2.3 4 5.3v7h-4v-6c0-1.5 0-3.3-2-3.3s-2.2 1.5-2.2 3.2V21H10z" fill="currentColor" stroke="none"/>',
        'external': '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 01-1 1H5a1 1 0 01-1-1V7a1 1 0 011-1h5"/>',
    }[name]
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'

FB = 'https://www.facebook.com/AdamuYolaFDN'
IGU = 'https://www.instagram.com/adamuyolafdn/'
LI = 'https://ng.linkedin.com/company/adamu-yola-foundation'
EMAIL = 'adamuytfoundation@gmail.com'
PHONE = '+234 812 063 8440'
TEL = '+2348120638440'
ADDRESS = 'No. 46 Billiri Street, Shongo Estate, Gombe State, Nigeria'

NAV = [
    ('About Us', 'about.html', [
        ('Our Story', 'about.html#story', 'How the foundation began in Gombe South', 'flag'),
        ('Mission, Vision & Values', 'about.html#mission', 'What we work towards and how', 'compass'),
        ('Leadership & History', 'about.html#leadership', 'Governance and a decade of milestones', 'users'),
    ]),
    ('Programmes & Projects', 'programs/', [
        ('Educational Scholarships', 'programs/scholarships.html', 'Keeping students in school', 'book'),
        ('Vocational Training', 'programs/vocational-training.html', 'Practical skills for livelihoods', 'tool'),
        ('Gombe South Unity Cup', 'programs/unity-cup.html', 'Football for peace and talent', 'ball'),
        ('Medical Outreach', 'programs/medical-outreach.html', 'Basic healthcare closer to home', 'heart'),
        ("Gombe State Principals' Cup", 'programs/principals-cup.html', 'Inter-school football across 11 LGAs', 'trophy'),
        ('Past Initiatives & Collaborations', 'programs/past-initiatives.html', 'Camps, farming support and partners', 'archive'),
    ]),
    ('News & Media', 'news.html', [
        ('News and Announcements', 'news.html', 'Results, updates and reports', 'news'),
        ('Photo & Video Gallery', 'gallery.html', 'Moments from the pitch and beyond', 'image'),
    ]),
    ('Get Involved', 'get-involved.html', [
        ('Partner / Sponsor', 'get-involved.html#partner', 'Back a programme or the Unity Cup', 'hand'),
        ('Volunteer', 'get-involved.html#volunteer', 'Give your time and skills', 'users'),
        ('Support / Donate', 'get-involved.html#support', 'Help fund opportunity', 'gift'),
    ]),
]

def esc(s): return html.escape(s, quote=True)

def head(title, desc, path, pfx, og_img='assets/photos/unity-cup-award-handshake.webp'):
    url = SITE + ('' if path == 'index.html' else path.replace('index.html', ''))
    full_title = 'Adamu Yola Foundation | Education, Skills, Health and Grassroots Sport in Gombe' if path == 'index.html' else f'{title} | Adamu Yola Foundation'
    return f'''<!doctype html>
<html lang="en-NG" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#172B4D">
<meta property="og:type" content="website"><meta property="og:site_name" content="Adamu Yola Foundation"><meta property="og:locale" content="en_NG">
<meta property="og:title" content="{esc(full_title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}assets/og-image.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Adamu Yola Foundation: Opportunity begins with people"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{SITE}assets/og-image.jpg">
<link rel="icon" href="{pfx}assets/brand/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="{pfx}assets/brand/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="{pfx}assets/brand/favicon-180.png">
<link rel="manifest" href="{pfx}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pfx}assets/site.css?v={V}">
<script>(function(){{var t;try{{t=localStorage.getItem('ayf-theme')}}catch(e){{}}if(t!=='light'&&t!=='dark'){{t=window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'}}document.documentElement.dataset.theme=t}})()</script>
<script defer src="{pfx}assets/site.js?v={V}"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def mark_html(cls=''):
    imgs = ''.join(f'<img class="m-{n[0]} m-{n}" src="__PFX__assets/brand/mark/{n}.webp" alt="" style="left:{l}%;top:{t}%;width:{w}%">' for n, l, t, w in MARK_LAYERS)
    return f'<span class="levitate"><span class="spin-interval" style="display:block"><span class="ayf-mark {cls}" role="img" aria-label="Adamu Yola Foundation">{imgs}</span></span></span>'

def header(pfx, active):
    nav = []
    for label, href, kids in NAV:
        wide = ' wide' if len(kids) > 3 else ''
        cur = ' aria-current="page"' if active == label else ''
        links = ''.join(f'<a href="{pfx}{h}"><span class="di">{I(ic)}</span><span><strong>{esc(t)}</strong><small>{esc(s)}</small></span></a>' for t, h, s, ic in kids)
        nav.append(f'<div class="nav-item has-menu"><button class="nav-link" aria-expanded="false" aria-haspopup="true"{cur}>{esc(label)} {I("chev","chev")}</button><div class="dropdown{wide}">{links}</div></div>')
    cur = ' aria-current="page"' if active == 'Contact' else ''
    nav.append(f'<div class="nav-item"><a class="nav-link" href="{pfx}contact.html"{cur}>Contact</a></div>')
    drawer = ''.join(
        f'<details><summary>{esc(label)} {I("plus")}</summary>' + ''.join(f'<a href="{pfx}{h}">{esc(t)}</a>' for t, h, s, ic in kids) + '</details>'
        for label, href, kids in NAV)
    stars = ''.join(f'<i style="left:{x}px;top:{y}px"></i>' for x, y in [(30, 6), (44, 12), (22, 14), (52, 5), (36, 18)])
    return f'''<header class="site-header">
<div class="wrap header-row">
<a class="brand" href="{pfx}./" aria-label="Adamu Yola Foundation home"><span class="mark-box">{mark_html()}</span><img class="wordmark on-light" src="{pfx}assets/brand/wordmark-name-blue.webp" alt="" width="161" height="30"><img class="wordmark on-dark" src="{pfx}assets/brand/wordmark-name-white.webp" alt="" width="161" height="30"></a>
<nav class="nav" aria-label="Main">{''.join(nav)}</nav>
<div class="header-tools">
<button class="horizon" role="switch" aria-checked="false" aria-label="Switch to night mode" title="Day or night"><span class="stars">{stars}</span><span class="sun"></span><span class="moon"></span><svg class="hills" viewBox="0 0 68 18" preserveAspectRatio="none" aria-hidden="true"><path class="h1" fill="#3D8F6E" d="M0 18V9c8-6 15-8 22-3s12 6 18 1 14-6 28 2v9z"/><path class="h2" fill="#60B596" d="M0 18v-4c10-5 20-6 30-1s20 3 38-2v7z"/></svg></button>
<a class="btn header-cta" href="{pfx}get-involved.html">Get involved</a>
<button class="menu-btn" aria-expanded="false" aria-controls="drawer" aria-label="Open menu"><span></span><span></span><span></span></button>
</div>
</div>
</header>
<div class="drawer" id="drawer">
<a class="solo" href="{pfx}./">Home</a>
{drawer}
<a class="solo" href="{pfx}contact.html">Contact</a>
<div class="drawer-foot"><a class="btn" href="{pfx}get-involved.html">Get involved {I("arrow")}</a><p>{EMAIL}<br>{PHONE}</p></div>
</div>
'''

def socials():
    return f'<div class="socials"><a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{I("fb")}</a><a href="{IGU}" target="_blank" rel="noopener" aria-label="Instagram">{I("ig")}</a><a href="{LI}" target="_blank" rel="noopener" aria-label="LinkedIn">{I("in")}</a></div>'

def footer(pfx):
    cols = ''.join(f'<div><h4>{esc(label)}</h4><ul>' + ''.join(f'<li><a href="{pfx}{h}">{esc(t)}</a></li>' for t, h, s, ic in kids) + '</ul></div>' for label, href, kids in NAV[:3])
    return f'''<footer class="site-footer">
<div class="wrap">
<div class="foot-grid">
<div class="foot-brand"><div class="foot-logo"><span class="foot-mark">{mark_html()}</span><img class="logo" src="{pfx}assets/brand/wordmark-name-white.webp" alt="Adamu Yola Foundation" width="180" height="33"></div><p class="foot-tag">Education, Entrepreneurship and Youth Development</p><p>Opening doors for young people and communities in Gombe through education, skills, health and grassroots sport.</p>{socials()}</div>
{cols}
<div><h4>Get in touch</h4><ul><li><a href="{pfx}get-involved.html">Get involved</a></li><li><a href="{pfx}contact.html">Contact us</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="tel:{TEL}">{PHONE}</a></li><li>Shongo Estate, Gombe</li></ul></div>
</div>
<div class="foot-bottom"><p style="margin:0;color:inherit">&copy; <span data-year>2026</span> Adamu Yola Foundation. All rights reserved.</p><nav aria-label="Legal"><a href="{pfx}privacy.html">Privacy Policy</a><a href="{pfx}terms.html">Terms of Use</a><a href="{pfx}contact.html">Contact</a></nav></div>
</div>
</footer>
<button class="to-top" aria-label="Back to top">{I("up")}</button>
</body>
</html>
'''

def page_hero(pfx, crumbs, title, lead, img=None, alt='', chips=None, extra='', badge=None):
    cr = f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{pfx}./">Home</a>' + ''.join(
        f'{I("crumb")}<a href="{pfx}{h}">{esc(t)}</a>' if h else f'{I("crumb")}<span aria-current="page">{esc(t)}</span>' for t, h in crumbs) + '</nav>'
    body = f'<div>{cr}<h1 class="reveal">{esc(title)}</h1><p class="lead reveal d1">{lead}</p>{extra}</div>'
    if img:
        inner = f'<div class="wrap ph-grid">{body}<div class="ph-media reveal d2"><figure class="ph-img" style="margin:0"><img src="{pfx}{img}" alt="{esc(alt)}" width="800" height="600"></figure>{badge.replace('__PFX__', pfx) if badge else ''}</div></div>'
        cls = 'page-hero has-img'
    else:
        inner = f'<div class="wrap">{body}</div><div class="bg-mark">{mark_html()}</div>'
        cls = 'page-hero'
    out = f'<section class="{cls}">{inner}</section>'
    if chips:
        out += '<nav class="onpage" aria-label="On this page"><div class="wrap">' + ''.join(f'<a href="#{i}">{esc(t)}</a>' for i, t in chips) + '</div></nav>'
    return out

def write(path, title, desc, active, body, og=None):
    pfx = '../' if '/' in path else './'
    pfx_fix = pfx
    doc = head(title, desc, path, pfx, og or 'assets/photos/unity-cup-award-handshake.webp') + header(pfx, active) + f'<main id="main">{body.replace("{P}", pfx_fix)}</main>' + footer(pfx)
    doc = doc.replace('href="./"', 'href="./"').replace('href=".././"', 'href="../"').replace('href="././"', 'href="./"')
    doc = doc.replace('__PFX__', pfx)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w').write(doc)

def btn(href, text, cls=''):
    return f'<a class="btn {cls}" href="{href}">{esc(text)} {I("arrow")}</a>'

def la(href, text, ext=False):
    t = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="link-arrow" href="{href}"{t}>{esc(text)} {I("external" if ext else "arrow")}</a>'

PH = 'assets/photos/'
# --------------------------------------------------------------------------- data
PROGRAMMES = [
    dict(slug='scholarships', name='Educational Scholarships', short='Educational Scholarships', icon='book', img='assets/education-photo.webp',
         alt='Secondary school students writing in a classroom',
         tag='Education', blurb='Helping students continue their education when financial barriers threaten their progress.',
         why='Educational opportunity should not depend on a family’s ability to meet every schooling expense. This programme provides financial assistance and scholarships for indigent learners at secondary and tertiary levels, so that talent and effort decide how far a student goes.',
         status=('Next scholarship intake', 'Award amounts, eligibility and application dates for the next intake will be announced on our news page and social channels. Families and schools can register interest with us now.'),
         steps=[('Schooling access', 'Support with eligible education costs for students experiencing financial hardship.'),
                ('Secondary and tertiary education', 'Help that recognises needs at both school and higher-education levels.'),
                ('Fair selection', 'Clear application, eligibility, verification and selection steps every time an intake opens.'),
                ('Learning progress', 'Ongoing support built on collaboration with families and learning institutions.')],
         facts=[('Who it serves', 'Indigent students in secondary and tertiary education'), ('Where', 'Gombe South and wider Gombe State'), ('Support type', 'Scholarships and education assistance')],
         topic='scholarships', pics=('education', 'Recent education projects', 'School materials for secondary school students and a new toilet project at GGSS Kaltungo.', [('education-materials-handover', 'School bags, books, writing materials and school consumables for secondary school students', 'Learning materials handed over to a school'), ('ggss-kaltungo-site-handover', 'Site allocated by the Gombe State Ministry of Education to build a modern toilet at GGSS Kaltungo', 'Site handover at GGSS Kaltungo'), ('education-materials-display', 'School bags, books, writing materials and school consumables for secondary school students', 'School materials ready for distribution')])),
    dict(slug='vocational-training', name='Vocational Training', short='Vocational Training', icon='tool', img='assets/skills-photo.webp',
         alt='Young women learning tailoring on sewing machines',
         tag='Skills', blurb='Practical learning that strengthens livelihoods, earning ability and self-reliance.',
         why='Vocational training closes the gap between ambition and usable skills. Through hands-on learning, participants build technical abilities for work, small enterprise and everyday economic independence, in line with the foundation’s focus on education, entrepreneurship and youth development.',
         status=('Upcoming cohorts', 'Trades, training centres and dates for the next cohort will be shared on our news page. Prospective trainees and partner workshops are welcome to get in touch.'),
         steps=[('Skills assessment', 'Identify community needs and the trades participants want to develop.'),
                ('Hands-on learning', 'Training built around practice, guided demonstration and finished work.'),
                ('Enterprise readiness', 'Basic customer service, costing, record-keeping and employability skills.'),
                ('Progress you can see', 'Completed sessions, participant work and follow-on opportunities, documented.')],
         facts=[('Who it serves', 'Young people and adults seeking practical skills'), ('Focus', 'Trades, enterprise and self-reliance'), ('Where', 'Communities across Gombe South')],
         topic='vocational-training', pics=('empowerment', 'Widows Support Programme', 'Food items and household support for widows, helping families stay on their feet.', [('widows-support-group', 'Widows Support Programme', 'Widows with their support packages'), ('widows-support-beneficiaries', 'Widows Support Programme', 'Beneficiaries with food items'), ('widows-support-items', 'Widows Support Programme', 'Support packages received')])),
    dict(slug='unity-cup', name='Gombe South Unity Cup', short='Gombe South Unity Cup', icon='ball', img=PH + 'unity-cup-champions-trophy.webp',
         alt='Champions holding the Adamu Yola Unity Cup trophy',
         tag='Grassroots sport', blurb='A grassroots tournament where football brings communities together and creates pathways for emerging players.',
         why='The Unity Cup began in 2016 and has grown into the foundation’s best-known initiative, played across Gombe South. Its model is simple: discover young talent through competition, develop players through camps and engagement, and promote them to a wider sporting audience, all while using football to promote peace between communities.',
         status=('10th edition in preparation', 'The organising committee will announce dates, club registration, venues and regulations for the next edition. Follow our news page and social channels for the call for clubs.'),
         steps=[('Discover', 'Community teams and grassroots players compete, giving emerging talent a stage.'),
                ('Develop', 'Past editions have included post-tournament camping, scouting and training.'),
                ('Promote', 'Outstanding players are connected with clubs and wider pathways.'),
                ('Unite', 'Respect, fair play, peaceful coexistence and drug-abuse prevention on and off the pitch.')],
         facts=[('First edition', '2016'), ('Editions played', 'Nine, with the 9th final in January 2026'), ('Club places', 'Up to 64 clubs in the 9th edition'), ('Motto', 'Promoting peace and developing talents')],
         topic='unity-cup', badge='<img class="ph-badge crest" src="__PFX__assets/unity-cup-badge-sm.webp" alt="Adamu Yola Gombe South Unity Cup 10th anniversary badge" width="170" height="170">'),
    dict(slug='medical-outreach', name='Medical Outreach', short='Medical Outreach', icon='heart', img='assets/medical-photo.webp',
         alt='A health worker checking the blood pressure of an older woman at an outreach',
         tag='Health', blurb='Community-centred efforts to bring basic healthcare services closer to people who need them.',
         why='For many households, even basic check-ups and preventive care are hard to reach. Medical outreach connects vulnerable communities with screening, health education and referrals, delivered with qualified partners.',
         status=('Next outreach', 'Locations and dates for upcoming outreach days will be announced through our news page. Health professionals and facilities interested in partnering can contact us.'),
         steps=[('Community needs', 'Work with local leaders and health workers to choose outreach locations.'),
                ('Basic checks', 'Screening and primary-level checks led by qualified professionals.'),
                ('Health information', 'Practical guidance on common preventable conditions and when to seek care.'),
                ('Referral and follow-up', 'Cases that need further care are referred through proper clinical channels.')],
         facts=[('Who it serves', 'Households with limited access to care'), ('Delivered with', 'Qualified health partners'), ('Where', 'Communities across Gombe South')],
         topic='medical-outreach'),
    dict(slug='principals-cup', name="Gombe State Principals' Cup", short="Principals' Cup", icon='trophy', img='assets/schools-football-photo.webp',
         alt='Secondary school students playing football on a school field',
         tag='School sport', blurb='An inter-school platform designed to connect boys’ public secondary schools across all 11 local government areas of Gombe State.',
         why='The Principals’ Cup brings the Unity Cup spirit into schools. It promotes healthy competition, teamwork, discipline and talent identification, moving from local government preliminaries through senatorial-zone stages to a state-level final.',
         status=('Planned initiative', 'Registration dates, eligibility rules and fixtures will be announced through official foundation channels. Schools and sponsors can register interest now.'),
         steps=[('School engagement', 'A clear participation structure for boys’ public secondary schools.'),
                ('Fair competition', 'School registration criteria, rules, officiating and player safeguarding.'),
                ('Talent development', 'Sporting excellence that never comes at the cost of schoolwork.'),
                ('Partnership', 'Transparent support for logistics, safe participation and recognition.')],
         facts=[('Who it serves', 'Boys’ public secondary schools'), ('Reach', 'All 11 local government areas of Gombe State'), ('Format', 'LGA rounds, senatorial zones, state final')],
         topic='principals-cup', badge='<img class="ph-badge crest" src="__PFX__assets/principals-cup-crest-sm.webp" alt="Gombe State Principals\u2019 Cup crest" width="170" height="170">'),
]

NEWS = [
    dict(cat='unity', year='2026', date='January 2026', title='9th Unity Cup: All Stars FC win the final', text='All Stars FC of Kaltungo overcame Oska FC in the January 2026 final, closing the ninth edition of the Gombe South Unity Cup.', url='https://markerbeyondborder.blogspot.com/2026/01/football-unites-gombe-south-as-all.html', src='Marker Beyond Border', img=PH + 'unity-cup-award-handshake-sm.webp'),
    dict(cat='education', year='', date='Education project', title='Site allocated by the Gombe State Ministry of Education to build a modern toilet at GGSS Kaltungo', text='The Gombe State Ministry of Education handed over a site at Government Girls Secondary School Kaltungo for the foundation to build a modern toilet for students.', url='gallery.html#education', src='See the photos', img=PH + 'ggss-kaltungo-site-handover-sm.webp', internal=True),
    dict(cat='education', year='', date='Education project', title='School bags, books, writing materials and school consumables for secondary school students', text='School bags, books, writing materials and other school consumables were presented to secondary schools for their students.', url='gallery.html#education', src='See the photos', img=PH + 'education-materials-handover-sm.webp', internal=True),
    dict(cat='empowerment', year='', date='Empowerment project', title='Widows Support Programme', text='Widows in our communities received food items and household support through the foundation’s Widows Support Programme.', url='gallery.html#empowerment', src='See the photos', img=PH + 'widows-support-group-sm.webp', internal=True),
    dict(cat='sport', year='', date='Sport project', title='Support to Gombe State Basketball City League', text='The foundation supported the Gombe Basketball City League with jerseys, awards and certificates for players, teams and officials.', url='gallery.html#basketball', src='See the photos', img=PH + 'basketball-league-champions-jersey-sm.webp', internal=True),
    dict(cat='unity', year='2025', date='June 2025', title='Unity Cup draw and awards season', text='The foundation marked June with highlights from the Unity Cup draw and the recognition of standout players and officials.', url=IGU, src='Instagram @adamuyolafdn', img=PH + 'unity-cup-draw-highlights-sm.webp'),
    dict(cat='unity', year='2025', date='2025', title='9th Unity Cup: registration opens for up to 64 clubs', text='The organising committee set a registration deadline and a maximum of 64 clubs for the ninth edition.', url='https://independent.ng/adamu-yola-unity-cup-2025-organisers-set-deadline-for-registering-football-clubs/', src='Independent Newspaper', img=PH + 'unity-cup-award-volunteer-sm.webp'),
    dict(cat='unity', year='2023', date='29 December 2023', title='Bare City FC and Dinge Flying Bees FC contest the final', text='The final was played at Billiri Township Stadium, with FC Leon and All Stars FC Kaltungo meeting earlier the same day for third place.', url=IGU, src='Instagram @adamuyolafdn', img=PH + 'unity-cup-final-2023-sm.webp'),
    dict(cat='unity', year='2023', date='27 December 2023', title='Zakari Akawu saves two penalties in the semi-final', text='Bare City FC goalkeeper Zakari Akawu was named Player of the Match as his saves sent his side to their second final in four years. He also won the Save Hand award of the 5th edition.', url=IGU, src='Instagram @adamuyolafdn', img=PH + 'unity-cup-goalkeeper-zakari-sm.webp'),
    dict(cat='unity', year='2023', date='2023', title='8th Unity Cup: Amana FM named broadcast partner', text='The local organising committee announced Amana FM as official radio partner, bringing match coverage to listeners across the region.', url='https://aytfoundation.org/local-organising-committee-of-the-8th-adamu-yola-gombe-south-unity-cup-announces-amana-fm-as-official-broadcast-partner/', src='Adamu Yola Foundation', img=PH + 'unity-cup-award-presentation-sm.webp'),
    dict(cat='unity', year='2022', date='2022', title='7th Unity Cup: Kaltungo Boys are champions', text='Kaltungo Boys defeated Komta United to win the 2022 edition.', url='https://jewelsport.blogspot.com/', src='Jewel Sport', img=PH + 'unity-cup-match-day-sm.webp'),
    dict(cat='players', year='2022', date='2022', title='18 Unity Cup stars invited to a closed camp in Abuja', text='Eighteen players shortlisted from the sixth tournament earned invitations to a closed camp, a step from community football towards wider opportunity.', url='https://www.sports247.ng/18-stars-of-adamu-yola-cup-earn-invitation-for-closed-camping-in-abuja/', src='Sports247', img=PH + 'unity-cup-award-player-sm.webp'),
    dict(cat='players', year='2021', date='2021', title='North-East Elite Basketball Camp', text='A development camp for young athletes from across the North-East, held in collaboration with the Jordan Nwora Foundation.', url='https://www.sports247.ng/100-talents-sweat-it-out-at-the-north-east-basketball-elite-camp/', src='Sports247', img=None),
    dict(cat='unity', year='2020', date='December 2020', title='5th Unity Cup: SportVote partnership', text='A partnership with SportVote set out to raise the visibility of grassroots players beyond Gombe South.', url='https://futbaloven.wordpress.com/2020/12/10/adamu-yola-cup-loc-seals-sport-vote-partnership/', src='Futbaloven', img=PH + 'unity-cup-award-coach-sm.webp'),
    dict(cat='community', year='', date='Community initiative', title='Ture Ward: 200 bags of fertiliser for farmers', text='An agricultural empowerment initiative distributed 200 bags of fertiliser to farmers in Ture Ward, Kaltungo West.', url='https://aytfoundation.org/fertilizer-distribution/', src='Adamu Yola Foundation', img=None),
]

GALLERY = [
    ('education', PH + 'education-materials-handover', 'School bags, books, writing materials and school consumables for secondary school students', 'Presentation to secondary schools', 'Adamu Yola Foundation archive', 1080, 810),
    ('education', PH + 'ggss-kaltungo-site-handover', 'Site allocated by the Gombe State Ministry of Education to build a modern toilet at GGSS Kaltungo', 'Site handover at GGSS Kaltungo', 'Adamu Yola Foundation archive', 780, 1040),
    ('basketball', PH + 'basketball-league-champions-jersey', 'Support to Gombe State Basketball City League', 'Champions jersey presentation', 'Adamu Yola Foundation archive', 1080, 720),
    ('empowerment', PH + 'widows-support-group', 'Widows Support Programme', 'Beneficiaries with their food packages', 'Adamu Yola Foundation archive', 1040, 780),
    ('education', PH + 'education-materials-display', 'School bags, books, writing materials and school consumables for secondary school students', 'Items ready for distribution', 'Adamu Yola Foundation archive', 1080, 810),
    ('education', PH + 'ggss-kaltungo-site-address', 'Site allocated by the Gombe State Ministry of Education to build a modern toilet at GGSS Kaltungo', 'Remarks at the site', 'Adamu Yola Foundation archive', 780, 1040),
    ('empowerment', PH + 'widows-support-beneficiaries', 'Widows Support Programme', 'Food items for widows', 'Adamu Yola Foundation archive', 567, 1008),
    ('education', PH + 'education-materials-speech', 'School bags, books, writing materials and school consumables for secondary school students', 'Address at the presentation', 'Adamu Yola Foundation archive', 810, 1080),
    ('education', PH + 'education-materials-rows', 'School bags, books, writing materials and school consumables for secondary school students', 'Items laid out for schools', 'Adamu Yola Foundation archive', 1080, 810),
    ('empowerment', PH + 'widows-support-items', 'Widows Support Programme', 'Support packages received', 'Adamu Yola Foundation archive', 1008, 567),
    ('education', PH + 'education-materials-address', 'School bags, books, writing materials and school consumables for secondary school students', 'Remarks to guests', 'Adamu Yola Foundation archive', 810, 1080),
    ('education', PH + 'education-materials-venue', 'School bags, books, writing materials and school consumables for secondary school students', 'At the venue', 'Adamu Yola Foundation archive', 1032, 581),
    ('empowerment', PH + 'widows-support-packages', 'Widows Support Programme', 'Rice, oil and food items', 'Adamu Yola Foundation archive', 1040, 780),
    ('basketball', PH + 'basketball-league-certificate', 'Support to Gombe State Basketball City League', 'Certificate for an official', 'Adamu Yola Foundation archive', 1080, 720),
    ('basketball', PH + 'basketball-league-player-award', 'Support to Gombe State Basketball City League', 'A player receives his award', 'Adamu Yola Foundation archive', 1080, 720),
    ('basketball', PH + 'basketball-league-presentation', 'Support to Gombe State Basketball City League', 'Presentation to a participant', 'Adamu Yola Foundation archive', 1080, 720),
    ('basketball', PH + 'basketball-league-courtside', 'Support to Gombe State Basketball City League', 'Courtside at the league', 'Adamu Yola Foundation archive', 1080, 720),
    ('education', PH + 'education-materials-closeup', 'School bags, books, writing materials and school consumables for secondary school students', 'Materials for students', 'Adamu Yola Foundation archive', 1080, 810),
    ('award', PH + 'unity-cup-award-handshake', 'Recognising service to the Unity Cup', 'Unity Cup awards ceremony', 'Facebook', 1600, 1068),
    ('award', PH + 'unity-cup-champions-trophy', 'Champions with the Unity Cup trophy', 'Unity Cup final', 'Facebook', 851, 575),
    ('award', PH + 'unity-cup-award-elder', 'A community elder honoured at the Unity Cup', 'Unity Cup awards ceremony', 'Facebook', 1600, 1068),
    ('match', PH + 'unity-cup-goalkeeper-zakari', 'Zakari Akawu, Player of the Match', 'Semi-final, December 2023', 'Instagram', 600, 298),
    ('award', PH + 'unity-cup-award-medal', 'A medal for a Unity Cup official', 'Unity Cup awards ceremony', 'Facebook', 1600, 1068),
    ('award', PH + 'unity-cup-award-presentation', 'Plaque presentation at the Unity Cup', 'Unity Cup awards', 'Instagram', 640, 427),
    ('match', PH + 'unity-cup-draw-highlights', 'Draw day and player awards', 'June 2025', 'Instagram', 640, 519),
    ('award', PH + 'unity-cup-award-volunteer', 'Thanking the volunteers who make it happen', 'Unity Cup awards ceremony', 'Facebook', 1600, 1068),
    ('fixtures', PH + 'unity-cup-final-2023', 'Final: Bare City FC v Dinge Flying Bees FC', 'Billiri Township Stadium, 29 December 2023', 'Instagram', 600, 600),
    ('fixtures', PH + 'unity-cup-semifinal-2023', 'Semi-final: FC Leon v Bare City', 'Billiri Township Stadium, 27 December 2023', 'Instagram', 600, 600),
]
VIDEOS = [
    (PH + 'unity-cup-match-day', 'Match day in Gombe South', 'Video, July 2024', 'https://www.instagram.com/adamuyolafdn/reel/C-HTllUNWKT/'),
    (PH + 'unity-cup-award-coach', 'Awards for the men behind the clubs', 'Video, January 2024', 'https://www.instagram.com/adamuyolafdn/reel/C1mtpoUs_KM/'),
    (PH + 'unity-cup-award-supporters', 'Families celebrate a Unity Cup award', 'Video, December 2023', 'https://www.instagram.com/adamuyolafdn/reel/C1h9AejsUVU/'),
    (PH + 'unity-cup-award-player', 'Player recognition at the final', 'Video, December 2023', 'https://www.instagram.com/adamuyolafdn/reel/C1h7wu9McRB/'),
]

def next_cards(pfx, items):
    return '<div class="next-grid">' + ''.join(f'<a class="next reveal d{i%4}" href="{pfx}{h}"><img src="{pfx}{img}" alt="" loading="lazy" width="84" height="84"><span><small>{esc(k)}</small><strong>{esc(t)}</strong></span></a>' for i, (k, t, h, img) in enumerate(items)) + '</div>'

# --------------------------------------------------------------------------- HOME
def home():
    P = './'
    tiles = []
    order = ['unity-cup', 'scholarships', 'vocational-training', 'medical-outreach', 'principals-cup']
    for i, slug in enumerate(order):
        p = next(x for x in PROGRAMMES if x['slug'] == slug)
        cls = 'tile big' if i == 0 else ('tile half' if i >= 3 else 'tile')
        tiles.append(f'<a class="{cls} reveal d{i%4}" href="{P}programs/{slug}.html"><img src="{P}{p["img"]}" alt="{esc(p["alt"])}" loading="lazy">{('<img class="tile-badge" src="'+P+{'principals-cup':'assets/principals-cup-crest-sm.webp','unity-cup':'assets/unity-cup-badge-sm.webp'}[slug]+'" alt="" loading="lazy">') if slug in ('principals-cup','unity-cup') else ''}<span class="tag">{esc(p["tag"])}</span><span class="go">{I("arrow")}</span><div class="tile-body"><h3>{esc(p["name"])}</h3><p>{esc(p["blurb"])}</p></div></a>')
    marquee_imgs = ['unity-cup-award-handshake', 'unity-cup-champions-trophy', 'unity-cup-goalkeeper-zakari', 'unity-cup-award-elder', 'unity-cup-award-presentation', 'unity-cup-draw-highlights', 'unity-cup-award-medal', 'unity-cup-award-volunteer', 'unity-cup-award-supporters']
    mq = ''.join(f'<figure><img src="{P}{PH}{m}-sm.webp" alt="" loading="lazy"></figure>' for m in marquee_imgs)
    tl = [('2016', 'The Unity Cup kicks off', 'Community football across Gombe South begins its journey.'),
          ('2018', 'The foundation is established', 'Headquartered in Gombe with a focus on education, entrepreneurship and youth development.'),
          ('2020', 'SportVote partnership', 'The 5th edition expands visibility for grassroots players.'),
          ('2021', 'North-East Elite Basketball Camp', 'Young athletes train with the Jordan Nwora Foundation.'),
          ('2022', '18 players to an Abuja camp', 'Unity Cup talent moves a step closer to the next level.'),
          ('2023', 'Live on Amana FM', 'The 8th edition reaches listeners across the region.'),
          ('2026', 'All Stars FC crowned', 'The 9th edition final is won in January.')]
    tlh = ''.join(f'<li class="reveal d{i%4}"><span class="yr">{y}</span><h3>{esc(t)}</h3><p>{esc(s)}</p></li>' for i, (y, t, s) in enumerate(tl))
    body = f'''
<section class="hero">
<div class="wrap hero-grid">
<div class="hero-copy">
<p class="kicker rise">Rooted in Gombe. Committed to communities.</p>
<h1 class="rise"><span class="line">Opportunity</span><span class="line">begins with people.</span></h1>
<p class="lead rise">Creating pathways through education, skills, community healthcare and grassroots sport, and recognising the people who make progress possible.</p>
<div class="btn-row rise">{btn(P+'programs/', 'Explore our programmes')}{btn(P+'about.html', 'Our story', 'btn-ghost')}</div>
<div class="hero-badges rise"><span class="chip"><i></i>10th Unity Cup in preparation</span><span class="chip">Charity begins at home</span></div>
</div>
<div class="stage" aria-hidden="false">
<div class="ring"></div>
<figure class="disc d1"><a href="{P}programs/scholarships.html#pictures"><img src="{P}{PH}education-materials-handover-sm.webp" alt="Learning materials handed over to secondary schools"><figcaption>Education</figcaption></a></figure>
<figure class="disc d2"><a href="{P}programs/vocational-training.html#pictures"><img src="{P}{PH}widows-support-group-sm.webp" alt="Women receiving support through the Widows Support Programme"><figcaption>Entrepreneurship</figcaption></a></figure>
<figure class="disc d3"><a href="{P}programs/unity-cup.html"><img src="{P}{PH}unity-cup-award-supporters-sm.webp" alt="Families celebrating with a young player"><figcaption>Youth development</figcaption></a></figure>
<div class="core"><div class="glow"></div><span class="mark-shadow"></span>{mark_html()}</div>
<p class="orbit-label">Education, Entrepreneurship <b>and</b> Youth Development</p>
</div>
</div>
</section>

<section class="section-tight">
<div class="wrap facts reveal">
<div class="fact"><b data-count="2016">2016</b><span>Unity Cup first kick-off</span></div>
<div class="fact"><b data-count="2018">2018</b><span>Foundation established in Gombe</span></div>
<div class="fact"><b data-count="9">9</b><span>Unity Cup editions played</span></div>
<div class="fact"><b data-count="64">64</b><span>Club places in the 9th edition</span></div>
<div class="fact"><b data-count="11">11</b><span>LGAs in the Principals' Cup plan</span></div>
</div>
</section>

<section class="section">
<div class="wrap">
<div class="section-head reveal"><div><p class="kicker">What we do</p><h2>Five programmes. One shared purpose.</h2><p>From keeping learners in school to discovering football talent, each programme opens a door for someone in our communities.</p></div>{la(P+'programs/', 'All programmes')}</div>
<div class="bento">{''.join(tiles)}</div>
</div>
</section>

<section class="section band-navy unity">
<div class="wrap unity-grid">
<div class="reveal">
<img class="emblem" src="{P}assets/unity-cup-badge-sm.webp" alt="Adamu Yola Gombe South Unity Cup 10th anniversary badge" width="150" height="150" loading="lazy">
<h2>The Gombe South Unity Cup</h2>
<p class="lead">Since 2016 the Unity Cup has brought communities together around competition, respect, player development and talent discovery. Past editions have included post-tournament camping and peace campaigns across Gombe South.</p>
<ul class="pillars">
<li><strong>Discover</strong><span>Grassroots players get a stage.</span></li>
<li><strong>Develop</strong><span>Camps, scouting and training.</span></li>
<li><strong>Promote</strong><span>Pathways to clubs and beyond.</span></li>
<li><strong>Unite</strong><span>Peace and fair play first.</span></li>
</ul>
<div class="btn-row">{btn(P+'programs/unity-cup.html', 'Explore the Unity Cup', 'btn-light')}</div>
</div>
<div class="collage reveal d2">
<figure class="c1"><img src="{P}{PH}unity-cup-award-handshake.webp" alt="An official congratulates a community leader at the Unity Cup" loading="lazy"><figcaption>Awards ceremony</figcaption></figure>
<figure class="c2"><img src="{P}{PH}unity-cup-champions-trophy-sm.webp" alt="Champions lift the trophy" loading="lazy"></figure>
<figure class="c3"><img src="{P}{PH}unity-cup-goalkeeper-zakari-sm.webp" alt="Goalkeeper Zakari Akawu with his award" loading="lazy"></figure>
<figure class="c4"><img src="{P}{PH}unity-cup-award-presentation-sm.webp" alt="A plaque presentation" loading="lazy"></figure>
<figure class="c5"><img src="{P}{PH}unity-cup-award-supporters-sm.webp" alt="Supporters celebrate" loading="lazy"></figure>
<figure class="c6"><img src="{P}{PH}unity-cup-match-day-sm.webp" alt="Players walk out on match day" loading="lazy"></figure>
</div>
</div>
</section>

<section class="section">
<div class="wrap">
<div class="section-head reveal"><div><p class="kicker">Our journey</p><h2>A decade of community activity.</h2><p>Documented milestones from the pitch, the classroom and the farm.</p></div>{la(P+'about.html#leadership', 'Full history')}</div>
<ol class="timeline">{tlh}</ol>
</div>
</section>

<section class="section surface">
<div class="wrap section-head reveal"><div><p class="kicker">Moments</p><h2>See the work in pictures.</h2></div>{la(P+'gallery.html', 'Open the gallery')}</div>
<div class="marquee reveal"><div class="marquee-track">{mq}{mq.replace('alt=""', 'alt="" aria-hidden="true"')}</div></div>
</section>

<section class="section">
<div class="wrap">
<div class="section-head reveal"><div><p class="kicker">Get involved</p><h2>Work with the foundation.</h2><p>Partnership, volunteering and support all begin with a conversation.</p></div></div>
<div class="paths">
<a class="path reveal" href="{P}get-involved.html#partner"><span class="ico">{I("hand")}</span><h3>Partner or sponsor</h3><p>Back a programme, sponsor the Unity Cup or bring resources your organisation already has.</p><span class="link-arrow">Become a partner {I("arrow")}</span></a>
<a class="path reveal d1" href="{P}get-involved.html#volunteer"><span class="ico">{I("users")}</span><h3>Volunteer</h3><p>Coaches, health workers, teachers and organisers: your time and skills change outcomes.</p><span class="link-arrow">Volunteer with us {I("arrow")}</span></a>
<a class="path reveal d2" href="{P}get-involved.html#support"><span class="ico">{I("gift")}</span><h3>Support our work</h3><p>Help fund scholarships, training kits, outreach supplies and tournament costs.</p><span class="link-arrow">Ways to give {I("arrow")}</span></a>
</div>
</div>
</section>
'''
    write('index.html', 'Home', 'The Adamu Yola Foundation creates opportunity in Gombe State through scholarships, vocational training, medical outreach and the Gombe South Unity Cup.', 'Home', body)

# --------------------------------------------------------------------------- ABOUT
def about():
    P = './'
    hist = [
        ('2016', 'The Unity Cup begins', 'Community football in Gombe South takes shape as a tournament for peace and talent.', None),
        ('2018', 'The foundation is established', 'The Adamu Yola Foundation is founded and headquartered in Gombe, earlier known publicly as the Adamu Yola Ture Foundation.', None),
        ('2020', '5th Unity Cup: sports development partnership', 'A SportVote partnership set out to expand the visibility of grassroots players.', 'https://futbaloven.wordpress.com/2020/12/10/adamu-yola-cup-loc-seals-sport-vote-partnership/'),
        ('2021', 'North-East Elite Basketball Camp', 'A development camp for young athletes across the North-East, in collaboration with the Jordan Nwora Foundation.', 'https://www.sports247.ng/100-talents-sweat-it-out-at-the-north-east-basketball-elite-camp/'),
        ('2022', 'Post-tournament player pathways', 'Eighteen shortlisted players from the sixth tournament were invited to a closed camp in Abuja.', 'https://www.sports247.ng/18-stars-of-adamu-yola-cup-earn-invitation-for-closed-camping-in-abuja/'),
        ('2022', '7th Unity Cup: Kaltungo Boys are champions', 'Kaltungo Boys defeated Komta United in the 2022 edition.', 'https://jewelsport.blogspot.com/'),
        ('2023', '8th Unity Cup: Amana FM broadcast partnership', 'Radio coverage brought the tournament to listeners across the region.', 'https://aytfoundation.org/local-organising-committee-of-the-8th-adamu-yola-gombe-south-unity-cup-announces-amana-fm-as-official-broadcast-partner/'),
        ('2025', '9th Unity Cup: preparations and registration', 'The organising committee opened registration for a maximum of 64 clubs.', 'https://independent.ng/adamu-yola-unity-cup-2025-organisers-set-deadline-for-registering-football-clubs/'),
        ('2026', '9th Unity Cup: All Stars FC win the final', 'All Stars FC of Kaltungo overcame Oska FC in the January 2026 final.', 'https://markerbeyondborder.blogspot.com/2026/01/football-unites-gombe-south-as-all.html'),
    ]
    hl = ''.join(f'<li class="reveal"><span class="yr">{y}</span><h3>{esc(t)}</h3><p>{esc(s)}</p>{la(u, "Read the report", True) if u else ""}</li>' for y, t, s, u in hist)
    body = page_hero(P, [('About Us', None)], 'A foundation built around people.',
                     'Founded in Gombe State, the Adamu Yola Foundation makes more opportunities available to young people and communities through education, skills, health and sport.',
                     img=PH + 'unity-cup-award-elder.webp', alt='A community elder honoured at a Unity Cup ceremony',
                     chips=[('story', 'Our Story'), ('mission', 'Mission, Vision & Values'), ('leadership', 'Leadership & History')]) + f'''
<section class="section" id="story">
<div class="wrap split">
<div class="prose reveal">
<p class="kicker">Our Story</p>
<h2>Local roots. Practical possibility.</h2>
<p>The foundation began with a simple conviction: young people from Gombe South deserve the same opportunities enjoyed by young people anywhere else. That idea connects everything we do, from educational assistance and vocational learning to grassroots sport and community health.</p>
<p>Our sporting story started first. The Gombe South Unity Cup kicked off in 2016, and its success in bringing communities together laid the ground for the foundation, established in 2018 and headquartered in Gombe. In earlier reporting and on our previous website, the organisation appears as the Adamu Yola Ture Foundation.</p>
<p>Today the foundation works under the banner of education, entrepreneurship and youth development, guided by a motto our supporters know well: charity begins at home.</p>
<div class="btn-row">{btn(P+'programs/', 'See our programmes')}{btn(P+'gallery.html', 'View the gallery', 'btn-ghost')}</div>
</div>
<aside class="facts-card reveal d2">
<h3>The foundation at a glance</h3>
<dl>
<div><dt>Headquarters</dt><dd>Gombe, Gombe State, Nigeria</dd></div>
<div><dt>Founded</dt><dd>2018</dd></div>
<div><dt>Communities</dt><dd>Gombe South and the wider Gombe State</dd></div>
<div><dt>Focus</dt><dd>Youth opportunity, education, empowerment and unity</dd></div>
<div><dt>Motto</dt><dd>Charity begins at home</dd></div>
<div><dt>Registration</dt><dd>Incorporated Trustees, IT/NO 117968</dd></div>
</dl>
</aside>
</div>
</section>

<section class="section surface" id="mission">
<div class="wrap">
<div class="section-head reveal"><div><p class="kicker">Mission, Vision &amp; Values</p><h2>What we work towards.</h2></div></div>
<div class="split even" style="margin-bottom:28px">
<div class="statement reveal"><h3>Our mission</h3><p>To open pathways to opportunity for young people and communities in Gombe through education, practical skills, community health and grassroots sport.</p></div>
<div class="statement reveal d1"><h3>Our vision</h3><p>A Gombe South where every young person has the same chance to learn, earn, stay healthy and shine as young people anywhere.</p></div>
</div>
<div class="values">
<div class="value reveal"><h3>Respect</h3><p>For the people we serve, for opponents on the pitch and for every community we work in.</p></div>
<div class="value reveal d1"><h3>Opportunity</h3><p>We look for talent and potential, then remove the barriers in front of them.</p></div>
<div class="value reveal d2"><h3>Accountability</h3><p>We document our work with dates, places, partners and real outcomes.</p></div>
<div class="value reveal d3"><h3>Unity</h3><p>Peaceful coexistence and fair play guide everything, from tournaments to outreach.</p></div>
</div>
</div>
</section>

<section class="section" id="leadership">
<div class="wrap split">
<div class="reveal sticky">
<p class="kicker">Leadership &amp; History</p>
<h2>How the foundation is run.</h2>
<p>The foundation is registered as Incorporated Trustees and governed by its Board of Trustees, who set direction and safeguard how resources are used.</p>
<div class="cards" style="margin-top:24px">
<div class="card"><span class="ico">{I("shield")}</span><h3>Board of Trustees</h3><p>Provides oversight, approves programmes and protects the foundation’s integrity.</p></div>
<div class="card"><span class="ico">{I("ball")}</span><h3>Unity Cup Organising Committee</h3><p>Plans each edition: club registration, fixtures, venues, officiating and media.</p></div>
<div class="card"><span class="ico">{I("users")}</span><h3>Volunteers and partners</h3><p>Coaches, officials, media partners such as Amana FM and allies such as the Jordan Nwora Foundation.</p></div>
</div>
</div>
<div class="reveal d2">
<h3 style="margin-bottom:22px">A documented timeline</h3>
<ol class="vlist">{hl}</ol>
</div>
</div>
</section>

<section class="section-tight">
<div class="wrap">
<div class="cta-band reveal"><div><h2>Beyond the five programmes.</h2><p>Basketball development, farming support, learning environments and help for widows are part of our story too.</p></div><div>{btn(P+'programs/past-initiatives.html', 'Past initiatives', 'btn-light')}</div></div>
</div>
</section>
'''
    write('about.html', 'About Us', 'The story, mission, values, leadership and history of the Adamu Yola Foundation in Gombe State, Nigeria.', 'About Us', body, PH + 'unity-cup-award-elder.webp')

# --------------------------------------------------------------------------- PROGRAMMES
def programmes_index():
    P = '../'
    rows = ''.join(f'''<article class="prog-row reveal">
<figure class="photo"><img src="{P}{p["img"]}" alt="{esc(p["alt"])}" loading="lazy">{p.get("badge","").replace("__PFX__",P).replace("ph-badge","photo-badge")}</figure>
<div><p class="kicker">{esc(p["tag"])}</p><h2 style="font-size:clamp(1.6rem,3vw,2.4rem)">{esc(p["name"])}</h2><p>{esc(p["why"])}</p>{la(P+"programs/"+p["slug"]+".html", "Read about "+p["short"])}</div>
</article>''' for p in PROGRAMMES)
    body = page_hero(P, [('Programmes & Projects', None)], 'Our work, explained.',
                     'Five programme areas reflect the foundation’s focus on opportunity, learning, health, community participation and grassroots talent.',
                     chips=[(p['slug'], p['short']) for p in PROGRAMMES] + [('past', 'Past initiatives')]) + f'''
<section class="section"><div class="wrap">{rows.replace('<article class="prog-row reveal">', '<article class="prog-row reveal" id="__ID__">')}</div></section>
<section class="section-tight" id="past"><div class="wrap"><div class="cta-band reveal"><div><h2>Initiatives beyond the five.</h2><p>Basketball development, agricultural empowerment, peace advocacy and widows’ assistance are part of our record.</p></div><div>{btn(P+'programs/past-initiatives.html', 'Past initiatives & collaborations', 'btn-light')}</div></div></div></section>
'''
    for p in PROGRAMMES:
        body = body.replace('id="__ID__"', f'id="{p["slug"]}"', 1)
    write('programs/index.html', 'Programmes & Projects', 'Scholarships, vocational training, medical outreach, the Gombe South Unity Cup and the Gombe State Principals’ Cup.', 'Programmes & Projects', body)

def programme(p):
    P = '../'
    steps = ''.join(f'<div class="card reveal d{i%4}"><span class="num">Step {i+1}</span><h3>{esc(t)}</h3><p>{esc(s)}</p></div>' for i, (t, s) in enumerate(p['steps']))
    facts = ''.join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in p['facts'])
    idx = PROGRAMMES.index(p)
    others = [PROGRAMMES[(idx + 1) % 5], PROGRAMMES[(idx + 2) % 5]]
    nxt = [('Next programme', o['name'], f'programs/{o["slug"]}.html', o['img']) for o in others] + [('Archive', 'Past initiatives & collaborations', 'programs/past-initiatives.html', 'assets/community-football-photo.webp')]
    extra = ''
    if p['slug'] == 'unity-cup':
        gal = ''.join(f'<figure class="photo reveal d{i%4}" style="aspect-ratio:4/3"><img src="{P}{PH}{f}-sm.webp" alt="{esc(a)}" loading="lazy"></figure>' for i, (f, a) in enumerate([
            ('unity-cup-award-handshake', 'Officials congratulate a community leader'), ('unity-cup-goalkeeper-zakari', 'Goalkeeper Zakari Akawu with his Player of the Match award'),
            ('unity-cup-award-supporters', 'Family members celebrate a player’s award'), ('unity-cup-award-medal', 'A medal presented to a Unity Cup official')]))
        ed = [('2026', '9th edition final', 'All Stars FC of Kaltungo beat Oska FC.', 'https://markerbeyondborder.blogspot.com/2026/01/football-unites-gombe-south-as-all.html'),
              ('2025', '9th edition registration', 'Up to 64 clubs invited to register.', 'https://independent.ng/adamu-yola-unity-cup-2025-organisers-set-deadline-for-registering-football-clubs/'),
              ('Dec 2023', 'Final at Billiri Township Stadium', 'Bare City FC v Dinge Flying Bees FC. Third place: FC Leon v All Stars FC Kaltungo.', IGU),
              ('2023', '8th edition on air', 'Amana FM named official broadcast partner.', 'https://aytfoundation.org/local-organising-committee-of-the-8th-adamu-yola-gombe-south-unity-cup-announces-amana-fm-as-official-broadcast-partner/'),
              ('2022', '7th edition champions', 'Kaltungo Boys defeated Komta United.', 'https://jewelsport.blogspot.com/'),
              ('2022', 'Abuja camp', '18 players from the 6th edition invited to a closed camp.', 'https://www.sports247.ng/18-stars-of-adamu-yola-cup-earn-invitation-for-closed-camping-in-abuja/'),
              ('2020', '5th edition partnership', 'SportVote partnership for player visibility.', 'https://futbaloven.wordpress.com/2020/12/10/adamu-yola-cup-loc-seals-sport-vote-partnership/')]
        edh = ''.join(f'<li class="reveal"><span class="yr">{y}</span><h3>{esc(t)}</h3><p>{esc(s)}</p>{la(u, "Source", True)}</li>' for y, t, s, u in ed)
        extra = f'''
<section class="section surface" id="editions">
<div class="wrap split">
<div class="reveal"><p class="kicker">Past editions</p><h2>Champions and milestones.</h2><p>Results and moments recorded in public reporting and on the foundation’s own channels.</p><ol class="vlist" style="margin-top:28px">{edh}</ol></div>
<div class="sticky"><div class="cards" style="grid-template-columns:1fr 1fr">{gal}</div><div class="btn-row">{btn(P+'gallery.html', 'Full photo and video gallery')}</div></div>
</div>
</section>'''
    pics = ''
    if p.get('pics'):
        cat, heading, intro, items = p['pics']
        figs = ''.join(f'<a class="pic reveal d{i%4}" href="{P}gallery.html#{cat}"><img src="{P}{PH}{f}-sm.webp" alt="{esc(a)}" loading="lazy"><span class="pic-cap">{esc(t)}</span></a>' for i, (f, t, a) in enumerate(items))
        pics = f'''
<section class="section surface" id="pictures">
<div class="wrap">
<div class="section-head reveal"><div><p class="kicker">In pictures</p><h2>{esc(heading)}</h2><p>{esc(intro)}</p></div><div class="btn-row" style="margin:0">{btn(P+"gallery.html#"+cat, "See all photos")}{btn(P+"news.html#"+cat, "Read the news", "btn-ghost")}</div></div>
<div class="pics">{figs}</div>
</div>
</section>'''
    chips = [('why', 'Why it matters')] + ([('pictures', 'In pictures')] if pics else []) + [('how', 'How it works')] + ([('editions', 'Past editions')] if extra else []) + [('ask', 'Ask us')]
    body = page_hero(P, [('Programmes & Projects', 'programs/'), (p['name'], None)], p['name'], esc(p['blurb']),
                     img=p['img'].replace('-sm.webp', '.webp'), alt=p['alt'], chips=chips, badge=p.get('badge'),
                     extra=f'<div class="btn-row">{btn(P+"contact.html?topic="+p["topic"], "Ask about this programme", "btn-light")}</div>') + f'''
<section class="section" id="why">
<div class="wrap split">
<div class="prose reveal"><p class="kicker">Why it matters</p><h2>The need behind the work.</h2><p>{esc(p["why"])}</p>
<div class="status" style="margin-top:28px"><span class="dot"></span><div><h3>{esc(p["status"][0])}</h3><p>{esc(p["status"][1])}</p>{la(P+"contact.html?topic="+p["topic"], "Register interest")}</div></div>
</div>
<aside class="facts-card reveal d2"><h3>At a glance</h3><dl>{facts}</dl></aside>
</div>
</section>{pics}
<section class="section{' ' if (extra or pics) else ' surface'}" id="how">
<div class="wrap"><div class="section-head reveal"><div><p class="kicker">How it works</p><h2>How the work takes shape.</h2></div></div><div class="cards">{steps}</div></div>
</section>
{extra}
<section class="section" id="ask">
<div class="wrap">
<div class="cta-band reveal" style="margin-bottom:48px"><div><h2>Questions about {esc(p["short"])}?</h2><p>For dates, availability and how to take part, speak with our team directly.</p></div><div>{btn(P+"contact.html?topic="+p["topic"], "Contact us", "btn-light")}</div></div>
<h3 class="reveal">Keep exploring</h3>
{next_cards(P, nxt)}
</div>
</section>'''
    write(f'programs/{p["slug"]}.html', p['name'], p['blurb'], 'Programmes & Projects', body, p['img'].replace('-sm', ''))

def past():
    P = '../'
    items = [
        ('city-league', 'Support to Gombe State Basketball City League', 'Sport', 'The foundation supported the Gombe Basketball City League, presenting jerseys, awards and certificates to players, teams and officials.', 'GALLERY:basketball', 'Photos in our gallery', 'trophy'),
        ('basketball', 'North-East Elite Basketball Camp', '2021', 'A development camp that gathered young basketball talent from across the North-East, delivered in collaboration with the Jordan Nwora Foundation.', 'https://www.sports247.ng/100-talents-sweat-it-out-at-the-north-east-basketball-elite-camp/', 'Sports247', 'ball'),
        ('farming', 'Ture Ward agricultural empowerment', 'Community initiative', 'Farmers in Ture Ward, Kaltungo West, received support through the distribution of 200 bags of fertiliser.', 'https://aytfoundation.org/fertilizer-distribution/', 'Adamu Yola Foundation', 'leaf'),
        ('camp', 'Player camp in Abuja', '2022', 'Eighteen players shortlisted from the sixth Unity Cup were invited to a closed camp in Abuja, a pathway from community football to wider opportunity.', 'https://www.sports247.ng/18-stars-of-adamu-yola-cup-earn-invitation-for-closed-camping-in-abuja/', 'Sports247', 'star'),
        ('sportvote', 'SportVote partnership', '2020', 'A partnership around the 5th Unity Cup to raise the visibility of grassroots players through sports technology.', 'https://futbaloven.wordpress.com/2020/12/10/adamu-yola-cup-loc-seals-sport-vote-partnership/', 'Futbaloven', 'hand'),
        ('amana', 'Amana FM broadcast partnership', '2023', 'Amana FM became the official broadcast partner of the 8th Unity Cup, taking match coverage to radio listeners.', 'https://aytfoundation.org/local-organising-committee-of-the-8th-adamu-yola-gombe-south-unity-cup-announces-amana-fm-as-official-broadcast-partner/', 'Adamu Yola Foundation', 'news'),
        ('peace', 'Peace and drug-abuse prevention campaigns', 'Across Unity Cup editions', 'Peace campaigns and anti-drug messages, including the Say No To Drugs call, have run alongside the tournament.', IGU, 'Instagram @adamuyolafdn', 'shield'),
        ('learning', 'Better learning environments', 'Historic programme', 'An initiative focused on improving the quality of learning environments for students.', None, None, 'book'),
        ('widows', 'Widows Support Programme', 'Empowerment', 'Food items and household support for widows in our communities, part of the foundation’s commitment that charity begins at home.', 'GALLERY:empowerment', 'Photos in our gallery', 'heart'),
    ]
    cards = ''.join(f'<article class="card reveal d{i%4}" id="{k}"><span class="ico">{I(ic)}</span><span class="num">{esc(y)}</span><h3>{esc(t)}</h3><p>{esc(s)}</p>{("<p style=margin-top:14px>"+(la(P+"gallery.html#"+u.split(":")[1], src) if u.startswith("GALLERY:") else la(u, "Source: "+src, True))+"</p>") if u else ""}</article>' for i, (k, t, y, s, u, src, ic) in enumerate(items))
    partners = ''.join(f'<div class="card reveal d{i%4}"><h3>{esc(n)}</h3><p>{esc(r)}</p></div>' for i, (n, r) in enumerate([
        ('Jordan Nwora Foundation', 'Co-delivered the North-East Elite Basketball Camp.'),
        ('Amana FM', 'Official broadcast partner of the 8th Unity Cup.'),
        ('SportVote', 'Player visibility partner for the 5th Unity Cup.'),
        ('Communities of Gombe South', 'Clubs, elders, families and volunteers who host and support every edition.')]))
    body = page_hero(P, [('Programmes & Projects', 'programs/'), ('Past Initiatives & Collaborations', None)], 'Past initiatives & collaborations.',
                     'Beyond our five current programmes, the foundation has supported athletes, farmers, learners and families, often alongside trusted partners.',
                     img='assets/community-football-photo.webp', alt='A coach talks with young footballers on a community pitch',
                     chips=[('pictures', 'Basketball City League'), ('initiatives', 'Initiatives'), ('partners', 'Collaborations')]) + f'''
<section class="section surface" id="pictures"><div class="wrap"><div class="section-head reveal"><div><p class="kicker">In pictures</p><h2>Support to Gombe State Basketball City League</h2><p>Jerseys, awards and certificates for players, teams and officials of the Gombe Basketball City League.</p></div><div class="btn-row" style="margin:0">{btn(P+"gallery.html#basketball", "See all photos")}{btn(P+"news.html#sport", "Read the news", "btn-ghost")}</div></div>
<div class="pics"><a class="pic reveal" href="{P}gallery.html#basketball"><img src="{P}{PH}basketball-league-champions-jersey-sm.webp" alt="A champions jersey presented to a player" loading="lazy"><span class="pic-cap">Champions jersey presentation</span></a><a class="pic reveal d1" href="{P}gallery.html#basketball"><img src="{P}{PH}basketball-league-player-award-sm.webp" alt="A player receives an award" loading="lazy"><span class="pic-cap">Recognising players</span></a><a class="pic reveal d2" href="{P}gallery.html#basketball"><img src="{P}{PH}basketball-league-certificate-sm.webp" alt="A certificate presented to an official of the league" loading="lazy"><span class="pic-cap">Certificates for officials</span></a></div></div></section>
<section class="section" id="initiatives"><div class="wrap"><div class="section-head reveal"><div><p class="kicker">Initiatives</p><h2>What we have done.</h2></div></div><div class="cards">{cards}</div></div></section>
<section class="section surface" id="partners"><div class="wrap"><div class="section-head reveal"><div><p class="kicker">Collaborations</p><h2>People we have worked with.</h2><p>Partnerships multiply impact. These organisations have helped us reach further.</p></div>{la(P+"get-involved.html#partner", "Become a partner")}</div><div class="cards">{partners}</div></div></section>
<section class="section-tight"><div class="wrap">{next_cards(P, [("Programme", "Gombe South Unity Cup", "programs/unity-cup.html", PH+"unity-cup-champions-trophy-sm.webp"), ("News", "News and Announcements", "news.html", PH+"unity-cup-final-2023-sm.webp"), ("About", "Leadership & History", "about.html#leadership", PH+"unity-cup-award-elder-sm.webp")])}</div></section>'''
    write('programs/past-initiatives.html', 'Past Initiatives & Collaborations', 'Basketball camps, agricultural empowerment, player pathways and partnerships from the Adamu Yola Foundation’s record.', 'Programmes & Projects', body, 'assets/community-football-photo.webp')

# --------------------------------------------------------------------------- NEWS
def news():
    P = './'
    cats = {'unity': 'Unity Cup', 'education': 'Education', 'empowerment': 'Empowerment', 'sport': 'Basketball', 'players': 'Player development', 'community': 'Community'}
    posts = []
    for i, n in enumerate(NEWS):
        feat = ' feature' if i == 0 else ''
        img = n['img'].replace('-sm.webp', '.webp') if (i == 0 and n['img']) else n['img']
        pimg = f'<div class="pimg"><img src="{P}{img}" alt="" loading="lazy"></div>' if img else f'<div class="pimg brand-fill">{mark_html()}</div>'
        tgt = '' if n.get('internal') else ' target="_blank" rel="noopener"'
        href = P + n['url'] if n.get('internal') else n['url']
        posts.append(f'<a class="post{feat} reveal d{i%3}" data-cat="{n["cat"]}" href="{href}"{tgt}>{pimg}<div class="pbody"><div class="meta"><span>{esc(n["date"])}</span><span>{cats[n["cat"]]}</span></div><h3>{esc(n["title"])}</h3><p>{esc(n["text"])}</p><span class="src">{esc(n["src"])} {I("arrow" if n.get("internal") else "external")}</span></div></a>')
    filt = '<div class="filters reveal" data-target="#news-list"><button data-filter="all" aria-pressed="true">All news</button>' + ''.join(f'<button data-filter="{k}" aria-pressed="false">{v}</button>' for k, v in cats.items()) + '</div>'
    body = page_hero(P, [('News & Media', None), ('News and Announcements', None)], 'News and announcements.',
                     'Results, partnerships and updates from the Unity Cup and the foundation’s wider work, with links to the original reports.',
                     chips=[('latest', 'Latest'), ('follow', 'Follow us')], extra='') + f'''
<section class="section" id="latest"><div class="wrap">{filt}<div class="news-grid" id="news-list">{''.join(posts)}</div></div></section>
<section class="section-tight" id="follow"><div class="wrap"><div class="cta-band reveal"><div><h2>Never miss an announcement.</h2><p>Fixtures, intakes and outreach dates are shared first on our social channels.</p></div><div class="btn-row" style="margin:0">{btn(FB, "Facebook", "btn-light")}{btn(IGU, "Instagram", "btn-light")}</div></div></div></section>'''
    write('news.html', 'News and Announcements', 'Unity Cup results, partnerships and updates from the Adamu Yola Foundation.', 'News & Media', body, NEWS[0]['img'].replace('-sm', ''))
    # keep old links working
    for old, to in [('stories.html', 'news.html'), ('stories/index.html', '../news.html')]:
        open(os.path.join(ROOT, old), 'w').write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>News and Announcements | Adamu Yola Foundation</title><link rel="canonical" href="{SITE}news.html"><meta http-equiv="refresh" content="0; url={to}"><meta name="robots" content="noindex"></head><body><p><a href="{to}">Go to News and Announcements</a></p></body></html>')

# --------------------------------------------------------------------------- GALLERY
def gallery():
    P = './'
    labels = {'education': 'Education', 'empowerment': 'Empowerment', 'basketball': 'Basketball', 'award': 'Unity Cup awards', 'match': 'Match day', 'fixtures': 'Fixtures and editions', 'video': 'Videos'}
    shots = ''.join(f'<button class="shot reveal" data-cat="{c}" data-full="{P}{f}.webp" data-title="{esc(t)}" data-meta="{esc(m)}. Source: {esc(src if src.startswith('Adamu') else 'Adamu Yola Foundation on ' + src)}"><img src="{P}{f}-sm.webp" alt="{esc(t)}" loading="lazy" width="{w}" height="{h}"><span class="cap">{esc(t)}</span></button>' for c, f, t, m, src, w, h in GALLERY)
    vids = ''.join(f'<a class="shot reveal" data-cat="video" href="{u}" target="_blank" rel="noopener"><img src="{P}{f}-sm.webp" alt="{esc(t)}" loading="lazy"><span class="play">{I("play")}</span><span class="cap">{esc(t)}. {esc(m)}, watch on Instagram</span></a>' for f, t, m, u in VIDEOS)
    filt = '<div class="filters reveal" data-target="#gallery-grid"><button data-filter="all" aria-pressed="true">Everything</button>' + ''.join(f'<button data-filter="{k}" aria-pressed="false">{v}</button>' for k, v in labels.items()) + '</div>'
    body = page_hero(P, [('News & Media', None), ('Photo & Video Gallery', None)], 'Photo & video gallery.',
                     'Education projects, support for widows, the Gombe Basketball City League and the faces and finals of the Gombe South Unity Cup. Tap any photo to view it larger.',
                     img=PH + 'unity-cup-champions-trophy.webp', alt='Champions with the Unity Cup trophy') + f'''
<section class="section"><div class="wrap">{filt}<div class="masonry" id="gallery-grid">{shots}{vids}</div>
<div class="cta-band reveal" style="margin-top:40px"><div><h2>Have photos from an AYF event?</h2><p>Help us preserve the story. Share pictures, dates and names with our media team.</p></div><div>{btn(P+"contact.html?topic=media", "Share your photos", "btn-light")}</div></div>
</div></section>
<dialog class="lightbox" aria-label="Photo viewer"><button class="lb-close" aria-label="Close">{I("x")}</button><button class="lb-nav lb-prev" aria-label="Previous photo">{I("left")}</button><button class="lb-nav lb-next" aria-label="Next photo">{I("right")}</button><figure><img src="" alt=""><figcaption><strong></strong><span></span></figcaption></figure></dialog>'''
    write('gallery.html', 'Photo & Video Gallery', 'Photos and videos from the Gombe South Unity Cup and Adamu Yola Foundation community events.', 'News & Media', body, PH + 'unity-cup-champions-trophy.webp')

# --------------------------------------------------------------------------- GET INVOLVED
def involved():
    P = './'
    body = page_hero(P, [('Get Involved', None)], 'Be part of what comes next.',
                     'Organisations, volunteers and community members help the foundation turn local potential into real opportunity.',
                     img=PH + 'unity-cup-award-volunteer.webp', alt='A volunteer receives recognition at the Unity Cup',
                     chips=[('partner', 'Partner / Sponsor'), ('volunteer', 'Volunteer'), ('support', 'Support / Donate'), ('archive', 'Share media')]) + f'''
<section class="section" id="partner">
<div class="wrap split">
<div class="reveal"><p class="kicker">Partner / Sponsor</p><h2>Back a programme you believe in.</h2><p>Companies, institutions and development partners can sponsor the Unity Cup, fund a scholarship cohort, equip a training workshop or support an outreach day. We agree clear goals with every partner and report back on what your support achieved.</p>
<div class="cards" style="margin-top:24px">
<div class="card"><span class="ico">{I("ball")}</span><h3>Unity Cup sponsorship</h3><p>Kits, prizes, officiating, media and post-tournament camps.</p></div>
<div class="card"><span class="ico">{I("book")}</span><h3>Education partnership</h3><p>Scholarships and learning materials for indigent students.</p></div>
</div>
<div class="btn-row">{btn(P+"contact.html?topic=partnership", "Discuss a partnership")}{btn(P+"contact.html?topic=unity-cup", "Sponsor the Unity Cup", "btn-ghost")}</div></div>
<figure class="photo reveal d2" style="aspect-ratio:4/3"><img src="{P}{PH}unity-cup-award-handshake.webp" alt="Unity Cup partners and officials shake hands" loading="lazy"></figure>
</div>
</section>
<section class="section surface" id="volunteer">
<div class="wrap split flip">
<div class="reveal"><p class="kicker">Volunteer</p><h2>Give your time and skills.</h2><p>Our programmes run on people. Volunteers help with match-day operations, coaching clinics, mentoring students, health outreach logistics, photography and community mobilisation.</p>
<ul class="vlist" style="margin-top:24px"><li><h3>Tell us about you</h3><p>Share your skills, location and availability.</p></li><li><h3>Meet the team</h3><p>We match you with a programme that needs what you offer.</p></li><li><h3>Make it count</h3><p>Join an activity and help us record the difference it makes.</p></li></ul>
<div class="btn-row">{btn(P+"contact.html?topic=volunteer", "Volunteer with us")}</div></div>
<figure class="photo reveal d2" style="aspect-ratio:4/3"><img src="{P}{PH}unity-cup-award-medal.webp" alt="A Unity Cup volunteer receives a medal" loading="lazy"></figure>
</div>
</section>
<section class="section" id="support">
<div class="wrap">
<div class="section-head reveal"><div><p class="kicker">Support / Donate</p><h2>Help fund opportunity.</h2><p>Online giving is being set up. Until it opens, you can pledge support directly and our team will share verified payment details and a receipt.</p></div></div>
<div class="paths">
<div class="path reveal"><span class="ico">{I("book")}</span><h3>A student’s school year</h3><p>Fees, books and materials that keep a learner in class.</p></div>
<div class="path reveal d1"><span class="ico">{I("tool")}</span><h3>A trainee’s toolkit</h3><p>Equipment and materials for a vocational trainee.</p></div>
<div class="path reveal d2"><span class="ico">{I("heart")}</span><h3>An outreach day</h3><p>Screening supplies and logistics for a community health day.</p></div>
</div>
<div class="btn-row">{btn(P+"contact.html?topic=support", "Pledge your support")}</div>
</div>
</section>
<section class="section-tight" id="archive">
<div class="wrap"><div class="cta-band reveal"><div><h2>Share foundation archive media.</h2><p>Photographs, captions, dates and memories from past events help us tell the full story.</p></div><div>{btn(P+"contact.html?topic=media", "Share archive material", "btn-light")}</div></div></div>
</section>'''
    write('get-involved.html', 'Get Involved', 'Partner, sponsor, volunteer or support the Adamu Yola Foundation’s work in Gombe State.', 'Get Involved', body, PH + 'unity-cup-award-volunteer.webp')

# --------------------------------------------------------------------------- CONTACT
def contact():
    P = './'
    topics = [('general', 'General enquiry'), ('partnership', 'Partnership or sponsorship'), ('volunteer', 'Volunteering'), ('support', 'Support or donation'),
              ('scholarships', 'Educational Scholarships'), ('vocational-training', 'Vocational Training'), ('unity-cup', 'Gombe South Unity Cup'),
              ('medical-outreach', 'Medical Outreach'), ('principals-cup', "Gombe State Principals' Cup"), ('media', 'Media and archive photos')]
    opts = ''.join(f'<option value="{v}">{esc(t)}</option>' for v, t in topics)
    body = page_hero(P, [('Contact', None)], 'Start a conversation.',
                     'Partnerships, programme questions, volunteering, media and general enquiries all come to the same team.') + f'''
<section class="section">
<div class="wrap contact-grid">
<div class="reveal">
<h2>Speak with us.</h2>
<p>We read every message and respond as quickly as we can.</p>
<div class="reach" style="margin-top:24px">
<a href="mailto:{EMAIL}"><span class="ico">{I("mail")}</span><span><small>Email</small><strong>{EMAIL}</strong></span></a>
<a href="tel:{TEL}"><span class="ico">{I("phone")}</span><span><small>Phone</small><strong>{PHONE}</strong></span></a>
<a href="https://www.google.com/maps/search/?api=1&query=Billiri+Street+Shongo+Estate+Gombe" target="_blank" rel="noopener"><span class="ico">{I("pin")}</span><span><small>Office</small><strong>{ADDRESS}</strong></span></a>
<div class="item"><span class="ico">{I("camera")}</span><span><small>Follow us</small><strong>@AdamuYolaFDN</strong></span></div>
</div>
<div style="margin-top:20px;color:var(--ink)">{socials()}</div>
</div>
<form class="form reveal d2" id="contact-form" novalidate>
<h3>Send a message</h3>
<div class="row"><div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required></div>
<div class="field"><label for="f-email">Email address</label><input id="f-email" name="email" type="email" autocomplete="email" required></div></div>
<div class="row"><div class="field"><label for="f-phone">Phone (optional)</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
<div class="field"><label for="f-topic">Topic</label><select id="f-topic" name="topic">{opts}</select></div></div>
<div class="field"><label for="f-msg">Your message</label><textarea id="f-msg" name="message" required></textarea></div>
<p class="form-note">Sending opens your email app with the message ready. Please do not include medical records or ID documents.</p>
<div><button class="btn" type="submit">Send message {I("arrow")}</button></div>
<p class="form-status" role="status" aria-live="polite"></p>
</form>
</div>
</section>'''
    write('contact.html', 'Contact', 'Contact the Adamu Yola Foundation in Gombe by email, phone or our message form.', 'Contact', body)

# --------------------------------------------------------------------------- LEGAL
def legal():
    P = './'
    priv = page_hero(P, [('Privacy Policy', None)], 'Privacy policy.', 'How the Adamu Yola Foundation handles information when you use this website or contact us. Last updated October 2026.') + f'''
<section class="section"><div class="wrap legal prose">
<h2>Who we are</h2><p>This website is operated by the Adamu Yola Foundation (Incorporated Trustees, IT/NO 117968), {ADDRESS}. You can reach us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Information you send us</h2><p>Our contact form prepares an email in your own email application. The website itself does not store or transmit your message. When you send the email, we receive your name, email address, any phone number you include and your message, and we use them only to respond and to manage the enquiry.</p>
<h2>Information this website stores</h2><ul><li>Your day or night display preference is saved in your browser’s local storage so the site remembers it. It never leaves your device.</li><li>We do not use advertising or analytics trackers.</li><li>Fonts are loaded from Google Fonts, which receives standard technical information such as your IP address when the fonts load.</li></ul>
<h2>Photos and people</h2><p>Photographs on this site come from foundation events and our official social media channels. If you appear in a photo and would like it removed, contact us and we will act promptly.</p>
<h2>Sensitive information</h2><p>Please do not send medical histories, identity documents or other sensitive personal data by email or social media. When a programme needs this information, we will provide a secure process.</p>
<h2>Children</h2><p>Programmes involving students and young players follow safeguarding practices. Applications for anyone under 18 should be made with a parent, guardian or school.</p>
<h2>Your rights</h2><p>In line with the Nigeria Data Protection Act 2023, you may ask to access, correct or delete personal information we hold about you, or object to how we use it. Email us and we will respond within a reasonable time.</p>
<h2>Changes</h2><p>We may update this policy as our website and programmes evolve. The latest version will always be on this page.</p>
<p>{la(P+"terms.html", "Read our Terms of Use")}</p>
</div></section>'''
    write('privacy.html', 'Privacy Policy', 'How the Adamu Yola Foundation handles information on its website and in enquiries.', '', priv)
    terms = page_hero(P, [('Terms of Use', None)], 'Terms of use.', 'The terms that apply when you visit and use the Adamu Yola Foundation website. Last updated October 2026.') + f'''
<section class="section"><div class="wrap legal prose">
<h2>Using this website</h2><p>By using this website you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>Content and ownership</h2><p>All text, logos, the Adamu Yola Foundation and Gombe South Unity Cup marks, photographs and design on this website belong to the Adamu Yola Foundation or are used with permission. All rights reserved. You may share links and short quotations with credit. Any other copying, editing or commercial use requires our written permission.</p>
<h2>Accuracy</h2><p>We work to keep information current, including programme details, dates and results. Details can change, so please confirm important information with us before acting on it.</p>
<h2>Programmes and applications</h2><p>Information about scholarships, training, outreach and tournaments does not guarantee a place or award. Each opportunity has its own eligibility and selection process, which we publish when it opens.</p>
<h2>Donations</h2><p>The foundation will only request support through its official contacts listed on this website. Be cautious of anyone requesting money in our name through other channels, and contact us to confirm.</p>
<h2>Links to other websites</h2><p>We link to news reports and social media for reference. We are not responsible for the content or privacy practices of those websites.</p>
<h2>Liability</h2><p>This website is provided as is. To the extent permitted by law, the foundation is not liable for loss arising from the use of this website.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of the Federal Republic of Nigeria.</p>
<h2>Contact</h2><p>Questions about these terms can be sent to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<p>{la(P+"privacy.html", "Read our Privacy Policy")}</p>
</div></section>'''
    write('terms.html', 'Terms of Use', 'Terms that apply to the use of the Adamu Yola Foundation website.', '', terms)
    nf = f'''<section class="section" style="text-align:center"><div class="wrap" style="max-width:640px"><div style="width:180px;margin:0 auto 26px;perspective:800px">{mark_html()}</div><h1>Page not found.</h1><p class="lead" style="margin-inline:auto">The page you were looking for has moved or no longer exists.</p><div class="btn-row" style="justify-content:center">{btn("./", "Back to home")}{btn("./programs/", "Our programmes", "btn-ghost")}</div></div></section>'''
    write('404.html', 'Page Not Found', 'This page could not be found.', '', nf)

def extras():
    pages = ['', 'about.html', 'programs/', 'programs/scholarships.html', 'programs/vocational-training.html', 'programs/unity-cup.html', 'programs/medical-outreach.html', 'programs/principals-cup.html', 'programs/past-initiatives.html', 'news.html', 'gallery.html', 'get-involved.html', 'contact.html', 'privacy.html', 'terms.html']
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{SITE}{p}</loc><lastmod>2026-10-18</lastmod></url>\n' for p in pages) + '</urlset>\n')
    open(os.path.join(ROOT, 'site.webmanifest'), 'w').write('''{
  "name": "Adamu Yola Foundation",
  "short_name": "AYF",
  "start_url": "./",
  "scope": "./",
  "display": "standalone",
  "background_color": "#F4F8FC",
  "theme_color": "#172B4D",
  "icons": [
    {"src": "./assets/brand/favicon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
    {"src": "./assets/brand/favicon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"}
  ]
}
''')

home(); about(); programmes_index()
for p in PROGRAMMES: programme(p)
past(); news(); gallery(); involved(); contact(); legal(); extras()
print('built')
