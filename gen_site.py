#!/usr/bin/env python3
import os, colorsys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "portfolio")
LANGS = ["en", "es", "fr"]
LANG_LABEL = {"en": "EN", "es": "LX", "fr": "FR"}
LANG_NAME = {"en": "English", "es": "Latinx", "fr": "Français"}

SITE = {
    "name": "Natalia Giraldo",
    "role": {
        "en": "Multimedia Arts &amp; Product Design",
        "es": "Artes Multimedia y Diseño de Producto",
        "fr": "Arts Multimédias &amp; Design produit",
    },
    "hero_title": {
        "en": "Multimedia Arts &amp; Product Design",
        "es": "Artes Multimedia y Diseño de Producto",
        "fr": "Arts Multimédias &amp; Design produit",
    },
    "hero": {
        "en": "I design at the intersection of digital interfaces and physical space — from VR experiences and blockchain archives to urban furniture and interactive/immersive installations. My work explores how technology and critical thinking can reshape how we inhabit the future of the public and digital space.",
        "es": "Diseño en la intersección entre interfaces digitales y el espacio físico — desde experiencias en VR y archivos en blockchain hasta mobiliario urbano e instalaciones interactivas/inmersivas. Mi trabajo explora cómo la tecnología y el pensamiento crítico pueden transformar la manera en que habitamos el futuro del espacio público y digital.",
        "fr": "Je conçois à la croisée des interfaces numériques et de l&#8217;espace physique — des expériences VR et archives blockchain jusqu&#8217;au mobilier urbain et aux installations interactives/immersives. Mon travail explore comment la technologie et la pensée critique peuvent transformer notre manière d&#8217;habiter le futur de l&#8217;espace public et numérique.",
    },
    "nav": {
        "home": {"en": "Home", "es": "Inicio", "fr": "Accueil"},
        "digital": {"en": "Multimedia Arts", "es": "Artes Multimedia", "fr": "Arts Multimédias"},
        "product": {"en": "Product Design", "es": "Diseño de Producto", "fr": "Design produit"},
        "contact": {"en": "Contact_", "es": "Contacto_", "fr": "Contact_"},
        "back": {"en": "Back", "es": "Volver", "fr": "Retour"},
        "prev": {"en": "Previous", "es": "Anterior", "fr": "Précédent"},
        "next": {"en": "Next", "es": "Siguiente", "fr": "Suivant"},
        "skip": {"en": "Skip to content", "es": "Saltar al contenido", "fr": "Aller au contenu"},
    },
    "section_titles": {
        "digital": {"en": "Multimedia Arts_", "es": "Artes Multimedia_", "fr": "Arts Multimédias_"},
        "product": {"en": "Product Design_", "es": "Diseño de Producto_", "fr": "Design produit_"},
    },
    "tile_tag": {
        "digital": {"en": "Multimedia", "es": "Multimedia", "fr": "Multimédia"},
        "product": {"en": "Product", "es": "Producto", "fr": "Produit"},
    },
    "footer_based": {"en": "Based in France", "es": "Con base en Francia", "fr": "Basée en France"},
    "back_to_top": {"en": "Back to top", "es": "Volver arriba", "fr": "Retour en haut"},
    "contact_form": {
        "title": {"en": "Get in touch_", "es": "Hablemos_", "fr": "Contactez-moi_"},
        "name": {"en": "Name", "es": "Nombre", "fr": "Nom"},
        "email": {"en": "Email", "es": "Correo electrónico", "fr": "E-mail"},
        "message": {"en": "Message", "es": "Mensaje", "fr": "Message"},
        "send": {"en": "Send", "es": "Enviar", "fr": "Envoyer"},
        "note": {
            "en": "This opens your email app with the message ready to send.",
            "es": "Esto abre tu aplicación de correo con el mensaje listo para enviar.",
            "fr": "Cela ouvre votre application e-mail avec le message pr&#234;t &#224; envoyer.",
        },
        "close": {"en": "Close", "es": "Cerrar", "fr": "Fermer"},
    },
    "contact_intro": {
        "en": "Let&#8217;s talk",
        "es": "Hablemos",
        "fr": "Discutons",
    },
    "cta": {
        "heading": {
            "en": "Let&#8217;s create<br>together.",
            "es": "Creemos algo<br>juntos.",
            "fr": "Cr&#233;ons quelque chose<br>ensemble.",
        },
        "button": {"en": "Say hello_", "es": "Escríbeme_", "fr": "Dis bonjour_"},
    },
    "location_tag": {"en": "MARSEILLE, 2026", "es": "MARSELLA, 2026", "fr": "MARSEILLE, 2026"},
    "scroll_cue": {"en": "(scroll)", "es": "(scroll)", "fr": "(scroll)"},
    "hero_visual_label": {"en": "REEL 01", "es": "REEL 01", "fr": "REEL 01"},
    "ticker_tag": {"en": "APPROACH_", "es": "ENFOQUE_", "fr": "APPROCHE_"},
    "ticker_words": {
        "en": ["DIGITAL ART", "PRODUCT DESIGN", "VR / XR", "BLOCKCHAIN", "URBAN INTERVENTION", "PUBLIC SPACE"],
        "es": ["ARTE DIGITAL", "DISEÑO DE PRODUCTO", "VR / XR", "BLOCKCHAIN", "INTERVENCIÓN URBANA", "ESPACIO PÚBLICO"],
        "fr": ["ART NUMÉRIQUE", "DESIGN PRODUIT", "VR / XR", "BLOCKCHAIN", "INTERVENTION URBAINE", "ESPACE PUBLIC"],
    },
    "band_tagline": {
        "digital": {
            "en": "Immersive tech, critical thinking, and hands-on public mediation.",
            "es": "Tecnología inmersiva, pensamiento crítico y mediación práctica con el público.",
            "fr": "Technologies immersives, pensée critique et médiation concrète avec le public.",
        },
        "product": {
            "en": "Reclaiming streets, one modular intervention at a time.",
            "es": "Recuperando las calles, una intervención modular a la vez.",
            "fr": "Reconquérir la rue, une intervention modulaire à la fois.",
        },
    },
    "work_label": {"en": "THE WORK_", "es": "EL TRABAJO_", "fr": "LE TRAVAIL_"},
    "featured_label": {"en": "FEATURED PROJECT_", "es": "PROYECTO DESTACADO_", "fr": "PROJET PHARE_"},
    "get_in_touch": {
        "eyebrow": {"en": "GET IN TOUCH", "es": "CONTACTO", "fr": "ME CONTACTER"},
        "body": {
            "en": "Available for cultural mediation, exhibition design, and public-space projects across Europe and Latin America.",
            "es": "Disponible para mediación cultural, diseño de exposiciones y proyectos de espacio público en Europa y América Latina.",
            "fr": "Disponible pour la médiation culturelle, la scénographie d&#8217;exposition et les projets d&#8217;espace public en Europe et en Amérique latine.",
        },
    },
}

