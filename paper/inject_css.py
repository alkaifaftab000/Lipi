path = r'D:\Papers\Lipi\paper\research_paper.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the old print block and replace
old = """    @media print {
      body { background: #fff; }
      .paper { box-shadow: none; margin: 0; }
    }
  </style>"""

new = """    /* A4 Print + Running Header & Footer */
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
    }

    /* Cover Page */
    .cover {
      width: 8.27in;
      height: 11.69in;
      margin: 40px auto;
      background: #fff;
      box-shadow: 0 4px 32px rgba(0,0,0,0.15);
      page-break-after: always;
      display: flex;
      flex-direction: column;
      align-items: stretch;
    }
    .cover-stripe-top  { background: #1a2e6e; height: 14px; flex-shrink: 0; }
    .cover-stripe-bottom { background: #c9a227; height: 10px; flex-shrink: 0; margin-top: auto; }

    .cover-body {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 0.5in 1in 0.4in 1in;
    }
    .cover-logo-row {
      width: 100%;
      display: flex;
      justify-content: center;
      padding-top: 0.3in;
      margin-bottom: 0.12in;
    }
    .cover-logo { width: 260px; }

    .cover-rule {
      width: 100%;
      border: none;
      border-top: 1.5px solid #1a2e6e;
      margin: 0.1in 0 0.18in 0;
    }
    .cover-univ-meta {
      text-align: center;
      font-size: 10.5pt;
      color: #333;
      line-height: 1.7;
      margin-bottom: 0.3in;
    }
    .cover-univ-meta strong { font-size: 12pt; color: #1a2e6e; }

    .cover-badge {
      display: inline-block;
      border: 1.5px solid #c9a227;
      color: #6b4c00;
      font-size: 9pt;
      font-weight: bold;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      padding: 5px 20px;
      margin-bottom: 0.26in;
    }
    .cover-paper-title {
      font-size: 17pt;
      font-weight: bold;
      text-align: center;
      color: #0d1b4b;
      line-height: 1.45;
      margin-bottom: 0.16in;
    }
    .cover-scope {
      font-size: 10.5pt;
      font-style: italic;
      text-align: center;
      color: #555;
      line-height: 1.6;
      margin-bottom: 0.38in;
    }
    .cover-gold-rule {
      width: 55%;
      border: none;
      border-top: 2px solid #c9a227;
      margin-bottom: 0.28in;
    }
    .cover-author-box {
      background: #f4f6ff;
      border-left: 4px solid #1a2e6e;
      padding: 0.16in 0.3in;
      width: 78%;
      margin-bottom: 0.22in;
    }
    .cover-author-name {
      font-size: 14pt;
      font-weight: bold;
      color: #0d1b4b;
      display: block;
      margin-bottom: 0.1in;
    }
    .cover-author-row {
      font-size: 10.5pt;
      color: #333;
      padding: 3px 0;
    }
    .cover-label-inline { font-weight: bold; color: #1a2e6e; }
    .cover-submitted {
      font-size: 10pt;
      color: #666;
      font-style: italic;
      text-align: center;
    }
  </style>"""

if old in content:
    content = content.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Cover CSS injected.")
else:
    # Try to find approximate match
    idx = content.find('@media print')
    print(f"Pattern not matched exactly. @media print found at char {idx}")
    print(repr(content[idx-5:idx+100]))
