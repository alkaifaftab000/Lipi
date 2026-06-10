path = r'D:\Papers\Lipi\paper\research_paper.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# ─── 1. CSS CHANGES ──────────────────────────────────────────────────────────
old_heading_css = """    h1 { /* Section: 1. Introduction */
      font-size: 12pt;
      font-weight: bold;
      text-align: left;
      text-transform: uppercase;
      margin-top: 2em;
      margin-bottom: 0;
    }
    h2 { /* Sub-section: 1.1 Background */
      font-size: 12pt;
      font-weight: bold;
      text-align: left;
      margin-top: 1.5em;
      margin-bottom: 0;
    }
    h3 { /* Sub-sub section */
      font-size: 12pt;
      font-weight: bold;
      font-style: italic;
      margin-top: 1em;
      margin-bottom: 0;
    }"""

new_heading_css = """    h1 { /* Section headings */
      font-size: 13pt;
      font-weight: bold;
      text-align: left;
      text-transform: uppercase;
      color: #1a2e6e;
      margin-top: 2em;
      margin-bottom: 0.4em;
      page-break-before: always;  /* each section starts on new page */
    }
    h2 { /* Sub-section */
      font-size: 12pt;
      font-weight: bold;
      text-align: left;
      color: #1a2e6e;
      margin-top: 1.5em;
      margin-bottom: 0;
    }
    h3 { /* Sub-sub section */
      font-size: 12pt;
      font-weight: bold;
      font-style: italic;
      color: #1a2e6e;
      margin-top: 1em;
      margin-bottom: 0;
    }
    /* Abstract heading: no page break (it's the first section of the paper) */
    .abstract-section h1 {
      page-break-before: avoid;
      text-align: center;
    }
    /* Prefatory pages (certificate, declaration, TOC etc.) */
    .report-prelim {
      width: 8.27in;
      min-height: 11.69in;
      margin: 30px auto;
      padding: 1in;
      background: #fff;
      box-shadow: 0 4px 32px rgba(0,0,0,0.15);
      page-break-after: always;
    }
    .prelim-title {
      font-size: 16pt;
      font-weight: bold;
      color: #1a2e6e;
      text-align: center;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 1.5em;
      padding-bottom: 0.4em;
      border-bottom: 2px solid #c9a227;
      page-break-before: avoid !important;
    }
    .prelim-body {
      font-size: 12pt;
      line-height: 2;
      color: #111;
    }
    .sign-block {
      margin-top: 2em;
      display: flex;
      justify-content: space-between;
    }
    .sign-item {
      text-align: center;
      line-height: 1.8;
    }
    .sign-line {
      border-top: 1px solid #333;
      width: 160px;
      margin: 0 auto 0.3em auto;
    }
    .toc-entry {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      border-bottom: 1px dotted #bbb;
      padding: 4px 0;
      font-size: 11.5pt;
      line-height: 1.7;
      text-indent: 0;
    }
    .toc-entry.toc-h2 {
      padding-left: 1.2em;
      font-size: 11pt;
      color: #444;
    }
    .toc-entry.toc-section {
      font-weight: bold;
      color: #1a2e6e;
      margin-top: 0.5em;
    }
    .toc-page { flex-shrink: 0; padding-left: 1em; color: #555; }
    @media print {
      .report-prelim {
        box-shadow: none;
        margin: 0;
        width: 100%;
        padding: 0.8in 1in;
        min-height: auto;
      }
    }"""

content = content.replace(old_heading_css, new_heading_css)
print("Step 1: Heading CSS updated" if new_heading_css[:30] in content else "STEP 1 FAILED")