PROJECTS = [
    {
        "slug": "electrocardiogr-ama",
        "category": "digital",
        "year": "2012",
        "title": "Electrocardiogr-ama",
        "subtitle": {"en": "Emotional calendar", "es": "Calendario emocional", "fr": "Calendrier émotionnel"},
        "desc": {
            "en": "An early experiment in emotional data visualization: a personal calendar that translates daily emotional states into a rhythmic, heartbeat-like graphic score, blurring the line between diary and biometric artwork.",
            "es": "Un experimento temprano de visualización de datos emocionales: un calendario personal que traduce los estados de ánimo diarios en una partitura gráfica rítmica, similar a un latido, difuminando la línea entre diario íntimo y obra biométrica.",
            "fr": "Une expérimentation précoce de visualisation de données émotionnelles&nbsp;: un calendrier personnel qui traduit les états d&#8217;âme quotidiens en une partition graphique rythmique, semblable à un battement de cœur, brouillant la frontière entre journal intime et œuvre biométrique.",
        },
    },
    {
        "slug": "moodlog",
        "category": "digital",
        "year": "2013",
        "title": "Moodlog",
        "subtitle": {"en": "Prototype for live events", "es": "Prototipo para eventos en vivo", "fr": "Prototype pour événements live"},
        "desc": {
            "en": "A prototype tool for capturing collective mood in real time during live events, letting audiences log emotional responses as a performance unfolds and turning that data into a shared, evolving visual.",
            "es": "Una herramienta prototipo para capturar el estado de ánimo colectivo en tiempo real durante eventos en vivo, permitiendo al público registrar sus reacciones emocionales mientras se desarrolla una performance, y convirtiendo esos datos en una pieza visual compartida y evolutiva.",
            "fr": "Un outil prototype pour capter l&#8217;humeur collective en temps réel lors d&#8217;événements live, permettant au public d&#8217;enregistrer ses réactions émotionnelles au fil d&#8217;une performance et de transformer ces données en une pièce visuelle partagée et évolutive.",
        },
    },
    {
        "slug": "artbyss",
        "category": "digital",
        "year": "2019",
        "title": "Artbyss",
        "subtitle": {"en": "VR / XR experience", "es": "Experiencia VR / XR", "fr": "Expérience VR / XR"},
        "desc": {
            "en": "An immersive VR/XR experience built on scientific documentation of the deep sea abyss, pairing an original soundscape and visuals with hands-on technical mediation to guide first-time users through headset-based exploration. Awarded at AADN&#8217;s Digital Arts Camp.",
            "es": "Una experiencia inmersiva en VR/XR construida a partir de documentación científica sobre el abismo marino, combinando un paisaje sonoro y visual original con una mediación técnica práctica para guiar a los usuarios primerizos en la exploración con visor. Premiada en el Digital Arts Camp de AADN.",
            "fr": "Une expérience immersive en VR/XR construite à partir de documentation scientifique sur les abysses marins, associant univers sonore et visuel original et médiation technique pour guider les visiteurs novices dans l&#8217;exploration au casque. Lauréate du Digital Arts Camp de l&#8217;AADN.",
        },
    },
    {
        "slug": "dendros",
        "category": "digital",
        "year": "2020",
        "title": "Dendros",
        "subtitle": {"en": "Interactive installation", "es": "Instalación interactiva", "fr": "Installation interactive"},
        "desc": {
            "en": "An audiovisual installation controlled by the public via motion sensors and LED screens, weaving together Latinx folklore, the medicinal uses of the coca leaf, and the industrial process of cocaine production into a single interactive narrative. Presented at the Biennale Internationale Design (Saint-Étienne), Casa Colombia (Paris 2024 Olympics), and Semaine de l&#8217;Amérique Latine (Marseille).",
            "es": "Una instalación audiovisual controlada por el público mediante sensores de movimiento y pantallas LED, que entreteje el folclore latino, los usos medicinales de la hoja de coca y el proceso industrial de fabricación de la cocaína en un único relato interactivo. Presentada en la Biennale Internationale Design (Saint-Étienne), Casa Colombia (Juegos Olímpicos de París 2024) y la Semaine de l&#8217;Amérique Latine (Marsella).",
            "fr": "Une installation audiovisuelle contrôlée par le public via capteurs de mouvement et écrans LED, qui tisse ensemble le folklore latino, les usages médicinaux de la feuille de coca et le processus industriel de fabrication de la cocaïne en un seul récit interactif. Présentée à la Biennale Internationale Design (Saint-Étienne), Casa Colombia (JO de Paris 2024) et la Semaine de l&#8217;Amérique latine (Marseille).",
        },
    },
    {
        "slug": "cryptomurals",
        "category": "digital",
        "year": "2021",
        "title": "Cryptomurals",
        "subtitle": {"en": "Street art archive — heritage preservation via blockchain", "es": "Archivo de arte urbano — preservación patrimonial con blockchain", "fr": "Archive de street art — préservation du patrimoine par blockchain"},
        "desc": {
            "en": "A collaborative archive preserving the heritage of street art and mural painting by minting works on the blockchain, protecting ephemeral urban art from erasure while raising awareness of the links between physical art and digital technology.",
            "es": "Un archivo colaborativo que preserva el patrimonio del arte urbano y los murales mediante su registro en blockchain, protegiendo el arte urbano efímero de la desaparición y sensibilizando sobre los vínculos entre el arte físico y la tecnología digital.",
            "fr": "Une archive collaborative qui préserve le patrimoine de l&#8217;art urbain et des fresques murales en les inscrivant sur la blockchain, protégeant l&#8217;art urbain éphémère de la disparition tout en sensibilisant aux liens entre art physique et technologies numériques.",
        },
    },
    {
        "slug": "ai-facial-recognition",
        "category": "digital",
        "year": "2024",
        "title": {"en": "AI Facial Recognition Installation", "es": "Instalación de Reconocimiento Facial con IA", "fr": "Installation de Reconnaissance Faciale par IA"},
        "subtitle": {"en": "with Women in Web3Privacy", "es": "con Women in Web3Privacy", "fr": "avec Women in Web3Privacy"},
        "desc": {
            "en": "An installation created with Women in Web3Privacy exploring facial recognition AI as both spectacle and warning — letting visitors experience, in real time, how easily their face becomes data, and opening a conversation on digital privacy.",
            "es": "Una instalación creada con Women in Web3Privacy que explora la IA de reconocimiento facial como espectáculo y advertencia a la vez, permitiendo a los visitantes experimentar en tiempo real la facilidad con la que su rostro se convierte en datos, abriendo así una conversación sobre la privacidad digital.",
            "fr": "Une installation réalisée avec Women in Web3Privacy qui explore l&#8217;IA de reconnaissance faciale à la fois comme spectacle et comme avertissement, permettant aux visiteurs de constater en temps réel la facilité avec laquelle leur visage devient donnée, ouvrant ainsi une conversation sur la vie privée numérique.",
        },
    },
    {
        "slug": "bolarbolitos-intervention",
        "category": "product",
        "year": "2012–2014",
        "title": "Bolarbolitos",
        "subtitle": {"en": "Urban intervention — guerrilla gardening (Bogotá)", "es": "Intervención urbana — guerrilla gardening (Bogotá)", "fr": "Intervention urbaine — guerrilla gardening (Bogotá)"},
        "desc": {
            "en": "A guerrilla gardening intervention across Bogotá&#8217;s public space: seed bombs and small-scale plantings deployed in neglected urban corners, reclaiming overlooked sites for greenery and community care.",
            "es": "Una intervención de guerrilla gardening en el espacio público de Bogotá: bombas de semillas y plantaciones a pequeña escala desplegadas en rincones urbanos abandonados, recuperando lugares olvidados para el verde y el cuidado comunitario.",
            "fr": "Une intervention de guerrilla gardening dans l&#8217;espace public de Bogotá&nbsp;: bombes de graines et plantations à petite échelle déployées dans des recoins urbains délaissés, pour reconquérir des lieux oubliés au profit du végétal et du soin collectif.",
        },
    },
    {
        "slug": "bolarbolitos-plant-pot",
        "category": "product",
        "year": "2013",
        "title": {"en": "Bolarbolitos Plant Pot", "es": "Maceta Bolarbolitos", "fr": "Pot Bolarbolitos"},
        "subtitle": {"en": "Plant pot for urban space", "es": "Maceta para el espacio urbano", "fr": "Pot pour l&#8217;espace urbain"},
        "desc": {
            "en": "A modular planter designed as an extension of the Bolarbolitos intervention, conceived to be produced cheaply and installed on sidewalks, ledges, and other in-between urban spaces to bring greenery into daily city life.",
            "es": "Una maceta modular diseñada como extensión de la intervención Bolarbolitos, pensada para producirse a bajo costo e instalarse en aceras, repisas y otros espacios urbanos intermedios, llevando el verde a la vida cotidiana de la ciudad.",
            "fr": "Un pot modulaire conçu comme prolongement de l&#8217;intervention Bolarbolitos, pensé pour être produit à faible coût et installé sur les trottoirs, rebords et autres espaces urbains interstitiels, afin d&#8217;apporter du végétal dans le quotidien de la ville.",
        },
    },
    {
        "slug": "biked",
        "category": "product",
        "year": "2022",
        "title": "Biked",
        "subtitle": {"en": "Modular bike parking lots", "es": "Estacionamientos modulares para bicicletas", "fr": "Places de stationnement vélo modulaires"},
        "desc": {
            "en": "A modular bike-parking system designed to convert underused street space into flexible, scalable parking lots — encouraging cycling as everyday urban mobility.",
            "es": "Un sistema modular de estacionamiento para bicicletas diseñado para convertir espacios de calle subutilizados en zonas de aparcamiento flexibles y escalables, fomentando el uso de la bicicleta como movilidad urbana cotidiana.",
            "fr": "Un système modulaire de stationnement pour vélos conçu pour transformer des espaces de rue sous-utilisés en zones de stationnement flexibles et évolutives, encourageant le vélo comme mobilité urbaine du quotidien.",
        },
    },
    {
        "slug": "e-biked",
        "category": "product",
        "year": "2023",
        "title": "E-Biked",
        "subtitle": {"en": "Solar-powered parking for electric bikes", "es": "Estacionamiento solar para bicicletas eléctricas", "fr": "Stationnement solaire pour vélos électriques"},
        "desc": {
            "en": "An evolution of Biked for electric bikes: modular parking lots fitted with solar panels that charge bikes on-site, pairing sustainable mobility with off-grid energy.",
            "es": "Una evolución de Biked para bicicletas eléctricas: estacionamientos modulares equipados con paneles solares que cargan las bicicletas in situ, combinando movilidad sostenible con energía fuera de la red.",
            "fr": "Une évolution de Biked pour les vélos électriques&nbsp;: des places de stationnement modulaires équipées de panneaux solaires qui rechargent les vélos sur place, alliant mobilité durable et énergie hors réseau.",
        },
    },
    {
        "slug": "rituals",
        "category": "digital",
        "year": "2022",
        "title": "Rituals",
        "subtitle": {
            "en": "NFT exhibition — art curation at DEVCON VI (Bogotá)",
            "es": "Exposición NFT — curaduría de arte en DEVCON VI (Bogotá)",
            "fr": "Exposition NFT — commissariat d&#8217;art à DEVCON VI (Bogotá)",
        },
        "desc": {
            "en": "Curated Rituals, an exhibition of NFT and electronic art featuring live-coding performances at DEVCON VI in Bogotá — welcoming an international audience and translating Web3 concepts into an accessible narrative for newcomers and collectors alike.",
            "es": "Curaduría de Rituals, una exposición de arte NFT y electrónico con performances de livecoding en DEVCON VI en Bogotá, recibiendo a un público internacional y traduciendo los conceptos de Web3 en un relato accesible tanto para principiantes como para coleccionistas.",
            "fr": "Commissariat de Rituals, une exposition d&#8217;art NFT et électronique avec des performances de livecoding à DEVCON VI à Bogotá, accueillant un public international et traduisant les concepts Web3 en un récit accessible aussi bien aux néophytes qu&#8217;aux collectionneurs.",
        },
    },
    {
        "slug": "villanova",
        "category": "product",
        "year": "2026",
        "title": "VillaNova",
        "subtitle": {
            "en": "Interactive assistant for events in the fictional city of VillaNova",
            "es": "Asistente interactivo para eventos en la ciudad ficticia de VillaNova",
            "fr": "Assistant interactif pour événements dans la ville fictive de VillaNova",
        },
        "desc": {
            "en": "A voice and chat assistant built for VillaNova, a fictional city imagined as an immersive event experience — guiding attendees through the program, answering questions in real time, and blending conversational AI with world-building.",
            "es": "Un asistente de voz y chat creado para VillaNova, una ciudad ficticia imaginada como experiencia inmersiva de eventos, que guía a los asistentes durante el programa, responde preguntas en tiempo real y combina IA conversacional con construcción de mundos.",
            "fr": "Un assistant vocal et conversationnel conçu pour VillaNova, une ville fictive imaginée comme une expérience d&#8217;événement immersive, qui guide les participants tout au long du programme, répond aux questions en temps réel et associe IA conversationnelle et world-building.",
        },
    },
]

