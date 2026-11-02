"""Générateur de la maquette E.G.C.P Électricité. Usage : python build.py <dossier-du-projet>
Contenus relevés sur la page Facebook d'E.G.C.P et l'annuaire des entreprises (novembre 2026). Rien d'inventé : textes, photos, coordonnées."""
import os
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
A = 'assets/'
PH = A + 'ph/'
V = 2  # cache : incrémenter à chaque changement de CSS ou JS
TEL, TELH, MAIL = '06 73 95 63 32', 'tel:0673956332', 'egcpelectricite@gmail.com'
FB = 'https://www.facebook.com/egcpelectricite'
ADR = ('23 rue de la Dombes', '01140 Saint-Étienne-sur-Chalaronne')

NAV = [('electricite.html', 'Électricité'), ('climatisation.html', 'Climatisation'), ('realisations.html', 'Réalisations')]


def pill(t, href, cls='', arrow='↗'):
    return f'<a class="pill {cls}" href="{href}"><span class="r"><span>{t}</span><span>{t}</span></span><b>{arrow}</b></a>'


def tile(src, cls='', style='', alt='', par=None, lazy=True):
    p = f' data-par="{par}" style="height:118%;width:100%"' if par else ''
    return f'<figure class="tile {cls}" style="{style}"><img src="{src}" alt="{alt}"{p}{" loading=lazy" if lazy else ""}></figure>'


def logo(cls=''):
    return f'<span class="lgo {cls}" aria-hidden="true"><img src="{A}logo-mark.png" alt="" width="40" height="40"><span>E.G.C.P<small>Électricité · Climatisation</small></span></span>'


def head(title, desc, cur):
    def a(h, t, cls=''):
        return f'<a href="{h}"{" class="+cls if cls else ""}{" aria-current=page" if h == cur else ""}>{t}</a>'
    items = a('index.html', 'Accueil') + ''.join(a(h, t) for h, t in NAV) + a('contact.html', 'Devis gratuit', 'hl')
    return f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#0a0d14">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{A}favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}style.css?v={V}">
</head><body>
<div id="bar"></div>
<header class="top">
<a class="logo" href="index.html" aria-label="E.G.C.P Électricité, accueil">{logo()}</a>
<nav class="nav" aria-label="Navigation principale"><button class="stop" type="button" aria-label="Fermer le menu"><span>MENU</span></button>{items}</nav>
<span class="side"><a class="tel" href="{TELH}" aria-label="Appeler le {TEL}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z" fill="currentColor"/></svg><span>{TEL}</span></a></span>
<button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</header>
<main>'''


def foot():
    return f'''</main>
<footer><div class="wrap"><div class="fg">
<div>{logo('big')}<p>Électricité générale, climatisation et automatismes. Neuf, rénovation et dépannage. Basé à Saint-Étienne-sur-Chalaronne, dans l’Ain, et alentours.</p></div>
<div><h4 class="micro">Savoir-faire</h4><ul><li><a href="electricite.html">Électricité</a></li><li><a href="climatisation.html">Climatisation</a></li><li><a href="electricite.html#automatismes">Automatismes</a></li><li><a href="realisations.html">Réalisations</a></li></ul></div>
<div><h4 class="micro">Contact</h4><ul><li><a href="{TELH}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="contact.html">Devis gratuit</a></li><li><a href="{FB}" rel="noopener" target="_blank">Facebook</a></li></ul></div>
<div><h4 class="micro">Adresse</h4><ul><li>{ADR[0]}</li><li>{ADR[1]}</li></ul></div>
</div></div>
<div class="fw" aria-hidden="true">E.G.C.P</div>
<div class="fb micro"><span class="pad">© E.G.C.P Électricité</span><span class="pad">Maquette de site · Le Génie Numérique</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="{A}main.js?v={V}"></script></body></html>'''


def cta(t='Un projet, <em>une panne</em> ?'):
    return f'''<section class="sec cta"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.6rem">Neuf · rénovation · dépannage</span><h2 class="sp">{t}</h2>
