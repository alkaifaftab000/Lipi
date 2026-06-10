import re

path = r'D:\Papers\Lipi\paper\research_paper.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. Paper width: Letter → A4 ─────────────────────────────────────────────
content = content.replace('width: 8.5in;', 'width: 8.27in;')

# ── 2. Paper: simulate visual page lines on screen ───────────────────────────
content = content.replace(
    '      background: #fff;\n      box-shadow: 0 4px 32px rgba(0,0,0,0.18);',
    '      background: #fff;\n      box-shadow: 0 4px 32px rgba(0,0,0,0.18);\n      background-image: repeating-linear-gradient(\n        to bottom,\n        transparent 0,\n        transparent calc(11.69in - 3px),\n        #bbb calc(11.69in - 3px),\n        #bbb calc(11.69in)\n      );'
)

# ── 3. Add page: cover-pg to .cover ─────────────────────────────────────────
content = content.replace(
    '      page-break-after: always;\n      display: flex;\n      flex-direction: column;\n      align-items: stretch;\n    }',
    '      page-break-after: always;\n      page: cover-pg;\n      display: flex;\n      flex-direction: column;\n      align-items: stretch;\n    }'
)

# ── 4. Replace the entire print/screen CSS block ─────────────────────────────
old_block = '    /* Screen running header */\n    .screen-header {'
new_block_start_idx = content.find(old_block)

# Find end: closing of @media print
media_end = content.find('\n    }\n', content.find('@media print {', new_block_start_idx)) + len('\n    }\n')

old_css = content[new_block_start_idx:media_end]

new_css = """    /* ── Screen running header (visible while scrolling) ── */
    .screen-header {
      position: fixed;
      top: 0;
      right: 0;
      z-index: 999;
      background: rgba(255,255,255,0.95);
      padding: 5px 16px 4px 16px;
      border-bottom-left-radius: 6px;
      border-bottom: 1px solid #c5cae9;
      border-left: 1px solid #c5cae9;
      font-family: "Times New Roman", Times, serif;
      font-size: 9pt;
      font-style: italic;
      color: #1a2e6e;
      pointer-events: none;
    }

    /* ── A4 Print: perfect PDF output ────────────────────────── */
    @page {
      size: A4;
      margin: 0.75in 1in 0.8in 1in;
      @top-right {
        content: "Amity University";
        font-family: "Times New Roman", Times, serif;
        font-size: 9pt;
        color: #1a2e6e;
        font-style: italic;
        vertical-align: bottom;
        padding-bottom: 4pt;
        border-bottom: 0.5pt solid #c5cae9;
      }
      @bottom-center {
        content: counter(page);
        font-family: "Times New Roman", Times, serif;
        font-size: 10pt;
        color: #333;
      }
    }

    /* Cover page: edge-to-edge, no header/footer */
    @page cover-pg {
      size: A4;
      margin: 0;
      @top-right  { content: none; }
      @bottom-center { content: none; }
    }

    @media print {
      html, body {
        margin: 0;
        padding: 0;
        background: #fff;
      }
      /* Paper: @page margins are the page margins, so zero out paper padding */
      .paper {
        width: 100%;
        margin: 0;
        padding: 0;
        box-shadow: none;
        background-image: none;
      }
      /* Cover fills the entire first page edge-to-edge */
      .cover {
        width: 100%;
        height: 100vh;
        margin: 0;
        box-shadow: none;
      }
      .screen-header { display: none; }
    }
"""

content = content.replace(old_css, new_css)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
checks = [
    'width: 8.27in',
    'repeating-linear-gradient',
    'page: cover-pg',
    '@page cover-pg',
    'background-image: none',
    '11 June 2026',
    'lipiv14@gmail.com'
]
print("Verification:")
for c in checks:
    print(f"  {'OK' if c in content else 'MISSING'}: {c}")