def t(field, lang):
    if isinstance(field, dict):
        return field.get(lang, field.get("en", ""))
    return field

CONTACT = {
    "location": "Marseille, France",
    "phone": "+33 7 84 33 69 79",
    "email": "ngiraldo@proton.me",
    "linkedin_label": "linkedin.com/nagiraldoa",
    "linkedin_url": "https://linkedin.com/in/nagiraldoa",
}

# ---------- Color system (WCAG-checked) ----------
# ink/paper 19.7:1 · muted/paper 8.8:1 (AAA) · accent-ink/paper 6.5:1 (AA/AAA small text)
# accent/paper 3.1:1 (large text/graphics only, per WCAG 1.4.11 non-text contrast)
# dark-ink/dark-bg 17.9:1 · accent/dark-bg 6.3:1 · dark-muted/dark-bg 7.9:1

DIGITAL_DUO = ("#150C2E", "#6C4DFF")   # deep indigo -> violet
PRODUCT_DUO = ("#241207", "#F2A65A")   # deep umber -> warm sand

def shift_hue(hex_color, degrees):
    hex_color = hex_color.lstrip("#")
    r, g, b = [int(hex_color[i:i+2], 16) / 255 for i in (0, 2, 4)]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h = (h + degrees / 360.0) % 1.0
    r2, g2, b2 = colorsys.hls_to_rgb(h, l, s)
    return "#%02x%02x%02x" % (round(r2 * 255), round(g2 * 255), round(b2 * 255))

def project_duo(category, local_index):
    base = DIGITAL_DUO if category == "digital" else PRODUCT_DUO
    step = 9 if category == "digital" else 11
    start, end = base
    return start, shift_hue(end, local_index * step)

def make_cover_svg(start, end, seed):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" role="img" aria-hidden="true" focusable="false">
  <defs>
    <linearGradient id="g{seed}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{start}"/>
      <stop offset="100%" stop-color="{end}"/>
    </linearGradient>
    <filter id="n{seed}">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch" result="noise"/>
      <feColorMatrix in="noise" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.06 0"/>
    </filter>
  </defs>
  <rect width="1200" height="900" fill="url(#g{seed})"/>
  <rect width="1200" height="900" filter="url(#n{seed})"/>
</svg>"""

def make_hero_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 900" role="img" aria-hidden="true" focusable="false">
  <defs>
    <radialGradient id="hg" cx="35%" cy="30%" r="75%">
      <stop offset="0%" stop-color="#d4ff8a"/>
      <stop offset="45%" stop-color="#8cff00"/>
      <stop offset="100%" stop-color="#0b0b0c"/>
    </radialGradient>
    <filter id="hn">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" result="noise"/>
      <feColorMatrix in="noise" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.07 0"/>
    </filter>
  </defs>
  <rect width="900" height="900" fill="#0b0b0c"/>
  <circle cx="420" cy="360" r="360" fill="url(#hg)"/>
  <rect width="900" height="900" filter="url(#hn)"/>
</svg>"""

def build_covers():
    covers = {}
    counters = {"digital": 0, "product": 0}
    for p in PROJECTS:
        cat = p["category"]
        local_idx = counters[cat]
        counters[cat] += 1
        start, end = project_duo(cat, local_idx)
        covers[p["slug"]] = make_cover_svg(start, end, p["slug"].replace("-", ""))
    return covers