<div class="row rv">{pill('Demander un devis', 'contact.html', 'blue')}{pill(TEL, TELH, 'ghost')}</div></div></section>'''


def pagehead(crumb, h1, lead, img, img2=None, extra=''):
    t2 = tile(img2, 'small', lazy=False) if img2 else ''
    return f'''<section class="ph"><div class="wrap"><div class="crumb micro"><a href="index.html">Accueil</a> / {crumb}</div><h1 class="sp">{h1}</h1><p class="lead rv">{lead}</p>{extra}</div>{tile(img, lazy=False)}{t2}</section>'''


def faq(its):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in its) + '</div>'


# photos publiées sur la page Facebook d'E.G.C.P (2024)
GAL = [('p03', 'Électricité', 'Spots encastrés entre les poutres'), ('p12', 'Climatisation', 'Unité extérieure posée en façade'),
       ('p06', 'Électricité', 'Tableau électrique neuf'), ('p16', 'Climatisation', 'Climatiseur mural en chambre'),
       ('p10', 'Électricité', 'Appliques de chevet'), ('p02', 'Climatisation', 'Climatisation en salle de bains'),
       ('p09', 'Électricité', 'Coffrets électriques extérieurs'), ('p18', 'Climatisation', 'Unité extérieure sur balcon'),
       ('p04', 'Électricité', 'Éclairage d’un plafond à poutres'), ('p14', 'Climatisation', 'Unité intérieure discrète'),
       ('p07', 'Électricité', 'Tableau en cours de câblage'), ('p13', 'Climatisation', 'Groupe extérieur, côté terrasse'),
       ('p05', 'Électricité', 'Pièce de vie éclairée'), ('p08', 'Électricité', 'Remplacement d’un ancien tableau'),
       ('p01', 'Entreprise', 'Le véhicule d’intervention'), ('p15', 'Entreprise', 'Toujours sur la route')]


def gal(items):
    return '<div class="gal">' + ''.join(f'<figure class="rv" data-c="{c}" style="--d:{(i % 3) * .07}s"><img src="{PH}{k}.webp" alt="{t}" loading="lazy"><figcaption><span class="micro">{c}</span>{t}</figcaption></figure>' for i, (k, c, t) in enumerate(items)) + '</div>'


def service(file, title, desc, crumb, h1, lead, img, img2, intro_h, intro_p, checks, cat, faqs, more=''):
    items = [g for g in GAL if g[1] == cat]
    extra = f'<div class="row rv" style="display:flex;gap:10px;flex-wrap:wrap;margin-top:2.2rem">{pill("Devis gratuit", "contact.html", "blue")}{pill(TEL, TELH, "ghost")}</div>'
    cl = ''.join(f'<li><span><b>{a}</b> {b}</span></li>' for a, b in checks)
    return head(title, desc, file) + pagehead(crumb, h1, lead, img, img2, extra) + f'''
<section class="sec"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Notre savoir-faire</span><h2 class="sp">{intro_h}</h2><p class="lead rv" style="margin-top:1.4rem">{intro_p}</p></div><ul class="checks rv">{cl}</ul></div></section>{more}
<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Réalisations</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,3.4rem)">Sur nos <em>chantiers</em></h2>{gal(items)}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Questions fréquentes</span><h2 class="sp">On vous <em>répond</em></h2></div><div class="rv">{faq(faqs)}</div></div></section>''' + cta() + foot()


FAQ_ZONE = ('Dans quel secteur intervenez-vous ?', 'Dans l’Ain et alentours. L’entreprise est basée à Saint-Étienne-sur-Chalaronne, entre Châtillon-sur-Chalaronne et Thoissey. Nous sommes aussi intervenus à Belleville-en-Beaujolais.')
FAQ_DEVIS = ('Le devis est-il gratuit ?', f'Oui. Appelez le {TEL} ou écrivez à {MAIL}. Décrivez votre projet, photos à l’appui si possible.')
FAQ_DEP = ('Faites-vous du dépannage ?', f'Oui, en électricité comme en climatisation. Appelez le {TEL} et décrivez la panne.')


