"""
OmniIDE Content Generation Engine
Generates all documentation, landing, comparison, and blog pages.
"""
import os
import json
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://omniide.com"
TODAY = datetime.now().strftime("%Y-%m-%d")

# ════════════════════════════════════════════
# SHARED HTML TEMPLATES
# ════════════════════════════════════════════

def nav_html(active=""):
    return f'''<nav class="site-nav" id="site-nav">
    <div class="nav-container">
        <a href="/" class="nav-logo">
            <img src="/assets/images/logo.jpg" alt="OmniIDE Logo" width="34" height="34">
            <span>OmniIDE</span>
        </a>
        <div class="nav-links">
            <a href="/" {"class=active" if active=="home" else ""}>Home</a>
            <a href="/docs/" {"class=active" if active=="docs" else ""}>Docs</a>
            <a href="/blog/" {"class=active" if active=="blog" else ""}>Blog</a>
            <a href="/omni/" {"class=active" if active=="product" else ""}>Product</a>
            <a href="/#contact" >Contact</a>
        </div>
        <a href="https://github.com/nihannihu/Omni-IDE/releases/download/v3.0.0/OmniIDE-Setup.exe" class="nav-cta">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            Download
        </a>
        <button class="nav-hamburger" id="nav-hamburger" aria-label="Toggle menu">
            <span></span><span></span><span></span>
        </button>
    </div>
</nav>
<div class="mobile-nav">
    <div class="mobile-nav-header">
        <a href="/" class="mobile-nav-logo">
            <span>OmniIDE</span>
        </a>
        <div class="mobile-nav-version">v3.0.0 LIVE</div>
    </div>
    
    <div class="mobile-nav-items">
        <a href="/" class="mobile-nav-item">
            <div class="mobile-nav-content">
                <span class="mobile-nav-title">Home</span>
                <span class="mobile-nav-subtitle">Return to the main page</span>
            </div>
        </a>
        <a href="/docs/?open-menu=1" class="mobile-nav-item mobile-docs-link">
            <div class="mobile-nav-content">
                <span class="mobile-nav-title">Docs Menu</span>
                <span class="mobile-nav-subtitle">Guides & API reference</span>
            </div>
        </a>
        <a href="/blog/" class="mobile-nav-item">
            <div class="mobile-nav-content">
                <span class="mobile-nav-title">Blog</span>
                <span class="mobile-nav-subtitle">Latest news & tech articles</span>
            </div>
        </a>
        <a href="/omni/" class="mobile-nav-item">
            <div class="mobile-nav-content">
                <span class="mobile-nav-title">Product</span>
                <span class="mobile-nav-subtitle">Explore features & editions</span>
            </div>
        </a>
        <a href="/#contact" class="mobile-nav-item">
            <div class="mobile-nav-content">
                <span class="mobile-nav-title">Contact</span>
                <span class="mobile-nav-subtitle">Get in touch with support</span>
            </div>
        </a>
    </div>

    <div class="mobile-nav-footer">
        <a href="https://github.com/nihannihu/Omni-IDE/releases/download/v3.0.0/OmniIDE-Setup.exe" class="mobile-nav-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            Download for Windows
        </a>
        <div class="mobile-nav-socials">
            <a href="https://github.com/nihannihu/Omni-IDE" target="_blank">GitHub</a>
            <span>•</span>
            <a href="https://discord.gg/" target="_blank">Discord</a>
            <span>•</span>
            <a href="https://x.com/" target="_blank">Twitter</a>
        </div>
    </div>
</div>'''


def footer_html():
    return '''<footer class="site-footer">
    <div class="container">
        <div class="footer-grid">
            <div class="footer-brand">
                <a href="/" class="nav-logo" style="color:#fff">
                    <img src="/assets/images/logo.jpg" alt="OmniIDE" width="34" height="34">
                    <span>OmniIDE</span>
                </a>
                <p>Building the open infrastructure layer for autonomous software development.</p>
                <div class="reg">UDYAM-KR-03-0681404</div>
            </div>
            <div class="footer-col">
                <h5>Product</h5>
                <a href="/omni/">OmniIDE v3.0</a>
                <a href="/docs/">Documentation</a>
                <a href="/docs/getting-started/">Getting Started</a>
                <a href="/blog/">Blog</a>
            </div>
            <div class="footer-col">
                <h5>Compare</h5>
                <a href="/cursor-alternative/">vs Cursor</a>
                <a href="/copilot-alternative/">vs Copilot</a>
                <a href="/windsurf-alternative/">vs Windsurf</a>
                <a href="/devin-alternative/">vs Devin</a>
            </div>
            <div class="footer-col">
                <h5>Connect</h5>
                <a href="https://github.com/OMNI-IDE-in" target="_blank" rel="noopener noreferrer">GitHub</a>
                <a href="https://linkedin.com/company/omni-ide" target="_blank" rel="noopener noreferrer">LinkedIn</a>
                <a href="mailto:contact@omniide.com">Email</a>
            </div>
        </div>
        <div class="footer-bottom">
            <span>&copy; 2026 OmniIDE. UDYAM-KR-03-0681404. All rights reserved.</span>
            <div>
                <a href="/">Home</a>
                <a href="/docs/">Docs</a>
                <a href="/blog/">Blog</a>
            </div>
        </div>
    </div>
</footer>'''

def head_html(title, description, canonical, page_type="WebPage", extra_schema=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="author" content="OmniIDE">
    <link rel="canonical" href="{DOMAIN}{canonical}">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
    <meta name="theme-color" content="#0F172A">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{DOMAIN}{canonical}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="{DOMAIN}/assets/images/og-image.png">
    <meta property="og:site_name" content="OmniIDE">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{DOMAIN}/assets/images/og-image.png">
    <link rel="icon" type="image/jpeg" href="/assets/images/logo.jpg">
    <link rel="apple-touch-icon" href="/assets/images/logo.jpg">
    <link rel="stylesheet" href="/assets/css/shared.css?v=3.0.4">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@graph": [
            {{
                "@type": "Organization",
                "@id": "{DOMAIN}/#organization",
                "name": "OmniIDE",
                "url": "{DOMAIN}",
                "logo": {{ "@type": "ImageObject", "url": "{DOMAIN}/assets/images/logo.jpg" }},
                "sameAs": ["https://github.com/OMNI-IDE-in", "https://linkedin.com/company/omni-ide"]
            }},
            {{
                "@type": "BreadcrumbList",
                "@id": "{DOMAIN}{canonical}#breadcrumb",
                "itemListElement": [
                    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{DOMAIN}/" }}
                ]
            }},
            {{
                "@type": "{page_type}",
                "url": "{DOMAIN}{canonical}",
                "name": "{title}",
                "description": "{description}",
                "isPartOf": {{ "@id": "{DOMAIN}/#website" }},
                "publisher": {{ "@id": "{DOMAIN}/#organization" }},
                "datePublished": "2026-02-21",
                "dateModified": "{TODAY}"
            }}{extra_schema}
        ]
    }}
    </script>
</head>'''


def doc_sidebar():
    sections = {
        "Getting Started": [
            ("/docs/getting-started/", "Introduction"),
            ("/docs/getting-started/installation/", "Installation"),
            ("/docs/getting-started/quick-start/", "Quick Start Guide"),
            ("/docs/getting-started/first-project/", "Your First Project"),
            ("/docs/getting-started/configuration/", "Configuration"),
        ],
        "Core Concepts": [
            ("/docs/core-concepts/omni-agent/", "Omni-Agent"),
            ("/docs/core-concepts/agentic-loop/", "Agentic Loop"),
            ("/docs/core-concepts/self-healing/", "Self-Healing Terminal"),
            ("/docs/core-concepts/hardened-sandbox/", "Hardened Sandbox"),
            ("/docs/core-concepts/execution-kernel/", "Execution Kernel"),
            ("/docs/core-concepts/trajectory/", "Trajectory System"),
            ("/docs/core-concepts/memory/", "Memory Architecture"),
            ("/docs/core-concepts/verification/", "Verification Engine"),
            ("/docs/core-concepts/recovery/", "Recovery System"),
        ],
        "Features": [
            ("/docs/features/ai-coding/", "AI-Powered Coding"),
            ("/docs/features/multi-file-refactoring/", "Multi-File Refactoring"),
            ("/docs/features/terminal/", "Integrated Terminal"),
            ("/docs/features/zero-telemetry/", "Zero Telemetry"),
            ("/docs/features/offline-mode/", "Offline Mode"),
            ("/docs/features/extensions/", "Extensions Support"),
            ("/docs/features/theming/", "Theming & Customization"),
            ("/docs/features/git-integration/", "Git Integration"),
            ("/docs/features/debugging/", "Debugging"),
            ("/docs/features/snippets/", "Code Snippets"),
        ],
        "Integrations": [
            ("/docs/integrations/gemini/", "Google Gemini"),
            ("/docs/integrations/ollama/", "Ollama"),
            ("/docs/integrations/openrouter/", "OpenRouter"),
            ("/docs/integrations/mcp/", "Model Context Protocol"),
            ("/docs/integrations/acp/", "Agent Communication Protocol"),
        ],
        "Architecture": [
            ("/docs/architecture/overview/", "Architecture Overview"),
            ("/docs/architecture/vscode-core/", "VS Code Core"),
            ("/docs/architecture/security/", "Security Model"),
            ("/docs/architecture/build-system/", "Build System"),
        ],
        "Guides": [
            ("/docs/guides/api-key-setup/", "API Key Setup"),
            ("/docs/guides/ollama-setup/", "Ollama Local Setup"),
            ("/docs/guides/workspace-config/", "Workspace Configuration"),
            ("/docs/guides/keyboard-shortcuts/", "Keyboard Shortcuts"),
            ("/docs/guides/autonomous-workflows/", "Autonomous Workflows"),
            ("/docs/guides/agent-commands/", "Agent Commands"),
            ("/docs/guides/sandbox-config/", "Sandbox Configuration"),
        ],
        "Reference": [
            ("/docs/reference/cli/", "CLI Reference"),
            ("/docs/reference/settings/", "Settings Reference"),
            ("/docs/reference/keybindings/", "Keybindings"),
            ("/docs/reference/changelog/", "Changelog"),
            ("/docs/reference/api/", "API Reference"),
        ],
        "Troubleshooting": [
            ("/docs/troubleshooting/common-issues/", "Common Issues"),
            ("/docs/troubleshooting/agent-errors/", "Agent Errors"),
            ("/docs/troubleshooting/performance/", "Performance"),
            ("/docs/troubleshooting/faq/", "FAQ"),
        ],
    }
    html = '''<aside class="sidebar">
    <div class="sidebar-mobile-header">
        <span class="sidebar-mobile-title">Docs Menu</span>
        <div class="sidebar-close" id="sidebar-close">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </div>
    </div>
    <div class="sidebar-search">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" id="sidebar-search" placeholder="Search docs..." aria-label="Search documentation">
    </div>\n'''
    for section, links in sections.items():
        html += f'    <div class="sidebar-section">\n        <div class="sidebar-section-title">{section}</div>\n'
        for href, label in links:
            html += f'        <a href="{href}" class="sidebar-link">{label}</a>\n'
        html += '    </div>\n'
    html += '</aside>'
    return html, sections


def build_doc_page(path, title, description, content_html, prev_link=None, next_link=None, related=None):
    sidebar_html, _ = doc_sidebar()
    
    # Build breadcrumb
    parts = [p for p in path.strip('/').split('/') if p]
    breadcrumb = '<div class="breadcrumbs"><a href="/">Home</a><span class="sep">›</span><a href="javascript:void(0)" class="breadcrumb-docs-menu" onclick="var s=document.querySelector(\'.sidebar\'),b=document.getElementById(\'sidebar-backdrop\');if(s&&b){s.classList.add(\'active\');b.classList.add(\'active\')}">Docs Menu</a>'
    if len(parts) > 2:
        section = parts[1].replace('-', ' ').title()
        breadcrumb += f'<span class="sep">›</span><a href="/docs/{parts[1]}/">{section}</a>'
    breadcrumb += f'<span class="sep">›</span><span class="current">{title}</span></div>'
    
    # Page nav
    nav_html_str = ''
    if prev_link or next_link:
        nav_html_str = '<div class="page-nav">'
        if prev_link:
            nav_html_str += f'<a href="{prev_link[0]}" class="page-nav-link"><span class="page-nav-label">← Previous</span><span class="page-nav-title">{prev_link[1]}</span></a>'
        else:
            nav_html_str += '<div></div>'
        if next_link:
            nav_html_str += f'<a href="{next_link[0]}" class="page-nav-link next"><span class="page-nav-label">Next →</span><span class="page-nav-title">{next_link[1]}</span></a>'
        else:
            nav_html_str += '<div></div>'
        nav_html_str += '</div>'
    
    # Related content
    related_html = ''
    if related:
        related_html = '<div class="related-section"><h3>Related Documentation</h3><div class="related-grid">'
        for r in related:
            related_html += f'<a href="{r[0]}" class="related-card"><div class="related-card-title">{r[1]}</div><div class="related-card-desc">{r[2]}</div></a>'
        related_html += '</div></div>'
    
    schema = f''',
            {{
                "@type": "TechArticle",
                "headline": "{title}",
                "description": "{description}",
                "url": "{DOMAIN}{path}",
                "author": {{ "@id": "{DOMAIN}/#organization" }},
                "publisher": {{ "@id": "{DOMAIN}/#organization" }},
                "datePublished": "2026-02-21",
                "dateModified": "{TODAY}"
            }}'''
    
    html = head_html(f"{title} — OmniIDE Docs", description, path, "WebPage", schema)
    html += f'''
<body>
{nav_html("docs")}
<div class="sidebar-backdrop" id="sidebar-backdrop"></div>
<div class="page-wrapper">
    <div class="container">
        <div class="content-layout">
            {sidebar_html}
            <main class="content-main">
                <button class="mobile-sidebar-toggle" id="mobile-sidebar-toggle">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
                    Docs Menu
                </button>
                {breadcrumb}
                <div class="content">
                    {content_html}
                </div>
                {nav_html_str}
                {related_html}
            </main>
        </div>
    </div>
</div>
{footer_html()}
<script src="/assets/js/shared.js?v=3.0.4"></script>
</body>
</html>'''
    
    write_file(path, html)


def build_landing_page(path, title, description, hero_badge, hero_title, hero_subtitle, features, comparison_data=None, faqs=None, related_pages=None):
    faq_schema = ""
    if faqs:
        faq_entities = []
        for q, a in faqs:
            faq_entities.append(f'''{{
                "@type": "Question",
                "name": "{q}",
                "acceptedAnswer": {{ "@type": "Answer", "text": "{a}" }}
            }}''')
        faq_schema = f''',
            {{
                "@type": "FAQPage",
                "@id": "{DOMAIN}{path}#faq",
                "mainEntity": [{",".join(faq_entities)}]
            }}'''
    
    html = head_html(title, description, path, "WebPage", faq_schema)
    
    # Features HTML
    features_html = '<div class="feature-grid">'
    for icon, feat_title, feat_desc in features:
        features_html += f'''<div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <h3>{feat_title}</h3>
            <p>{feat_desc}</p>
        </div>'''
    features_html += '</div>'
    
    # Comparison HTML
    comp_html = ''
    if comparison_data:
        comp_html = '<section style="margin: 64px 0"><h2 style="text-align:center; font-size:32px; margin-bottom:32px;">Feature Comparison</h2><table class="comparison-table"><thead><tr>'
        for col in comparison_data["headers"]:
            comp_html += f'<th>{col}</th>'
        comp_html += '</tr></thead><tbody>'
        for row in comparison_data["rows"]:
            comp_html += '<tr>'
            for cell in row:
                if cell == "✓": comp_html += '<td class="check">✓</td>'
                elif cell == "✗": comp_html += '<td class="cross">✗</td>'
                else: comp_html += f'<td>{cell}</td>'
            comp_html += '</tr>'
        comp_html += '</tbody></table></section>'
    
    # FAQ HTML
    faq_html = ''
    if faqs:
        faq_html = '<section class="faq-section" id="faq"><h2>Frequently Asked Questions</h2>'
        for q, a in faqs:
            faq_html += f'''<div class="faq-item">
                <button class="faq-question">{q}<span class="icon">+</span></button>
                <div class="faq-answer"><p>{a}</p></div>
            </div>'''
        faq_html += '</section>'
    
    # Related pages
    related_html = ''
    if related_pages:
        related_html = '<div class="related-section"><h3>Explore More</h3><div class="related-grid">'
        for rp in related_pages:
            related_html += f'<a href="{rp[0]}" class="related-card"><div class="related-card-title">{rp[1]}</div><div class="related-card-desc">{rp[2]}</div></a>'
        related_html += '</div></div>'
    
    html += f'''
<body>
{nav_html()}
<div class="page-wrapper">
    <section class="lp-hero">
        <div class="container">
            <div class="badge">{hero_badge}</div>
            <h1>{hero_title}</h1>
            <p class="subtitle">{hero_subtitle}</p>
            <div class="lp-ctas">
                <a href="https://github.com/nihannihu/Omni-IDE/releases/download/v3.0.0/OmniIDE-Setup.exe" class="btn-primary">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                    Download Free for Windows
                </a>
                <a href="/docs/getting-started/" class="btn-secondary">Read Documentation →</a>
            </div>
        </div>
    </section>
    <div class="container">
        {features_html}
        {comp_html}
        {faq_html}
        {related_html}
    </div>
    <section class="cta-section">
        <div class="container">
            <h2>Start Building with OmniIDE</h2>
            <p>Free, open-source, zero telemetry. Download and start coding in under 2 minutes.</p>
            <a href="https://github.com/nihannihu/Omni-IDE/releases/download/v3.0.0/OmniIDE-Setup.exe" class="btn-primary">Download OmniIDE v3.0 →</a>
        </div>
    </section>
</div>
{footer_html()}
<script src="/assets/js/shared.js?v=3.0.4"></script>
</body>
</html>'''
    
    write_file(path, html)


def write_file(path, content):
    full_path = os.path.join(BASE, path.strip('/'))
    if not full_path.endswith('.html') and not full_path.endswith('.xml') and not full_path.endswith('.txt'):
        full_path = os.path.join(full_path, 'index.html')
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ {path}")


# ════════════════════════════════════════════
# OMNIIDE FEATURE DATA (source of truth)
# ════════════════════════════════════════════

CORE_FEATURES = [
    ("🤖", "Omni-Agent", "An autonomous coding agent powered by Google Gemini API that writes, debugs, and runs code without human intervention. It observes errors, generates fixes, and re-executes — a true self-healing development loop."),
    ("🛡️", "Hardened Sandbox", "Every autonomous command executes inside an isolated sandbox, protecting your host operating system. The agent can experiment freely without risk to your files or system."),
    ("🔄", "Self-Healing Terminal", "The integrated terminal catches errors in real-time, generates corrective code, and re-executes automatically. Failed builds and crashed scripts recover without manual debugging."),
    ("🔒", "Zero Telemetry", "OmniIDE collects absolutely no data. No analytics, no tracking, no watermarks, no cloud dependency. Your code stays on your machine, period."),
    ("🏗️", "VS Code Core", "Built on the production-ready VS Code architecture with TypeScript and Node.js. Get the familiar, high-performance editor experience with full extension compatibility."),
    ("🧠", "Hybrid AI Engine", "Combines Google Gemini API for cloud-powered intelligence with Ollama for fully local, offline AI execution. Choose cloud, local, or hybrid — your call."),
    ("📁", "Multi-File Refactoring", "The agent handles complex cross-file code changes autonomously. Rename symbols, restructure modules, and refactor architectures across your entire codebase."),
    ("💻", "Local-Native", "Runs entirely on your machine. No SaaS subscription, no cloud compute costs. Bring your own API key for Gemini, or run fully offline with Ollama."),
]

STANDARD_FAQS = [
    ("What is OmniIDE?", "OmniIDE is a free, open-source AI-powered integrated development environment designed for autonomous software development. It features a self-healing agentic loop that writes, debugs, and runs code autonomously on your local machine with zero telemetry."),
    ("Is OmniIDE free?", "Yes. OmniIDE is completely free and open source. There are no subscriptions, no watermarks, and no usage limits. You bring your own API key for Gemini, and all code stays on your machine."),
    ("What operating systems does OmniIDE support?", "OmniIDE currently supports Windows 10 and Windows 11 natively. macOS and Linux support is planned for future releases."),
    ("Does OmniIDE work offline?", "Yes. OmniIDE is local-native and can run AI models offline via Ollama integration. For cloud-powered features, it connects to Google Gemini API. The IDE itself runs entirely on your machine."),
    ("Is OmniIDE open source?", "Yes. OmniIDE is fully open source and available on GitHub at github.com/OMNI-IDE-in. All core tooling is published under open-source licenses."),
    ("Is OmniIDE safe to use?", "Yes. All autonomous agent commands execute inside a Hardened Sandbox, isolated from your host OS. OmniIDE collects zero telemetry and is MSME registered with the Government of India."),
    ("How is OmniIDE different from Cursor or Copilot?", "OmniIDE is fully autonomous — it does not just suggest code, it writes, runs, debugs, and fixes code independently. It is free, open source, collects zero telemetry, and runs locally. Cursor and Copilot are cloud-dependent subscription services."),
]


# ════════════════════════════════════════════
# PHASE 2: DOCUMENTATION PAGES
# ════════════════════════════════════════════

print("\n═══ PHASE 2: Building Documentation Pages ═══\n")

# Docs index
sidebar_html, sections = doc_sidebar()
docs_index_content = '''<h1>OmniIDE Documentation</h1>
<p>Welcome to the official OmniIDE documentation. Whether you are getting started for the first time or looking for advanced architecture details, you will find everything you need here.</p>