# ---------- CSS ----------
CSS = """
:root {
  --ink: #0b0b0c;
  --paper: #f2f1ee;       /* light gray page background — 17.4:1 with --ink */
  --muted: #4d4a45;
  --line: #8cff00;
  --accent: #8cff00;      /* large graphics / fills / dark-bg text only — 1.3:1 on white, 15.4:1 on dark-bg */
  --accent-ink: #2a5c00;  /* small text / links on light gray — 7.1:1 (AAA) */
  --on-accent: #0b0b0c;   /* fixed text color for content sitting on a bright accent fill, in either theme */
  --panel: #e9e7e2;
  --header-bg: rgba(255,255,255,0.05);
  --dark-bg: #0b0b0c;
  --dark-ink: #f5f4f1;
  --dark-muted: #a8a49c;  /* 7.9:1 on dark-bg */

  --font-display: "Space Grotesk", -apple-system, "Helvetica Neue", Arial, sans-serif;
  --font-body: "Inter", -apple-system, "Helvetica Neue", Arial, sans-serif;
  --font-pixel: "Silkscreen", "Space Grotesk", monospace;
  --font-script: "Instrument Serif", Georgia, serif;
}

/* Dark mode — remapped for best contrast (checked against WCAG AA/AAA) */
:root[data-theme="dark"] {
  --ink: #f5f4f1;         /* 17.9:1 on dark paper */
  --paper: #0b0b0c;
  --muted: #a8a49c;       /* 7.9:1 on dark paper */
  --line: #8cff00;
  --accent-ink: #8cff00;  /* 15.4:1 on dark paper */
  --panel: #151517;
  --header-bg: rgba(0,0,0,0.1);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  * { transition: none !important; animation: none !important; }
}
body {
  margin: 0;
  font-family: var(--font-body);
  color: var(--ink);
  background: var(--paper);
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}
a { color: inherit; text-decoration: none; }
img { max-width: 100%; display: block; }
.wrap { max-width: 1080px; margin: 0 auto; padding: 0 48px; }

.skip-link {
  position: absolute; left: -9999px; top: 0; z-index: 100;
  background: var(--ink); color: var(--paper); padding: 12px 18px; font-weight: 600; font-size: 14px;
}
.skip-link:focus { left: 16px; top: 16px; }

:focus-visible { outline: 2px solid var(--accent-ink); outline-offset: 3px; }

header.site {
  border: none;
  position: sticky; top: 0; background: var(--header-bg);
  backdrop-filter: blur(8px);
  z-index: 20;
  transition: background .2s ease;
}
.header-inner {
  display: flex; align-items: center; justify-content: space-between;
  padding: 20px 0;
  flex-wrap: wrap; gap: 12px;
}
.header-brand { display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap; }
.logo { font-family: var(--font-display); font-size: clamp(40px, 5vw, 120px); font-weight: 700; letter-spacing: -0.02em; }
.logo span { color: var(--accent); }
.header-subtitle { font-family: var(--font-display); font-size: 30px; font-weight: 400; letter-spacing: 0.02em; text-transform: uppercase; color: var(--accent); padding: 2px 10px; }
:root:not([data-theme="dark"]) .header-subtitle { background: #000; }
nav.main { display: flex; gap: 24px; align-items: center; flex-wrap: wrap; }
nav.main a.js-contact-trigger { display: none; }
nav.main a { font-size: 13.5px; font-weight: 600; color: var(--ink); opacity: 0.78; border-bottom: 2px solid transparent; padding-bottom: 3px; transition: border-color .15s ease, opacity .15s ease, color .15s ease; }
nav.main a:hover, nav.main a:focus-visible { opacity: 1; color: var(--accent-ink); border-bottom-color: var(--accent); }
.lang-dropdown { position: relative; margin-left: 4px; }
.lang-toggle {
  display: flex; align-items: center; gap: 7px; background: none; cursor: pointer;
  border: none; border-bottom: 2px solid transparent; border-radius: 0; padding: 7px 2px;
  font-family: var(--font-body); font-size: 12px; font-weight: 700; color: var(--ink);
  transition: border-color .15s ease, color .15s ease;
}
.lang-toggle:hover, .lang-toggle:focus-visible { color: var(--accent); border-bottom-color: var(--accent); }
.lang-dropdown.is-open .lang-toggle { color: var(--accent); border-bottom-color: var(--accent); }

.theme-toggle {
  display: flex; align-items: center; justify-content: center;
  background: none; border: none; cursor: pointer; padding: 6px; color: var(--ink);
  transition: color .15s ease;
}
.theme-toggle:hover, .theme-toggle:focus-visible { color: var(--accent-ink); }
.theme-toggle .icon-sun, .theme-toggle .icon-moon { display: none; }
:root:not([data-theme="dark"]) .theme-toggle .icon-moon { display: block; }
:root[data-theme="dark"] .theme-toggle .icon-sun { display: block; }

@media (max-width: 1024px) {
  .logo { font-size: clamp(32px, 7.5vw, 110px); }
}
@media (max-width: 760px) {
  .header-inner { position: relative; flex-wrap: wrap; min-height: 70px; }
  .header-brand { max-width: calc(100% - 70px); }
  nav.main {
    position: absolute; top: 50%; right: 0; transform: translateY(-50%);
    flex-direction: column; align-items: flex-end; gap: 8px;
  }
  .logo { font-size: clamp(24px, 12vw, 90px); }
}
@media (max-width: 480px) {
  .header-subtitle { font-size: 14px; padding: 2px 6px; }
}
.lang-menu {
  position: absolute; top: calc(100% + 8px); right: 0; min-width: 130px;
  background: transparent; border: none; box-shadow: none;
  padding: 4px 0; display: none; z-index: 30;
}
.lang-dropdown.is-open .lang-menu { display: block; }
.lang-menu a {
  display: block; padding: 7px 2px; font-size: 13px; font-weight: 600; color: var(--ink);
  border-bottom: 2px solid transparent; transition: border-color .15s ease, color .15s ease;
}
.lang-menu a:hover, .lang-menu a:focus-visible { color: var(--accent); border-bottom-color: var(--accent); }
.lang-menu a.active { color: var(--accent); border-bottom-color: var(--accent); }

.location-tag { position: absolute; top: 22px; right: 28px; font-family: var(--font-pixel); font-size: 11px; letter-spacing: 0.06em; color: var(--muted); }

.hero { padding: 84px 0 0; position: relative; }
.hero-grid { display: grid; grid-template-columns: minmax(0, 1.3fr) minmax(0, 1fr); gap: 32px; align-items: center; }
.hero .kicker { font-family: var(--font-pixel); font-size: 12px; font-weight: 400; text-transform: uppercase; letter-spacing: 0.1em; color: var(--accent-ink); margin-bottom: 18px; }
.hero h1 {
  font-family: var(--font-display); font-weight: 700;
  font-size: clamp(40px, 5vw, 120px); line-height: 1; letter-spacing: -0.03em;
  margin: 0 0 26px; max-width: 20ch; position: relative; display: inline-block;
  overflow-wrap: break-word; word-break: break-word;
}
.hero h1 .glitch-a, .hero h1 .glitch-b { position: absolute; inset: 0; opacity: 0; }
.hero h1:hover .glitch-a { opacity: 0.7; color: var(--accent); transform: translate(2px,-2px); mix-blend-mode: multiply; }
.hero h1:hover .glitch-b { opacity: 0.7; color: #2b6cff; transform: translate(-2px,2px); mix-blend-mode: multiply; }
.hero p.lede { font-size: clamp(16px, 1.6vw, 19px); color: var(--muted); max-width: 56ch; margin: 0 0 40px; line-height: 1.7; }

.hero-visual { position: relative; aspect-ratio: 1/1; border-radius: 0; overflow: hidden; transform-style: preserve-3d; min-width: 0; }
.hero-visual img { width: 100%; height: 100%; object-fit: cover; display: block; transition: transform .2s ease-out; }
.hero-visual .hv-label { position: absolute; top: 18px; right: 18px; font-family: var(--font-body); font-size: 13px; color: var(--dark-ink); text-align: right; line-height: 1.4; }
.hero-visual .hv-scroll { position: absolute; left: 18px; bottom: 16px; font-family: var(--font-pixel); font-size: 15px; color: var(--accent); }

@media (min-width: 1025px) {
  .hero.wrap, .header-inner.wrap, .footer-inner.wrap { max-width: none; padding-left: 24px; padding-right: 24px; }
}
@media (max-width: 1024px) {
  .hero h1 { font-size: clamp(32px, 7.5vw, 110px); }
  .hero-text { margin-left: 20px; }
}
@media (max-width: 760px) {
  .hero-grid { grid-template-columns: 1fr; }
  .hero-visual { aspect-ratio: 16/11; margin-top: 8px; }
  .hero h1 { font-size: clamp(24px, 12vw, 90px); }
}

/* full-bleed category bands — transparent by default, green glow + fill on hover */
.band-stack { border-top: 1px solid var(--line); margin-top: 56px; }
.band {
  border-bottom: 1px solid var(--line); overflow: hidden; position: relative;
  background: transparent; color: var(--ink);
}
.band::before {
  content: ""; position: absolute; inset: -20%;
  background: radial-gradient(circle 260px at var(--mx, 50%) var(--my, 50%), rgba(140,255,0,0.55), rgba(140,255,0,0) 70%);
  opacity: 0; transition: opacity .25s ease; pointer-events: none;
}
.band::after {
  content: ""; position: absolute; inset: 0; background: var(--accent);
  opacity: 0; transition: opacity .3s ease; z-index: 0;
}
.band:hover::before, .band:focus-within::before { opacity: 1; }
.band:hover::after, .band:focus-within::after { opacity: 1; }
.band:hover, .band:focus-within { color: var(--on-accent); }
.band a.band-link { position: relative; z-index: 1; display: flex; align-items: center; justify-content: space-between; gap: 24px; padding: 30px 28px; flex-wrap: wrap; }
@media (max-width: 1024px) {
  .band a.band-link { padding-left: 48px; padding-right: 48px; }
  .band .band-note { text-align: right; margin-left: auto; }
}
.band h2 { font-family: var(--font-display); font-weight: 700; font-size: clamp(34px, 6.5vw, 74px); letter-spacing: -0.03em; margin: 0; }
.band .band-note { font-family: var(--font-body); font-size: 14px; max-width: 30ch; text-align: right; opacity: 0; transform: translateY(4px); transition: opacity .25s ease, transform .25s ease; }
.band:hover .band-note, .band:focus-within .band-note { opacity: 1; transform: translateY(0); }

/* sticky-tag ticker */
.ticker-band { display: flex; align-items: stretch; background: var(--dark-bg); color: var(--dark-ink); overflow: hidden; position: relative; }
.ticker-band::before {
  content: ""; position: absolute; inset: -20%;
  background: radial-gradient(circle 280px at var(--mx, 50%) var(--my, 50%), rgba(140,255,0,0.4), rgba(140,255,0,0) 70%);
  opacity: 0; transition: opacity .25s ease; pointer-events: none; z-index: 0;
}
.ticker-band:hover::before, .ticker-band:focus-within::before { opacity: 1; }
.ticker-tag { position: relative; z-index: 1; flex: 0 0 auto; background: var(--dark-ink); color: var(--dark-bg); font-family: var(--font-pixel); font-size: 13px; letter-spacing: 0.06em; padding: 18px 22px; display: flex; align-items: center; transition: background .2s ease, color .2s ease; }
.ticker-band:hover .ticker-tag, .ticker-band:focus-within .ticker-tag { background: var(--accent); }
.marquee { position: relative; z-index: 1; flex: 1; overflow: hidden; white-space: nowrap; display: flex; align-items: center; }
.ticker-band:hover .marquee-track, .ticker-band:focus-within .marquee-track { animation-play-state: paused; }
.marquee-track { display: inline-flex; animation: marquee 26s linear infinite; }
.marquee-set { padding-right: 40px; font-family: var(--font-display); font-weight: 600; font-size: 15px; letter-spacing: 0.02em; }
.marquee-set .sep { color: var(--accent); padding: 0 14px; }
@keyframes marquee { from { transform: translateX(0); } to { transform: translateX(-50%); } }
@media (prefers-reduced-motion: reduce) { .marquee-track { animation: none; } }

/* work index grid */
section.work-index { background: var(--dark-bg); color: var(--dark-ink); padding: 64px 0 72px; }
section.work-index .work-label { font-family: var(--font-pixel); font-size: 13px; letter-spacing: 0.08em; color: var(--dark-muted); margin-bottom: 28px; }
.work-grid { display: grid; grid-template-columns: repeat(5, 1fr); border-top: 1px solid rgba(140,255,0,0.15); border-left: 1px solid rgba(140,255,0,0.15); }
.work-tile { border-right: 1px solid rgba(140,255,0,0.15); border-bottom: 1px solid rgba(140,255,0,0.15); aspect-ratio: 1/1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; gap: 6px; padding: 12px; transition: background .15s ease, color .15s ease; }
.work-tile .num { font-family: var(--font-display); font-weight: 700; font-size: clamp(24px,2.8vw,36px); }
.work-tile .name { font-family: var(--font-body); font-size: 12px; opacity: 0.75; }
.work-tile:hover, .work-tile:focus-visible { background: var(--accent); color: var(--on-accent); }
.work-tile .tile-tag-default {
  display: block; font-family: var(--font-pixel); font-size: 10px; letter-spacing: 0.08em;
  color: var(--dark-muted); text-transform: uppercase; margin-top: 6px; transition: opacity .2s ease;
}
.work-tile:hover .tile-tag-default, .work-tile:focus-visible .tile-tag-default { opacity: 0; }
.work-tile .tile-reveal { max-height: 0; opacity: 0; overflow: hidden; transition: max-height .25s ease, opacity .2s ease, margin-top .25s ease; margin-top: 0; }
.work-tile:hover .tile-reveal, .work-tile:focus-visible .tile-reveal { max-height: 90px; opacity: 1; margin-top: 6px; }
.tile-reveal .tile-desc { display: block; font-size: 11.5px; line-height: 1.4; opacity: 0.85; max-width: 22ch; margin: 0 auto; }
@media (max-width: 900px) { .work-grid { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 560px) { .work-grid { grid-template-columns: repeat(2, 1fr); } }

/* spotlight panel */
section.spotlight { padding: 0; }
.spotlight a.spotlight-link { display: grid; grid-template-columns: 1fr 1fr; min-height: 420px; }
.spotlight .sp-text { display: flex; flex-direction: column; justify-content: center; padding: 48px; background: var(--panel); }
.spotlight .sp-eyebrow { font-family: var(--font-display); font-weight: 700; font-size: 12px; color: var(--accent); letter-spacing: 0.06em; margin-bottom: 18px; display: inline-block; padding: 2px 10px; }
:root:not([data-theme="dark"]) .spotlight .sp-eyebrow { background: #000; }
.spotlight .sp-title { font-family: var(--font-script); font-style: italic; font-size: clamp(40px, 6vw, 72px); margin: 0 0 14px; }
.spotlight .sp-desc { font-size: 15px; color: var(--muted); max-width: 42ch; }
.spotlight .sp-visual { position: relative; overflow: hidden; }
.spotlight .sp-visual img { width: 100%; height: 100%; object-fit: cover; }
@media (max-width: 760px) { .spotlight a.spotlight-link { grid-template-columns: 1fr; } .spotlight .sp-visual { min-height: 260px; } }

section.projects { padding: 52px 0 12px; border-top: 1px solid var(--line); }
section.projects h2 { font-family: var(--font-display); font-weight: 700; font-size: clamp(26px, 3.4vw, 38px); margin: 0 0 32px; letter-spacing: -0.02em; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 28px; margin-bottom: 60px; }

.card { display: block; border: 1px solid var(--line); border-radius: 0; overflow: hidden; transition: transform .15s ease, box-shadow .15s ease; background: var(--paper); }
.card:hover, .card:focus-visible { transform: translateY(-3px); box-shadow: 0 12px 28px rgba(0,0,0,0.08); }

.cover { aspect-ratio: 4 / 3; position: relative; overflow: hidden; background: var(--panel); border-radius: 0; }
.cover img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.cover::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0) 45%, rgba(0,0,0,0.55) 100%); }
.cover .idx { position: absolute; top: 14px; right: 16px; font-family: var(--font-display); font-size: 12px; font-weight: 700; color: rgba(255,255,255,0.9); z-index: 2; }
.cover .glyph { position: absolute; left: 16px; bottom: 14px; font-family: var(--font-display); font-size: 14px; font-weight: 700; color: rgba(255,255,255,0.96); letter-spacing: 0.02em; z-index: 2; }

.card-body { padding: 18px 18px 22px; }
.card-body .cat { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--accent-ink); margin-bottom: 7px; }
.card-body h3 { font-family: var(--font-display); font-weight: 600; font-size: 18px; margin: 0 0 4px; letter-spacing: -0.01em; }
.card-body .sub { font-size: 13.5px; color: var(--muted); margin: 0 0 10px; }
.card-body .year { font-size: 12px; color: var(--muted); font-weight: 500; }

/* dark CTA band */
section.cta-band { background: var(--dark-bg); color: var(--dark-ink); padding: 96px 0; margin-top: 24px; }
section.cta-band h2 {
  font-family: var(--font-display); font-weight: 700; text-transform: uppercase;
  font-size: clamp(36px, 7vw, 84px); line-height: 0.98; letter-spacing: -0.03em; margin: 0 0 36px;
}
.cta-btn {
  display: inline-flex; align-items: center; gap: 10px;
  background: var(--dark-ink); color: var(--dark-bg); border: none; cursor: pointer;
  font-family: var(--font-display); font-weight: 700; font-size: 15px;
  padding: 16px 30px; border-radius: 999px;
}
.cta-btn:hover, .cta-btn:focus-visible { background: var(--accent); color: var(--dark-bg); }

footer.site { border: none; background: #000; }
.footer-inner { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; padding-top: 0; padding-bottom: 0; text-align: left; }
.social-links { display: flex; gap: 18px; align-items: center; }
.social-links a { color: var(--dark-muted); transition: color .15s ease; }
.social-links a:hover, .social-links a:focus-visible { color: var(--accent); }
.back-to-top { display: inline-flex; align-items: center; justify-content: center; color: var(--accent); background: none; border: none; cursor: pointer; padding: 8px; transition: transform .15s ease; }
.back-to-top:hover, .back-to-top:focus-visible { transform: translateY(-4px); }
.copyright { font-size: 12px; color: var(--dark-muted); padding: 18px 0 0; text-align: center; border-top: 1px solid var(--line); }

/* contact modal */
.modal-overlay {
  position: fixed; inset: 0; background: rgba(11,11,12,0.72);
  display: flex; align-items: center; justify-content: center; padding: 20px;
  z-index: 100; opacity: 0; pointer-events: none; transition: opacity .2s ease;
}
.modal-overlay.is-open { opacity: 1; pointer-events: auto; }
.modal-box {
  background: var(--paper); border-radius: 16px; padding: 40px; max-width: 440px; width: 100%;
  position: relative; transform: translateY(14px); transition: transform .2s ease;
}
.modal-overlay.is-open .modal-box { transform: translateY(0); }
.modal-close {
  position: absolute; top: 14px; right: 16px; font-size: 24px; line-height: 1;
  background: none; border: none; cursor: pointer; color: var(--muted); padding: 6px;
}
.modal-box h3 { font-family: var(--font-display); font-weight: 700; font-size: 26px; margin: 0 0 22px; letter-spacing: -0.01em; }
#contact-form label { display: block; font-size: 13px; font-weight: 600; margin-bottom: 16px; }
#contact-form input, #contact-form textarea {
  display: block; width: 100%; margin-top: 6px; padding: 11px 2px;
  border: none; border-bottom: 2px solid var(--line); border-radius: 0;
  font-family: var(--font-body); font-size: 14px; color: var(--ink); background: transparent;
  transition: border-color .15s ease;
}
#contact-form input:hover, #contact-form textarea:hover { border-color: var(--accent-ink); }
#contact-form input:focus, #contact-form textarea:focus {
  outline: none; border-color: var(--accent);
  animation: form-underscore-blink 1s step-end infinite;
}
@keyframes form-underscore-blink { 50% { border-color: var(--line); } }
#contact-form textarea { resize: vertical; }
.modal-note { font-size: 12px; color: var(--muted); margin: 2px 0 20px; }
.modal-close:hover, .modal-close:focus-visible { color: var(--accent-ink); }
.cta-btn2 {
  display: block; width: 100%; text-align: center; border: none; cursor: pointer;
  background: var(--ink); color: var(--paper); transition: background .15s ease, color .15s ease;
  font-family: var(--font-display); font-weight: 700; font-size: 15px;
  padding: 14px 24px; border-radius: 999px;
}
.cta-btn2:hover, .cta-btn2:focus-visible { background: var(--accent); color: var(--on-accent); }

/* project page */
.project-hero { padding: 44px 0 0; }
.back-link { display: inline-block; font-size: 13px; font-weight: 700; color: var(--muted); margin-bottom: 24px; }
.back-link:hover, .back-link:focus-visible { color: var(--accent); }
.project-cover { border-radius: 0; aspect-ratio: 16/7; position: relative; overflow: hidden; margin-bottom: 36px; background: var(--panel); }
.project-cover img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.project-cover::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(0,0,0,0.55) 100%); }
.project-cover .glyph-lg { position: absolute; left: 28px; bottom: 24px; font-family: var(--font-display); font-size: clamp(18px,2.4vw,24px); font-weight: 700; color: rgba(255,255,255,0.96); z-index: 2; }
.project-meta { display: flex; gap: 10px; align-items: center; margin-bottom: 12px; }
.tag { font-size: 11.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--accent); }
.dot { width: 3px; height: 3px; border-radius: 50%; background: var(--muted); }
.project-body h1 { font-family: var(--font-display); font-weight: 700; font-size: clamp(32px, 5.5vw, 64px); margin: 0 0 8px; letter-spacing: -0.03em; line-height: 1.02; }
.project-body .sub { font-size: 17px; color: var(--muted); margin: 0 0 30px; }
.project-body p.desc { font-size: clamp(16px,1.6vw,18px); max-width: 66ch; margin: 0 0 44px; line-height: 1.75; }
.project-nav { border-top: 1px solid var(--line); padding: 28px 0 60px; display: flex; justify-content: space-between; gap: 20px; flex-wrap: wrap; }
.project-nav .nav-item .eyebrow { display: block; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); margin-bottom: 4px; }
.project-nav .nav-item.next { text-align: right; margin-left: auto; }
.project-nav a.nav-item { font-family: var(--font-display); font-size: 17px; font-weight: 600; }
.project-nav a.nav-item:hover, .project-nav a.nav-item:focus-visible { color: var(--accent); }

@media (max-width: 1024px) {
  .project-body { margin-left: 20px; }
  .project-nav { margin-left: 20px; margin-right: 20px; }
}
@media (max-width: 640px) {
  .project-nav .nav-item.next { text-align: left; margin-left: 0; }
}
"""