# ─── 2. INSERT PREFATORY PAGES before <div class="paper"> ────────────────────
prelim_pages = """
<!-- ═══════ CERTIFICATE PAGE ═══════ -->
<div class="report-prelim">
  <div style="text-align:center; margin-bottom:1.5em;">
    <img src="logo.png" alt="Amity University" style="width:220px;" />
  </div>
  <h2 class="prelim-title">Certificate</h2>
  <div class="prelim-body">
    <p style="text-indent:0;">
      This is to certify that the Minor Project Report titled:
    </p>
    <p style="text-align:center; font-weight:bold; font-style:italic; text-indent:0; margin:1em 0; color:#1a2e6e;">
      &ldquo;UPI at the Tipping Point: Structural Divergence, Market Concentration,
      and the Systemic Infrastructure Risk of India&rsquo;s Micro-Transaction Economy&rdquo;
    </p>
    <p style="text-indent:0;">
      submitted by <strong>Ms. Lipi Virmani</strong>, Enrollment No. _______________,
      a student of the Final Year MBA Programme, Department of Management Studies,
      Amity University, Noida &mdash; Uttar Pradesh, is a bonafide work carried out
      under my supervision and guidance.
    </p>
    <p style="text-indent:0;">
      This report has not been previously submitted for the award of any degree,
      diploma, or other similar title or recognition.
    </p>
    <div class="sign-block" style="margin-top:3em;">
      <div class="sign-item">
        <div class="sign-line"></div>
        <div><strong>Ms. Lipi Virmani</strong></div>
        <div>Student</div>
        <div>MBA Final Year</div>
      </div>
      <div class="sign-item">
        <div class="sign-line"></div>
        <div><strong>Guide / Supervisor</strong></div>
        <div>Department of Management Studies</div>
        <div>Amity University</div>
      </div>
      <div class="sign-item">
        <div class="sign-line"></div>
        <div><strong>Head of Department</strong></div>
        <div>Department of Management Studies</div>
        <div>Amity University</div>
      </div>
    </div>
    <p style="text-align:center; margin-top:3em; color:#666; font-style:italic; text-indent:0;">
      Date: _______________ &nbsp;&nbsp;&nbsp; Place: Noida, Uttar Pradesh
    </p>
  </div>
</div>

<!-- ═══════ DECLARATION PAGE ═══════ -->
<div class="report-prelim">
  <div style="text-align:center; margin-bottom:1.5em;">
    <img src="logo.png" alt="Amity University" style="width:180px;" />
  </div>
  <h2 class="prelim-title">Student Declaration</h2>
  <div class="prelim-body">
    <p style="text-indent:0;">
      I, <strong>Lipi Virmani</strong>, Enrollment No. _______________,
      a student of Final Year MBA, Department of Management Studies,
      Amity University, Noida, hereby declare that the Minor Project Report titled:
    </p>
    <p style="text-align:center; font-weight:bold; font-style:italic; text-indent:0; margin:1em 0; color:#1a2e6e;">
      &ldquo;UPI at the Tipping Point: Structural Divergence, Market Concentration,
      and the Systemic Infrastructure Risk of India&rsquo;s Micro-Transaction Economy&rdquo;
    </p>
    <p style="text-indent:0;">
      submitted to Amity University in partial fulfilment of the requirement for the award
      of the degree of <strong>Master of Business Administration (MBA)</strong>, is my
      original work and has not been previously submitted for the award of any degree,
      diploma, or other qualification by any university or institution.
    </p>
    <p style="text-indent:0;">
      All information and data used in this report have been sourced from publicly
      available official statistics published by the National Payments Corporation
      of India (NPCI) and have been duly acknowledged.
    </p>
    <p style="text-indent:0;">
      I also declare that the report has been checked for plagiarism and the content
      is original to the best of my knowledge and belief.
    </p>
    <div class="sign-block" style="margin-top:4em; justify-content:flex-start; gap:3em;">
      <div class="sign-item" style="text-align:left;">
        <div class="sign-line" style="margin-left:0;"></div>
        <div><strong>Lipi Virmani</strong></div>
        <div>Final Year MBA Student</div>
        <div>Enrollment No.: _______________</div>
        <div>Date: 11 June 2026</div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════ TABLE OF CONTENTS ═══════ -->
<div class="report-prelim">
  <h2 class="prelim-title">Table of Contents</h2>
  <div class="prelim-body">
    <div class="toc-entry toc-section"><span>Certificate</span><span class="toc-page">ii</span></div>
    <div class="toc-entry toc-section"><span>Student Declaration</span><span class="toc-page">iii</span></div>
    <div class="toc-entry toc-section"><span>Table of Contents</span><span class="toc-page">iv</span></div>
    <div class="toc-entry toc-section"><span>Table of Figures</span><span class="toc-page">v</span></div>
    <div class="toc-entry toc-section"><span>List of Tables</span><span class="toc-page">vi</span></div>
    <div class="toc-entry toc-section"><span>Abstract</span><span class="toc-page">vii</span></div>
    <div class="toc-entry toc-section" style="margin-top:1em;"><span>1. &nbsp; Introduction</span><span class="toc-page">1</span></div>
    <div class="toc-entry toc-h2"><span>1.1 &nbsp; Research Contributions</span><span class="toc-page">3</span></div>
    <div class="toc-entry toc-h2"><span>1.2 &nbsp; Primary Research Question and Hypotheses</span><span class="toc-page">4</span></div>
    <div class="toc-entry toc-section"><span>2. &nbsp; Background and Literature Review</span><span class="toc-page">6</span></div>
    <div class="toc-entry toc-h2"><span>2.1 &nbsp; Evolution of UPI</span><span class="toc-page">6</span></div>
    <div class="toc-entry toc-h2"><span>2.2 &nbsp; Market Concentration and TPAP Duopoly</span><span class="toc-page">8</span></div>
    <div class="toc-entry toc-h2"><span>2.3 &nbsp; Banking Infrastructure Scalability</span><span class="toc-page">10</span></div>
    <div class="toc-entry toc-h2"><span>2.4 &nbsp; Research Gap</span><span class="toc-page">11</span></div>
    <div class="toc-entry toc-section"><span>3. &nbsp; Methodology</span><span class="toc-page">13</span></div>
    <div class="toc-entry toc-h2"><span>3.1 &nbsp; Data Source and Collection</span><span class="toc-page">13</span></div>
    <div class="toc-entry toc-h2"><span>3.2 &nbsp; Dataset Description</span><span class="toc-page">14</span></div>
    <div class="toc-entry toc-h2"><span>3.3 &nbsp; Data Preprocessing and Feature Engineering</span><span class="toc-page">15</span></div>
    <div class="toc-entry toc-h2"><span>3.4 &nbsp; Analytical Framework</span><span class="toc-page">16</span></div>
    <div class="toc-entry toc-section"><span>4. &nbsp; Results</span><span class="toc-page">18</span></div>
    <div class="toc-entry toc-h2"><span>4.1 &nbsp; Phase 1: ATS Divergence Forecasting</span><span class="toc-page">18</span></div>
    <div class="toc-entry toc-h2"><span>4.2 &nbsp; Phase 2: Merchant Clustering</span><span class="toc-page">20</span></div>
    <div class="toc-entry toc-h2"><span>4.3 &nbsp; Phase 3: App Market Concentration (HHI)</span><span class="toc-page">22</span></div>
    <div class="toc-entry toc-h2"><span>4.4 &nbsp; Phase 4: Bank Infrastructure Stress Test</span><span class="toc-page">24</span></div>
    <div class="toc-entry toc-h2"><span>4.5 &nbsp; Phase 5: Geographic Maturity Mapping</span><span class="toc-page">26</span></div>
    <div class="toc-entry toc-section"><span>5. &nbsp; Discussion</span><span class="toc-page">28</span></div>
    <div class="toc-entry toc-section"><span>6. &nbsp; Conclusion</span><span class="toc-page">32</span></div>
    <div class="toc-entry toc-section" style="margin-top:1em;"><span>References</span><span class="toc-page">35</span></div>
    <div class="toc-entry toc-section"><span>Appendix A &mdash; Interactive Dashboard</span><span class="toc-page">37</span></div>
    <div class="toc-entry toc-section"><span>Appendix B &mdash; GitHub Repository</span><span class="toc-page">37</span></div>
  </div>
</div>

<!-- ═══════ TABLE OF FIGURES ═══════ -->
<div class="report-prelim">
  <h2 class="prelim-title">Table of Figures</h2>
  <div class="prelim-body">
    <div class="toc-entry"><span>Figure 3 &nbsp; XGBoost V1 vs V2: Forecast Comparison (10-Month Test Set)</span><span class="toc-page">19</span></div>
    <div class="toc-entry"><span>Figure 4 &nbsp; XGBoost V2 Feature Importance Weights</span><span class="toc-page">19</span></div>
    <div class="toc-entry"><span>Figure 5 &nbsp; Elbow Method: Optimal K for Merchant Clustering</span><span class="toc-page">21</span></div>
    <div class="toc-entry"><span>Figure 6 &nbsp; K-Means Cluster Assignments: 62 UPI Merchant Categories</span><span class="toc-page">21</span></div>
    <div class="toc-entry"><span>Figure 7 &nbsp; Longitudinal HHI Score: UPI Consumer App Ecosystem</span><span class="toc-page">22</span></div>
    <div class="toc-entry"><span>Figure 8 &nbsp; Volume Market Share Distribution Across UPI Applications</span><span class="toc-page">23</span></div>
    <div class="toc-entry"><span>Figure 9 &nbsp; ATS Comparison Across Major UPI Applications</span><span class="toc-page">23</span></div>
    <div class="toc-entry"><span>Figure 10 &nbsp; Average TD% Rates: Public vs. Private Sector Banks</span><span class="toc-page">24</span></div>
    <div class="toc-entry"><span>Figure 11 &nbsp; Top 10 Banks Ranked by Average TD%</span><span class="toc-page">25</span></div>
    <div class="toc-entry"><span>Figure 12 &nbsp; Random Forest Feature Importance (Bank Stress Predictors)</span><span class="toc-page">25</span></div>
    <div class="toc-entry"><span>Figure 13 &nbsp; Volume Share: Top 4 States vs. Rest of India</span><span class="toc-page">26</span></div>
    <div class="toc-entry"><span>Figure 14 &nbsp; Average Ticket Size (ATS) for 15 Emerging Adopter States</span><span class="toc-page">27</span></div>
    <div class="toc-entry"><span>Figure 15 &nbsp; K-Means State UPI Maturity Cluster Scatter Plot</span><span class="toc-page">27</span></div>
  </div>
</div>

<!-- ═══════ LIST OF TABLES ═══════ -->
<div class="report-prelim">
  <h2 class="prelim-title">List of Tables</h2>
  <div class="prelim-body">
    <div class="toc-entry"><span>Table 1 &nbsp; Summary of Datasets Used Across the Five Analytical Phases</span><span class="toc-page">14</span></div>
    <div class="toc-entry"><span>Table 2 &nbsp; Summary of Analytical Framework Across Five Phases</span><span class="toc-page">16</span></div>
    <div class="toc-entry"><span>Table 3 &nbsp; ATS Divergence Forecasting Model Performance Comparison</span><span class="toc-page">18</span></div>
    <div class="toc-entry"><span>Table 4 &nbsp; K-Means Merchant Cluster Summary (K=3)</span><span class="toc-page">21</span></div>
    <div class="toc-entry"><span>Table 5 &nbsp; Bank Infrastructure Stress Test: Model Performance Comparison</span><span class="toc-page">24</span></div>
    <div class="toc-entry"><span>Table 6 &nbsp; K-Means State UPI Maturity Cluster Summary (K=3)</span><span class="toc-page">26</span></div>
  </div>
</div>

"""