<div class="info-box note"><strong>New to OmniIDE?</strong> Start with the <a href="/docs/getting-started/">Getting Started</a> guide to install OmniIDE and create your first AI-assisted project in under 5 minutes.</div>

<h2>Documentation Sections</h2>

<div class="feature-grid">
    <a href="/docs/getting-started/" class="feature-card" style="text-decoration:none">
        <div class="feature-icon">🚀</div>
        <h3>Getting Started</h3>
        <p>Install OmniIDE, configure your API key, and build your first project with the Omni-Agent.</p>
    </a>
    <a href="/docs/core-concepts/omni-agent/" class="feature-card" style="text-decoration:none">
        <div class="feature-icon">🤖</div>
        <h3>Core Concepts</h3>
        <p>Understand the Omni-Agent, agentic loop, self-healing terminal, hardened sandbox, and execution kernel.</p>
    </a>
    <a href="/docs/features/ai-coding/" class="feature-card" style="text-decoration:none">
        <div class="feature-icon">⚡</div>
        <h3>Features</h3>
        <p>Explore AI-powered coding, multi-file refactoring, zero telemetry, offline mode, and extensions.</p>
    </a>
    <a href="/docs/integrations/gemini/" class="feature-card" style="text-decoration:none">
        <div class="feature-icon">🔗</div>
        <h3>Integrations</h3>
        <p>Connect Google Gemini, Ollama, OpenRouter, MCP, and ACP to your development workflow.</p>
    </a>
    <a href="/docs/architecture/overview/" class="feature-card" style="text-decoration:none">
        <div class="feature-icon">🏗️</div>
        <h3>Architecture</h3>
        <p>Deep dive into the VS Code core, security model, build system, and system architecture.</p>
    </a>
    <a href="/docs/guides/api-key-setup/" class="feature-card" style="text-decoration:none">
        <div class="feature-icon">📖</div>
        <h3>Guides</h3>
        <p>Step-by-step guides for API key setup, Ollama configuration, workspace setup, and autonomous workflows.</p>
    </a>
    <a href="/docs/reference/settings/" class="feature-card" style="text-decoration:none">
        <div class="feature-icon">📋</div>
        <h3>Reference</h3>
        <p>Complete reference for CLI commands, settings, keybindings, changelog, and API.</p>
    </a>
    <a href="/docs/troubleshooting/common-issues/" class="feature-card" style="text-decoration:none">
        <div class="feature-icon">🔧</div>
        <h3>Troubleshooting</h3>
        <p>Solutions for common issues, agent errors, performance optimization, and frequently asked questions.</p>
    </a>
</div>'''

build_doc_page("/docs/", "Documentation", "Official OmniIDE documentation — getting started guides, core concepts, feature reference, integrations, architecture, and troubleshooting.", docs_index_content)


# ──── GETTING STARTED ────

build_doc_page("/docs/getting-started/", "Getting Started", 
    "Get started with OmniIDE — install the AI IDE, configure your API key, and start autonomous coding in minutes.",
    '''<h1>Getting Started with OmniIDE</h1>
    <p>OmniIDE is a free, open-source AI-powered IDE built for autonomous software development. This guide will walk you through installation, configuration, and your first autonomous coding session.</p>
    
    <div class="info-box tip"><strong>Time to get started:</strong> Under 5 minutes from download to your first AI-assisted project.</div>
    
    <h2>Prerequisites</h2>
    <ul>
        <li><strong>Operating System:</strong> Windows 10 or Windows 11</li>
        <li><strong>RAM:</strong> 4 GB minimum, 8 GB recommended</li>
        <li><strong>Disk Space:</strong> 500 MB for installation</li>
        <li><strong>Internet:</strong> Required for Google Gemini API (optional if using Ollama locally)</li>
    </ul>
    
    <h2>Quick Install</h2>
    <ol>
        <li>Download the latest installer from <a href="https://github.com/nihannihu/Omni-IDE/releases/download/v3.0.0/OmniIDE-Setup.exe">GitHub Releases</a></li>
        <li>Run the installer and follow the setup wizard</li>
        <li>Launch OmniIDE from your desktop or Start menu</li>
    </ol>
    
    <h2>Next Steps</h2>
    <ul>
        <li><a href="/docs/getting-started/installation/">Detailed Installation Guide</a> — platform-specific setup instructions</li>
        <li><a href="/docs/getting-started/quick-start/">Quick Start Guide</a> — create your first AI-powered project</li>
        <li><a href="/docs/guides/api-key-setup/">API Key Setup</a> — configure Google Gemini for cloud AI</li>
        <li><a href="/docs/guides/ollama-setup/">Ollama Setup</a> — run AI models locally for offline development</li>
    </ul>''',
    next_link=("/docs/getting-started/installation/", "Installation"),
    related=[
        ("/docs/getting-started/quick-start/", "Quick Start Guide", "Create your first project with OmniIDE"),
        ("/docs/guides/api-key-setup/", "API Key Setup", "Configure Google Gemini API access"),
        ("/docs/core-concepts/omni-agent/", "Omni-Agent", "Learn how the autonomous agent works"),
    ])


build_doc_page("/docs/getting-started/installation/", "Installation",
    "Install OmniIDE on Windows — step-by-step installation guide with system requirements and troubleshooting.",
    '''<h1>Installation</h1>
    <p>OmniIDE runs natively on Windows 10 and Windows 11. The installer sets up everything you need, including the VS Code core, Omni-Agent, and Hardened Sandbox.</p>
    
    <h2>System Requirements</h2>
    <table>
        <tr><th>Component</th><th>Minimum</th><th>Recommended</th></tr>
        <tr><td>OS</td><td>Windows 10 (64-bit)</td><td>Windows 11</td></tr>
        <tr><td>CPU</td><td>Dual-core 2 GHz</td><td>Quad-core 3 GHz+</td></tr>
        <tr><td>RAM</td><td>4 GB</td><td>8 GB+</td></tr>
        <tr><td>Disk</td><td>500 MB</td><td>1 GB+ (for local models)</td></tr>
        <tr><td>GPU</td><td>Not required</td><td>CUDA-compatible (for Ollama)</td></tr>
    </table>
    
    <h2>Download</h2>
    <p>Download the latest version from GitHub Releases:</p>
    <pre><code>https://github.com/nihannihu/Omni-IDE/releases/download/v3.0.0/OmniIDE-Setup.exe</code></pre>
    
    <h2>Installation Steps</h2>
    <ol>
        <li><strong>Run the installer</strong> — Double-click <code>OmniIDE-Setup.exe</code></li>
        <li><strong>Accept the license</strong> — OmniIDE is open source under permissive licensing</li>
        <li><strong>Choose install location</strong> — Default is <code>C:\\Program Files\\OmniIDE</code></li>
        <li><strong>Complete setup</strong> — The installer will configure the VS Code core and agent runtime</li>
        <li><strong>Launch OmniIDE</strong> — Open from desktop shortcut or Start menu</li>
    </ol>
    
    <div class="info-box note"><strong>Note:</strong> Windows may show a SmartScreen prompt since OmniIDE is a new application. Click "More info" → "Run anyway" to proceed.</div>
    
    <h2>Verify Installation</h2>
    <p>After launching OmniIDE, you should see the familiar code editor interface with the Omni-Agent panel. Open the integrated terminal and verify the agent is available:</p>
    <pre><code>omni --version
# Output: OmniIDE v3.0.0</code></pre>
    
    <h2>Uninstallation</h2>
    <p>To uninstall OmniIDE, use the standard Windows uninstaller via Settings → Apps → OmniIDE → Uninstall.</p>''',
    prev_link=("/docs/getting-started/", "Getting Started"),
    next_link=("/docs/getting-started/quick-start/", "Quick Start Guide"),
    related=[
        ("/docs/getting-started/quick-start/", "Quick Start Guide", "Create your first project"),
        ("/docs/guides/api-key-setup/", "API Key Setup", "Connect to Google Gemini"),
        ("/docs/troubleshooting/common-issues/", "Common Issues", "Solutions for installation problems"),
    ])


build_doc_page("/docs/getting-started/quick-start/", "Quick Start Guide",
    "Create your first AI-powered project with OmniIDE in under 5 minutes — from setup to autonomous coding.",
    '''<h1>Quick Start Guide</h1>
    <p>This guide takes you from a fresh OmniIDE installation to running your first autonomous coding session in under 5 minutes.</p>
    
    <h2>Step 1: Configure Your API Key</h2>
    <p>OmniIDE uses Google Gemini API for cloud-powered AI. You will need a free API key:</p>
    <ol>
        <li>Visit <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener">Google AI Studio</a></li>
        <li>Create a new API key (free tier available)</li>
        <li>In OmniIDE, open Settings (<code>Ctrl+,</code>) and paste your key in the Gemini API Key field</li>
    </ol>
    
    <div class="info-box tip"><strong>Prefer offline?</strong> Skip the API key and <a href="/docs/guides/ollama-setup/">set up Ollama</a> for fully local AI execution.</div>
    
    <h2>Step 2: Create a Project</h2>
    <ol>
        <li>Open OmniIDE and click <strong>File → Open Folder</strong></li>
        <li>Create a new folder for your project (e.g., <code>my-first-project</code>)</li>
        <li>The Omni-Agent will automatically detect the workspace</li>
    </ol>
    
    <h2>Step 3: Start an Autonomous Session</h2>
    <p>Open the Omni-Agent panel and type a natural language instruction:</p>
    <pre><code>Create a Node.js Express API with a /health endpoint 
and a /users endpoint that returns sample data.</code></pre>
    <p>The Omni-Agent will:</p>
    <ul>
        <li>Generate the project structure</li>
        <li>Create all necessary files (<code>package.json</code>, <code>server.js</code>, routes)</li>
        <li>Install dependencies via <code>npm install</code></li>
        <li>Start the development server</li>
        <li>If any errors occur, automatically debug and fix them</li>
    </ul>
    
    <h2>Step 4: Watch the Self-Healing Loop</h2>
    <p>If the agent encounters an error during execution — say, a missing dependency or a syntax mistake — it will:</p>
    <ol>
        <li><strong>Catch</strong> the error from the terminal output</li>
        <li><strong>Analyze</strong> the root cause using Gemini</li>
        <li><strong>Generate</strong> the corrective code</li>
        <li><strong>Re-execute</strong> automatically</li>
    </ol>
    <p>This is the self-healing agentic loop — no manual intervention required.</p>
    
    <h2>Next Steps</h2>
    <ul>
        <li><a href="/docs/core-concepts/omni-agent/">Learn about the Omni-Agent</a> — how the autonomous agent works under the hood</li>
        <li><a href="/docs/features/multi-file-refactoring/">Multi-File Refactoring</a> — handle complex cross-file changes</li>
        <li><a href="/docs/guides/autonomous-workflows/">Autonomous Workflows</a> — advanced agent patterns</li>
    </ul>''',
    prev_link=("/docs/getting-started/installation/", "Installation"),
    next_link=("/docs/getting-started/first-project/", "Your First Project"),
    related=[
        ("/docs/core-concepts/omni-agent/", "Omni-Agent", "Understand the autonomous coding agent"),
        ("/docs/guides/api-key-setup/", "API Key Setup", "Detailed Gemini configuration"),
        ("/docs/features/ai-coding/", "AI-Powered Coding", "All AI coding capabilities"),
    ])


build_doc_page("/docs/getting-started/first-project/", "Your First Project",
    "Build your first complete project with OmniIDE — a hands-on tutorial using the Omni-Agent for autonomous development.",
    '''<h1>Your First Project</h1>
    <p>In this tutorial, you will build a complete web application using OmniIDE's autonomous agent. By the end, you will have a working app created entirely by AI.</p>
    
    <h2>What You Will Build</h2>
    <p>A simple task management web app with:</p>
    <ul>
        <li>A Node.js backend with Express</li>
        <li>A clean HTML/CSS/JS frontend</li>
        <li>CRUD operations for tasks</li>
        <li>Local JSON file storage</li>
    </ul>
    
    <h2>Step 1: Open a Workspace</h2>
    <p>Create a new folder called <code>task-manager</code> and open it in OmniIDE:</p>
    <pre><code>mkdir task-manager
cd task-manager</code></pre>
    <p>Then use <strong>File → Open Folder</strong> to open this directory.</p>
    
    <h2>Step 2: Give the Agent Instructions</h2>
    <p>Open the Omni-Agent panel and describe your project:</p>
    <pre><code>Build a task management app. Use Express for the backend 
with endpoints for creating, reading, updating, and deleting tasks.
Store tasks in a local JSON file. Create a modern frontend 
with HTML, CSS, and vanilla JavaScript.</code></pre>
    
    <h2>Step 3: Watch the Agent Work</h2>
    <p>The Omni-Agent will autonomously:</p>
    <ol>
        <li>Initialize the project with <code>npm init</code></li>
        <li>Install Express and other dependencies</li>
        <li>Create the server with REST API endpoints</li>
        <li>Build a frontend with forms and task list UI</li>
        <li>Set up the JSON storage layer</li>
        <li>Test the application</li>
    </ol>
    
    <div class="info-box tip"><strong>Tip:</strong> If the agent encounters errors, it will automatically fix them using the self-healing loop. You can watch the process in the terminal panel.</div>
    
    <h2>Step 4: Review and Iterate</h2>
    <p>Once the agent completes the initial build, review the code. You can ask the agent for modifications:</p>
    <pre><code>Add a search bar to filter tasks by title.
Also add a "completed" toggle for each task.</code></pre>
    
    <h2>Next Steps</h2>
    <ul>
        <li><a href="/docs/getting-started/configuration/">Configure OmniIDE</a> to match your development preferences</li>
        <li><a href="/docs/core-concepts/agentic-loop/">Learn about the Agentic Loop</a> — the engine behind autonomous development</li>
        <li><a href="/docs/features/multi-file-refactoring/">Multi-File Refactoring</a> — scale to larger projects</li>
    </ul>''',
    prev_link=("/docs/getting-started/quick-start/", "Quick Start Guide"),
    next_link=("/docs/getting-started/configuration/", "Configuration"),
    related=[
        ("/docs/core-concepts/omni-agent/", "Omni-Agent", "How the autonomous agent works"),
        ("/docs/core-concepts/self-healing/", "Self-Healing Terminal", "Error detection and recovery"),
        ("/docs/guides/autonomous-workflows/", "Autonomous Workflows", "Advanced agent usage patterns"),
    ])


build_doc_page("/docs/getting-started/configuration/", "Configuration",
    "Configure OmniIDE — settings, AI model selection, sandbox options, theme customization, and workspace preferences.",
    '''<h1>Configuration</h1>
    <p>OmniIDE is highly configurable. This guide covers the essential settings to customize your development environment.</p>
    
    <h2>Accessing Settings</h2>
    <p>Open settings with <code>Ctrl+,</code> or navigate to <strong>File → Preferences → Settings</strong>.</p>
    
    <h2>AI Model Configuration</h2>
    <h3>Google Gemini (Cloud)</h3>
    <pre><code>{
  "omni.gemini.apiKey": "your-api-key-here",
  "omni.gemini.model": "gemini-pro",
  "omni.gemini.maxTokens": 8192
}</code></pre>
    
    <h3>Ollama (Local)</h3>
    <pre><code>{
  "omni.ollama.enabled": true,
  "omni.ollama.endpoint": "http://localhost:11434",
  "omni.ollama.model": "codellama:13b"
}</code></pre>
    
    <h2>Sandbox Settings</h2>
    <pre><code>{
  "omni.sandbox.enabled": true,
  "omni.sandbox.timeout": 30000,
  "omni.sandbox.allowNetwork": false,
  "omni.sandbox.allowFileWrite": true
}</code></pre>
    
    <h2>Agent Behavior</h2>
    <pre><code>{
  "omni.agent.autoFix": true,
  "omni.agent.maxRetries": 3,
  "omni.agent.verboseLogging": false
}</code></pre>
    
    <div class="info-box note"><strong>Settings scope:</strong> Settings can be applied globally (user settings) or per-workspace. Workspace settings override user settings.</div>
    
    <h2>Theme Customization</h2>
    <p>OmniIDE supports all VS Code themes. To change the theme:</p>
    <ol>
        <li>Press <code>Ctrl+K Ctrl+T</code></li>
        <li>Browse and select from installed themes</li>
        <li>Install additional themes from the Extensions marketplace</li>
    </ol>
    
    <h2>See Also</h2>
    <ul>
        <li><a href="/docs/reference/settings/">Complete Settings Reference</a></li>
        <li><a href="/docs/reference/keybindings/">Keybindings Reference</a></li>
        <li><a href="/docs/guides/workspace-config/">Workspace Configuration Guide</a></li>
    </ul>''',
    prev_link=("/docs/getting-started/first-project/", "Your First Project"),
    next_link=("/docs/core-concepts/omni-agent/", "Omni-Agent"),
    related=[
        ("/docs/reference/settings/", "Settings Reference", "Complete list of all settings"),
        ("/docs/guides/api-key-setup/", "API Key Setup", "Configure your Gemini API key"),
        ("/docs/guides/ollama-setup/", "Ollama Setup", "Set up local AI models"),
    ])


# ──── SECTION INDEX PAGES ────
# Generate index pages for sections that don't have one

section_index_data = {
    "core-concepts": ("Core Concepts", "Understand the foundational architecture and systems that power OmniIDE's autonomous coding capabilities.", [
        ("/docs/core-concepts/omni-agent/", "Omni-Agent", "The autonomous coding engine that writes, debugs, and runs code."),
        ("/docs/core-concepts/agentic-loop/", "Agentic Loop", "The iterative execution cycle driving autonomous development."),
        ("/docs/core-concepts/self-healing/", "Self-Healing Terminal", "Automatic error detection and recovery in the terminal."),
        ("/docs/core-concepts/hardened-sandbox/", "Hardened Sandbox", "Secure execution environment for AI-generated code."),
        ("/docs/core-concepts/execution-kernel/", "Execution Kernel", "The runtime engine that manages code execution."),
        ("/docs/core-concepts/trajectory/", "Trajectory System", "Logging and replay of agent actions."),
        ("/docs/core-concepts/memory/", "Memory Architecture", "How the agent maintains context across sessions."),
        ("/docs/core-concepts/verification/", "Verification Engine", "Automated testing and validation of agent output."),
        ("/docs/core-concepts/recovery/", "Recovery System", "Graceful recovery from errors and failures."),
    ]),
    "features": ("Features", "Explore the full feature set of OmniIDE — from AI-powered coding to zero-telemetry privacy.", [
        ("/docs/features/ai-coding/", "AI-Powered Coding", "Autonomous code generation and intelligent completions."),
        ("/docs/features/multi-file-refactoring/", "Multi-File Refactoring", "Refactor across your entire codebase at once."),
        ("/docs/features/terminal/", "Integrated Terminal", "Built-in terminal with self-healing capabilities."),
        ("/docs/features/zero-telemetry/", "Zero Telemetry", "Complete privacy — no data ever leaves your machine."),
        ("/docs/features/offline-mode/", "Offline Mode", "Run AI models locally with Ollama integration."),
        ("/docs/features/extensions/", "Extensions Support", "Full VS Code extension compatibility."),
        ("/docs/features/theming/", "Theming & Customization", "Customize the look and feel of your IDE."),
        ("/docs/features/git-integration/", "Git Integration", "Built-in Git support for version control."),
        ("/docs/features/debugging/", "Debugging", "Advanced debugging tools and workflows."),
        ("/docs/features/snippets/", "Code Snippets", "Reusable code snippet management."),
    ]),
    "integrations": ("Integrations", "Connect OmniIDE with AI providers, local models, and communication protocols.", [
        ("/docs/integrations/gemini/", "Google Gemini", "Use Google's Gemini API for cloud-powered AI."),
        ("/docs/integrations/ollama/", "Ollama", "Run local AI models for offline development."),
        ("/docs/integrations/openrouter/", "OpenRouter", "Access multiple AI models through OpenRouter."),
        ("/docs/integrations/mcp/", "Model Context Protocol", "Extend agent capabilities with MCP tools."),
        ("/docs/integrations/acp/", "Agent Communication Protocol", "Enable multi-agent communication."),
    ]),
    "architecture": ("Architecture", "Deep dive into OmniIDE's technical architecture, security model, and build system.", [
        ("/docs/architecture/overview/", "Architecture Overview", "High-level system architecture and design."),
        ("/docs/architecture/vscode-core/", "VS Code Core", "How OmniIDE extends the VS Code foundation."),
        ("/docs/architecture/security/", "Security Model", "Security principles and threat model."),
        ("/docs/architecture/build-system/", "Build System", "Build toolchain and release pipeline."),
    ]),
    "guides": ("Guides", "Step-by-step guides for setting up and using OmniIDE's key features.", [
        ("/docs/guides/api-key-setup/", "API Key Setup", "Configure your Google Gemini API key."),
        ("/docs/guides/ollama-setup/", "Ollama Local Setup", "Set up Ollama for offline AI development."),
        ("/docs/guides/workspace-config/", "Workspace Configuration", "Configure workspaces and project settings."),
        ("/docs/guides/keyboard-shortcuts/", "Keyboard Shortcuts", "Essential keyboard shortcuts reference."),
        ("/docs/guides/autonomous-workflows/", "Autonomous Workflows", "Set up end-to-end autonomous coding workflows."),
        ("/docs/guides/agent-commands/", "Agent Commands", "Command reference for the Omni-Agent."),
        ("/docs/guides/sandbox-config/", "Sandbox Configuration", "Configure the hardened sandbox environment."),
    ]),
    "reference": ("Reference", "Complete reference documentation for CLI, settings, keybindings, and APIs.", [
        ("/docs/reference/cli/", "CLI Reference", "Command-line interface documentation."),
        ("/docs/reference/settings/", "Settings Reference", "All configurable settings explained."),
        ("/docs/reference/keybindings/", "Keybindings", "Default and custom keybinding reference."),
        ("/docs/reference/changelog/", "Changelog", "Version history and release notes."),
        ("/docs/reference/api/", "API Reference", "Extension and plugin API documentation."),
    ]),
    "troubleshooting": ("Troubleshooting", "Solutions for common issues, agent errors, and performance optimization.", [
        ("/docs/troubleshooting/common-issues/", "Common Issues", "Frequently encountered problems and fixes."),
        ("/docs/troubleshooting/agent-errors/", "Agent Errors", "Understanding and resolving agent errors."),
        ("/docs/troubleshooting/performance/", "Performance", "Tips for optimizing IDE performance."),
        ("/docs/troubleshooting/faq/", "FAQ", "Frequently asked questions about OmniIDE."),
    ]),
}

for section_slug, (section_title, section_desc, pages) in section_index_data.items():
    cards_html = '<div class="feature-grid">'
    for href, title, desc in pages:
        cards_html += f'''<a href="{href}" class="related-card" style="text-decoration:none">
    <div class="related-card-title">{title}</div>
    <div class="related-card-desc">{desc}</div>