def pages():
    P = {}
    hero_tiles = [('t1', 'p03'), ('t2', 'p16'), ('t3', 'p06'), ('t4', 'p12'), ('t5', 'p10'), ('t6', 'p02'), ('t7', 'p01')]
    ht = ''.join(f'<figure class="tile {c}"><div class="fl"><div class="in"><img src="{PH}{f}.webp" alt=""></div></div></figure>' for c, f in hero_tiles)
    stack = ''.join(tile(f'{PH}{f}.webp') for f in ['p03', 'p04', 'p05', 'p10', 'p06', 'p07', 'p09', 'p08'])
    wall_imgs = ['p03', 'p12', 'p06', 'p16', 'p10', 'p02', 'p09', 'p18', 'p04', 'p14', 'p07', 'p13', 'p05', 'p01', 'p08']
    wall = ''.join(tile(f'{PH}{wall_imgs[i % len(wall_imgs)]}.webp') for i in range(54))
    items = [('electricite.html', '01', 'Électricité', 'Installation neuve, rénovation, tableaux, éclairage.', 'p03'),
             ('climatisation.html', '02', 'Climatisation', 'Installation, entretien et dépannage. Modèles réversibles.', 'p16'),
             ('electricite.html#automatismes', '03', 'Automatismes', 'Pilotage à distance, alarmes et équipements connectés.', 'p09'),
             ('contact.html', '04', 'Dépannage', 'Une panne ? Un appel, et on vient voir.', 'p01')]
    pl = ''.join(f'<a href="{h}"><span class="micro mute">{n}</span><span class="nm">{t}</span><span class="d">{d}<b>Devis gratuit</b></span></a>' for h, n, t, d, _ in items)
    prev = ''.join(tile(f'{PH}{im}.webp', 'on' if i == 0 else '') for i, (*_, im) in enumerate(items))
    track = ''.join(f'<figure class="tile"><img src="{PH}{f}.webp" alt="{l}" loading="lazy"><span class="tag">{l}</span></figure>' for f, l in [('p16', 'En chambre'), ('p12', 'En façade'), ('p02', 'En salle de bains'), ('p18', 'Sur balcon'), ('p14', 'Discrète'), ('p13', 'Côté terrasse')])
    steps = [('Votre appel', f'Un coup de fil au {TEL}, un message ou un e-mail. Vous décrivez votre besoin ou votre panne.'),
             ('Visite et devis', 'On vient voir sur place et on vous remet un devis clair, gratuit.'),
             ('Installation', 'Du passage des câbles au raccordement, un seul interlocuteur du début à la fin.'),
             ('Suivi', 'Entretien de votre climatisation et dépannage si besoin.')]
    st = ''.join(f'<div class="stp"><div class="n">{i + 1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    mq = ''.join(f'<span>{x}</span>' for x in ['Électricité', 'Climatisation', 'Automatismes', 'Neuf', 'Rénovation', 'Dépannage'] * 2)
    zones = [('Saint-Étienne-sur-Chalaronne', 'Le siège de l’entreprise', '01'), ('Ain et alentours', 'Dombes, Val de Saône, Bresse…', '01'), ('Beaujolais', 'Déjà intervenu à Belleville-en-Beaujolais', '69')]
    zl = '<div class="agl">' + ''.join(f'<article class="row"><h3>{n}</h3><address>{a}</address><span class="dep micro">{d}</span><a class="tel" href="{TELH}">{TEL}</a></article>' for n, a, d in zones) + '</div>'

    P['index.html'] = head('E.G.C.P Électricité — Électricien et climatisation à Saint-Étienne-sur-Chalaronne (Ain)', 'E.G.C.P, électricien dans l’Ain : électricité générale, climatisation, automatismes. Neuf, rénovation, dépannage. Saint-Étienne-sur-Chalaronne et alentours. Devis gratuit.', 'index.html') + f'''
<section class="hero">
<div class="cap micro c1"><b>Électricité · Clim</b>Automatismes</div>
<div class="cap micro c2"><b>Neuf · Rénovation</b>Dépannage</div>
<div class="cap micro c3"><b>Ain</b>&amp; alentours</div>
<div class="go">{pill('Devis gratuit', 'contact.html')}</div>
{ht}
<p class="para">Le courant, le chaud, le froid. Un seul artisan, dans l’Ain.</p>
<h1 class="word">E.G.C.P</h1>
<div class="scrollhint micro"><i></i>Défiler</div>
</section>

<div class="mq" aria-hidden="true"><div>{mq}</div></div>

<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Pourquoi E.G.C.P ?</span><h2 class="sp">Votre électricien, <em>tout simplement</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Électricité générale, climatisation et automatismes. Pour les maisons comme pour les professionnels, du neuf au dépannage.</p>
<ul class="checks rv" style="margin-bottom:2rem"><li><span><b>Un seul interlocuteur.</b> Électricité et climatisation, sans multiplier les artisans.</span></li><li><span><b>Particuliers et pros.</b> De la salle de bains à l’hôtel de 19 chambres.</span></li><li><span><b>Devis gratuit.</b> Un appel au {TEL}.</span></li></ul>{pill('Voir nos réalisations', 'realisations.html', 'blue')}</div>{tile(PH + 'p05.webp', '', par=8, alt='Pièce de vie éclairée par E.G.C.P')}</div></section>

<section class="story"><span class="micro mute m3">L’électricité</span>
<h2><span class="w">De</span> <span class="w">la</span> <span class="w">lumière</span> <span class="w">là</span> <span class="w">où</span> <span class="w">vous</span> <span class="w">en</span> <span class="w"><em>voulez</em></span></h2>
<div class="stack">{stack}</div>
<p class="micro mute m1">Tableaux, prises, éclairage, câblage. En neuf comme en rénovation.</p><span class="micro mute m2">Dedans comme dehors</span></section>

<section class="wall"><div class="grid">{wall}</div><div class="mid"><span class="micro mute">Chantier après chantier</span><h2>Du câble <em>au confort</em></h2>{pill('Voir les réalisations', 'realisations.html', 'blue')}</div></section>

<section class="sec" id="services"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Nos savoir-faire</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,4rem)">De quoi avez-vous <em>besoin ?</em></h2>
<div class="plist">{pl}</div></div><div class="prev">{prev}</div></section>

<section class="hz"><div class="pin"><div class="wrap top2"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Climatisation réversible</span><h2>Frais l’été, <em>chaud l’hiver</em></h2></div>{pill('La climatisation', 'climatisation.html')}</div>
<div class="track">{track}</div></div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Grands chantiers</span><h2 class="sp">Ils ont <em>compté</em></h2>
<div class="cnt rv"><div><b data-to="19">0</b><span>salles de bains d’hôtel équipées : éclairage, appareillage, sèche-serviettes, ventilation</span></div><div><b data-to="320">0</b><span>mètres de câble d’alimentation 4G120 mm² tirés et raccordés</span></div><div><b data-to="2">0</b><span>métiers, un seul artisan : l’électricité et la climatisation</span></div></div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Votre projet</span><h2 class="sp">Du premier appel <em>au suivi</em></h2><div class="steps">{st}</div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><div style="display:flex;justify-content:space-between;align-items:flex-end;gap:2rem;flex-wrap:wrap;margin-bottom:clamp(2rem,5vw,4rem)"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Secteur d’intervention</span><h2 class="sp">L’Ain <em>et alentours</em></h2></div>{pill('Nous contacter', 'contact.html', 'ghost')}</div>{zl}</div></section>
{cta()}''' + foot()

    auto = f'''
<section class="sec" id="automatismes" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Automatismes</span><h2 class="sp">Une maison <em>qui obéit</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Pilotage à distance, équipements connectés, alarmes : on installe et on raccorde vos automatismes, en même temps que votre électricité.</p></div>{tile(PH + 'p09.webp', '', par=8, alt='Coffrets électriques posés par E.G.C.P')}</div></section>'''
    P['electricite.html'] = service('electricite.html', 'Électricien à Saint-Étienne-sur-Chalaronne (Ain) — E.G.C.P', 'Électricité générale : installation neuve, rénovation, tableaux électriques, éclairage, automatismes et dépannage. Saint-Étienne-sur-Chalaronne, Ain et alentours.',
        'Électricité', 'L’électricité, <em>bien faite</em>', 'Installation neuve, rénovation, mise en sécurité et dépannage. Pour les particuliers comme pour les professionnels.', PH + 'p03.webp', PH + 'p06.webp',
        'Du tableau <em>à la lumière</em>', 'Tableaux électriques, prises, éclairage, câblage : nous réalisons votre installation de A à Z. Dernier gros chantier : les 19 salles de bains d’un hôtel.',
        [('Installation neuve.', 'Maisons, extensions, locaux professionnels.'), ('Rénovation.', 'Remplacement d’anciens tableaux, remise aux normes.'), ('Éclairage.', 'Spots encastrés, appliques, éclairage extérieur.'), ('Gros câblage.', 'Câbles d’alimentation de forte section, sur de longues distances.'), ('Dépannage.', 'Une panne, un disjoncteur qui saute : on vient voir.')], 'Électricité',
        [FAQ_DEP, ('Travaillez-vous pour les professionnels ?', 'Oui. Par exemple, l’électricité de 19 salles de bains d’un hôtel : éclairage, appareillage, sèche-serviettes et ventilation.'), FAQ_DEVIS, FAQ_ZONE], auto)

    P['climatisation.html'] = service('climatisation.html', 'Climatisation à Saint-Étienne-sur-Chalaronne (Ain) — E.G.C.P', 'Installation, entretien et dépannage de climatisations réversibles (Toshiba, Heiwa…). Pilotage à distance. Saint-Étienne-sur-Chalaronne, Ain et alentours.',
        'Climatisation', 'Le bon air, <em>toute l’année</em>', 'Installation, entretien et dépannage de vos systèmes de climatisation. N’attendez pas les beaux jours pour vous rafraîchir.', PH + 'p16.webp', PH + 'p12.webp',
        'Réversible <em>et économe</em>', 'Nous posons des climatisations réversibles : fraîches l’été, chauffantes l’hiver. Par exemple la gamme Haori de Toshiba, économique et basse consommation, en plusieurs couleurs. Ou une Heiwa pilotable depuis votre téléphone, posée à Belleville-en-Beaujolais.',
        [('Installation.', 'Unité intérieure et groupe extérieur, raccordement compris.'), ('Réversible.', 'Rafraîchit l’été, chauffe l’hiver.'), ('Pilotage à distance.', 'Selon le modèle, depuis une application.'), ('Entretien.', 'Pour garder un appareil efficace et sain.'), ('Dépannage.', 'Votre clim ne souffle plus ? Appelez-nous.')], 'Climatisation',
        [('Quelles marques installez-vous ?', 'Par exemple Toshiba (gamme Haori) et Heiwa. Nous vous conseillons selon la pièce et votre budget.'), ('La climatisation peut-elle chauffer ?', 'Oui : un modèle réversible rafraîchit l’été et chauffe l’hiver.'), FAQ_DEP, FAQ_DEVIS, FAQ_ZONE])

    P['realisations.html'] = head('Réalisations — E.G.C.P Électricité', 'Photos de chantiers E.G.C.P : tableaux électriques, éclairage, climatisations dans l’Ain.', 'realisations.html') + pagehead('Réalisations', 'Nos <em>réalisations</em>', 'Tableaux, éclairage, climatisations : quelques chantiers, en photos.', PH + 'p04.webp', PH + 'p14.webp') + f'''
<section class="sec"><div class="wrap"><div class="flt" data-t=".gal figure"><button class="on" data-f="*">Tout</button><button data-f="Électricité">Électricité</button><button data-f="Climatisation">Climatisation</button><button data-f="Entreprise">L’entreprise</button></div>{gal(GAL)}<p class="note" style="margin-top:2rem">Photos publiées par E.G.C.P sur sa page Facebook.</p></div></section>''' + cta() + foot()

    P['contact.html'] = head('Contact et devis gratuit — E.G.C.P Électricité', f'Demandez votre devis gratuit à E.G.C.P : {TEL}, {MAIL}. {ADR[0]}, {ADR[1]}.', 'contact.html') + pagehead('Contact', 'Parlons de <em>votre projet</em>', 'Devis gratuit. Électricité, climatisation, automatismes, dépannage. Ain et alentours.', PH + 'p15.webp') + f'''
<section class="sec" id="contact"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Coordonnées</span><h2 class="sp">Un appel <em>suffit</em></h2>
<div class="contactline rv" style="margin-top:2rem"><a href="{TELH}">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a></div>
<p class="lead rv" style="margin-top:1.6rem">{ADR[0]}<br>{ADR[1]}</p></div>
<form class="f calc rv"><div class="r2"><div class="fld"><label for="n">Nom</label><input id="n" required></div><div class="fld"><label for="t">Téléphone</label><input id="t" type="tel" required></div></div>
<div class="fld"><label for="e">E-mail</label><input id="e" type="email"></div>
<div class="r2"><div class="fld"><label for="p">Besoin</label><select id="p"><option>Électricité</option><option>Climatisation</option><option>Automatismes</option><option>Dépannage</option><option>Autre</option></select></div><div class="fld"><label for="v">Commune</label><input id="v"></div></div>
<div class="fld"><label for="m">Votre besoin en quelques mots</label><textarea id="m" rows="4" placeholder="Pièces, surface, panne constatée, photos à envoyer…"></textarea></div>
<button class="pill blue" type="submit" style="justify-self:start"><span class="r"><span>Envoyer</span><span>Envoyer</span></span><b>↗</b></button><div class="ok">Merci ! (Maquette : aucun message n’est envoyé.)</div></form></div></section>''' + foot()
    return P


for k, v in pages().items():
    open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
print('ok')