FONT_LINKS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&family=Silkscreen:wght@400;700&family=Instrument+Serif:ital@1&display=swap" rel="stylesheet">"""

def cover_html(slug, category, label_text, alt_text, size="sm", covers_prefix="", loading="lazy"):
    if size == "sm":
        return (
            f'<div class="cover">'
            f'<img src="{covers_prefix}covers/{slug}.svg" alt="" loading="{loading}" decoding="async" width="640" height="480">'
            f'<span class="idx">{label_text}</span>'
            f'<span class="glyph">{category.upper()}</span>'
            f'</div>'
        )
    return (
        f'<div class="project-cover">'
        f'<img src="{covers_prefix}covers/{slug}.svg" alt="{alt_text}" loading="{loading}" decoding="async" fetchpriority="high" width="1280" height="560">'
        f'<span class="glyph-lg">{category.upper()} — {label_text}</span>'
        f'</div>'
    )

THEME_INIT_SCRIPT = """<script>
(function(){
  try {
    var saved = localStorage.getItem('ng-theme');
    var theme = saved || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    if (theme === 'dark') document.documentElement.setAttribute('data-theme', 'dark');
  } catch (e) {}
})();
</script>"""

def head(title, lang, depth):
    css_path = "../" * depth + "assets/style.css"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
{THEME_INIT_SCRIPT}
{FONT_LINKS}
<link rel="stylesheet" href="{css_path}">
</head>
<body>
<a class="skip-link" href="#content">{t(SITE['nav']['skip'], lang)}</a>
"""

GLOBE_ICON = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 3 2.5 15 0 18M12 3c-2.5 3-2.5 15 0 18"/></svg>'

def lang_switch(current_lang, target_kind, target_slug=None):
    items = []
    for l in LANGS:
        if target_kind == "home":
            href = f"../{l}/index.html"
        else:
            href = f"../../{l}/projects/{target_slug}.html"
        cls = "active" if l == current_lang else ""
        aria = ' aria-current="page"' if l == current_lang else ""
        items.append(f'<a class="{cls}" href="{href}" lang="{l}" hreflang="{l}"{aria} role="menuitem">{LANG_NAME[l]}</a>')
    return f"""<div class="lang-dropdown">
  <button type="button" class="lang-toggle" aria-haspopup="true" aria-expanded="false" aria-label="Language">
    {GLOBE_ICON}<span class="lang-current">{LANG_LABEL[current_lang]}</span>
  </button>
  <div class="lang-menu" role="menu">{''.join(items)}</div>