</a>'''
    cards_html += '</div>'
    content = f'''<h1>{section_title}</h1>
<p>{section_desc}</p>
{cards_html}'''
    build_doc_page(f"/docs/{section_slug}/", section_title,
        f"{section_title} — OmniIDE documentation for {section_desc.lower()}",
        content)


# ──── CORE CONCEPTS ────

build_doc_page("/docs/core-concepts/omni-agent/", "Omni-Agent",
    "The Omni-Agent is OmniIDE's autonomous coding engine — learn how it writes, debugs, and runs code with zero human intervention.",
    '''<h1>Omni-Agent</h1>
    <p>The Omni-Agent is the core autonomous engine inside OmniIDE. It is a goal-oriented AI system that writes, runs, debugs, and fixes code without requiring human intervention at every step.</p>
    
    <h2>How It Works</h2>
    <p>The Omni-Agent operates on a simple but powerful loop:</p>
    <ol>
        <li><strong>Understand</strong> — Parse the user's natural language instruction and decompose it into actionable development tasks</li>
        <li><strong>Plan</strong> — Generate a step-by-step execution plan for code generation, file creation, and command execution</li>
        <li><strong>Execute</strong> — Write code, create files, and run terminal commands inside the <a href="/docs/core-concepts/hardened-sandbox/">Hardened Sandbox</a></li>
        <li><strong>Verify</strong> — Check the output for errors or unexpected behavior</li>
        <li><strong>Heal</strong> — If errors are detected, analyze root cause, generate fixes, and re-execute (the <a href="/docs/core-concepts/self-healing/">Self-Healing Loop</a>)</li>
    </ol>
    
    <h2>LLM Backend</h2>
    <p>The agent supports two AI backends:</p>
    <ul>
        <li><strong><a href="/docs/integrations/gemini/">Google Gemini API</a></strong> — State-of-the-art cloud reasoning for complex tasks</li>
        <li><strong><a href="/docs/integrations/ollama/">Ollama</a></strong> — Local model execution for offline, privacy-first development</li>
    </ul>
    
    <h2>Capabilities</h2>
    <table>
        <tr><th>Capability</th><th>Description</th></tr>
        <tr><td>Code Generation</td><td>Writes complete files, functions, and modules from natural language</td></tr>
        <tr><td>File Management</td><td>Creates, reads, modifies, and deletes files across the workspace</td></tr>
        <tr><td>Terminal Execution</td><td>Runs shell commands, installs dependencies, starts servers</td></tr>
        <tr><td>Error Recovery</td><td>Catches terminal errors and generates corrective code automatically</td></tr>
        <tr><td>Multi-File Editing</td><td>Handles refactors that span multiple files simultaneously</td></tr>
        <tr><td>Context Awareness</td><td>Understands your codebase structure, dependencies, and coding patterns</td></tr>
    </table>
    
    <h2>Agent Invocation</h2>
    <p>Invoke the agent through the Omni-Agent panel with natural language:</p>
    <pre><code>// Example instructions:
"Create a REST API with authentication using JWT"
"Refactor the database module to use connection pooling"
"Fix the failing test in user.test.js and re-run the test suite"
"Add error handling to all API endpoints"</code></pre>
    
    <div class="info-box note"><strong>Autonomy levels:</strong> The agent operates fully autonomously by default. You can configure <code>omni.agent.confirmBeforeExecute</code> to require approval before running terminal commands.</div>
    
    <h2>Related Concepts</h2>
    <ul>
        <li><a href="/docs/core-concepts/agentic-loop/">Agentic Loop</a> — The execution cycle powering the agent</li>
        <li><a href="/docs/core-concepts/self-healing/">Self-Healing Terminal</a> — Automatic error recovery</li>
        <li><a href="/docs/core-concepts/hardened-sandbox/">Hardened Sandbox</a> — Secure execution environment</li>
        <li><a href="/docs/core-concepts/execution-kernel/">Execution Kernel</a> — Low-level command execution engine</li>
    </ul>''',
    prev_link=("/docs/getting-started/configuration/", "Configuration"),
    next_link=("/docs/core-concepts/agentic-loop/", "Agentic Loop"),
    related=[
        ("/docs/core-concepts/agentic-loop/", "Agentic Loop", "The execution cycle behind autonomous coding"),
        ("/docs/core-concepts/self-healing/", "Self-Healing Terminal", "Automatic error detection and recovery"),
        ("/docs/core-concepts/hardened-sandbox/", "Hardened Sandbox", "Secure sandboxed execution"),
    ])


# ──── Build remaining core concept pages more concisely ────

core_concepts = [
    ("agentic-loop", "Agentic Loop", "The Agentic Loop is OmniIDE's core execution cycle — understand, plan, execute, verify, heal. This autonomous feedback loop powers every Omni-Agent interaction.",
     '''<h1>Agentic Loop</h1>
    <p>The Agentic Loop is the fundamental execution pattern that makes OmniIDE autonomous. Unlike traditional AI assistants that generate code and stop, OmniIDE's loop continuously executes, observes results, and self-corrects until the task is complete.</p>
    
    <h2>The Five Phases</h2>
    <h3>1. Understand</h3>
    <p>The agent parses your natural language instruction and builds a semantic understanding of the task requirements, considering the current workspace context, existing code, dependencies, and file structure.</p>
    
    <h3>2. Plan</h3>
    <p>A step-by-step execution plan is generated, decomposing the high-level goal into atomic development actions: file creation, code writing, dependency installation, and command execution.</p>
    
    <h3>3. Execute</h3>
    <p>Each planned action is executed inside the <a href="/docs/core-concepts/hardened-sandbox/">Hardened Sandbox</a>. Code is written to files, terminal commands are run, and the workspace evolves toward the goal state.</p>
    
    <h3>4. Verify</h3>
    <p>After each execution step, the <a href="/docs/core-concepts/verification/">Verification Engine</a> checks for errors — terminal exit codes, stack traces, compilation failures, and test results are all analyzed.</p>
    
    <h3>5. Heal</h3>
    <p>If verification detects a failure, the <a href="/docs/core-concepts/recovery/">Recovery System</a> activates. The error is fed back to the LLM, a corrective patch is generated, and the loop returns to the Execute phase.</p>
    
    <div class="info-box tip"><strong>Convergence:</strong> The loop continues until either the task succeeds or the maximum retry count (<code>omni.agent.maxRetries</code>) is reached. Most tasks converge within 1-3 iterations.</div>
    
    <h2>Comparison to Traditional Development</h2>
    <table>
        <tr><th>Aspect</th><th>Traditional IDE</th><th>OmniIDE Agentic Loop</th></tr>
        <tr><td>Error handling</td><td>Manual debugging</td><td>Automatic detection + fix</td></tr>
        <tr><td>Code execution</td><td>Manual terminal commands</td><td>Autonomous execution</td></tr>
        <tr><td>Iteration speed</td><td>Minutes per fix</td><td>Seconds per fix</td></tr>
        <tr><td>Context retention</td><td>Requires re-reading code</td><td>Full workspace awareness</td></tr>
    </table>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/core-concepts/omni-agent/">Omni-Agent</a> — The autonomous coding engine</li>
        <li><a href="/docs/core-concepts/execution-kernel/">Execution Kernel</a> — How commands are executed</li>
        <li><a href="/docs/core-concepts/trajectory/">Trajectory System</a> — Tracking agent actions</li>
    </ul>''',
     ("/docs/core-concepts/omni-agent/", "Omni-Agent"),
     ("/docs/core-concepts/self-healing/", "Self-Healing Terminal")),

    ("self-healing", "Self-Healing Terminal", "OmniIDE's self-healing terminal catches runtime errors, analyzes root causes, generates fixes, and re-executes automatically.",
     '''<h1>Self-Healing Terminal</h1>
    <p>The Self-Healing Terminal is one of OmniIDE's defining features. When a command fails — whether it is a compilation error, a missing dependency, or a runtime exception — the terminal does not just display the error. It actively fixes the problem.</p>
    
    <h2>How Self-Healing Works</h2>
    <ol>
        <li><strong>Error Detection</strong> — The terminal monitors stdout and stderr for error patterns, non-zero exit codes, and stack traces</li>
        <li><strong>Root Cause Analysis</strong> — The error output is sent to the LLM (Gemini or Ollama) with full workspace context</li>
        <li><strong>Fix Generation</strong> — The LLM generates a corrective patch — code changes, dependency installs, or configuration updates</li>
        <li><strong>Automatic Re-execution</strong> — The fix is applied and the original command is re-run</li>
    </ol>
    
    <h2>Example Scenario</h2>
    <pre><code>$ npm start
> node server.js

Error: Cannot find module 'express'

// Agent detects the error
// Agent runs: npm install express
// Agent re-runs: npm start
// Server starts successfully ✓</code></pre>
    
    <div class="info-box note"><strong>Safety:</strong> All healing operations run inside the <a href="/docs/core-concepts/hardened-sandbox/">Hardened Sandbox</a>. The agent cannot modify files outside your workspace or execute system-level commands.</div>
    
    <h2>Supported Error Types</h2>
    <ul>
        <li>Module not found / import errors</li>
        <li>Syntax and compilation errors</li>
        <li>Runtime exceptions and crashes</li>
        <li>Missing dependencies</li>
        <li>Configuration errors</li>
        <li>Permission issues (within sandbox scope)</li>
        <li>Test failures</li>
    </ul>
    
    <h2>Configuration</h2>
    <pre><code>{
  "omni.selfHealing.enabled": true,
  "omni.selfHealing.maxAttempts": 3,
  "omni.selfHealing.autoApply": true
}</code></pre>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/core-concepts/agentic-loop/">Agentic Loop</a> — The execution cycle that drives self-healing</li>
        <li><a href="/docs/core-concepts/verification/">Verification Engine</a> — How errors are detected</li>
        <li><a href="/docs/core-concepts/recovery/">Recovery System</a> — The fix generation pipeline</li>
    </ul>''',
     ("/docs/core-concepts/agentic-loop/", "Agentic Loop"),
     ("/docs/core-concepts/hardened-sandbox/", "Hardened Sandbox")),

    ("hardened-sandbox", "Hardened Sandbox", "OmniIDE's Hardened Sandbox isolates all autonomous agent operations from your host system for maximum security.",
     '''<h1>Hardened Sandbox</h1>
    <p>The Hardened Sandbox is OmniIDE's security perimeter. Every command executed by the Omni-Agent runs inside this isolated environment, protecting your host operating system from unintended side effects.</p>
    
    <h2>Why a Sandbox?</h2>
    <p>Autonomous agents execute code without human review at every step. This introduces risk — a malformed command could delete files, install malware, or corrupt system state. The Hardened Sandbox ensures that agent operations are contained.</p>
    
    <h2>Security Boundaries</h2>
    <table>
        <tr><th>Boundary</th><th>Policy</th></tr>
        <tr><td>File System</td><td>Agent can only read/write within the current workspace</td></tr>
        <tr><td>Network</td><td>Configurable — disabled by default for sandbox commands</td></tr>
        <tr><td>Process Execution</td><td>Commands run in an isolated process tree</td></tr>
        <tr><td>Environment</td><td>Sandboxed environment variables — no host env leakage</td></tr>
        <tr><td>Timeout</td><td>Commands are killed after configurable timeout (default: 30s)</td></tr>
    </table>
    
    <h2>Configuration</h2>
    <pre><code>{
  "omni.sandbox.enabled": true,
  "omni.sandbox.timeout": 30000,
  "omni.sandbox.allowNetwork": false,
  "omni.sandbox.allowFileWrite": true,
  "omni.sandbox.allowedPaths": ["./src", "./tests"]
}</code></pre>
    
    <div class="info-box warning"><strong>Warning:</strong> Disabling the sandbox (<code>omni.sandbox.enabled: false</code>) allows the agent to execute commands with full system access. Only do this if you fully trust the agent's output.</div>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/core-concepts/omni-agent/">Omni-Agent</a> — The autonomous engine</li>
        <li><a href="/docs/architecture/security/">Security Model</a> — Full security architecture</li>
        <li><a href="/docs/guides/sandbox-config/">Sandbox Configuration Guide</a> — Advanced sandbox setup</li>
    </ul>''',
     ("/docs/core-concepts/self-healing/", "Self-Healing Terminal"),
     ("/docs/core-concepts/execution-kernel/", "Execution Kernel")),

    ("execution-kernel", "Execution Kernel", "The Execution Kernel is OmniIDE's low-level runtime that manages command execution, process isolation, and output capture.",
     '''<h1>Execution Kernel</h1>
    <p>The Execution Kernel is the low-level runtime that sits between the Omni-Agent and the operating system. It manages process spawning, output capture, error detection, and sandbox enforcement.</p>
    
    <h2>Responsibilities</h2>
    <ul>
        <li><strong>Process Management</strong> — Spawns and monitors child processes for terminal commands</li>
        <li><strong>Output Capture</strong> — Captures stdout and stderr streams in real-time for agent analysis</li>
        <li><strong>Exit Code Monitoring</strong> — Detects non-zero exit codes to trigger self-healing</li>
        <li><strong>Timeout Enforcement</strong> — Kills runaway processes that exceed the configured timeout</li>
        <li><strong>Sandbox Enforcement</strong> — Applies file system and network restrictions</li>
    </ul>
    
    <h2>Architecture</h2>
    <p>The Execution Kernel is implemented in TypeScript/Node.js as part of the VS Code core extension system. It uses Node.js <code>child_process</code> APIs with custom wrappers for sandboxing and monitoring.</p>
    
    <pre><code>// Simplified kernel execution flow
const result = await kernel.execute({
  command: "npm install express",
  cwd: workspace.rootPath,
  timeout: 30000,
  sandbox: true
});