# Insert prefatory pages before the paper div
content = content.replace('<div class="paper">', prelim_pages + '<div class="paper">', 1)
print("Step 2: Prefatory pages inserted" if 'Table of Contents' in content else "STEP 2 FAILED")

# ─── 3. ADD APPENDIX before closing </div><!-- /.paper --> ───────────────────
appendix = """
  <!-- ═══════ APPENDIX ═══════ -->
  <h1 id="appendix">Appendix</h1>

  <h2>Appendix A &mdash; Interactive Power BI Dashboard</h2>
  <p>
    A fully interactive Power BI dashboard summarizing all five analytical phases
    of this study &mdash; including dynamic charts for ATS divergence trends,
    merchant cluster scatter plots, HHI longitudinal views, bank TD% heat maps,
    and state-level geographic maturity maps &mdash; is available at the
    following link:
  </p>
  <p style="text-indent:0; margin-top:0.5em;">
    <strong>Dashboard URL:</strong>
    <a href="https://1drv.ms/b/c/702EBD7490371CD4/AWt5UanYJn9DiuHsADi_kvk?e=lUc47s"
       target="_blank" style="color:#1a2e6e;">
      https://1drv.ms/b/c/702EBD7490371CD4/AWt5UanYJn9DiuHsADi_kvk?e=lUc47s
    </a>
  </p>

  <h2>Appendix B &mdash; Code Repository and Data</h2>
  <p>
    All Python scripts used for data preprocessing, machine learning model training,
    and figure generation, along with the processed datasets, are available in the
    open-access project repository:
  </p>
  <p style="text-indent:0; margin-top:0.5em;">
    <strong>GitHub Repository:</strong>
    <a href="https://github.com/alkaifaftab000/Lipi"
       target="_blank" style="color:#1a2e6e;">
      https://github.com/alkaifaftab000/Lipi
    </a>
  </p>
  <p>
    The repository contains the following components:
  </p>
  <ul style="margin-left:0.75in; line-height:2;">
    <li><code>src/</code> &mdash; All 13 Python analysis and preprocessing scripts</li>
    <li><code>data/</code> &mdash; Processed CSV datasets for all five phases</li>
    <li><code>eda/</code> &mdash; Exploratory data analysis figures</li>
    <li><code>models/</code> &mdash; Model output figures and feature importance charts</li>
    <li><code>paper/</code> &mdash; This HTML report</li>
  </ul>

  <h2>Appendix C &mdash; Data Source</h2>
  <p>
    All raw data used in this study was sourced from official NPCI public statistics,
    available at:
  </p>
  <p style="text-indent:0; margin-top:0.5em;">
    <a href="https://www.npci.org.in/product/bhim/product-statistics"
       target="_blank" style="color:#1a2e6e;">
      https://www.npci.org.in/product/bhim/product-statistics
    </a>
  </p>
  <p>
    <strong>Coverage:</strong> January 2022 &ndash; March 2026 (51 months).<br>
    <strong>Datasets:</strong> UPI Macro, Merchant Categories, UPI Apps (TPAPs),
    Bank Performance, State-wise Data.
  </p>

"""

content = content.replace(
    '\n</div><!-- /.paper -->',
    appendix + '\n</div><!-- /.paper -->'
)
print("Step 3: Appendix added" if 'Appendix A' in content else "STEP 3 FAILED")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nAll done. Final checks:")
checks = ['Table of Contents', 'Student Declaration', 'Certificate', 'Table of Figures',
          'List of Tables', 'color: #1a2e6e', 'page-break-before: always', 'Appendix A']
for c in checks:
    print(f"  {'OK' if c in content else 'MISSING'}: {c}")