</div>"""

def site_header(lang, kind, slug=None):
    home_href = "index.html" if kind == "home" else f"../../{lang}/index.html"
    ls = lang_switch(lang, kind, slug)
    return f"""<header class="site">
  <div class="wrap header-inner">
    <div class="header-brand">
      <a class="logo" href="{home_href}">NG<span>_</span></a>
      <span class="header-subtitle">{SITE['name']}</span>
    </div>
    <nav class="main" aria-label="Main">
      <a href="#" class="js-contact-trigger">{t(SITE['nav']['contact'], lang)}</a>
      <button type="button" class="theme-toggle" aria-label="Toggle dark mode">
        <svg class="icon-sun" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2.5M12 19.5V22M4.2 4.2l1.8 1.8M18 18l1.8 1.8M2 12h2.5M19.5 12H22M4.2 19.8l1.8-1.8M18 6l1.8-1.8"/></svg>
        <svg class="icon-moon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3 7 7 0 0 0 21 12.8Z"/></svg>
      </button>
      {ls}
    </nav>
  </div>
</header>
<script>
(function(){{
  document.querySelectorAll('.lang-dropdown').forEach(function(dd){{
    var toggle = dd.querySelector('.lang-toggle');
    toggle.addEventListener('click', function(e){{
      e.stopPropagation();
      var open = dd.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    }});
  }});
  document.addEventListener('click', function(){{
    document.querySelectorAll('.lang-dropdown.is-open').forEach(function(dd){{
      dd.classList.remove('is-open');
      dd.querySelector('.lang-toggle').setAttribute('aria-expanded', 'false');
    }});
  }});
  document.addEventListener('keydown', function(e){{
    if (e.key === 'Escape') {{
      document.querySelectorAll('.lang-dropdown.is-open').forEach(function(dd){{ dd.classList.remove('is-open'); }});
    }}
  }});
  document.querySelectorAll('.theme-toggle').forEach(function(btn){{
    btn.addEventListener('click', function(){{
      var isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      var next = isDark ? 'light' : 'dark';
      if (next === 'dark') {{
        document.documentElement.setAttribute('data-theme', 'dark');
      }} else {{
        document.documentElement.removeAttribute('data-theme');
      }}
      try {{ localStorage.setItem('ng-theme', next); }} catch (e) {{}}
    }});
  }});
}})();
</script>
"""

def cta_band(lang):
    return f"""<section class="cta-band">
  <div class="wrap">
    <h2>{t(SITE['cta']['heading'], lang)}</h2>
    <button type="button" class="cta-btn js-contact-trigger">{t(SITE['cta']['button'], lang)} &#8594;</button>
  </div>