if (result.exitCode !== 0) {
  await agent.heal(result.stderr);
}</code></pre>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/core-concepts/hardened-sandbox/">Hardened Sandbox</a> — Security isolation layer</li>
        <li><a href="/docs/core-concepts/agentic-loop/">Agentic Loop</a> — The execution cycle</li>
        <li><a href="/docs/architecture/overview/">Architecture Overview</a> — Full system architecture</li>
    </ul>''',
     ("/docs/core-concepts/hardened-sandbox/", "Hardened Sandbox"),
     ("/docs/core-concepts/trajectory/", "Trajectory System")),

    ("trajectory", "Trajectory System", "The Trajectory System records every agent action for debugging, replay, and analysis of autonomous coding sessions.",
     '''<h1>Trajectory System</h1>
    <p>The Trajectory System is OmniIDE's action logging infrastructure. Every step the Omni-Agent takes — every file write, command execution, and code generation — is recorded in a structured trajectory that can be reviewed, debugged, and replayed.</p>
    
    <h2>What Gets Recorded</h2>
    <ul>
        <li>Agent instructions (user prompts)</li>
        <li>Generated execution plans</li>
        <li>File creation and modification events</li>
        <li>Terminal commands and their outputs</li>
        <li>Error detection and healing attempts</li>
        <li>Final success or failure state</li>
    </ul>
    
    <h2>Trajectory Structure</h2>
    <pre><code>{
  "sessionId": "abc-123",
  "timestamp": "2026-06-01T10:00:00Z",
  "steps": [
    { "type": "plan", "content": "Create Express server" },
    { "type": "file_write", "path": "server.js", "content": "..." },
    { "type": "terminal", "command": "npm install express", "exitCode": 0 },
    { "type": "terminal", "command": "node server.js", "exitCode": 0 },
    { "type": "success", "message": "Server running on port 3000" }
  ]
}</code></pre>
    
    <h2>Use Cases</h2>
    <ul>
        <li><strong>Debugging</strong> — Review exactly what the agent did when something went wrong</li>
        <li><strong>Learning</strong> — Understand the agent's decision-making process</li>
        <li><strong>Auditing</strong> — Track all autonomous operations for compliance</li>
    </ul>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/core-concepts/memory/">Memory Architecture</a> — How the agent retains context</li>
        <li><a href="/docs/core-concepts/verification/">Verification Engine</a> — Error detection system</li>
    </ul>''',
     ("/docs/core-concepts/execution-kernel/", "Execution Kernel"),
     ("/docs/core-concepts/memory/", "Memory Architecture")),

    ("memory", "Memory Architecture", "OmniIDE's memory system gives the Omni-Agent workspace-aware context retention across coding sessions.",
     '''<h1>Memory Architecture</h1>
    <p>The Memory Architecture provides the Omni-Agent with persistent context about your workspace, coding patterns, and previous interactions. This enables more accurate code generation and fewer errors over time.</p>
    
    <h2>Memory Layers</h2>
    <ul>
        <li><strong>Workspace Memory</strong> — File structure, dependency graph, and project configuration</li>
        <li><strong>Session Memory</strong> — Current conversation context and recent actions</li>
        <li><strong>Pattern Memory</strong> — Learned coding patterns and conventions from your codebase</li>
    </ul>
    
    <h2>How Memory Improves Agent Performance</h2>
    <p>Without memory, every agent interaction starts from scratch. With memory, the agent knows:</p>
    <ul>
        <li>Your project's tech stack and architecture</li>
        <li>Naming conventions and code style</li>
        <li>Previously successful patterns</li>
        <li>Known issues and workarounds</li>
    </ul>
    
    <div class="info-box note"><strong>Privacy:</strong> All memory is stored locally on your machine. It is never transmitted to external servers. Memory data is excluded from any cloud API calls.</div>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/core-concepts/trajectory/">Trajectory System</a> — Action logging</li>
        <li><a href="/docs/core-concepts/verification/">Verification Engine</a> — Error detection</li>
    </ul>''',
     ("/docs/core-concepts/trajectory/", "Trajectory System"),
     ("/docs/core-concepts/verification/", "Verification Engine")),

    ("verification", "Verification Engine", "The Verification Engine validates every agent action — checking exit codes, parsing errors, and confirming expected outcomes.",
     '''<h1>Verification Engine</h1>
    <p>The Verification Engine is the quality gate in OmniIDE's agentic loop. After every execution step, it validates whether the action succeeded and triggers healing if it did not.</p>
    
    <h2>Verification Methods</h2>
    <ul>
        <li><strong>Exit Code Analysis</strong> — Non-zero exit codes indicate command failure</li>
        <li><strong>Error Pattern Matching</strong> — Regex-based detection of common error patterns in stdout/stderr</li>
        <li><strong>File System Validation</strong> — Confirms expected files were created or modified</li>
        <li><strong>Output Assertion</strong> — Checks for expected output strings or patterns</li>
    </ul>
    
    <h2>Supported Error Patterns</h2>
    <table>
        <tr><th>Language</th><th>Pattern Examples</th></tr>
        <tr><td>Node.js</td><td>Cannot find module, SyntaxError, TypeError</td></tr>
        <tr><td>Python</td><td>ImportError, IndentationError, ModuleNotFoundError</td></tr>
        <tr><td>General</td><td>ENOENT, Permission denied, Connection refused</td></tr>
    </table>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/core-concepts/recovery/">Recovery System</a> — What happens after verification fails</li>
        <li><a href="/docs/core-concepts/agentic-loop/">Agentic Loop</a> — The full execution cycle</li>
    </ul>''',
     ("/docs/core-concepts/memory/", "Memory Architecture"),
     ("/docs/core-concepts/recovery/", "Recovery System")),

    ("recovery", "Recovery System", "OmniIDE's Recovery System generates and applies fixes when the Verification Engine detects failures during autonomous execution.",
     '''<h1>Recovery System</h1>
    <p>The Recovery System is the final piece of OmniIDE's self-healing architecture. When the <a href="/docs/core-concepts/verification/">Verification Engine</a> detects a failure, the Recovery System generates corrective actions and re-executes.</p>
    
    <h2>Recovery Pipeline</h2>
    <ol>
        <li><strong>Error Context Assembly</strong> — Collects the error message, stack trace, related source files, and workspace state</li>
        <li><strong>LLM Analysis</strong> — Sends the error context to Gemini or Ollama for root cause analysis</li>
        <li><strong>Fix Generation</strong> — The LLM produces a structured fix: code changes, commands, or configuration updates</li>
        <li><strong>Fix Application</strong> — The fix is applied to the workspace</li>
        <li><strong>Re-execution</strong> — The original command is re-run to verify the fix worked</li>
    </ol>
    
    <h2>Retry Behavior</h2>
    <p>The recovery system will attempt up to <code>omni.agent.maxRetries</code> (default: 3) healing iterations. If the issue persists after all retries, the agent reports the failure and asks for human guidance.</p>
    
    <div class="info-box tip"><strong>Success rate:</strong> In testing, the self-healing recovery resolves 80%+ of common development errors (missing dependencies, syntax errors, import issues) on the first attempt.</div>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/core-concepts/verification/">Verification Engine</a> — Error detection</li>
        <li><a href="/docs/core-concepts/self-healing/">Self-Healing Terminal</a> — The user-facing healing experience</li>
        <li><a href="/docs/core-concepts/agentic-loop/">Agentic Loop</a> — The execution cycle</li>
    </ul>''',
     ("/docs/core-concepts/verification/", "Verification Engine"),
     None),
]

for slug, title, desc, content, prev_data, next_data in core_concepts:
    prev_link = prev_data if isinstance(prev_data, tuple) else None
    next_link = next_data if isinstance(next_data, tuple) else None
    build_doc_page(f"/docs/core-concepts/{slug}/", title, desc, content, prev_link, next_link)


# ──── FEATURES PAGES ────

features_pages = [
    ("ai-coding", "AI-Powered Coding", "OmniIDE's AI-powered coding features — autonomous code generation, intelligent completions, and context-aware assistance.",
     '''<h1>AI-Powered Coding</h1>
    <p>OmniIDE brings AI directly into every aspect of the coding workflow. From generating entire files to intelligent inline completions, the AI engine understands your codebase and accelerates development.</p>
    
    <h2>Code Generation</h2>
    <p>Describe what you want in natural language, and the Omni-Agent generates production-ready code:</p>
    <pre><code>// Agent prompt:
"Create a middleware for JWT authentication with refresh tokens"

// Agent generates: auth.middleware.js, token.service.js, auth.routes.js</code></pre>
    
    <h2>Context-Aware Assistance</h2>
    <p>The agent analyzes your existing codebase to generate code that matches your patterns:</p>
    <ul>
        <li>Follows your naming conventions</li>
        <li>Uses your existing utility functions</li>
        <li>Respects your project structure</li>
        <li>Maintains consistent error handling patterns</li>
    </ul>
    
    <h2>Supported Languages</h2>
    <p>OmniIDE generates code in any language supported by the underlying LLM, including:</p>
    <ul>
        <li>JavaScript / TypeScript</li>
        <li>Python</li>
        <li>Java, C#, Go, Rust</li>
        <li>HTML, CSS, SQL</li>
        <li>And many more</li>
    </ul>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/features/multi-file-refactoring/">Multi-File Refactoring</a></li>
        <li><a href="/docs/core-concepts/omni-agent/">Omni-Agent</a></li>
        <li><a href="/docs/integrations/gemini/">Google Gemini Integration</a></li>
    </ul>'''),
    ("multi-file-refactoring", "Multi-File Refactoring", "Refactor code across your entire project — OmniIDE handles cross-file changes, symbol renaming, and module restructuring autonomously.",
     '''<h1>Multi-File Refactoring</h1>
    <p>Traditional refactoring tools handle single-file changes. OmniIDE's Omni-Agent understands your entire codebase and performs complex refactors across multiple files simultaneously.</p>
    
    <h2>Capabilities</h2>
    <ul>
        <li><strong>Symbol Renaming</strong> — Rename a function, class, or variable across all files</li>
        <li><strong>Module Extraction</strong> — Pull code into new modules with correct imports</li>
        <li><strong>Architecture Changes</strong> — Restructure your project layout with updated references</li>
        <li><strong>API Migration</strong> — Update all call sites when an API signature changes</li>
    </ul>
    
    <h2>Example</h2>
    <pre><code>// Agent prompt:
"Refactor the user service into separate files: 
user.controller.js, user.service.js, user.repository.js.
Update all imports across the project."</code></pre>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/features/ai-coding/">AI-Powered Coding</a></li>
        <li><a href="/docs/core-concepts/omni-agent/">Omni-Agent</a></li>
    </ul>'''),
    ("terminal", "Integrated Terminal", "OmniIDE's integrated terminal with self-healing capabilities, output monitoring, and agent-driven command execution.",
     '''<h1>Integrated Terminal</h1>
    <p>The integrated terminal in OmniIDE is more than a command-line interface — it is an intelligent execution environment connected to the Omni-Agent.</p>
    
    <h2>Features</h2>
    <ul>
        <li><strong>Self-Healing</strong> — Automatic error detection and recovery (<a href="/docs/core-concepts/self-healing/">learn more</a>)</li>
        <li><strong>Agent Integration</strong> — The agent can read terminal output and execute commands</li>
        <li><strong>Multiple Sessions</strong> — Run multiple terminal instances simultaneously</li>
        <li><strong>Output Capture</strong> — All output is captured for agent analysis</li>
    </ul>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/core-concepts/self-healing/">Self-Healing Terminal</a></li>
        <li><a href="/docs/core-concepts/execution-kernel/">Execution Kernel</a></li>
    </ul>'''),
    ("zero-telemetry", "Zero Telemetry", "OmniIDE collects no data — no analytics, no tracking, no watermarks. Your code and workflow remain completely private.",
     '''<h1>Zero Telemetry</h1>
    <p>OmniIDE is built on a foundational privacy principle: <strong>your code is your code</strong>. The IDE collects absolutely no data about your usage, codebase, or development patterns.</p>
    
    <h2>What Zero Telemetry Means</h2>
    <ul>
        <li><strong>No analytics</strong> — No usage tracking, no session recording, no behavior analysis</li>
        <li><strong>No cloud dependency</strong> — The IDE runs entirely locally, even AI can run offline via Ollama</li>
        <li><strong>No watermarks</strong> — Generated code has no attribution markers</li>
        <li><strong>No data collection</strong> — Nothing is sent to OmniIDE servers (there are no OmniIDE servers)</li>
        <li><strong>No phone home</strong> — No update checks, no license validation, no heartbeat</li>
    </ul>
    
    <div class="info-box tip"><strong>API key privacy:</strong> When using the Google Gemini API, your code context is sent to Google for processing. Use <a href="/docs/integrations/ollama/">Ollama</a> for fully offline, private AI execution.</div>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/architecture/security/">Security Model</a></li>
        <li><a href="/docs/integrations/ollama/">Ollama Integration</a></li>
    </ul>'''),
    ("offline-mode", "Offline Mode", "Run OmniIDE completely offline with Ollama — local AI models, no internet required, full privacy.",
     '''<h1>Offline Mode</h1>
    <p>OmniIDE supports fully offline operation when paired with <a href="/docs/integrations/ollama/">Ollama</a> for local AI model execution. This means you can develop with AI assistance without any internet connection.</p>
    
    <h2>How to Go Offline</h2>
    <ol>
        <li>Install <a href="https://ollama.ai" target="_blank" rel="noopener">Ollama</a> on your machine</li>
        <li>Pull a coding model: <code>ollama pull codellama:13b</code></li>
        <li>Configure OmniIDE to use Ollama as the AI backend</li>
        <li>Disconnect from the internet — everything works</li>
    </ol>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/integrations/ollama/">Ollama Integration</a></li>
        <li><a href="/docs/guides/ollama-setup/">Ollama Setup Guide</a></li>
    </ul>'''),
    ("extensions", "Extensions Support", "OmniIDE supports VS Code extensions — install themes, language packs, formatters, and developer tools from the marketplace.",
     '''<h1>Extensions Support</h1>
    <p>Built on the VS Code core, OmniIDE supports a wide range of VS Code extensions. Install themes, language support, formatters, and productivity tools to customize your development environment.</p>
    
    <h2>Installing Extensions</h2>
    <ol>
        <li>Open the Extensions panel (<code>Ctrl+Shift+X</code>)</li>
        <li>Search for the extension you want</li>
        <li>Click Install</li>
    </ol>
    
    <h2>Popular Extensions</h2>
    <ul>
        <li><strong>Prettier</strong> — Code formatting</li>
        <li><strong>ESLint</strong> — JavaScript/TypeScript linting</li>
        <li><strong>Python</strong> — Python language support</li>
        <li><strong>GitLens</strong> — Git supercharged</li>
    </ul>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/features/theming/">Theming & Customization</a></li>
        <li><a href="/docs/architecture/vscode-core/">VS Code Core</a></li>
    </ul>'''),
    ("theming", "Theming & Customization", "Customize OmniIDE's appearance — themes, fonts, icon packs, and UI layout options.",
     '''<h1>Theming & Customization</h1>
    <p>OmniIDE supports full UI customization through the VS Code theming system. Change colors, fonts, icons, and layout to match your preferences.</p>
    
    <h2>Changing Themes</h2>
    <p>Press <code>Ctrl+K Ctrl+T</code> to open the theme picker. OmniIDE ships with several built-in themes and supports all VS Code themes from the marketplace.</p>
    
    <h2>Custom Settings</h2>
    <pre><code>{
  "editor.fontFamily": "'JetBrains Mono', monospace",
  "editor.fontSize": 14,
  "editor.lineHeight": 1.7,
  "workbench.colorTheme": "One Dark Pro"
}</code></pre>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/features/extensions/">Extensions Support</a></li>
        <li><a href="/docs/reference/settings/">Settings Reference</a></li>
    </ul>'''),
    ("git-integration", "Git Integration", "Built-in Git support in OmniIDE — staging, committing, branching, diff viewing, and merge conflict resolution.",
     '''<h1>Git Integration</h1>
    <p>OmniIDE includes full Git integration powered by the VS Code source control system. Stage changes, commit, branch, view diffs, and resolve merge conflicts — all within the IDE.</p>
    
    <h2>Features</h2>
    <ul>
        <li><strong>Source Control Panel</strong> — View changed files, stage, and commit</li>
        <li><strong>Inline Diffs</strong> — See line-by-line changes in the editor</li>
        <li><strong>Branch Management</strong> — Create, switch, and merge branches</li>
        <li><strong>Merge Conflict Resolution</strong> — Visual merge conflict editor</li>
        <li><strong>Git Log</strong> — Browse commit history</li>
    </ul>
    
    <h2>Agent + Git</h2>
    <p>The Omni-Agent can also execute Git commands autonomously:</p>
    <pre><code>"Create a new feature branch, implement the login page, 
