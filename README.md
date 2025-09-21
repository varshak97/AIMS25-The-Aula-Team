# AIMS Hackathon - The Aula Team
This is a repository submitted as part of the [AI against Modern Slavery (AIMS) 2025 Hackathon](https://fundacionpasoslibres.org/aimshackathon/). More information about Project AIMS can be found [here](https://mila.quebec/en/ai4humanity/applied-projects/ai-against-modern-slavery-aims) 

# 1. Problem Statement
**Our Inspiration:** We were inspired by the story of a teen in Nepal, whose family unknowingly placed her into a trafficking scam. If they had access to the right information, they could have made a different choice. Survivors of modern slavery are best positioned to dismantle it, but they lack accessible, reliable sources of information, for safety, prosecution, and policy work. While there are valuable inputs (Survivor Stories, research, law enforcement data, investigative reporting, and corporate supply chain statements), these are rarely contextualized together. Connecting these sources in ways meaningful to Survivors and their allies is a critical, yet complex, interdisciplinary challenge. More details on this is available in our [Comprehensive Project Package](https://github.com/varshak97/AIMS25-The-Aula-Team/blob/main/documentation/Survivors%20Dashboard%20Complete%20Project%20Package%20AIMS%20Hackathon%202025%20Aula.pdf)

# 2. Objective
Leverage the AIMS provided [datasets](https://huggingface.co/datasets/mila-ai4h/AIMS.au/tree/main) consisting of annotated modern slavery statements reported by corporates from AU, UK, CA, fine-tuned sentence classification model ([AIMSDistill BERT model](https://github.com/mila-ai4h/ai4h_aims-au/tree/main/AIMSDistill)), plus the hackathon learnings, and our Team skills to provide survivors and the people who support them a dashboard for getting a wide array of types of information shout any given forced labour situation (industry + region). 

# 3. Proposed Solution: Survivor’s Dashboard
The Dashboard leverages human curation and LLM fine-tuning to contextualize survivor narratives with multiple publicly available data streams: supply chain statements, scam patterns, scholarly research, and reputable media, and directing users to the NGO sources hosting each story (to increase traffic to their sites). Survivors and NGOs can highlight complex lived realities, law enforcement can trace scam patterns, and government assessors can gauge corporate report fidelity using outlier-triangulation methods borrowed from tax auditing. Existing story repositories lack this cross-referenced coding and AIMS-level supply-chain detail. A coded database of NGO story repositories, scholarly work, and law-enforcement reports, and media and government reports. Enables searches by industry and region, revealing survivor experiences alongside the industries and geographies implicated. A two-step LLM process queries curated datasets leveraging the AIMS DistilBERT to classify the curated dataset with the supply chain report classification method, to return detailed and contextualized information. 

**Purpose:** 
- **Survivors:** gain clarity, evidence, representation, and tools to protect others.
- **NGOs:** strengthen advocacy, design localized scam-awareness campaigns, boost SEO traffic, and build political legitimacy.
- **Governments/Law Enforcement/AIMS:** assess corporate report accuracy, plan rescues, and provide AIMS with additional tools for quality control.

**Limitations, Risks & Safeguards**
Plans address ethics, data fidelity, participant safety, ecological impacts, and the tech sector’s own labour risks.

**Proof of Concept & Development**
Team members, including survivors, validated key assumptions with AIMS presenters from the NGOs, governments, law enforcement, and survivor representatives. We then reached out to Nairobi NGO HAART to see if our solution can be of service to the survivors they represent. Next steps: refine through local focus groups, micro-campaigns, expand the curated database, integrate with other AIMS tools or workflows, and pursue public-private partnerships. Future phases include multilingual support, larger NGO participation, and government-level report-triangulation features.

We are Fellows of the Aula Fellowship for AI Science, Policy, and Tech. We are a small but growing NGO. Our website is: [https://theaulafellowship.org](https://theaulafellowship.org). The complete project document contains details on the above, as well as the data and code notes for our submission. 

# 4. Links
- Demo: [App Link](https://aims-app.streamlit.app/)
- GitHub: [fpasoslibres/AIMS-The-Aula-Team](https://github.com/varshak97/AIMS25-The-Aula-Team) 
- Pitch Video: [Link to YouTube video](https://youtu.be/6Ox5CZ0LexA) 

# 5. Datasets
Location: [Datasets.md](https://github.com/varshak97/AIMS25-The-Aula-Team/blob/main/Datasets.md)

# 6. Project Code
Location: [/project_codes](https://github.com/varshak97/AIMS25-The-Aula-Team/tree/main/project_codes)

# 7. Additional docs
Location: [/documentation](https://github.com/varshak97/AIMS25-The-Aula-Team/tree/main/documentation) 

We provide:
- [Comprehensive Project Package (CPP)](https://github.com/varshak97/AIMS25-The-Aula-Team/blob/main/documentation/Survivors%20Dashboard%20Complete%20Project%20Package%20AIMS%20Hackathon%202025%20Aula.pdf)
- [AIMs Dashboard Instructions]()
- [Code Implementation Guide]()
- [Streamlit App Deployment Guide]()
- [survivors_dashboard_documentation](https://github.com/varshak97/AIMS25-The-Aula-Team/blob/main/documentation/survivors_dashboard_documentation.pdf)

# 8. Declaration of Intellectual Property
Copyright the [https://theaulafellowship.org](https://theaulafellowship.org)

# 9. The Team
**Tammy Mackenzie, MBA.**,
The Aula Fellowship,
Montreal, Canada,
[tammy@theaulafellowship.org](tammy@theaulafellowship.org),
Team Lead. Responsible AI systems development.

**Lesly Nzeusseu Kouamou,**
Canada & Belgium,
The Aula Fellowship,
[lesly.nzeusseu.kouamou@umontreal.ca](lesly.nzeusseu.kouamou@umontreal.ca),
Researcher & Doctoral candidate in Organizational psychology,
Mental health and social impacts.

**Onyedikachi Hope Amaechi-Okorie,**
Lagos, Nigeria,
The Aula Fellowship,
[onyedikachi@theaualfellowship.org](onyedikachi@theaualfellowship.org),
Open Source Technical Community Advocate,
Communications, Accessibility & Inclusion and Data Researcher.

**Sukriti Punj,**
Delhi, India,
The Aula Fellowship/ Indira Gandhi Delhi Technical University for Women,
[sukriti@theaulafellowship.org](sukriti@theaulafellowship.org),
Undergrad, Electronics and Communication Engineering,
Contributors from The Aula Fellowship.

**Other Contributors:**

**Varsha Kesavan, MSc.,**
The Aula Fellowship / University of Alberta,
Canada and India,
[vkesavan@ualberta.ca](vkesavan@ualberta.ca),
AI Developer, Ph.D. Candidate (Medical Sciences).

**Faith Wamalwa, M.A. (P.S.)**
The Aula Fellowship,
Nairobi, Kenya,
[fwamalwa@theaulafellowship.org](fwamalwa@theaulafellowship.org),
Strategic Communications and Multimedia Expert.

**Cleopatra Mushonga, Ph.D.,**
Canada & Zimbabwe,
The Aula Fellowship/ Athabasca University,
[cleopatra@theaulafellowship.org](cleopatra@theaulafellowship.org),
Cybersecurity Governance Risk & Compliance (CISSP; ISO/IEC 27001 Lead Auditor-PECB),
AI Governance (ISO/IEC 42001 Lead Auditor- PECB).

**Devin Almonor**,
Washington, D.C., USA,
The Aula Fellowship,
[devin@theaulafellowship.org](devin@theaulafellowship.org),
Software Engineer.