</section>
"""

SOCIAL_ICONS = {
    "instagram": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="0.6" fill="currentColor" stroke="none"/></svg>',
    "x": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg>',
    "linkedin": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><line x1="7.5" y1="10" x2="7.5" y2="16.5"/><circle cx="7.5" cy="7" r="0.6" fill="currentColor" stroke="none"/><path d="M11.5 16.5v-4a2.2 2.2 0 0 1 4.4 0v4"/><line x1="11.5" y1="10" x2="11.5" y2="16.5"/></svg>',
}

def site_footer(lang):
    socials = "".join(
        f'<a href="#" aria-label="{name.capitalize()}">{svg}</a>'
        for name, svg in SOCIAL_ICONS.items()
    )
    return f"""<footer class="site">
  <div class="wrap footer-inner">
    <div class="social-links">{socials}</div>
    <button type="button" class="back-to-top js-back-to-top" aria-label="{t(SITE['back_to_top'], lang)}">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
    </button>
  </div>
  <div class="copyright">&copy; 2026 NG<span style="color: var(--accent);">_</span></div>
</footer>
<script>
(function(){{
  var btn = document.querySelector('.js-back-to-top');
  if (!btn) return;
  btn.addEventListener('click', function(){{
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  }});
}})();
</script>
"""

def render_contact_modal(lang):
    cf = SITE['contact_form']
    return f"""<div class="modal-overlay" id="contact-modal" aria-hidden="true">
  <div class="modal-box" role="dialog" aria-modal="true" aria-labelledby="contact-modal-title">
    <button type="button" class="modal-close" data-close-contact aria-label="{t(cf['close'], lang)}">&#215;</button>
    <h3 id="contact-modal-title">{t(cf['title'], lang)}</h3>
    <form id="contact-form">
      <label>{t(cf['name'], lang)}<input type="text" name="name" required></label>
      <label>{t(cf['email'], lang)}<input type="email" name="email" required></label>
      <label>{t(cf['message'], lang)}<textarea name="message" rows="4" required></textarea></label>
      <p class="modal-note">{t(cf['note'], lang)}</p>
      <button type="submit" class="cta-btn2">{t(cf['send'], lang)}</button>
    </form>
  </div>
</div>
<script>
(function(){{
  var overlay = document.getElementById('contact-modal');
  if (!overlay) return;
  var openers = document.querySelectorAll('.js-contact-trigger');
  var closers = overlay.querySelectorAll('[data-close-contact]');
  var lastFocus;
  function openModal(e){{
    if (e) e.preventDefault();
    lastFocus = document.activeElement;
    overlay.classList.add('is-open');
    overlay.setAttribute('aria-hidden', 'false');
    var firstField = overlay.querySelector('input, textarea');
    if (firstField) firstField.focus();
    document.addEventListener('keydown', onKey);
  }}
  function closeModal(){{
    overlay.classList.remove('is-open');
    overlay.setAttribute('aria-hidden', 'true');
    document.removeEventListener('keydown', onKey);
    if (lastFocus) lastFocus.focus();
  }}
  function onKey(e){{ if (e.key === 'Escape') closeModal(); }}
  openers.forEach(function(el){{ el.addEventListener('click', openModal); }});
  closers.forEach(function(el){{ el.addEventListener('click', closeModal); }});
  overlay.addEventListener('click', function(e){{ if (e.target === overlay) closeModal(); }});
  var form = document.getElementById('contact-form');
  if (form) {{
    form.addEventListener('submit', function(e){{
      e.preventDefault();
      var subject = encodeURIComponent('Portfolio contact from ' + form.name.value);
      var body = encodeURIComponent(form.message.value + '\\n\\n' + form.email.value);
      window.location.href = 'mailto:{CONTACT["email"]}?subject=' + subject + '&body=' + body;
      closeModal();
    }});
  }}
}})();
</script>
"""

def render_card(p, idx, lang, cat_counters):
    href = f"projects/{p['slug']}.html"
    local_idx = cat_counters[p['category']]
    cat_counters[p['category']] += 1
    label = f"{local_idx + 1:02d}"
    alt = f"{t(p['title'], lang)} — {t(p['subtitle'], lang)}"
    cover = cover_html(p['slug'], p['category'], label, alt, size="sm", covers_prefix="../assets/", loading="lazy")
    return f"""<a class="card" href="{href}">
  {cover}
  <div class="card-body">
    <div class="cat">{t(SITE['section_titles'][p['category']], lang)}</div>
    <h3>{t(p['title'], lang)}</h3>
    <p class="sub">{t(p['subtitle'], lang)}</p>
    <div class="year">{p['year']}</div>
  </div>
</a>"""

def render_ticker(lang):
    words = t(SITE['ticker_words'], lang)
    one_set = '<span class="sep">&#8212;</span>'.join(words)
    return f"""<section class="ticker-band">
  <div class="ticker-tag">{t(SITE['ticker_tag'], lang)}</div>
  <div class="marquee">
    <div class="marquee-track">
      <span class="marquee-set">{one_set}<span class="sep">&#8212;</span></span>
      <span class="marquee-set" aria-hidden="true">{one_set}<span class="sep">&#8212;</span></span>
    </div>
  </div>
</section>
"""

def render_bands(lang):
    return f"""<div class="band-stack">
  <div class="band digital" id="digital">
    <a class="band-link" href="#work">
      <h2>{t(SITE['section_titles']['digital'], lang)}</h2>
      <p class="band-note">{t(SITE['band_tagline']['digital'], lang)}</p>
    </a>
  </div>
  <div class="band product" id="product">
    <a class="band-link" href="#work">
      <h2>{t(SITE['section_titles']['product'], lang)}</h2>
      <p class="band-note">{t(SITE['band_tagline']['product'], lang)}</p>
    </a>
  </div>
</div>
"""

def render_work_index(lang):
    tiles = []
    for i, p in enumerate(PROJECTS):
        tag = t(SITE['tile_tag'][p['category']], lang)
        tiles.append(
            f'<a class="work-tile" href="projects/{p["slug"]}.html">'
            f'<span class="num">{i+1:02d}</span>'
            f'<span class="name">{t(p["title"], lang)}</span>'
            f'<span class="tile-tag-default">{tag}</span>'
            f'<span class="tile-reveal">'
            f'<span class="tile-desc">{t(p["subtitle"], lang)}</span>'
            f'</span></a>'
        )
    return f"""<section class="work-index" id="work">
  <div class="wrap">
    <div class="work-label">{t(SITE['work_label'], lang)}</div>
  </div>
  <div class="work-grid">
    {''.join(tiles)}
  </div>