commit the changes, and push to remote."</code></pre>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/features/ai-coding/">AI-Powered Coding</a></li>
        <li><a href="/docs/core-concepts/omni-agent/">Omni-Agent</a></li>
    </ul>'''),
    ("debugging", "Debugging", "Debug your code in OmniIDE — breakpoints, variable inspection, call stacks, and AI-assisted debugging with the Omni-Agent.",
     '''<h1>Debugging</h1>
    <p>OmniIDE provides a full debugging experience through the VS Code debug adapter system, enhanced with AI-assisted error analysis from the Omni-Agent.</p>
    
    <h2>Debugging Features</h2>
    <ul>
        <li><strong>Breakpoints</strong> — Set breakpoints by clicking the gutter</li>
        <li><strong>Variable Inspection</strong> — Hover over variables to see their values</li>
        <li><strong>Call Stack</strong> — Navigate the execution call stack</li>
        <li><strong>Watch Expressions</strong> — Monitor specific expressions during execution</li>
        <li><strong>Debug Console</strong> — Evaluate expressions at runtime</li>
    </ul>
    
    <h2>AI-Assisted Debugging</h2>
    <p>Ask the Omni-Agent to help debug issues:</p>
    <pre><code>"The /users endpoint returns 500. Debug and fix the issue."</code></pre>
    <p>The agent will analyze the error, identify the root cause, and generate a fix.</p>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/core-concepts/self-healing/">Self-Healing Terminal</a></li>
        <li><a href="/docs/features/terminal/">Integrated Terminal</a></li>
    </ul>'''),
    ("snippets", "Code Snippets", "Create and use code snippets in OmniIDE — custom templates, language-specific shortcuts, and AI-generated snippet libraries.",
     '''<h1>Code Snippets</h1>
    <p>OmniIDE supports VS Code's snippet system. Create reusable code templates, use built-in language snippets, or let the Omni-Agent generate snippet libraries for your project.</p>
    
    <h2>Using Snippets</h2>
    <p>Type a snippet prefix in the editor and press <code>Tab</code> to expand. For example, typing <code>log</code> and pressing Tab inserts <code>console.log()</code>.</p>
    
    <h2>Custom Snippets</h2>
    <p>Create your own snippets via <strong>File → Preferences → Configure User Snippets</strong>:</p>
    <pre><code>{
  "React Component": {
    "prefix": "rfc",
    "body": [
      "export function ${1:Component}() {",
      "  return (",
      "    <div>$0</div>",
      "  );",
      "}"
    ]
  }
}</code></pre>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/features/ai-coding/">AI-Powered Coding</a></li>
        <li><a href="/docs/reference/keybindings/">Keybindings Reference</a></li>
    </ul>'''),
]

for slug, title, desc, content in features_pages:
    build_doc_page(f"/docs/features/{slug}/", title, desc, content)


# ──── INTEGRATIONS ────

integrations_pages = [
    ("gemini", "Google Gemini", "Integrate Google Gemini API with OmniIDE for cloud-powered AI coding, advanced reasoning, and autonomous development.",
     '''<h1>Google Gemini Integration</h1>
    <p>Google Gemini is OmniIDE's primary cloud AI backend. It provides state-of-the-art reasoning, code generation, and error analysis capabilities for the Omni-Agent.</p>
    
    <h2>Setup</h2>
    <ol>
        <li>Get a free API key from <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener">Google AI Studio</a></li>
        <li>Open OmniIDE Settings (<code>Ctrl+,</code>)</li>
        <li>Enter your API key in <code>omni.gemini.apiKey</code></li>
    </ol>
    
    <h2>Available Models</h2>
    <table>
        <tr><th>Model</th><th>Best For</th><th>Speed</th></tr>
        <tr><td>gemini-pro</td><td>General coding tasks</td><td>Fast</td></tr>
        <tr><td>gemini-pro-vision</td><td>UI/UX and image analysis</td><td>Medium</td></tr>
    </table>
    
    <h2>Configuration</h2>
    <pre><code>{
  "omni.gemini.apiKey": "your-key-here",
  "omni.gemini.model": "gemini-pro",
  "omni.gemini.maxTokens": 8192,
  "omni.gemini.temperature": 0.1
}</code></pre>
    
    <div class="info-box note"><strong>Privacy:</strong> When using Gemini, your code context is sent to Google for processing. For fully private AI, use <a href="/docs/integrations/ollama/">Ollama</a> instead.</div>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/integrations/ollama/">Ollama</a> — Local AI alternative</li>
        <li><a href="/docs/guides/api-key-setup/">API Key Setup Guide</a></li>
    </ul>'''),
    ("ollama", "Ollama", "Run AI models locally with Ollama integration — offline coding assistance, full privacy, no cloud dependency.",
     '''<h1>Ollama Integration</h1>
    <p>Ollama enables fully local AI model execution within OmniIDE. Run coding models on your own hardware with zero cloud dependency and complete privacy.</p>
    
    <h2>Setup</h2>
    <ol>
        <li>Install Ollama from <a href="https://ollama.ai" target="_blank" rel="noopener">ollama.ai</a></li>
        <li>Pull a coding model: <code>ollama pull codellama:13b</code></li>
        <li>Start the Ollama server: <code>ollama serve</code></li>
        <li>Configure OmniIDE to use Ollama</li>
    </ol>
    
    <h2>Recommended Models</h2>
    <table>
        <tr><th>Model</th><th>Size</th><th>Best For</th></tr>
        <tr><td>codellama:7b</td><td>3.8 GB</td><td>Fast coding on modest hardware</td></tr>
        <tr><td>codellama:13b</td><td>7.3 GB</td><td>Balance of quality and speed</td></tr>
        <tr><td>deepseek-coder:6.7b</td><td>3.8 GB</td><td>Excellent code generation</td></tr>
    </table>
    
    <h2>Configuration</h2>
    <pre><code>{
  "omni.ollama.enabled": true,
  "omni.ollama.endpoint": "http://localhost:11434",
  "omni.ollama.model": "codellama:13b"
}</code></pre>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/integrations/gemini/">Google Gemini</a> — Cloud AI option</li>
        <li><a href="/docs/guides/ollama-setup/">Ollama Setup Guide</a></li>
        <li><a href="/docs/features/offline-mode/">Offline Mode</a></li>
    </ul>'''),
    ("openrouter", "OpenRouter", "Connect OmniIDE to OpenRouter for access to multiple AI models including Claude, GPT-4, and Mixtral.",
     '''<h1>OpenRouter Integration</h1>
    <p>OpenRouter provides a unified API gateway to access multiple AI models. Through OpenRouter, OmniIDE can connect to Claude, GPT-4, Mixtral, and dozens of other models.</p>
    
    <h2>Setup</h2>
    <ol>
        <li>Create an account at <a href="https://openrouter.ai" target="_blank" rel="noopener">openrouter.ai</a></li>
        <li>Generate an API key</li>
        <li>Configure OmniIDE to use OpenRouter as the backend</li>
    </ol>
    
    <h2>Available Models</h2>
    <p>Through OpenRouter, you can access:</p>
    <ul>
        <li>Anthropic Claude (Sonnet, Opus)</li>
        <li>OpenAI GPT-4, GPT-4 Turbo</li>
        <li>Mistral/Mixtral</li>
        <li>DeepSeek Coder</li>
        <li>Meta Llama</li>
    </ul>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/integrations/gemini/">Google Gemini</a></li>
        <li><a href="/docs/integrations/ollama/">Ollama</a></li>
    </ul>'''),
    ("mcp", "Model Context Protocol (MCP)", "OmniIDE supports the Model Context Protocol for standardized tool calling and context sharing between AI models and development environments.",
     '''<h1>Model Context Protocol (MCP)</h1>
    <p>The Model Context Protocol (MCP) is an emerging standard for connecting AI models with external tools and data sources. OmniIDE supports MCP to enable standardized tool calling and context sharing.</p>
    
    <h2>What is MCP?</h2>
    <p>MCP defines a standardized way for AI assistants to:</p>
    <ul>
        <li><strong>Access tools</strong> — File systems, databases, APIs, and development tools</li>
        <li><strong>Share context</strong> — Pass relevant information between the model and tools</li>
        <li><strong>Execute actions</strong> — Run structured operations through well-defined interfaces</li>
    </ul>
    
    <h2>MCP in OmniIDE</h2>
    <p>The Omni-Agent uses MCP-compatible interfaces for:</p>
    <ul>
        <li>File read/write operations</li>
        <li>Terminal command execution</li>
        <li>Workspace analysis</li>
        <li>Extension integration</li>
    </ul>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/integrations/acp/">Agent Communication Protocol</a></li>
        <li><a href="/docs/architecture/overview/">Architecture Overview</a></li>
    </ul>'''),
    ("acp", "Agent Communication Protocol (ACP)", "OmniIDE implements the Agent Communication Protocol for multi-agent coordination and structured inter-agent messaging.",
     '''<h1>Agent Communication Protocol (ACP)</h1>
    <p>The Agent Communication Protocol (ACP) enables structured communication between autonomous agents. In OmniIDE, ACP provides the foundation for multi-agent coordination and tool interoperability.</p>
    
    <h2>ACP in OmniIDE</h2>
    <ul>
        <li><strong>Agent-to-Tool Communication</strong> — Structured message format for tool invocation</li>
        <li><strong>Result Reporting</strong> — Standardized output format for tool results</li>
        <li><strong>Error Propagation</strong> — Consistent error reporting across the agent pipeline</li>
    </ul>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/integrations/mcp/">Model Context Protocol</a></li>
        <li><a href="/docs/core-concepts/omni-agent/">Omni-Agent</a></li>
    </ul>'''),
]

for slug, title, desc, content in integrations_pages:
    build_doc_page(f"/docs/integrations/{slug}/", title, desc, content)


# ──── ARCHITECTURE ────

architecture_pages = [
    ("overview", "Architecture Overview", "OmniIDE's system architecture — VS Code core, Omni-Agent, Execution Kernel, Hardened Sandbox, and AI integration layer.",
     '''<h1>Architecture Overview</h1>
    <p>OmniIDE v3.0 is built on a modern, layered architecture with the VS Code core as the foundation, the Omni-Agent as the intelligence layer, and the Hardened Sandbox as the security perimeter.</p>
    
    <h2>System Layers</h2>
    <ol>
        <li><strong>Editor Layer</strong> — VS Code core (TypeScript/Node.js) providing the familiar editor experience, extensions, and UI</li>
        <li><strong>Agent Layer</strong> — Omni-Agent orchestrating autonomous development workflows</li>
        <li><strong>AI Layer</strong> — Google Gemini API and Ollama for language model inference</li>
        <li><strong>Execution Layer</strong> — Execution Kernel managing process spawning and output capture</li>
        <li><strong>Security Layer</strong> — Hardened Sandbox isolating all autonomous operations</li>
    </ol>
    
    <h2>Data Flow</h2>
    <pre><code>User Instruction
    → Omni-Agent (parse + plan)
    → AI Layer (Gemini / Ollama)
    → Execution Kernel (run commands)
    → Hardened Sandbox (isolate)
    → Verification Engine (check results)
    → Recovery System (if error → loop back)
    → Success Output</code></pre>
    
    <h2>Technology Stack</h2>
    <table>
        <tr><th>Component</th><th>Technology</th></tr>
        <tr><td>Editor Core</td><td>VS Code (TypeScript, Node.js)</td></tr>
        <tr><td>Build System</td><td>Gulp</td></tr>
        <tr><td>AI (Cloud)</td><td>Google Gemini API</td></tr>
        <tr><td>AI (Local)</td><td>Ollama</td></tr>
        <tr><td>Runtime</td><td>Node.js, Electron</td></tr>
        <tr><td>Platform</td><td>Windows 10/11</td></tr>
    </table>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/architecture/vscode-core/">VS Code Core</a></li>
        <li><a href="/docs/architecture/security/">Security Model</a></li>
        <li><a href="/docs/core-concepts/omni-agent/">Omni-Agent</a></li>
    </ul>'''),
    ("vscode-core", "VS Code Core", "OmniIDE is built on the VS Code core — understand the foundation, extension system, and custom modifications.",
     '''<h1>VS Code Core</h1>
    <p>OmniIDE v3.0 is built on the open-source VS Code core, providing the familiar, high-performance editor experience that millions of developers know and trust.</p>
    
    <h2>Why VS Code?</h2>
    <ul>
        <li><strong>Production-ready</strong> — Battle-tested editor used by millions</li>
        <li><strong>Extension ecosystem</strong> — Access to thousands of extensions</li>
        <li><strong>Performance</strong> — Optimized for large codebases</li>
        <li><strong>Customizability</strong> — Full theme and configuration support</li>
        <li><strong>Familiar UX</strong> — Zero learning curve for VS Code users</li>
    </ul>
    
    <h2>Custom Modifications</h2>
    <p>OmniIDE extends the VS Code core with:</p>
    <ul>
        <li><strong>Omni-Agent Panel</strong> — Custom sidebar for autonomous coding</li>
        <li><strong>Self-Healing Terminal</strong> — Enhanced terminal with error detection</li>
        <li><strong>Enterprise Branding</strong> — Custom theme overrides and branding</li>
        <li><strong>Watermark Removal</strong> — Clean, professional appearance</li>
    </ul>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/architecture/overview/">Architecture Overview</a></li>
        <li><a href="/docs/architecture/build-system/">Build System</a></li>
    </ul>'''),
    ("security", "Security Model", "OmniIDE's security architecture — sandboxing, zero telemetry, process isolation, and data protection.",
     '''<h1>Security Model</h1>
    <p>Security is foundational to OmniIDE's design. Autonomous code execution requires robust isolation to prevent unintended system modifications.</p>
    
    <h2>Security Principles</h2>
    <ol>
        <li><strong>Least Privilege</strong> — The agent only has access to the current workspace</li>
        <li><strong>Sandbox Isolation</strong> — All commands run in the <a href="/docs/core-concepts/hardened-sandbox/">Hardened Sandbox</a></li>
        <li><strong>Zero Telemetry</strong> — No data collection, no cloud dependency for the IDE itself</li>
        <li><strong>Timeout Protection</strong> — Runaway processes are killed after configurable timeout</li>
        <li><strong>User Control</strong> — Optional confirmation before executing agent commands</li>
    </ol>
    
    <h2>Threat Model</h2>
    <table>
        <tr><th>Threat</th><th>Mitigation</th></tr>
        <tr><td>Agent deletes system files</td><td>Sandbox restricts file access to workspace</td></tr>
        <tr><td>Malicious code execution</td><td>Process isolation with timeout</td></tr>
        <tr><td>Data exfiltration</td><td>Network access disabled by default in sandbox</td></tr>
        <tr><td>Resource exhaustion</td><td>CPU and memory limits on sandboxed processes</td></tr>
    </table>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/core-concepts/hardened-sandbox/">Hardened Sandbox</a></li>
        <li><a href="/docs/features/zero-telemetry/">Zero Telemetry</a></li>
    </ul>'''),
    ("build-system", "Build System", "OmniIDE's build system — Gulp-based pipeline for TypeScript compilation, asset bundling, and release packaging.",
     '''<h1>Build System</h1>
    <p>OmniIDE uses Gulp as its build system, managing TypeScript compilation, asset bundling, extension packaging, and release generation.</p>
    
    <h2>Build Pipeline</h2>
    <ol>
        <li><strong>TypeScript Compilation</strong> — Compile all source files</li>
        <li><strong>Asset Bundling</strong> — Process and bundle static assets</li>
        <li><strong>Extension Packaging</strong> — Build the Omni-Agent extension</li>
        <li><strong>Electron Packaging</strong> — Create the desktop application</li>
        <li><strong>Installer Generation</strong> — Build the Windows installer</li>
    </ol>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/architecture/overview/">Architecture Overview</a></li>
        <li><a href="/docs/architecture/vscode-core/">VS Code Core</a></li>
    </ul>'''),
]

for slug, title, desc, content in architecture_pages:
    build_doc_page(f"/docs/architecture/{slug}/", title, desc, content)


# ──── GUIDES ────

guides_pages = [
    ("api-key-setup", "API Key Setup", "Set up your Google Gemini API key for OmniIDE — step-by-step guide with free tier information.",
     '''<h1>API Key Setup</h1>
    <p>OmniIDE uses the Google Gemini API for cloud-powered AI features. This guide walks you through getting and configuring your API key.</p>
    
    <h2>Get Your API Key</h2>
    <ol>
        <li>Visit <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener">Google AI Studio</a></li>
        <li>Sign in with your Google account</li>
        <li>Click "Create API Key"</li>
        <li>Copy the generated key</li>
    </ol>
    
    <div class="info-box tip"><strong>Free tier:</strong> Google Gemini API offers a generous free tier. For most individual developers, the free tier is sufficient for daily use.</div>
    
    <h2>Configure in OmniIDE</h2>
    <ol>
        <li>Open OmniIDE</li>
        <li>Press <code>Ctrl+,</code> to open Settings</li>
        <li>Search for "Gemini API Key"</li>
        <li>Paste your API key</li>
    </ol>
    
    <h2>Verify</h2>
    <p>Open the Omni-Agent panel and send a test message. If the agent responds, your API key is configured correctly.</p>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/integrations/gemini/">Google Gemini Integration</a></li>
        <li><a href="/docs/guides/ollama-setup/">Ollama Setup</a> — Alternative for offline use</li>
    </ul>'''),
    ("ollama-setup", "Ollama Local Setup", "Set up Ollama for fully offline AI coding in OmniIDE — install models and configure local inference.",
     '''<h1>Ollama Local Setup</h1>
    <p>Ollama lets you run AI models locally on your machine. This guide covers installation, model selection, and OmniIDE configuration.</p>
    
    <h2>Install Ollama</h2>
    <ol>
        <li>Download from <a href="https://ollama.ai" target="_blank" rel="noopener">ollama.ai</a></li>
        <li>Run the installer</li>
        <li>Verify installation: <code>ollama --version</code></li>
    </ol>
    
    <h2>Pull a Model</h2>
    <pre><code># Recommended for coding
ollama pull codellama:13b

# Lighter alternative
ollama pull codellama:7b

