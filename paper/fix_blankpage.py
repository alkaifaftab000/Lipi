path = r'D:\Papers\Lipi\paper\research_paper.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# ── Fix 1: Cover in @media print — use exact 297mm (A4), overflow:hidden ─────
old = """      /* Cover fills the entire first page edge-to-edge */
      .cover {
        width: 100%;
        height: 100vh;
        margin: 0;
        box-shadow: none;
      }"""

new = """      /* Cover: exact A4 height in mm (eliminates blank-page rounding bug) */
      .cover {
        width: 100%;
        height: 297mm;
        margin: 0;
        overflow: hidden;
        box-shadow: none;
      }"""

if old in content:
    content = content.replace(old, new)
    print("Fix 1 OK: cover height → 297mm + overflow:hidden")
else:
    print("Fix 1 MISSING — searching for partial...")
    idx = content.find('height: 100vh')
    print(f"  '100vh' found at char {idx}")
    # Brute replace
    content = content.replace('height: 100vh;', 'height: 297mm;')
    content = content.replace(
        'margin: 0;\n        box-shadow: none;\n      }\n      .screen-header',
        'margin: 0;\n        overflow: hidden;\n        box-shadow: none;\n      }\n      .screen-header'
    )
    print("Fix 1 applied via brute replace")

# ── Fix 2: Paper in @media print — also ensure no top margin bleeds ──────────
# Make sure .paper has margin-top: 0 and padding-top: 0.5in for the header space
old2 = """      /* Paper: @page margins are the page margins, so zero out paper padding */
      .paper {
        width: 100%;
        margin: 0;
        padding: 0;
        box-shadow: none;
        background-image: none;
      }"""

new2 = """      /* Paper: @page margins handle spacing, zero out .paper padding/margin */
      .paper {
        width: 100%;
        margin: 0;
        padding: 0;
        box-shadow: none;
        background-image: none;
        break-before: page;  /* modern CSS page break */
      }"""

if old2 in content:
    content = content.replace(old2, new2)
    print("Fix 2 OK: paper break-before:page added")
else:
    print("Fix 2 MISSING — .paper @media print block not found exactly")

# ── Fix 3: cover screen height — use exact A4 ────────────────────────────────
# Change screen .cover height to exactly match (prevents content squeeze issue)
old3 = '      height: 11.69in;\n      margin: 40px auto;'
new3 = '      height: 11.69in;\n      margin: 30px auto;\n      overflow: hidden;'

if old3 in content:
    content = content.replace(old3, new3)
    print("Fix 3 OK: cover screen overflow:hidden added")
else:
    print("Fix 3 SKIPPED (already has overflow or different)")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify key elements
checks = ['297mm', 'overflow: hidden', 'break-before: page', '11 June 2026', 'lipiv14@gmail.com', 'Final Year MBA Student']
print("\nFinal verification:")
for c in checks:
    print(f"  {'OK' if c in content else 'MISSING'}: {c}")