</section>
"""

def render_spotlight(lang, slug="dendros"):
    p = next(x for x in PROJECTS if x['slug'] == slug)
    return f"""<section class="spotlight">
  <a class="spotlight-link" href="projects/{p['slug']}.html">
    <div class="sp-text">
      <div class="sp-eyebrow">{t(SITE['featured_label'], lang)}</div>
      <h2 class="sp-title">{t(p['title'], lang)}</h2>
      <p class="sp-desc">{t(p['subtitle'], lang)} &#8212; {p['year']}</p>
    </div>
    <div class="sp-visual">
      <img src="../assets/covers/{p['slug']}.svg" alt="{t(p['title'], lang)}" loading="lazy" decoding="async" width="900" height="900">
    </div>
  </a>
</section>
"""

def render_home(lang):
    html_out = head(f"Natalia Giraldo — {t(SITE['role'], lang).replace('&amp;','&')}", lang, depth=1)
    html_out += site_header(lang, "home")
    html_out += f"""
<main id="content">
<section class="hero wrap">
  <div class="hero-grid">
    <div class="hero-text">
      <h1 data-glitch="{t(SITE['hero_title'], lang).replace('&amp;','&')}">
        <span>{t(SITE['hero_title'], lang).replace('&amp;','&')}</span>
        <span class="glitch-a" aria-hidden="true">{t(SITE['hero_title'], lang).replace('&amp;','&')}</span>
        <span class="glitch-b" aria-hidden="true">{t(SITE['hero_title'], lang).replace('&amp;','&')}</span>
      </h1>
      <p class="lede">{t(SITE['hero'], lang)}</p>
    </div>
    <div class="hero-visual" data-tilt>
      <img src="../assets/covers/hero.svg" alt="" loading="eager" fetchpriority="high" decoding="async" width="900" height="900">
      <div class="hv-label">{t(SITE['role'], lang).replace('&amp;','&').replace(' &amp; ', ' &amp; ')}<br>{t(SITE['hero_visual_label'], lang)}</div>
      <div class="hv-scroll">{t(SITE['scroll_cue'], lang)}</div>
    </div>
  </div>
</section>

{render_bands(lang)}
{render_ticker(lang)}
</main>

{render_work_index(lang)}
{render_spotlight(lang)}
"""
    html_out += cta_band(lang)
    html_out += site_footer(lang)
    html_out += render_contact_modal(lang)
    html_out += """<script>
(function(){
  var visual = document.querySelector('[data-tilt]');
  if (!visual || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var img = visual.querySelector('img');
  visual.addEventListener('mousemove', function(e){
    var r = visual.getBoundingClientRect();
    var x = (e.clientX - r.left) / r.width - 0.5;
    var y = (e.clientY - r.top) / r.height - 0.5;
    img.style.transform = 'scale(1.06) translate(' + (x*-14) + 'px,' + (y*-14) + 'px)';
  });
  visual.addEventListener('mouseleave', function(){ img.style.transform = 'scale(1) translate(0,0)'; });
})();
(function(){
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  document.querySelectorAll('.band, .ticker-band').forEach(function(band){
    band.addEventListener('mousemove', function(e){
      var r = band.getBoundingClientRect();
      band.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100) + '%');
      band.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100) + '%');
    });
  });
})();
</script>
"""
    html_out += "</body>\n</html>\n"
    return html_out

def render_project(p, idx, lang):
    order = [x['slug'] for x in PROJECTS]
    pos = order.index(p['slug'])
    prev_p = PROJECTS[pos - 1] if pos > 0 else PROJECTS[-1]
    next_p = PROJECTS[pos + 1] if pos < len(PROJECTS) - 1 else PROJECTS[0]
    counters = {"digital": 0, "product": 0}
    for x in PROJECTS[:pos + 1]:
        if x['slug'] == p['slug']:
            local_idx = counters[x['category']]
            break
        counters[x['category']] += 1
    label = f"{local_idx + 1:02d}"
    alt = f"{t(p['title'], lang)} — {t(p['subtitle'], lang)}"
    cover = cover_html(p['slug'], p['category'], label, alt, size="lg", covers_prefix="../../assets/", loading="eager")

    html_out = head(f"{t(p['title'], lang)} — Natalia Giraldo", lang, depth=2)
    html_out += site_header(lang, "project", p['slug'])
    html_out += f"""
<main id="content">
<section class="project-hero wrap">
  <a class="back-link" href="../../{lang}/index.html">&#8592; {t(SITE['nav']['back'], lang)}</a>
  {cover}
  <div class="project-body">
    <div class="project-meta">
      <span class="tag">{t(SITE['section_titles'][p['category']], lang)}</span>
      <span class="dot"></span>
      <span class="tag" style="color: var(--muted);">{p['year']}</span>
    </div>
    <h1>{t(p['title'], lang)}</h1>
    <p class="sub">{t(p['subtitle'], lang)}</p>
    <p class="desc">{t(p['desc'], lang)}</p>
  </div>
  <nav class="project-nav" aria-label="Project navigation">
    <a class="nav-item prev" href="../../{lang}/projects/{prev_p['slug']}.html"><span class="eyebrow">{t(SITE['nav']['prev'], lang)}</span>{t(prev_p['title'], lang)}</a>
    <a class="nav-item next" href="../../{lang}/projects/{next_p['slug']}.html"><span class="eyebrow">{t(SITE['nav']['next'], lang)}</span>{t(next_p['title'], lang)}</a>
  </nav>
</section>
</main>
"""
    html_out += site_footer(lang)
    html_out += render_contact_modal(lang)
    html_out += "</body>\n</html>\n"
    return html_out

def render_root():
    lang_cards = "\n".join(
        f'<a href="{l}/index.html" style="border:1px solid var(--line); padding:14px 30px; border-radius:8px; font-family:var(--font-display); font-weight:600;">{LANG_NAME[l]}</a>'
        for l in LANGS
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Natalia Giraldo — Portfolio</title>
{FONT_LINKS}
<link rel="stylesheet" href="assets/style.css">
<script>
  (function(){{
    var m = {{ en: "en", es: "es", fr: "fr" }};
    var lang = (navigator.language || "en").slice(0,2).toLowerCase();
    if (m[lang]) {{ window.location.replace(m[lang] + "/index.html"); }}
  }})();
</script>
</head>
<body>
<main id="content">
<section class="hero wrap" style="text-align:center; padding-top:130px;">
  <div class="kicker">Digital Arts &amp; Product Design</div>
  <h1 style="max-width:none;">Natalia Giraldo<span style="color:var(--accent-ink);">_</span></h1>
  <p class="lede" style="margin:0 auto 36px;">Choose your language / Elige tu idioma / Choisis ta langue</p>
  <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap;">
    {lang_cards}
  </div>
</section>
</main>
</body>
</html>
"""

def build():
    os.makedirs(os.path.join(ROOT, "assets", "covers"), exist_ok=True)
    with open(os.path.join(ROOT, "assets", "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS)

    covers = build_covers()
    for slug, svg in covers.items():
        with open(os.path.join(ROOT, "assets", "covers", f"{slug}.svg"), "w", encoding="utf-8") as f:
            f.write(svg)
    with open(os.path.join(ROOT, "assets", "covers", "hero.svg"), "w", encoding="utf-8") as f:
        f.write(make_hero_svg())

    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_root())

    for lang in LANGS:
        lang_dir = os.path.join(ROOT, lang)
        proj_dir = os.path.join(lang_dir, "projects")
        os.makedirs(proj_dir, exist_ok=True)
        with open(os.path.join(lang_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(render_home(lang))
        for idx, p in enumerate(PROJECTS):
            with open(os.path.join(proj_dir, f"{p['slug']}.html"), "w", encoding="utf-8") as f:
                f.write(render_project(p, idx, lang))

    total_files = sum(len(files) for _, _, files in os.walk(ROOT))
    print(f"Built site at {ROOT} — {total_files} files")

if __name__ == "__main__":
    build()