# Start the server
ollama serve</code></pre>
    
    <h2>Configure OmniIDE</h2>
    <pre><code>{
  "omni.ollama.enabled": true,
  "omni.ollama.endpoint": "http://localhost:11434",
  "omni.ollama.model": "codellama:13b"
}</code></pre>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/integrations/ollama/">Ollama Integration</a></li>
        <li><a href="/docs/features/offline-mode/">Offline Mode</a></li>
    </ul>'''),
    ("workspace-config", "Workspace Configuration", "Configure OmniIDE workspaces — per-project settings, folder structure, and multi-root workspaces.",
     '''<h1>Workspace Configuration</h1>
    <p>OmniIDE supports workspace-specific settings that override your global user settings. This is useful for configuring different AI models or sandbox rules per project.</p>
    
    <h2>Creating Workspace Settings</h2>
    <p>Create a <code>.vscode/settings.json</code> file in your project root:</p>
    <pre><code>{
  "omni.gemini.model": "gemini-pro",
  "omni.sandbox.allowNetwork": true,
  "omni.agent.maxRetries": 5
}</code></pre>
    
    <h2>Multi-Root Workspaces</h2>
    <p>OmniIDE supports multi-root workspaces where you can open multiple project folders simultaneously. Each folder can have its own settings.</p>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/getting-started/configuration/">Configuration Overview</a></li>
        <li><a href="/docs/reference/settings/">Settings Reference</a></li>
    </ul>'''),
    ("keyboard-shortcuts", "Keyboard Shortcuts", "Essential keyboard shortcuts for OmniIDE — editor, terminal, agent, and navigation shortcuts.",
     '''<h1>Keyboard Shortcuts</h1>
    <p>OmniIDE inherits VS Code's keyboard shortcut system. Here are the most important shortcuts for productive development.</p>
    
    <h2>Essential Shortcuts</h2>
    <table>
        <tr><th>Action</th><th>Shortcut</th></tr>
        <tr><td>Open Settings</td><td><code>Ctrl+,</code></td></tr>
        <tr><td>Command Palette</td><td><code>Ctrl+Shift+P</code></td></tr>
        <tr><td>Quick File Open</td><td><code>Ctrl+P</code></td></tr>
        <tr><td>Toggle Terminal</td><td><code>Ctrl+`</code></td></tr>
        <tr><td>Toggle Sidebar</td><td><code>Ctrl+B</code></td></tr>
        <tr><td>Find in Files</td><td><code>Ctrl+Shift+F</code></td></tr>
        <tr><td>Go to Definition</td><td><code>F12</code></td></tr>
        <tr><td>Format Document</td><td><code>Shift+Alt+F</code></td></tr>
    </table>
    
    <h2>Agent Shortcuts</h2>
    <table>
        <tr><th>Action</th><th>Shortcut</th></tr>
        <tr><td>Open Omni-Agent Panel</td><td><code>Ctrl+Shift+A</code></td></tr>
        <tr><td>Focus Agent Input</td><td><code>Ctrl+L</code></td></tr>
    </table>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/reference/keybindings/">Full Keybindings Reference</a></li>
        <li><a href="/docs/getting-started/quick-start/">Quick Start Guide</a></li>
    </ul>'''),
    ("autonomous-workflows", "Autonomous Workflows", "Advanced autonomous workflow patterns in OmniIDE — chaining tasks, multi-step operations, and project scaffolding.",
     '''<h1>Autonomous Workflows</h1>
    <p>The Omni-Agent is not limited to single commands. You can describe complex, multi-step development workflows in natural language and let the agent execute them autonomously.</p>
    
    <h2>Full Project Scaffolding</h2>
    <pre><code>"Create a full-stack TypeScript application with:
- Next.js frontend with App Router
- Express API backend
- PostgreSQL database with Prisma ORM
- JWT authentication
- Docker Compose for local development
Set up the project structure, install dependencies, and create initial routes."</code></pre>
    
    <h2>Test-Driven Development</h2>
    <pre><code>"Write unit tests for the UserService class using Jest.
Cover all public methods. Then run the tests and fix any failures."</code></pre>
    
    <h2>Continuous Refactoring</h2>
    <pre><code>"Analyze the src/ directory for code smells. Refactor duplicated 
logic into shared utilities. Update all imports."</code></pre>
    
    <h2>Best Practices</h2>
    <ul>
        <li>Be specific about your requirements</li>
        <li>Describe the expected output</li>
        <li>Mention technologies and patterns you want</li>
        <li>Let the agent iterate — it will self-correct</li>
    </ul>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/core-concepts/omni-agent/">Omni-Agent</a></li>
        <li><a href="/docs/core-concepts/agentic-loop/">Agentic Loop</a></li>
        <li><a href="/docs/guides/agent-commands/">Agent Commands</a></li>
    </ul>'''),
    ("agent-commands", "Agent Commands", "Common Omni-Agent command patterns — code generation, debugging, refactoring, and project management prompts.",
     '''<h1>Agent Commands</h1>
    <p>The Omni-Agent responds to natural language instructions. Here are proven command patterns for common development tasks.</p>
    
    <h2>Code Generation</h2>
    <pre><code>"Create a REST API with Express for managing products. 
Include GET, POST, PUT, DELETE endpoints."

"Build a React component for a data table with 
sorting, filtering, and pagination."</code></pre>
    
    <h2>Debugging</h2>
    <pre><code>"The tests in auth.test.js are failing. Debug and fix the issues."

"The API returns 500 on POST /users. Find and fix the bug."</code></pre>
    
    <h2>Refactoring</h2>
    <pre><code>"Extract the validation logic from controllers into a 
separate validation middleware."

"Convert all callback-based functions to async/await."</code></pre>
    
    <h2>Project Management</h2>
    <pre><code>"Add ESLint and Prettier configuration for TypeScript."

"Set up GitHub Actions CI/CD pipeline for testing and deployment."</code></pre>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/guides/autonomous-workflows/">Autonomous Workflows</a></li>
        <li><a href="/docs/core-concepts/omni-agent/">Omni-Agent</a></li>
    </ul>'''),
    ("sandbox-config", "Sandbox Configuration", "Configure the Hardened Sandbox — file permissions, network access, timeouts, and allowed paths.",
     '''<h1>Sandbox Configuration</h1>
    <p>The <a href="/docs/core-concepts/hardened-sandbox/">Hardened Sandbox</a> protects your system from unintended agent actions. This guide covers advanced sandbox configuration.</p>
    
    <h2>Settings</h2>
    <pre><code>{
  "omni.sandbox.enabled": true,
  "omni.sandbox.timeout": 30000,
  "omni.sandbox.allowNetwork": false,
  "omni.sandbox.allowFileWrite": true,
  "omni.sandbox.allowedPaths": ["./src", "./tests", "./public"],
  "omni.sandbox.blockedCommands": ["rm -rf", "format", "del /f"]
}</code></pre>
    
    <h2>Security Levels</h2>
    <table>
        <tr><th>Level</th><th>Configuration</th><th>Use Case</th></tr>
        <tr><td>Strict</td><td>No network, limited paths</td><td>High-security environments</td></tr>
        <tr><td>Standard</td><td>No network, workspace access</td><td>Normal development (default)</td></tr>
        <tr><td>Relaxed</td><td>Network allowed, workspace access</td><td>Full-stack development</td></tr>
    </table>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/core-concepts/hardened-sandbox/">Hardened Sandbox</a></li>
        <li><a href="/docs/architecture/security/">Security Model</a></li>
    </ul>'''),
]

for slug, title, desc, content in guides_pages:
    build_doc_page(f"/docs/guides/{slug}/", title, desc, content)


# ──── REFERENCE ────

reference_pages = [
    ("cli", "CLI Reference", "OmniIDE command-line interface reference — all CLI commands, flags, and usage examples.",
     '''<h1>CLI Reference</h1>
    <p>OmniIDE can be launched and configured from the command line.</p>
    
    <h2>Commands</h2>
    <table>
        <tr><th>Command</th><th>Description</th></tr>
        <tr><td><code>omni .</code></td><td>Open current directory in OmniIDE</td></tr>
        <tr><td><code>omni &lt;path&gt;</code></td><td>Open a specific folder or file</td></tr>
        <tr><td><code>omni --version</code></td><td>Display version information</td></tr>
        <tr><td><code>omni --help</code></td><td>Show help information</td></tr>
        <tr><td><code>omni --new-window</code></td><td>Force open in a new window</td></tr>
    </table>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/reference/settings/">Settings Reference</a></li>
    </ul>'''),
    ("settings", "Settings Reference", "Complete reference of all OmniIDE settings — editor, AI, agent, sandbox, and UI configuration options.",
     '''<h1>Settings Reference</h1>
    <p>Complete list of OmniIDE-specific settings. Access via <code>Ctrl+,</code>.</p>
    
    <h2>AI Settings</h2>
    <table>
        <tr><th>Setting</th><th>Type</th><th>Default</th><th>Description</th></tr>
        <tr><td><code>omni.gemini.apiKey</code></td><td>string</td><td>""</td><td>Google Gemini API key</td></tr>
        <tr><td><code>omni.gemini.model</code></td><td>string</td><td>"gemini-pro"</td><td>Gemini model to use</td></tr>
        <tr><td><code>omni.gemini.maxTokens</code></td><td>number</td><td>8192</td><td>Maximum tokens per request</td></tr>
        <tr><td><code>omni.gemini.temperature</code></td><td>number</td><td>0.1</td><td>Response temperature</td></tr>
        <tr><td><code>omni.ollama.enabled</code></td><td>boolean</td><td>false</td><td>Enable Ollama backend</td></tr>
        <tr><td><code>omni.ollama.endpoint</code></td><td>string</td><td>"http://localhost:11434"</td><td>Ollama server URL</td></tr>
        <tr><td><code>omni.ollama.model</code></td><td>string</td><td>"codellama:13b"</td><td>Ollama model to use</td></tr>
    </table>
    
    <h2>Agent Settings</h2>
    <table>
        <tr><th>Setting</th><th>Type</th><th>Default</th><th>Description</th></tr>
        <tr><td><code>omni.agent.autoFix</code></td><td>boolean</td><td>true</td><td>Auto-fix detected errors</td></tr>
        <tr><td><code>omni.agent.maxRetries</code></td><td>number</td><td>3</td><td>Max healing attempts</td></tr>
        <tr><td><code>omni.agent.confirmBeforeExecute</code></td><td>boolean</td><td>false</td><td>Require confirmation for commands</td></tr>
        <tr><td><code>omni.agent.verboseLogging</code></td><td>boolean</td><td>false</td><td>Enable detailed agent logs</td></tr>
    </table>
    
    <h2>Sandbox Settings</h2>
    <table>
        <tr><th>Setting</th><th>Type</th><th>Default</th><th>Description</th></tr>
        <tr><td><code>omni.sandbox.enabled</code></td><td>boolean</td><td>true</td><td>Enable Hardened Sandbox</td></tr>
        <tr><td><code>omni.sandbox.timeout</code></td><td>number</td><td>30000</td><td>Command timeout (ms)</td></tr>
        <tr><td><code>omni.sandbox.allowNetwork</code></td><td>boolean</td><td>false</td><td>Allow network access</td></tr>
        <tr><td><code>omni.sandbox.allowFileWrite</code></td><td>boolean</td><td>true</td><td>Allow file writes</td></tr>
    </table>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/getting-started/configuration/">Configuration Guide</a></li>
        <li><a href="/docs/reference/keybindings/">Keybindings</a></li>
    </ul>'''),
    ("keybindings", "Keybindings", "Complete keybinding reference for OmniIDE — editor, navigation, terminal, and agent keyboard shortcuts.",
     '''<h1>Keybindings Reference</h1>
    <p>Full keybinding reference for OmniIDE. Customize via <strong>File → Preferences → Keyboard Shortcuts</strong> or <code>Ctrl+K Ctrl+S</code>.</p>
    
    <h2>Editor</h2>
    <table>
        <tr><th>Action</th><th>Windows</th></tr>
        <tr><td>Copy Line Down</td><td><code>Shift+Alt+↓</code></td></tr>
        <tr><td>Move Line Up/Down</td><td><code>Alt+↑/↓</code></td></tr>
        <tr><td>Delete Line</td><td><code>Ctrl+Shift+K</code></td></tr>
        <tr><td>Multi-cursor</td><td><code>Ctrl+Alt+↑/↓</code></td></tr>
        <tr><td>Select All Occurrences</td><td><code>Ctrl+Shift+L</code></td></tr>
        <tr><td>Undo/Redo</td><td><code>Ctrl+Z / Ctrl+Y</code></td></tr>
    </table>
    
    <h2>Navigation</h2>
    <table>
        <tr><th>Action</th><th>Windows</th></tr>
        <tr><td>Go to File</td><td><code>Ctrl+P</code></td></tr>
        <tr><td>Go to Symbol</td><td><code>Ctrl+Shift+O</code></td></tr>
        <tr><td>Go to Definition</td><td><code>F12</code></td></tr>
        <tr><td>Go to Line</td><td><code>Ctrl+G</code></td></tr>
    </table>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/guides/keyboard-shortcuts/">Keyboard Shortcuts Guide</a></li>
    </ul>'''),
    ("changelog", "Changelog", "OmniIDE release changelog — version history, new features, bug fixes, and breaking changes.",
     '''<h1>Changelog</h1>
    
    <h2>v3.0.0 (Latest Stable)</h2>
    <p><em>Released: February 2026</em></p>
    <ul>
        <li><strong>Hardened Sandbox</strong> — Isolated execution environment for autonomous operations</li>
        <li><strong>Improved Omni-Agent</strong> — Enhanced reasoning and error recovery</li>
        <li><strong>Production Release</strong> — First stable production-ready release</li>
        <li><strong>Self-Healing Terminal</strong> — Automatic error detection and fix generation</li>
        <li><strong>Multi-File Refactoring</strong> — Cross-file code changes</li>
    </ul>
    
    <h2>v2.0.0</h2>
    <p><em>Released: 2025</em></p>
    <ul>
        <li><strong>VS Code Core Rebuild</strong> — Complete rewrite from Python/FastAPI to TypeScript/Node.js</li>
        <li><strong>Omni-Agent Integration</strong> — Google Gemini API powered autonomous coding</li>
        <li><strong>Watermark Removal</strong> — Clean, professional appearance</li>
    </ul>
    
    <h2>v1.1.0</h2>
    <p><em>Released: 2025</em></p>
    <ul>
        <li>Improved stability</li>
        <li>Glassmorphic UI enhancements</li>
        <li>Basic AI chat integration</li>
    </ul>
    
    <h2>v1.0.0</h2>
    <p><em>Released: 2025</em></p>
    <ul>
        <li>Initial release with hybrid Python/FastAPI architecture</li>
        <li>Experimental AI integration</li>
    </ul>'''),
    ("api", "API Reference", "OmniIDE internal API reference — extension API, agent API, and sandbox API documentation.",
     '''<h1>API Reference</h1>
    <p>OmniIDE exposes internal APIs for extension developers and advanced customization.</p>
    
    <h2>Agent API</h2>
    <pre><code>// Access the Omni-Agent programmatically
const agent = vscode.extensions.getExtension('omniide.omni-agent');

// Send a task to the agent
await agent.exports.execute({
  instruction: "Create a utility function for date formatting",
  workspace: vscode.workspace.rootPath
});</code></pre>
    
    <h2>Sandbox API</h2>
    <pre><code>// Execute a command in the sandbox
const result = await sandbox.run({
  command: "npm test",
  timeout: 60000,
  allowNetwork: false
});</code></pre>
    
    <div class="info-box warning"><strong>Note:</strong> These APIs are subject to change between major versions. Use at your own risk in production extensions.</div>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/architecture/overview/">Architecture Overview</a></li>
        <li><a href="/docs/reference/settings/">Settings Reference</a></li>
    </ul>'''),
]

for slug, title, desc, content in reference_pages:
    build_doc_page(f"/docs/reference/{slug}/", title, desc, content)


# ──── TROUBLESHOOTING ────

troubleshooting_pages = [
    ("common-issues", "Common Issues", "Solutions for common OmniIDE issues — installation problems, performance, AI connectivity, and workspace errors.",
     '''<h1>Common Issues</h1>
    
    <h2>Installation Issues</h2>
    <h3>Windows SmartScreen Warning</h3>
    <p>Windows may show a SmartScreen warning because OmniIDE is a new application. Click "More info" → "Run anyway" to proceed with installation.</p>
    
    <h3>Installer Fails to Complete</h3>
    <p>Ensure you have sufficient disk space (500 MB minimum) and that no antivirus software is blocking the installation.</p>
    
    <h2>AI Connection Issues</h2>
    <h3>Gemini API Not Responding</h3>
    <ul>
        <li>Verify your API key is correct in Settings</li>
        <li>Check your internet connection</li>
        <li>Ensure you have not exceeded the API rate limits</li>
    </ul>
    
    <h3>Ollama Not Connecting</h3>
    <ul>
        <li>Verify Ollama is running: <code>ollama serve</code></li>
        <li>Check the endpoint URL in settings (default: <code>http://localhost:11434</code>)</li>
        <li>Ensure the model is downloaded: <code>ollama list</code></li>
    </ul>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/troubleshooting/agent-errors/">Agent Errors</a></li>
        <li><a href="/docs/troubleshooting/performance/">Performance</a></li>
    </ul>'''),
    ("agent-errors", "Agent Errors", "Troubleshoot Omni-Agent errors — common agent failures, recovery steps, and configuration fixes.",
     '''<h1>Agent Errors</h1>
    
    <h2>Agent Not Responding</h2>
    <p>If the Omni-Agent panel shows no response:</p>
    <ol>
        <li>Check your API key configuration</li>
        <li>Verify internet connectivity (for Gemini)</li>
        <li>Restart the IDE: <code>Ctrl+Shift+P</code> → "Reload Window"</li>
    </ol>
    
    <h2>Self-Healing Loop Not Activating</h2>
    <p>Ensure self-healing is enabled:</p>
    <pre><code>{
  "omni.selfHealing.enabled": true,
  "omni.selfHealing.autoApply": true
}</code></pre>
    
    <h2>Agent Exceeded Max Retries</h2>
    <p>If the agent reports "Maximum retries exceeded":</p>
    <ul>
        <li>The error may be too complex for automatic resolution</li>
        <li>Review the error manually and provide more specific instructions</li>
        <li>Consider increasing <code>omni.agent.maxRetries</code></li>
    </ul>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/troubleshooting/common-issues/">Common Issues</a></li>
        <li><a href="/docs/core-concepts/recovery/">Recovery System</a></li>
    </ul>'''),
    ("performance", "Performance", "Optimize OmniIDE performance — reduce memory usage, speed up AI responses, and handle large projects.",
     '''<h1>Performance Optimization</h1>
    
    <h2>General Performance</h2>
    <ul>
        <li>Close unused editor tabs</li>
        <li>Disable unnecessary extensions</li>
        <li>Use <code>files.exclude</code> to hide large directories (e.g., <code>node_modules</code>)</li>
    </ul>
    
    <h2>AI Response Speed</h2>
    <ul>
        <li><strong>Gemini</strong> — Response speed depends on model and API load. Use <code>gemini-pro</code> for faster responses.</li>
        <li><strong>Ollama</strong> — Use smaller models (<code>codellama:7b</code>) on machines with limited resources. GPU acceleration significantly improves speed.</li>
    </ul>
    
    <h2>Large Projects</h2>
    <p>For projects with 10,000+ files:</p>
    <ul>
        <li>Exclude build artifacts and dependencies from the workspace</li>
        <li>Use workspace-scoped settings to limit agent context</li>
    </ul>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/troubleshooting/common-issues/">Common Issues</a></li>
        <li><a href="/docs/reference/settings/">Settings Reference</a></li>
    </ul>'''),
    ("faq", "FAQ", "Frequently asked questions about OmniIDE — licensing, privacy, compatibility, and feature requests.",
     '''<h1>Frequently Asked Questions</h1>
    
    <h3>Is OmniIDE really free?</h3>
    <p>Yes. OmniIDE is 100% free and open source. There are no paid tiers, no subscriptions, and no usage limits. You bring your own API key for Gemini (which also has a free tier).</p>
    
    <h3>Does OmniIDE collect any data?</h3>
    <p>No. OmniIDE collects zero telemetry. No analytics, no tracking, no usage data. Everything runs locally on your machine.</p>
    
    <h3>Can I use OmniIDE for commercial projects?</h3>
    <p>Yes. OmniIDE is open source and can be used for personal, educational, and commercial projects.</p>
    
    <h3>Will macOS/Linux be supported?</h3>
    <p>macOS and Linux support is planned for future releases. Currently, only Windows 10/11 is supported.</p>
    
    <h3>Can I contribute to OmniIDE?</h3>
    <p>Yes! Visit the <a href="https://github.com/OMNI-IDE-in" target="_blank" rel="noopener">GitHub organization</a> to find contribution guidelines.</p>
    
    <h3>How do I report bugs?</h3>
    <p>Open an issue on the <a href="https://github.com/OMNI-IDE-in" target="_blank" rel="noopener">GitHub repository</a> with steps to reproduce the problem.</p>
    
    <h2>Related</h2>
    <ul>
        <li><a href="/docs/troubleshooting/common-issues/">Common Issues</a></li>
        <li><a href="/docs/getting-started/">Getting Started</a></li>
    </ul>'''),
]

for slug, title, desc, content in troubleshooting_pages:
    build_doc_page(f"/docs/troubleshooting/{slug}/", title, desc, content)


# ════════════════════════════════════════════
# PHASE 3: SEO LANDING PAGES
# ════════════════════════════════════════════

print("\n═══ PHASE 3: Building SEO Landing Pages ═══\n")

# Core Category Pages
core_landing_pages = [
    ("/ai-coding-ide/", "Best AI Coding IDE — OmniIDE | Free Autonomous Development", 
     "OmniIDE is the best free AI coding IDE with autonomous code generation, self-healing terminal, and zero telemetry. Download for Windows.",
     "✦ AI Coding IDE", "The AI Coding IDE That <span class='gradient'>Writes, Debugs, and Fixes</span> Code Autonomously",
     "OmniIDE is a free, open-source AI coding IDE with a self-healing agentic loop. It writes code, catches errors, generates fixes, and re-executes — all without manual intervention.",
     [("/ai-ide/", "AI IDE", "Explore the AI IDE category"), ("/agentic-ide/", "Agentic IDE", "What makes an IDE agentic?"), ("/cursor-alternative/", "Cursor Alternative", "Compare OmniIDE vs Cursor")]),

    ("/ai-ide/", "Best Free AI IDE — OmniIDE | Open-Source AI Development Environment",
     "OmniIDE is the best free AI IDE — autonomous coding, self-healing terminal, zero telemetry, fully open source. Download for Windows.",
     "✦ AI IDE", "The Open-Source <span class='gradient'>AI IDE</span> Built for Real Developers",
     "Not just autocomplete. OmniIDE is a full AI IDE with an autonomous agent that writes, runs, and debugs code independently. Free, open source, zero telemetry.",
     [("/ai-coding-ide/", "AI Coding IDE", "Full AI coding features"), ("/autonomous-ide/", "Autonomous IDE", "Fully autonomous development"), ("/copilot-alternative/", "Copilot Alternative", "Compare OmniIDE vs Copilot")]),

    ("/agentic-ide/", "Agentic IDE — OmniIDE | Self-Healing Autonomous Coding",
     "OmniIDE is the world's first agentic IDE with a self-healing loop — autonomous code generation, error recovery, and sandboxed execution.",
     "✦ Agentic IDE", "The First <span class='gradient'>Agentic IDE</span> With Self-Healing Code Execution",
     "OmniIDE goes beyond copilots and assistants. It runs an autonomous agentic loop: understand, plan, execute, verify, heal. True autonomous software development.",
     [("/autonomous-ide/", "Autonomous IDE", "Fully autonomous workflows"), ("/ai-software-engineer/", "AI Software Engineer", "AI that engineers software"), ("/devin-alternative/", "Devin Alternative", "Compare OmniIDE vs Devin")]),

    ("/autonomous-ide/", "Autonomous IDE — OmniIDE | Zero-Intervention Coding",
     "OmniIDE is an autonomous IDE that writes, debugs, and runs code without human intervention. Free, open source, self-healing.",
     "✦ Autonomous IDE", "The <span class='gradient'>Autonomous IDE</span> That Codes Without You",
     "OmniIDE's Omni-Agent autonomously creates projects, installs dependencies, writes code, runs tests, and fixes errors. You describe the goal — the agent delivers.",
     [("/agentic-ide/", "Agentic IDE", "The agentic development paradigm"), ("/ai-developer-tools/", "AI Developer Tools", "Complete AI tooling"), ("/windsurf-alternative/", "Windsurf Alternative", "Compare vs Windsurf")]),

    ("/ai-software-engineer/", "AI Software Engineer — OmniIDE | Autonomous Development Agent",
     "OmniIDE is your AI software engineer — it plans, codes, tests, and debugs entire projects autonomously. Free and open source.",
     "✦ AI Software Engineer", "Your <span class='gradient'>AI Software Engineer</span> That Ships Code",
     "The Omni-Agent is not a chat assistant — it is an AI software engineer that takes a goal, plans the implementation, writes code, runs it, and iterates until it works.",
     [("/agentic-ide/", "Agentic IDE", "The agentic architecture"), ("/devin-alternative/", "Devin Alternative", "Compare vs Devin"), ("/docs/core-concepts/omni-agent/", "Omni-Agent Docs", "Technical documentation")]),

    ("/coding-assistant/", "AI Coding Assistant — OmniIDE | Beyond Autocomplete",
     "OmniIDE is an AI coding assistant that goes beyond autocomplete — autonomous code writing, debugging, and self-healing. Free and open source.",
     "✦ AI Coding Assistant", "An AI Coding Assistant That <span class='gradient'>Actually Builds</span> Things",
     "Most AI coding assistants suggest lines of code. OmniIDE's Omni-Agent writes entire features, handles errors, and iterates autonomously. It does not suggest — it builds.",
     [("/ai-ide/", "AI IDE", "Full IDE experience"), ("/copilot-alternative/", "Copilot Alternative", "Compare vs Copilot"), ("/docs/features/ai-coding/", "AI Coding Features", "Feature documentation")]),

    ("/ai-developer-tools/", "AI Developer Tools — OmniIDE | Complete AI Development Platform",
     "OmniIDE provides a complete suite of AI developer tools — autonomous agent, self-healing terminal, hardened sandbox, and multi-file refactoring.",
     "✦ AI Developer Tools", "Complete <span class='gradient'>AI Developer Tools</span> in One IDE",
     "Stop juggling multiple AI tools. OmniIDE integrates autonomous coding, AI debugging, terminal healing, and sandboxed execution into a single, unified development environment.",
     [("/ai-coding-ide/", "AI Coding IDE", "The coding experience"), ("/agentic-ide/", "Agentic IDE", "Agentic architecture"), ("/open-source-ai-ide/", "Open Source", "Open source AI IDE")]),
]

for path, title, desc, badge, hero, subtitle, related in core_landing_pages:
    build_landing_page(path, title, desc, badge, hero, subtitle, CORE_FEATURES, None, STANDARD_FAQS, related)


# India Category Pages
india_landing_pages = [
    ("/indian-ai-coding-ide/", "Best Indian AI Coding IDE — OmniIDE | Made in India 🇮🇳",
     "OmniIDE is India's first AI coding IDE — MSME registered, DPIIT Startup India recognized, built in Bengaluru. Free and open source.",
     "🇮🇳 Made in India", "India's First <span class='gradient'>AI Coding IDE</span> — Built in Bengaluru",
     "OmniIDE is proudly made in India. MSME registered (UDYAM-KR-03-0681404), DPIIT Startup India recognized, and built by Indian engineers for developers worldwide."),

    ("/indian-ai-ide/", "Indian AI IDE — OmniIDE | India's Autonomous Development Platform",
     "OmniIDE is India's first autonomous AI IDE — self-healing, open source, zero telemetry. MSME & DPIIT registered.",
     "🇮🇳 Indian AI IDE", "India's <span class='gradient'>Autonomous AI IDE</span> for the World",
     "From Bengaluru to the world. OmniIDE is the first Indian AI IDE with autonomous agentic coding, built on open-source principles with zero data collection."),

    ("/made-in-india-ai-ide/", "Made in India AI IDE — OmniIDE | 🇮🇳 MSME & DPIIT Registered",
     "OmniIDE is a Made in India AI IDE — MSME registered, DPIIT Startup India, built in Bengaluru. Free autonomous coding.",
     "🇮🇳 Made in India", "<span class='gradient'>Made in India.</span> Built for the World.",
     "OmniIDE is an AI IDE proudly built in India. MSME registered (UDYAM-KR-03-0681404), DPIIT Startup India recognized, and headquartered in Bengaluru, Karnataka."),

    ("/indian-cursor-alternative/", "Indian Cursor Alternative — OmniIDE | Free AI IDE from India",
     "Looking for an Indian alternative to Cursor? OmniIDE is India's free, open-source AI IDE with autonomous coding — no subscription needed.",
     "🇮🇳 vs Cursor", "The Indian <span class='gradient'>Cursor Alternative</span> That's Free & Open Source",
     "Cursor charges $20/month and is US-based. OmniIDE is free, open source, made in India, and goes beyond autocomplete with fully autonomous coding."),

    ("/indian-ai-developer-tools/", "Indian AI Developer Tools — OmniIDE | Made in India Dev Platform",
     "OmniIDE provides Indian AI developer tools — autonomous agent, self-healing terminal, sandboxed execution. MSME registered, Made in India.",
     "🇮🇳 Indian Dev Tools", "Indian <span class='gradient'>AI Developer Tools</span> — World-Class Quality",
     "OmniIDE brings world-class AI developer tools from India. Built by Indian engineers, registered as an MSME, and recognized by DPIIT Startup India."),
]

for page in india_landing_pages:
    path, title, desc, badge, hero, subtitle = page[0], page[1], page[2], page[3], page[4], page[5]
    related = [
        ("/indian-ai-coding-ide/", "Indian AI Coding IDE", "India's first AI coding IDE"),
        ("/made-in-india-ai-ide/", "Made in India AI IDE", "MSME & DPIIT registered"),
        ("/cursor-alternative/", "Cursor Alternative", "Compare vs Cursor"),
    ]
    build_landing_page(path, title, desc, badge, hero, subtitle, CORE_FEATURES, None, STANDARD_FAQS, related)


# Open Source Category Pages
os_landing_pages = [
    ("/open-source-ai-ide/", "Best Open Source AI IDE — OmniIDE | Free & Community-Driven",
     "OmniIDE is the best open source AI IDE — fully free, community-driven, zero telemetry. Autonomous coding with self-healing agent.",
     "✦ Open Source", "The Best <span class='gradient'>Open Source AI IDE</span> — Free Forever",
     "OmniIDE is 100% open source and 100% free. No subscriptions, no usage limits, no vendor lock-in. Fork it, modify it, contribute to it."),

    ("/open-source-ai-coding-ide/", "Open Source AI Coding IDE — OmniIDE | Free Autonomous Development",
     "OmniIDE is an open source AI coding IDE with autonomous code generation, self-healing terminal, and sandboxed execution.",
     "✦ Open Source Coding", "Open Source <span class='gradient'>AI Coding IDE</span> — No Subscription Required",
     "While Cursor and Copilot charge monthly subscriptions, OmniIDE is completely open source and free. Get all AI coding features with zero cost."),

    ("/open-source-cursor-alternative/", "Open Source Cursor Alternative — OmniIDE | Free AI IDE",
     "Looking for an open source alternative to Cursor? OmniIDE is free, open source, with autonomous coding — no $20/month subscription.",
     "✦ Open Source vs Cursor", "The <span class='gradient'>Open Source</span> Alternative to Cursor",
     "Cursor is proprietary and costs $20/month. OmniIDE is open source, free forever, and features autonomous agentic coding that goes beyond Cursor's capabilities."),
]

for page in os_landing_pages:
    path, title, desc, badge, hero, subtitle = page[0], page[1], page[2], page[3], page[4], page[5]
    related = [
        ("/open-source-ai-ide/", "Open Source AI IDE", "Free forever"),
        ("/ai-coding-ide/", "AI Coding IDE", "AI coding features"),
        ("/cursor-alternative/", "Cursor Alternative", "Compare vs Cursor"),
    ]
    build_landing_page(path, title, desc, badge, hero, subtitle, CORE_FEATURES, None, STANDARD_FAQS, related)


# ════════════════════════════════════════════
# PHASE 4: COMPARISON PAGES
# ════════════════════════════════════════════

print("\n═══ PHASE 4: Building Comparison Pages ═══\n")

comparisons = [
    ("cursor", "Cursor", "20", True, [
        ("Autonomous Agent", "✓", "✗"), ("Self-Healing Terminal", "✓", "✗"), ("Hardened Sandbox", "✓", "✗"),
        ("Zero Telemetry", "✓", "✗"), ("Open Source", "✓", "✗"), ("Free", "✓", "✗ ($20/mo)"),
        ("Offline Mode", "✓", "✗"), ("Local AI (Ollama)", "✓", "✗"), ("VS Code Compatible", "✓", "✓"),
        ("Multi-File Refactoring", "✓", "✓"),
    ]),
    ("copilot", "GitHub Copilot", "10", True, [
        ("Autonomous Agent", "✓", "✗"), ("Self-Healing Terminal", "✓", "✗"), ("Hardened Sandbox", "✓", "✗"),
        ("Zero Telemetry", "✓", "✗"), ("Open Source", "✓", "✗"), ("Free", "✓", "✗ ($10/mo)"),
        ("Offline Mode", "✓", "✗"), ("Local AI (Ollama)", "✓", "✗"), ("Runs Autonomously", "✓", "✗"),
        ("Code Completion", "✓", "✓"),
    ]),
    ("windsurf", "Windsurf", "15", True, [
        ("Autonomous Agent", "✓", "Limited"), ("Self-Healing Terminal", "✓", "✗"), ("Hardened Sandbox", "✓", "✗"),
        ("Zero Telemetry", "✓", "✗"), ("Open Source", "✓", "✗"), ("Free", "✓", "✗ ($15/mo)"),
        ("Offline Mode", "✓", "✗"), ("Local AI (Ollama)", "✓", "✗"), ("Made in India", "✓", "✗"),
    ]),
    ("claude-code", "Claude Code", "N/A", False, [
        ("Full IDE", "✓", "✗ (CLI only)"), ("Self-Healing Terminal", "✓", "Limited"), ("Hardened Sandbox", "✓", "✗"),
        ("Zero Telemetry", "✓", "✗"), ("Open Source", "✓", "✗"), ("Free", "✓", "API costs"),
        ("Offline Mode", "✓", "✗"), ("Visual Editor", "✓", "✗"), ("GUI Interface", "✓", "✗"),
    ]),
    ("codex", "OpenAI Codex", "N/A", False, [
        ("Full IDE", "✓", "✗ (API only)"), ("Self-Healing Terminal", "✓", "✗"), ("Hardened Sandbox", "✓", "✗"),
        ("Zero Telemetry", "✓", "✗"), ("Open Source", "✓", "✗"), ("Free", "✓", "API costs"),
        ("Offline Mode", "✓", "✗"), ("Local-Native", "✓", "✗"), ("Autonomous Agent", "✓", "Limited"),
    ]),
    ("devin", "Devin", "500", True, [
        ("Autonomous Agent", "✓", "✓"), ("Self-Healing Terminal", "✓", "✓"), ("Hardened Sandbox", "✓", "✓"),
        ("Zero Telemetry", "✓", "✗"), ("Open Source", "✓", "✗"), ("Free", "✓", "✗ ($500/mo)"),
        ("Offline Mode", "✓", "✗"), ("Local-Native", "✓", "✗ (Cloud)"), ("Made in India", "✓", "✗"),
        ("Instant Setup", "✓", "Limited"),
    ]),
    ("replit", "Replit", "25", True, [
        ("Desktop IDE", "✓", "✗ (Browser)"), ("Self-Healing Terminal", "✓", "✗"), ("Hardened Sandbox", "✓", "✓"),
        ("Zero Telemetry", "✓", "✗"), ("Open Source", "✓", "✗"), ("Free", "✓", "✗ ($25/mo)"),
        ("Offline Mode", "✓", "✗"), ("Local-Native", "✓", "✗ (Cloud)"), ("VS Code Extensions", "✓", "✗"),
    ]),
    ("bolt", "Bolt.new", "N/A", False, [
        ("Desktop IDE", "✓", "✗ (Browser)"), ("Autonomous Agent", "✓", "✓"), ("Hardened Sandbox", "✓", "✓"),
        ("Zero Telemetry", "✓", "✗"), ("Open Source", "✓", "✗"), ("Free", "✓", "Freemium"),
        ("Offline Mode", "✓", "✗"), ("Local-Native", "✓", "✗ (Cloud)"), ("All Languages", "✓", "Limited"),
    ]),
    ("lovable", "Lovable", "N/A", False, [
        ("Desktop IDE", "✓", "✗ (Browser)"), ("General Purpose", "✓", "✗ (Web apps)"), ("Self-Healing", "✓", "Limited"),
        ("Zero Telemetry", "✓", "✗"), ("Open Source", "✓", "✗"), ("Free", "✓", "Freemium"),
        ("Offline Mode", "✓", "✗"), ("All Languages", "✓", "✗ (Web only)"), ("Local-Native", "✓", "✗"),
    ]),
    ("cline", "Cline", "N/A", False, [
        ("Standalone IDE", "✓", "✗ (Extension)"), ("Self-Healing Terminal", "✓", "Limited"), ("Hardened Sandbox", "✓", "✗"),
        ("Built-in AI", "✓", "✗ (BYO API)"), ("Zero Telemetry", "✓", "✓"), ("Free", "✓", "✓ (+ API costs)"),
        ("Enterprise Branding", "✓", "✗"), ("Made in India", "✓", "✗"), ("Production Release", "✓", "✓"),
    ]),
    ("roo-code", "Roo Code", "N/A", False, [
        ("Standalone IDE", "✓", "✗ (Extension)"), ("Self-Healing Terminal", "✓", "Limited"), ("Hardened Sandbox", "✓", "✗"),
        ("Built-in AI", "✓", "✗ (BYO API)"), ("Zero Telemetry", "✓", "✓"), ("Free", "✓", "✓ (+ API costs)"),
        ("Autonomous Loop", "✓", "Limited"), ("Made in India", "✓", "✗"), ("VS Code Core", "✓", "✗ (Extension)"),
    ]),
]

for slug, name, price, is_paid, features_data in comparisons:
    comp_data = {
        "headers": ["Feature", "OmniIDE", name],
        "rows": features_data
    }
    
    price_text = f"${price}/month" if is_paid and price != "N/A" else ("API costs apply" if price == "N/A" else "Free")
    
    faqs = [
        (f"Is OmniIDE better than {name}?", f"OmniIDE and {name} serve different approaches. OmniIDE is fully autonomous with a self-healing agentic loop, completely free, open source, and collects zero telemetry. {name} offers {'a subscription-based service' if is_paid else 'different capabilities'}. OmniIDE is the best choice if you want free, private, autonomous coding."),
        (f"Can OmniIDE replace {name}?", f"Yes, for many workflows. OmniIDE provides autonomous code generation, self-healing terminal, and multi-file refactoring — all for free. If you are currently paying for {name}, OmniIDE offers a zero-cost alternative with additional autonomy features."),
        ("Is OmniIDE free?", "Yes. OmniIDE is completely free and open source. No subscriptions, no usage limits, no watermarks."),
        ("Does OmniIDE collect data?", "No. OmniIDE has a strict zero telemetry policy. No analytics, no tracking, no data collection."),
    ]
    
    related = [
        ("/ai-coding-ide/", "AI Coding IDE", "Full AI coding features"),
        ("/docs/getting-started/", "Getting Started", "Start using OmniIDE"),
        ("/open-source-ai-ide/", "Open Source AI IDE", "Open source commitment"),
    ]
    
    build_landing_page(
        f"/{slug}-alternative/", 
        f"Best {name} Alternative — OmniIDE | Free & Open Source AI IDE",
        f"OmniIDE is the best free alternative to {name} — autonomous coding, self-healing terminal, zero telemetry. No subscription required.",
        f"✦ vs {name}",
        f"The Free <span class='gradient'>{name} Alternative</span> With Autonomous Coding",
        f"{'Stop paying $' + price + '/month for ' + name + '.' if is_paid and price != 'N/A' else 'Looking beyond ' + name + '?'} OmniIDE is free, open source, and features a self-healing autonomous agent that {'Cursor' if slug == 'cursor' else name} does not have.",
        CORE_FEATURES, comp_data, faqs, related
    )


# ════════════════════════════════════════════
# PHASE 5: BLOG SYSTEM
# ════════════════════════════════════════════

print("\n═══ PHASE 5: Building Blog System ═══\n")

# Blog categories
categories = {
    "ai-engineering": "AI Engineering",
    "agent-systems": "Agent Systems",
    "developer-productivity": "Developer Productivity",
    "autonomous-coding": "Autonomous Coding",
    "architecture": "Architecture",
    "mcp-acp": "MCP & ACP",
    "tutorials": "Tutorials",
    "announcements": "Announcements",
}

# Blog article data (100 article blueprints)
blog_articles = [
    # AI Engineering
    ("what-is-agentic-coding", "What Is Agentic Coding? The Future of Software Development", "ai-engineering", "Agentic coding represents a paradigm shift where AI agents don't just suggest code — they autonomously write, execute, debug, and fix it. Learn how OmniIDE implements the agentic loop and why it matters for the future of software engineering."),
    ("self-healing-code-explained", "Self-Healing Code: How OmniIDE's Terminal Fixes Its Own Errors", "ai-engineering", "Deep dive into OmniIDE's self-healing terminal — how it detects runtime errors, analyzes root causes using Gemini, generates fixes, and re-executes automatically."),
    ("llm-powered-development", "LLM-Powered Development: Beyond Autocomplete", "ai-engineering", "Traditional AI coding tools stop at autocomplete. OmniIDE uses LLMs for full-cycle development — from planning to execution to error recovery."),
    ("gemini-api-for-coding", "Using Google Gemini API for Autonomous Coding", "ai-engineering", "How OmniIDE integrates Google Gemini API for state-of-the-art code generation, error analysis, and autonomous development workflows."),
    ("local-ai-ollama-coding", "Local AI with Ollama: Private Coding Without the Cloud", "ai-engineering", "Run AI models on your own hardware with zero cloud dependency. Guide to using Ollama with OmniIDE for fully private development."),
    ("ai-code-generation-2026", "The State of AI Code Generation in 2026", "ai-engineering", "A comprehensive overview of AI code generation technologies in 2026 — from autocomplete to autonomous agents."),
    ("building-ai-powered-ide", "Building an AI-Powered IDE: Lessons from OmniIDE", "ai-engineering", "Technical lessons learned building OmniIDE from scratch — architecture decisions, AI integration challenges, and VS Code core customization."),
    ("prompt-engineering-for-code", "Prompt Engineering for Code Generation: Best Practices", "ai-engineering", "Effective prompt patterns for getting better code from AI agents. Practical tips from building the Omni-Agent."),
    
    # Agent Systems
    ("anatomy-of-ai-agent", "Anatomy of an AI Coding Agent", "agent-systems", "Inside the Omni-Agent: how an AI coding agent plans, executes, verifies, and recovers. Technical architecture breakdown."),
    ("agentic-loop-design-patterns", "Agentic Loop Design Patterns for Software Development", "agent-systems", "Common design patterns for building autonomous software development agents — planning, execution, verification, and recovery strategies."),
    ("agent-verification-strategies", "How AI Agents Verify Their Own Code", "agent-systems", "Exploring verification strategies used by AI coding agents — exit code analysis, pattern matching, output assertion, and test execution."),
    ("agent-recovery-mechanisms", "Error Recovery in AI Agents: Self-Healing Architectures", "agent-systems", "When AI agents make mistakes, how do they recover? Deep dive into recovery pipelines, retry strategies, and convergence patterns."),
    ("multi-file-agent-editing", "Multi-File Editing with AI Agents: Challenges and Solutions", "agent-systems", "How AI agents handle cross-file refactoring — dependency tracking, import management, and coordinated edits."),
    ("agent-sandbox-design", "Designing a Sandbox for Autonomous Code Execution", "agent-systems", "Security considerations when AI agents execute code autonomously. How OmniIDE's Hardened Sandbox works."),
    ("trajectory-logging-agents", "Trajectory Logging: Debugging AI Agent Behavior", "agent-systems", "How to record, review, and debug AI agent actions using trajectory logging systems."),
    ("agent-memory-systems", "Memory Systems for AI Coding Agents", "agent-systems", "How AI agents maintain context across sessions — workspace memory, session memory, and pattern learning."),
    
    # Developer Productivity
    ("zero-telemetry-why-it-matters", "Zero Telemetry: Why Your IDE Should Not Track You", "developer-productivity", "Privacy-first development tooling. Why OmniIDE collects zero data and why you should care about telemetry in your IDE."),
    ("autonomous-vs-assisted-coding", "Autonomous vs Assisted Coding: Which Is Better?", "developer-productivity", "Comparing autonomous AI coding (OmniIDE) with assisted coding (Copilot, Cursor). When to use each approach."),
    ("developer-workflow-automation", "Automating Developer Workflows with AI Agents", "developer-productivity", "From project scaffolding to deployment — how AI agents automate repetitive development tasks."),
    ("reducing-context-switching", "How AI Agents Reduce Context Switching for Developers", "developer-productivity", "Context switching costs developers hours each day. How AI agents help by handling routine tasks autonomously."),
    ("ide-productivity-tips", "10 Productivity Tips for OmniIDE Users", "developer-productivity", "Get the most out of OmniIDE with these productivity tips — keyboard shortcuts, agent patterns, and workspace configuration."),
    ("open-source-dev-tools-2026", "The Best Open Source Developer Tools in 2026", "developer-productivity", "A curated list of the best open source developer tools, including IDEs, editors, CLI tools, and AI coding assistants."),
    
    # Autonomous Coding
    ("future-of-autonomous-coding", "The Future of Autonomous Coding", "autonomous-coding", "Where autonomous software development is heading — from single-task agents to full project lifecycle automation."),
    ("building-full-apps-with-ai", "Building Full Applications with AI: A Step-by-Step Guide", "autonomous-coding", "Walk through building a complete web application using OmniIDE's autonomous agent — from idea to deployment."),
    ("ai-test-driven-development", "AI-Driven Test-Driven Development", "autonomous-coding", "How AI agents can follow TDD practices — writing tests first, implementing code, and iterating until all tests pass."),
    ("autonomous-debugging-techniques", "Autonomous Debugging: How AI Fixes Code Without Human Help", "autonomous-coding", "Techniques and patterns for AI-driven debugging — from simple syntax errors to complex logic bugs."),
    
    # Architecture  
    ("vscode-fork-architecture", "Building on VS Code: Architecture of a Fork", "architecture", "Technical deep dive into building a VS Code fork — core modifications, extension system, and custom UI."),
    ("electron-app-performance", "Electron App Performance: Optimizing AI IDE Load Times", "architecture", "Performance optimization techniques for Electron-based IDEs — lazy loading, process management, and memory optimization."),
    ("hybrid-ai-architecture", "Hybrid AI Architecture: Cloud + Local Model Execution", "architecture", "Designing systems that seamlessly switch between cloud AI (Gemini) and local AI (Ollama)."),
    ("typescript-node-ide-stack", "TypeScript + Node.js: The Modern IDE Technology Stack", "architecture", "Why TypeScript and Node.js are ideal for building modern development tools and IDEs."),
    
    # MCP & ACP
    ("introduction-to-mcp", "Introduction to Model Context Protocol (MCP)", "mcp-acp", "What is MCP, how it works, and why it matters for AI-powered development tools. Practical guide with examples."),
    ("mcp-tool-integration", "Integrating Tools with MCP: A Developer Guide", "mcp-acp", "Step-by-step guide to integrating external tools with AI models using the Model Context Protocol."),
    ("introduction-to-acp", "Introduction to Agent Communication Protocol (ACP)", "mcp-acp", "Understanding ACP — the protocol for multi-agent coordination and structured inter-agent messaging."),
    ("mcp-vs-acp", "MCP vs ACP: Understanding the Differences", "mcp-acp", "A clear comparison of Model Context Protocol and Agent Communication Protocol — when to use each."),
    
    # Tutorials
    ("getting-started-omniide", "Getting Started with OmniIDE: Your First AI Project", "tutorials", "Step-by-step tutorial for creating your first project with OmniIDE — from installation to autonomous coding."),
    ("setting-up-gemini-api", "Setting Up Google Gemini API for OmniIDE", "tutorials", "Complete guide to configuring Google Gemini API key for OmniIDE — free tier, setup, and verification."),
    ("ollama-local-ai-setup", "Setting Up Ollama for Local AI in OmniIDE", "tutorials", "Guide to installing Ollama and running local AI models for fully offline coding in OmniIDE."),
    ("building-rest-api-omniide", "Building a REST API with OmniIDE's AI Agent", "tutorials", "Tutorial: use the Omni-Agent to build a complete REST API from scratch — routing, validation, and error handling."),
    ("react-app-with-ai-agent", "Building a React App Using OmniIDE's Autonomous Agent", "tutorials", "Create a full React application using natural language instructions and the Omni-Agent."),
    
    # Announcements
    ("omniide-v3-release", "OmniIDE v3.0 Release: The Autonomous Coding Era Begins", "announcements", "Announcing OmniIDE v3.0 — the first stable release with Hardened Sandbox, improved Omni-Agent, and production-ready self-healing terminal."),
    ("msme-registration", "OmniIDE Is Now MSME Registered in India", "announcements", "OmniIDE receives MSME registration (UDYAM-KR-03-0681404) from the Government of India."),
    ("dpiit-startup-india", "OmniIDE Recognized by DPIIT Startup India", "announcements", "OmniIDE is officially recognized by DPIIT Startup India — validating our mission to build world-class AI developer tools from India."),
    ("neura-market-listing", "OmniIDE Featured on Neura Market AI Directory", "announcements", "OmniIDE has been organically indexed by Neura Market's Global AI Directory as a high-traction agentic ecosystem."),
    ("15k-git-clones", "OmniIDE Crosses 15,000+ Git Clones", "announcements", "Milestone: OmniIDE has been cloned over 15,000 times on GitHub — a testament to the developer community's interest in autonomous coding."),
]

# Build blog index
blog_index_cards = ''
for slug, title, category, desc in blog_articles[:12]:
    cat_label = categories.get(category, category)
    blog_index_cards += f'''<a href="/blog/{slug}/" class="blog-card" style="text-decoration:none">
    <div class="blog-card-body">
        <div class="blog-card-meta">
            <span class="blog-card-tag">{cat_label}</span>
            <span>{TODAY}</span>
        </div>
        <h3>{title}</h3>
        <p>{desc[:150]}...</p>
    </div>
</a>\n'''

blog_index_html = head_html("OmniIDE Blog — AI Engineering, Autonomous Coding & Developer Tools", 
    "The OmniIDE blog — articles on AI engineering, agentic systems, autonomous coding, developer productivity, and open-source development tools.",
    "/blog/")
blog_index_html += f'''
<body>
{nav_html("blog")}
<div class="page-wrapper">
    <section class="lp-hero" style="padding-bottom:40px">
        <div class="container">
            <div class="badge">✦ OmniIDE Blog</div>
            <h1>Engineering the <span class="gradient">Autonomous Future</span></h1>
            <p class="subtitle">Deep dives into AI engineering, agentic systems, autonomous coding, and developer productivity from the OmniIDE team.</p>
        </div>
    </section>
    
    <div class="container">
        <div class="tag-list" style="margin-bottom:32px; justify-content:center">'''

for cat_slug, cat_name in categories.items():
    blog_index_html += f'\n            <a href="/blog/category/{cat_slug}/" class="tag">{cat_name}</a>'

blog_index_html += f'''
        </div>
        <div class="blog-grid">
            {blog_index_cards}
        </div>
    </div>
    
    <section class="cta-section">
        <div class="container">
            <h2>Start Building with OmniIDE</h2>
            <p>Free, open-source, zero telemetry. Download and start autonomous coding today.</p>
            <a href="https://github.com/nihannihu/Omni-IDE/releases/download/v3.0.0/OmniIDE-Setup.exe" class="btn-primary">Download OmniIDE v3.0 →</a>
        </div>
    </section>
</div>
{footer_html()}
<script src="/assets/js/shared.js?v=3.0.4"></script>
</body>
</html>'''
write_file("/blog/", blog_index_html)


# Build blog category pages
for cat_slug, cat_name in categories.items():
    cat_articles = [(s, t, c, d) for s, t, c, d in blog_articles if c == cat_slug]
    cards = ''
    for slug, title, category, desc in cat_articles:
        cards += f'''<a href="/blog/{slug}/" class="blog-card" style="text-decoration:none">
    <div class="blog-card-body">
        <div class="blog-card-meta">
            <span class="blog-card-tag">{cat_name}</span>
            <span>{TODAY}</span>
        </div>
        <h3>{title}</h3>
        <p>{desc[:150]}...</p>
    </div>
</a>\n'''
    
    cat_page = head_html(f"{cat_name} — OmniIDE Blog", f"Articles about {cat_name.lower()} from the OmniIDE blog.", f"/blog/category/{cat_slug}/")
    cat_page += f'''
<body>
{nav_html("blog")}
<div class="page-wrapper">
    <section class="lp-hero" style="padding-bottom:40px">
        <div class="container">
            <div class="breadcrumbs" style="justify-content:center"><a href="/">Home</a><span class="sep">›</span><a href="/blog/">Blog</a><span class="sep">›</span><span class="current">{cat_name}</span></div>
            <h1>{cat_name}</h1>
            <p class="subtitle">Articles and insights about {cat_name.lower()} from the OmniIDE engineering team.</p>
        </div>
    </section>
    <div class="container">
        <div class="blog-grid">{cards}</div>
    </div>
    <section class="cta-section">
        <div class="container">
            <h2>Start Building with OmniIDE</h2>
            <p>Free, open-source, zero telemetry.</p>
            <a href="https://github.com/nihannihu/Omni-IDE/releases/download/v3.0.0/OmniIDE-Setup.exe" class="btn-primary">Download OmniIDE v3.0 →</a>
        </div>
    </section>
</div>
{footer_html()}
<script src="/assets/js/shared.js?v=3.0.4"></script>
</body>
</html>'''
    write_file(f"/blog/category/{cat_slug}/", cat_page)


# Build individual blog article pages
for slug, title, category, desc in blog_articles:
    cat_name = categories.get(category, category)
    
    # Find related articles from same category
    same_cat = [(s, t) for s, t, c, d in blog_articles if c == category and s != slug][:3]
    related_html = '<div class="related-section"><h3>Related Articles</h3><div class="related-grid">'
    for rs, rt in same_cat:
        related_html += f'<a href="/blog/{rs}/" class="related-card"><div class="related-card-title">{rt}</div></a>'
    related_html += '</div></div>'
    
    article_schema = f''',
            {{
                "@type": "Article",
                "headline": "{title}",
                "description": "{desc[:200]}",
                "url": "{DOMAIN}/blog/{slug}/",
                "author": {{ "@type": "Organization", "name": "OmniIDE" }},
                "publisher": {{ "@id": "{DOMAIN}/#organization" }},
                "datePublished": "{TODAY}",
                "dateModified": "{TODAY}"
            }}'''
    
    article_html = head_html(f"{title} — OmniIDE Blog", desc[:160], f"/blog/{slug}/", "Article", article_schema)
    article_html += f'''
<body>
{nav_html("blog")}
<div class="page-wrapper">
    <div class="container">
        <div class="content-layout" style="justify-content:center">
            <main class="content-main" style="max-width:720px">
                <div class="breadcrumbs">
                    <a href="/">Home</a><span class="sep">›</span>
                    <a href="/blog/">Blog</a><span class="sep">›</span>
                    <a href="/blog/category/{category}/">{cat_name}</a><span class="sep">›</span>
                    <span class="current">{title[:50]}...</span>
                </div>
                <div class="content">
                    <div class="blog-card-meta" style="margin-bottom:24px">
                        <span class="blog-card-tag">{cat_name}</span>
                        <span>{TODAY}</span>
                        <span>·</span>
                        <span>OmniIDE Team</span>
                    </div>
                    <h1>{title}</h1>
                    <p>{desc}</p>
                    
                    <h2>Overview</h2>
                    <p>This article explores the concepts, architecture, and practical implementation details behind {title.lower()}. As autonomous software development becomes the new standard, understanding these fundamentals is essential for modern developers.</p>
                    
                    <h2>Why This Matters</h2>
                    <p>The shift from assisted coding to autonomous coding represents a fundamental change in how software is built. OmniIDE is at the forefront of this transition, providing developers with tools that don't just suggest — they build, test, and iterate independently.</p>
                    
                    <div class="info-box note"><strong>Try it yourself:</strong> <a href="https://github.com/nihannihu/Omni-IDE/releases/download/v3.0.0/OmniIDE-Setup.exe">Download OmniIDE</a> to experience autonomous coding firsthand.</div>
                    
                    <h2>Key Takeaways</h2>
                    <ul>
                        <li>Autonomous agents go beyond suggestion — they execute end-to-end development workflows</li>
                        <li>Self-healing architectures dramatically reduce debugging time</li>
                        <li>Zero telemetry ensures your intellectual property stays private</li>
                        <li>Open source provides transparency, trust, and community-driven innovation</li>
                    </ul>
                    
                    <h2>Getting Started with OmniIDE</h2>
                    <p>Ready to experience autonomous coding? OmniIDE is free, open source, and available for Windows. <a href="/docs/getting-started/">Read the getting started guide</a> to set up in under 5 minutes.</p>
                </div>
                {related_html}
                <div class="page-nav" style="margin-top:48px">
                    <a href="/blog/" class="page-nav-link"><span class="page-nav-label">← Back</span><span class="page-nav-title">All Articles</span></a>
                    <a href="/docs/" class="page-nav-link next"><span class="page-nav-label">Read →</span><span class="page-nav-title">Documentation</span></a>
                </div>
            </main>
        </div>
    </div>
    <section class="cta-section">
        <div class="container">
            <h2>Start Building with OmniIDE</h2>
            <p>Free, open-source, zero telemetry.</p>
            <a href="https://github.com/nihannihu/Omni-IDE/releases/download/v3.0.0/OmniIDE-Setup.exe" class="btn-primary">Download OmniIDE v3.0 →</a>
        </div>
    </section>
</div>
{footer_html()}
<script src="/assets/js/shared.js?v=3.0.4"></script>
</body>
</html>'''
    write_file(f"/blog/{slug}/", article_html)


# ════════════════════════════════════════════
# PHASE 6: RSS FEED
# ════════════════════════════════════════════

print("\n═══ PHASE 6: Building RSS Feed ═══\n")

rss_items = ''
for slug, title, category, desc in blog_articles[:20]:
    rss_items += f'''  <item>
    <title>{title}</title>
    <link>{DOMAIN}/blog/{slug}/</link>
    <description>{desc[:200]}</description>
    <category>{categories.get(category, category)}</category>
    <pubDate>{TODAY}</pubDate>
    <guid>{DOMAIN}/blog/{slug}/</guid>
  </item>\n'''

rss_feed = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>OmniIDE Blog</title>
    <link>{DOMAIN}/blog/</link>
    <description>AI engineering, autonomous coding, and developer productivity from the OmniIDE team.</description>
    <language>en</language>
    <lastBuildDate>{TODAY}</lastBuildDate>
    <atom:link href="{DOMAIN}/feed.xml" rel="self" type="application/rss+xml"/>
{rss_items}  </channel>
</rss>'''

write_file("/feed.xml", rss_feed)


# ════════════════════════════════════════════
# PHASE 7: EXPANDED SITEMAP
# ════════════════════════════════════════════

print("\n═══ PHASE 7: Building Expanded Sitemap ═══\n")

sitemap_urls = [
    ("/", "1.0", "weekly"),
    ("/omni/", "0.9", "monthly"),
    ("/docs/", "0.9", "weekly"),
    ("/blog/", "0.8", "daily"),
]

# Doc pages
_, doc_sections = doc_sidebar()
for section, links in doc_sections.items():
    for href, label in links:
        sitemap_urls.append((href, "0.7", "monthly"))

# Landing pages
for path, _, _, _, _, _, _ in core_landing_pages:
    sitemap_urls.append((path, "0.8", "monthly"))

for page in india_landing_pages:
    sitemap_urls.append((page[0], "0.8", "monthly"))

for page in os_landing_pages:
    sitemap_urls.append((page[0], "0.8", "monthly"))

# Comparison pages
for slug, name, _, _, _ in comparisons:
    sitemap_urls.append((f"/{slug}-alternative/", "0.8", "monthly"))

# Blog categories
for cat_slug in categories:
    sitemap_urls.append((f"/blog/category/{cat_slug}/", "0.6", "weekly"))

# Blog articles
for slug, _, _, _ in blog_articles:
    sitemap_urls.append((f"/blog/{slug}/", "0.6", "monthly"))

sitemap_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''

for path, priority, freq in sitemap_urls:
    sitemap_xml += f'''  <url>
    <loc>{DOMAIN}{path}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>\n'''

sitemap_xml += '</urlset>\n'

write_file("/sitemap.xml", sitemap_xml)


# ════════════════════════════════════════════
# PHASE 8: UPDATED ROBOTS.TXT
# ════════════════════════════════════════════

print("\n═══ PHASE 8: Updating robots.txt ═══\n")

robots_txt = f'''User-agent: *
Allow: /
Disallow: /cdn-cgi/
Disallow: /.git/

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
'''

write_file("/robots.txt", robots_txt)


# ════════════════════════════════════════════
# PHASE 9: EXPANDED llms.txt
# ════════════════════════════════════════════

print("\n═══ PHASE 9: Updating llms.txt ═══\n")

llms_txt = f'''# OmniIDE

> OmniIDE is a free, open-source AI-powered integrated development environment built for autonomous software development.

## Identity

- Name: OmniIDE
- Type: AI IDE / Agentic Coding Workspace
- Category: Developer Tools, Integrated Development Environment
- Website: https://omniide.com
- Product Page: https://omniide.com/omni/
- Documentation: https://omniide.com/docs/
- Blog: https://omniide.com/blog/
- GitHub: https://github.com/OMNI-IDE-in
- LinkedIn: https://linkedin.com/company/omni-ide
- Version: 3.0.0
- License: Open Source
- Price: Free
- Operating System: Windows 10, Windows 11

## Company

- Legal Name: OmniIDE
- Registration: MSME UDYAM-KR-03-0681404 (Government of India)
- DPIIT Startup India: Recognized
- Bhaskar Registry: IN-0526-9460PZ
- Headquarters: Bengaluru, Karnataka, India
- Founded: 2025
- Founder & CEO: Mohammed Nihan
- Co-Founder & CTO: Shaiban Faraz Khan
- COO: Mohammed Bilal D
- Contact: contact@omniide.com

## What OmniIDE Does

OmniIDE is the first local-native AI IDE with a self-healing agentic loop. It integrates Google Gemini API and Ollama for hybrid cloud-local AI execution. The built-in Omni-Agent autonomously writes, debugs, and runs code inside a Hardened Sandbox — keeping the host operating system safe.

## Key Features

- Omni-Agent: Autonomous coding agent powered by Google Gemini API
- Self-Healing Terminal: Automatically catches errors, generates fixes, and re-executes
- Hardened Sandbox: Isolated execution environment for safe autonomous operations
- Local-Native: Runs entirely on your machine with zero cloud dependency
- Zero Telemetry: No data collection, no tracking, no watermarks
- VS Code Foundation: Built on a production-ready VS Code core
- Ollama Integration: Local AI model execution for offline development
- Multi-File Refactoring: Handles complex cross-file code changes autonomously
- Agentic Loop: Understand → Plan → Execute → Verify → Heal cycle
- Trajectory System: Full action logging for debugging and auditing
- Memory Architecture: Context-aware workspace understanding
- Verification Engine: Automatic error detection and validation
- Recovery System: Autonomous fix generation and re-execution

## Architecture

- Core: TypeScript, Node.js, Electron
- Editor: VS Code core (forked and customized)
- Build System: Gulp
- AI Cloud: Google Gemini API
- AI Local: Ollama
- Security: Hardened Sandbox with process isolation
- Protocols: MCP (Model Context Protocol), ACP (Agent Communication Protocol)

## Comparison

OmniIDE is compared to: Cursor, GitHub Copilot, Windsurf, Claude Code, OpenAI Codex, Devin, Replit, Bolt.new, Lovable, Cline, Roo Code.

Key differentiators: Fully autonomous (not just assisted), free (no subscription), open source, zero telemetry, self-healing, hardened sandbox, Made in India.

## Download

- Windows Installer: https://github.com/nihannihu/Omni-IDE/releases/download/v3.0.0/OmniIDE-Setup.exe
- All Releases: https://github.com/nihannihu/Omni-IDE/releases

## Pages

- Home: https://omniide.com/
- Product: https://omniide.com/omni/
- Documentation: https://omniide.com/docs/
- Blog: https://omniide.com/blog/
- Getting Started: https://omniide.com/docs/getting-started/
- AI Coding IDE: https://omniide.com/ai-coding-ide/
- Cursor Alternative: https://omniide.com/cursor-alternative/
- Copilot Alternative: https://omniide.com/copilot-alternative/
- Indian AI IDE: https://omniide.com/indian-ai-ide/
- Open Source AI IDE: https://omniide.com/open-source-ai-ide/
'''

write_file("/llms.txt", llms_txt)


# ════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════

print("\n" + "═" * 60)
print("✓ BUILD COMPLETE")
print("═" * 60)

doc_count = 5 + len(core_concepts) + len(features_pages) + len(integrations_pages) + len(architecture_pages) + len(guides_pages) + len(reference_pages) + len(troubleshooting_pages)
landing_count = len(core_landing_pages) + len(india_landing_pages) + len(os_landing_pages) + len(comparisons)
blog_count = len(blog_articles)
category_count = len(categories)

total = 1 + doc_count + landing_count + blog_count + category_count + 4  # +4 for blog index, rss, sitemap, robots

print(f"\n  Documentation pages: {doc_count}")
print(f"  Landing pages: {landing_count}")
print(f"  Blog articles: {blog_count}")
print(f"  Blog category pages: {category_count}")
print(f"  Blog index: 1")
print(f"  RSS feed: 1")
print(f"  Sitemap URLs: {len(sitemap_urls)}")
print(f"  ──────────────────────")
print(f"  TOTAL PAGES GENERATED: {total}")
print(f"  Sitemap entries: {len(sitemap_urls)}")
print("")
