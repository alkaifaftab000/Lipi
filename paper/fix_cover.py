path = r'D:\Papers\Lipi\paper\research_paper.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# ─── 1. Add screen header (Amity University top-right) + print styles ────────
old_print = """    /* A4 Print + Running Header & Footer */
    @page {
      size: A4;
      margin: 1.1in 1in 0.9in 1in;
    }
    @page {
      @top-right {
        content: "Amity University";
        font-family: "Times New Roman", Times, serif;
        font-size: 9pt;
        color: #1a2e6e;
        font-style: italic;
        vertical-align: bottom;
        padding-bottom: 3pt;
      }
      @bottom-center {
        content: counter(page);
        font-family: "Times New Roman", Times, serif;
        font-size: 10pt;
        color: #333;
      }
    }

    @media print {
      body { background: #fff; }
      .paper { box-shadow: none; margin: 0; width: 100%; }
      .cover { box-shadow: none; }
    }"""

new_print = """    /* Screen running header */
    .screen-header {
      position: fixed;
      top: 0;
      right: 0;
      z-index: 999;
      background: rgba(255,255,255,0.92);
      padding: 5px 14px 4px 14px;
      border-bottom-left-radius: 6px;
      border-bottom: 1px solid #dde;
      border-left: 1px solid #dde;
      font-family: "Times New Roman", Times, serif;
      font-size: 9pt;
      font-style: italic;
      color: #1a2e6e;
      letter-spacing: 0.02em;
      pointer-events: none;
    }

    /* Print: running header + page numbers */
    @page {
      size: A4;
      margin: 1.1in 1in 0.9in 1in;
      @top-right {
        content: "Amity University";
        font-family: "Times New Roman", Times, serif;
        font-size: 9pt;
        color: #1a2e6e;
        font-style: italic;
      }
      @bottom-center {
        content: counter(page);
        font-family: "Times New Roman", Times, serif;
        font-size: 10pt;
        color: #333;
      }
    }

    @media print {
      body { background: #fff; }
      .paper { box-shadow: none; margin: 0; width: 100%; }
      .cover { box-shadow: none; }
      .screen-header { display: none; }
    }"""

content = content.replace(old_print, new_print)

# ─── 2. Replace author box with clean academic style ─────────────────────────
old_author = """    <!-- Author box -->
    <div class="cover-author-box">
      <span class="cover-author-name">Lipi Virmani</span>
      <div class="cover-author-row">
        <span class="cover-label-inline">Role:</span> Corresponding Author &nbsp;|&nbsp;
        <span class="cover-label-inline">Programme:</span> Final Year MBA
      </div>
      <div class="cover-author-row">
        <span class="cover-label-inline">Roll No.:</span> &nbsp;_______________
      </div>
      <div class="cover-author-row">
        <span class="cover-label-inline">Department:</span> Management Studies, Amity University
      </div>
    </div>

    <div class="cover-submitted">Submitted: June 2026</div>"""

new_author = """    <!-- Author box -->
    <div class="cover-author-box">
      <span class="cover-author-name">Lipi Virmani</span>
      <div class="cover-author-row">Final Year MBA Student</div>
      <div class="cover-author-row">
        <span class="cover-label-inline">Roll No.:</span> _______________
      </div>
      <div class="cover-author-row">Department of Management Studies, Amity University</div>
      <div class="cover-author-row">
        <span class="cover-label-inline">Corresponding Author:</span>
        <a href="mailto:lipiv14@gmail.com" style="color:#1a2e6e;">lipiv14@gmail.com</a>
      </div>
    </div>

    <div class="cover-submitted">Submitted: 11 June 2026</div>"""

content = content.replace(old_author, new_author)

# ─── 3. Add screen-header div right after <body> tag ─────────────────────────
old_body_open = """</head>
<body>

<!-- COVER PAGE -->"""

new_body_open = """</head>
<body>

<!-- Running header visible on screen -->
<div class="screen-header">Amity University</div>

<!-- COVER PAGE -->"""

content = content.replace(old_body_open, new_body_open)

# ─── Write back ──────────────────────────────────────────────────────────────
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
checks = ['screen-header', 'lipiv14@gmail.com', '11 June 2026', 'Final Year MBA Student']
for c in checks:
    print(('OK:' if c in content else 'MISSING:'), c)
