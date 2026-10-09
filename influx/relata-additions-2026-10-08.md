# relata additions, 2026-10-08

Joseph asked: "Please add Anthropic's frontier compliance framework to relata and anything else we're missing that will be important (nvidia stuff? other gov't stuff?)". This file records:
- what was added;
- what was already there;
- what could not be obtained;
- what was left out on purpose.

UK AISI's own publications were left to a separate agent working at the same time. One item overlapped: that agent added the May 2024 interim International Scientific Report (`bengio-2024-iasr-interim`) earlier the same day, so it is not repeated here.

**In short.**
- **Added:** 103 new relata entries, each with a PDF and with provenance recorded on the entry. Three existing entries that had no document now have one.
- **Conversion:** all 106 were submitted for conversion (`relata prep … --background`); see *Conversion queue* for the state at writing.
- **Not obtained:** Anthropic's Frontier Compliance Framework v1 (see *Could not get*).
- **Company frameworks:** relata already held the current version of every framework the catalog names, NVIDIA's included. What was missing was earlier versions and companion reports.

## How the entries were made, and where the provenance is

- **Open-access papers (48)** were created from arXiv's own BibTeX export, and relata fetched each PDF itself with `relata fetch`. On these entries `pdfs[].added_by` is `relata-fetch` and `pdfs[].source` is the arXiv URL.
- **Everything else (55)** was created with `relata add`, and its PDF registered with `relata pdf --source <url>`. `source` is the URL the bytes were fetched from.
  - Five documents with DOIs went through `relata fetch` first and fell back to this path: Reason, Kaplan & Garrick, Jensen & Meckling, Mitchell, Agle & Wood, and the OECD paper. Unpaywall found no copy relata could download for any of them.
  - Bernheim & Whinston's entry came from its DOI record, and its PDF was attached directly.
- **Web-only documents (13)** were printed with headless Chrome, with a provenance first page in the same format as the existing AISI blog entries (title, source URL, rendering date, agent). They are:
  - the Model Spec;
  - the Seoul commitments, the Bletchley Declaration, both Korean texts and the CAC measures;
  - PROV-DM;
  - Christiano's and Hubinger's posts and METR's 2023 post;
  - two Frontier Model Forum briefs;
  - the PubMed Central text of Reason (2000).
- **Every new entry has an `internal_note`.** It says who added the entry, where its metadata came from, and which repo files cite it. Where an addition was my judgment rather than a citation, the note says so.
- **The earlier framework versions** were checked against Zhu's hash-pinned corpus (`github.com/louisyzhu/frontier-safety-framework-corpus`, commit `2bb68947`). Every file matches the SHA-256 in that corpus's manifest. Most were re-downloaded from the provider's own URL; two exist only in the Internet Archive.
- **Three paywalled papers** (Jensen & Meckling 1976; Bernheim & Whinston 1986; Mitchell, Agle & Wood 1997) are attached from copies that a spike sub-agent downloaded on 2026-10-06 without recording a URL. I could not reconstruct where they came from. Their `source` field says exactly that and quotes the copy's own marks (the Mitchell, Agle & Wood copy has a JSTOR cover sheet). A licensed copy would be better provenance, if Joseph has one.
- **Corrections after creation** were made through relata's own `Relata::Entry#save`, its atomic write, because there is no edit verb:
  - for nine arXiv entries, `year` was set to the v1 year, because arXiv's export gives the latest revision's year, and the keys and the repo's citations use v1. The latest-revision year is in each note;
  - a split corporate author (DSIT) and a stray ":" author (Shanghai AI Lab) were fixed;
  - the IPCC annex's authorship was set as the annex itself directs;
  - three notes I had written from memory were checked against the PDFs and replaced.

  The relata code repo is unchanged.

## Added

The *PDF source* column gives where the PDF came from. "relata fetch (arXiv)" means relata fetched it from arXiv itself.

### Company frameworks: earlier versions and companion documents (15)

| Key | Document | PDF source |
|---|---|---|
| `anthropic-2023-rsp-v1-0` | Anthropic (2023), *Anthropic's Responsible Scaling Policy, Version 1.0* | https://www-cdn.anthropic.com/1adf000c8f675958c2ee23805d91aaade1cd4613/responsible-scaling-policy.pdf |
| `anthropic-2024-rsp-v2-0` | Anthropic (2024), *Responsible Scaling Policy (Version 2.0)* | https://www-cdn.anthropic.com/616dee633636e5bd309cb73aed8622e80fe47839.pdf |
| `anthropic-2025-rsp-v2-1` | Anthropic (2025), *Responsible Scaling Policy, Version 2.1* | https://www-cdn.anthropic.com/17310f6d70ae5627f55313ed067afc1a762a4068.pdf |
| `anthropic-2026-rsp-v3-1` | Anthropic (2026), *Responsible Scaling Policy, Version 3.1* | https://www-cdn.anthropic.com/files/4zrzovbb/website/bf04581e4f329735fd90634f6a1962c13c0bd351.pdf |
| `anthropic-2026-rsp-v3-2` | Anthropic (2026), *Responsible Scaling Policy, Version 3.2* | https://cdn.sanity.io/files/4zrzovbb/website/28c6241900d90410628a8a2003a5572faae4365a.pdf |
| `anthropic-2026-rsp-v3-3` | Anthropic (2026), *Responsible Scaling Policy, Version 3.3* | https://cdn.sanity.io/files/4zrzovbb/website/c11e84981d0a7281a1b229f3fa6af0da66eaf43f.pdf |
| `anthropic-2025-rsp-noncompliance-policy` | Anthropic (2025), *RSP Noncompliance Reporting and Anti-Retaliation Policy* | https://www-cdn.anthropic.com/fcf136d0f2204e2184f73c6bd082bea27f2d631b/RSP%20Noncompliance%20Reporting%20an... |
| `openai-2023-preparedness-framework-beta` | OpenAI (2023), *Preparedness Framework (Beta)* | https://cdn.openai.com/openai-preparedness-framework-beta.pdf |
| `xai-2025-rmf-draft-feb10` | xAI (2025), *xAI Risk Management Framework (Draft)* | https://web.archive.org/web/20250210221647id_/https://x.ai/documents/2025.02.10-RMF-Draft.pdf |
| `xai-2025-rmf-draft-feb20` | xAI (2025), *xAI Risk Management Framework (Draft)* | https://data.x.ai/2025.02.20-RMF-Draft.pdf |
| `meta-2025-frontier-ai-framework-feb` | Meta (2025), *Frontier AI Framework, Version 1.1* | https://web.archive.org/web/20250213105620id_/https://ai.meta.com/static-resource/meta-frontier-ai-framework/ |
| `samsung-2026-ai-safety-framework` | Samsung Electronics (2026), *AI Safety Framework* | https://www.samsung.com/global/sustainability/policy-file/AZTUlveqAMoALYMV/Samsung_Electronics_AI_Safety_Fr... |
| `shanghaiailab-2025-frontier-practice` | Shanghai AI Lab et al. (2025), *Frontier AI Risk Management Framework in Practice: A Risk Analysis Technical Report* | relata fetch (arXiv) |
| `shanghaiailab-2026-frontier-practice-v1-5` | Dongrui Liu et al. (2026), *Frontier AI Risk Management Framework in Practice: A Risk Analysis Technical Report v1.5* | relata fetch (arXiv) |
| `ghosh-2025-safety` | Shaona Ghosh et al. (2025), *A Safety and Security Framework for Real-World Agentic Systems* | relata fetch (arXiv) |

### Developer behaviour and policy documents (3)

| Key | Document | PDF source |
|---|---|---|
| `anthropic-2026-constitution` | Anthropic (2026), *Claude's Constitution* | https://cdn.sanity.io/files/4zrzovbb/website/d0636f72a9493d279ed36b33987da3430bcb5911.pdf |
| `openai-2026-model-spec` | OpenAI (2026), *Model Spec (2026/08/18)* | https://model-spec.openai.com/2026-08-18.html |
| `anthropic-2025-transparency-framework` | Anthropic (2025), *Proposed Frontier Model Transparency Framework* | https://www-cdn.anthropic.com/19cc4bf9eb6a94f9762ac67368f3322cf82b09fe.pdf |

### Government and intergovernmental (16)

| Key | Document | PDF source |
|---|---|---|
| `dsit-2024-frontier-ai-safety-commitments` | Department for Science, Innovation and Technology (2024), *Frontier AI Safety Commitments, AI Seoul Summit 2024* | https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-... |
| `bletchley-2023-declaration` | Countries attending the AI Safety Summit (2023), *The Bletchley Declaration by Countries Attending the AI Safety Summit, 1-2 November 2023* | https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration/the-bletchley-de... |
| `oecd-2024-defining-ai-incidents` | OECD (2024), *Defining AI Incidents and Related Terms* | https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/05/defining-ai-incidents-and-related-ter... |
| `eo-2023-14110` | Executive Office of the President (2023), *Executive Order 14110: Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence* | https://www.govinfo.gov/content/pkg/FR-2023-11-01/pdf/2023-24283.pdf |
| `eo-2025-14179` | Executive Office of the President (2025), *Executive Order 14179: Removing Barriers to American Leadership in Artificial Intelligence* | https://www.govinfo.gov/content/pkg/FR-2025-01-31/pdf/2025-02172.pdf |
| `nist-2026-nccoe-agent-identity` | Booth et al. (2026), *Accelerating the Adoption of Software and AI Agent Identity and Authorization (Concept Paper, Draft)* | https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-i... |
| `colorado-2024-sb24-205` | General Assembly of the State of Colorado (2024), *Senate Bill 24-205: Concerning Consumer Protections in Interactions with Artificial Intelligence Systems* | https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf |
| `colorado-2026-sb26-189` | General Assembly of the State of Colorado (2026), *Senate Bill 26-189: Concerning the Use of Automated Decision-Making Technology in Consequential Decisions* | https://leg.colorado.gov/bill_files/116489/download |
| `korea-2025-ai-framework-act` | Republic of Korea (2025), *Framework Act on the Development of Artificial Intelligence and the Creation of a Foundation for Trust (Act No. 20676, as amended by Act No. 21311)* | https://elaw.klri.re.kr/eng_service/lawViewContent.do?hseq=73499 |
| `korea-2026-ai-framework-act-decree` | Republic of Korea (2026), *Enforcement Decree of the Framework Act on the Development of Artificial Intelligence and the Creation of a Foundation for Trust (Presidential Decree No. 36053)* | https://elaw.klri.re.kr/eng_service/lawViewContent.do?hseq=73696 |
| `imda-2026-mgf-agentic-v1-5` | Infocomm Media Development Authority (2026), *Model AI Governance Framework for Agentic AI, Version 1.5* | https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for... |
| `csa-farai-2025-securing-agentic` | Cyber Security Agency of Singapore & FAR.AI (2025), *Securing Agentic AI: A Discussion Paper* | https://isomer-user-content.by.gov.sg/36/79c01f19-43b1-4955-8584-19364973d303/securing-agentic-ai-discussio... |
| `csa-2026-securing-agentic-addendum` | Cyber Security Agency of Singapore (2026), *Securing Agentic AI: An Addendum to the Guidelines and Companion Guide on Securing AI Systems* | https://isomer-user-content.by.gov.sg/36/9f94d260-ea28-4b12-bf59-cc77cbc0a421/Securing%20Agentic%20AI%E2%80... |
| `tc260-2024-ai-safety-governance-framework` | National Technical Committee 260 on Cybersecurity of Standardization Administration of China (2024), *AI Safety Governance Framework (Version 1.0)* | https://web.archive.org/web/20240911072425/https://www.tc260.org.cn/upload/2024-09-09/1725849192841090989.p... |
| `tc260-2025-ai-safety-governance-framework-2` | National Technical Committee 260 on Cybersecurity of Standardization Administration of China (2025), *AI Safety Governance Framework 2.0* | https://www.cac.gov.cn/rootimages/uploadimg/1759653474200838/1759653474200838.pdf |
| `cac-2023-interim-measures-genai` | Cyberspace Administration of China & others (2023), *Interim Measures for the Management of Generative Artificial Intelligence Services (生成式人工智能服务管理暂行办法)* | https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm |

### Industry bodies and METR (5)

| Key | Document | PDF source |
|---|---|---|
| `fmf-2024-foundational-security` | Frontier Model Forum (2024), *Issue Brief: Foundational Security Practices* | https://www.frontiermodelforum.org/updates/issue-brief-foundational-security-practices/ |
| `fmf-2024-components` | Frontier Model Forum (2024), *Issue Brief: Components of Frontier AI Safety Frameworks* | https://www.frontiermodelforum.org/updates/issue-brief-components-of-frontier-ai-safety-frameworks/ |
| `fmf-2025-risk-taxonomy-thresholds` | Frontier Model Forum (2025), *Risk Taxonomy and Thresholds for Frontier AI Frameworks* | https://www.frontiermodelforum.org/uploads/2025/06/FMF-Technical-Report-on-Frontier-Risk-Taxonomy-and-Thres... |
| `owasp-2025-agentic-top10` | OWASP GenAI Security Project, Agentic Security Initiative (2025), *OWASP Top 10 for Agentic Applications 2026* | https://genai.owasp.org/download/52117/?tmstv=1765059207 |
| `metr-2023-rsp` | Barnes et al. (2023), *Responsible Scaling Policies (RSPs)* | https://metr.org/blog/2023-09-26-rsp/ |

### Catalog upstream sources: papers (2)

| Key | Document | PDF source |
|---|---|---|
| `greenblatt-2023-ai-control` | Ryan Greenblatt et al. (2023), *AI Control: Improving Safety Despite Intentional Subversion* | relata fetch (arXiv) |
| `yampolskiy-2016-taxonomy` | Roman V. Yampolskiy (2015), *Taxonomy of Pathways to Dangerous AI* | relata fetch (arXiv) |

### Risk-analysis and risk-vocabulary literature (17)

| Key | Document | PDF source |
|---|---|---|
| `kaplan-garrick-1981-quantitative` | Kaplan & Garrick (1981), *On The Quantitative Definition of Risk* | https://www.risksciences.ucla.edu/s/On-the-Quantitative-Definition-of-Risk.pdf |
| `reason-2000-human` | Reason, J. (2000), *Human error: models and management* | https://pmc.ncbi.nlm.nih.gov/articles/PMC1117770/ |
| `hse-2001-r2p2` | Health & Safety Executive (2001), *Reducing Risks, Protecting People: HSE's Decision-Making Process* | https://web.archive.org/web/20201210181413id_/https://www.hse.gov.uk/risk/theory/r2p2.pdf |
| `nist-2012-sp800-30r1` | Joint Task Force Transformation Initiative (2012), *Guide for Conducting Risk Assessments (NIST Special Publication 800-30 Revision 1)* | https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf |
| `un-2016-a71644` | United Nations General Assembly (2016), *Report of the Open-Ended Intergovernmental Expert Working Group on Indicators and Terminology Relating to Disaster Risk Reduction (A/71/644)* | https://documents.un.org/doc/undoc/gen/n16/410/23/pdf/n1641023.pdf |
| `leveson-thomas-2018-stpa` | Leveson & Thomas (2018), *STPA Handbook* | https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf |
| `sra-2018-glossary` | Society for Risk Analysis (2018), *Society for Risk Analysis Glossary* | https://www.sra.org/wp-content/uploads/2020/04/SRA-Glossary-FINAL.pdf |
| `ipcc-2022-ar6-wg2-annex-ii` | IPCC (2022), *Annex II: Glossary* | https://www.ipcc.ch/report/ar6/wg2/downloads/report/IPCC_AR6_WGII_Annex-II.pdf |
| `caa-2026-hydrogen-bowtie` | UK Civil Aviation Authority (2026), *CAA Hydrogen Challenge: Bowtie Analysis -- Aircraft Refuelling* | https://www.caa.co.uk/publication/download/29369 |
| `koessler-2023-risk` | Leonie Koessler & Jonas Schuett (2023), *Risk assessment at AGI companies: A review of popular risk assessment techniques from other safety-critical industries* | relata fetch (arXiv) |
| `schnitzer-2023-hazard` | Ronald Schnitzer et al. (2023), *AI Hazard Management: A framework for the systematic management of root causes for AI risks* | relata fetch (arXiv) |
| `salem-2024-risk` | Nayel Fabian Salem et al. (2024), *Risk Management Core -- Towards an Explicit Representation of Risk in Automated Driving* | relata fetch (arXiv) |
| `nolte-2025-review` | Marcus Nolte et al. (2025), *A Review of Conceptualizations of Safety and Risk in Current Automated Driving Regulation* | relata fetch (arXiv) |
| `bommasani-2021-opportunities` | Rishi Bommasani et al. (2021), *On the Opportunities and Risks of Foundation Models* | relata fetch (arXiv) |
| `cobbe-2023-understanding` | Jennifer Cobbe et al. (2023), *Understanding accountability in algorithmic supply chains* | relata fetch (arXiv) |
| `hopkins-2025-supply` | Aspen Hopkins et al. (2025), *AI Supply Chains: An Emerging Ecosystem of AI Actors, Products, and Services* | relata fetch (arXiv) |
| `chu-2026-systematic` | Kexin Chu (2026), *A Systematic Survey of Security Threats and Defenses in LLM-Based AI Agents: A Layered Attack Surface Framework* | relata fetch (arXiv) |

### Alignment and role-vocabulary literature (45)

| Key | Document | PDF source |
|---|---|---|
| `bernheim-whinston-1986-common` | Bernheim & Whinston (1986), *Common Agency* | no origin URL recorded: copy downloaded 2026-10-06 by a law/economics research sub-agent of the ai-risk-mod... |
| `cai-2025-getting` | Will Cai et al. (2025), *Are You Getting What You Pay For? Auditing Model Substitution in LLM APIs* | relata fetch (arXiv) |
| `chan-2025-infrastructure` | Alan Chan et al. (2025), *Infrastructure for AI Agents* | relata fetch (arXiv) |
| `carlsmith-2022-power-seeking` | Joseph Carlsmith (2022), *Is Power-Seeking AI an Existential Risk?* | relata fetch (arXiv) |
| `chan-2024-visibility` | Alan Chan et al. (2024), *Visibility into AI Agents* | relata fetch (arXiv) |
| `christiano-2018-clarifying` | Christiano, Paul (2018), *Clarifying "AI Alignment"* | https://www.lesswrong.com/posts/ZeE7EKHTFMBs8eMxn/clarifying-ai-alignment |
| `conitzer-2024-social` | Vincent Conitzer et al. (2024), *Social Choice Should Guide AI Alignment in Dealing with Diverse Human Feedback* | relata fetch (arXiv) |
| `critch-russell-2017-servant` | Andrew Critch & Stuart Russell (2017), *Servant of Many Masters: Shifting priorities in Pareto-optimal sequential decision-making* | relata fetch (arXiv) |
| `critch-2020-arches` | Andrew Critch & David Krueger (2020), *AI Research Considerations for Human Existential Safety (ARCHES)* | relata fetch (arXiv) |
| `edelman-2025-full-stack` | Joe Edelman et al. (2025), *Full-Stack Alignment: Co-Aligning AI and Institutions with Thick Models of Value* | relata fetch (arXiv) |
| `diaz-2025-secure-agents` | Díaz, Kern & Olive (2025), *An Introduction to Google's Approach for Secure AI Agents* | https://storage.googleapis.com/gweb-research2023-media/pubtools/1018686.pdf |
| `fickinger-2020-multi-principal` | Arnaud Fickinger et al. (2020), *Multi-Principal Assistance Games* | relata fetch (arXiv) |
| `feng-2026-decomposing` | Zhiming Feng (2026), *Decomposing Common Agency* | relata fetch (arXiv) |
| `friedman-kahn-borning-2006-value` | Friedman et al. (2006), *Value Sensitive Design and Information Systems* | https://vsd.ccs.neu.edu/introduction/resources.files/Value_Sensitive_Design.pdf |
| `gabriel-2024-ethics` | Iason Gabriel et al. (2024), *The Ethics of Advanced AI Assistants* | relata fetch (arXiv) |
| `gabriel-2020-artificial` | Iason Gabriel (2020), *Artificial Intelligence, Values and Alignment* | relata fetch (arXiv) |
| `hellrigel-holderbaum-2025-misalignment` | Max Hellrigel-Holderbaum & Leonard Dung (2025), *Misalignment or misuse? The AGI alignment tradeoff* | relata fetch (arXiv) |
| `huang-2026-loyal` | Zimeng Huang et al. (2026), *Loyal Agents: Training LLM Agents to Protect Principal Interests Under Strategic Information Asymmetry* | relata fetch (arXiv) |
| `hubinger-2020-clarifying` | Hubinger, Evan (2020), *Clarifying Inner Alignment Terminology* | https://www.alignmentforum.org/posts/SzecSPYxqRa5GCaSF/clarifying-inner-alignment-terminology |
| `jensen-meckling-1976-theory` | Jensen & Meckling (1976), *Theory of the firm: Managerial behavior, agency costs and ownership structure* | no origin URL recorded: copy downloaded 2026-10-06 by a law/economics research sub-agent of the ai-risk-mod... |
| `kenton-2021-alignment` | Zachary Kenton et al. (2021), *Alignment of Language Agents* | relata fetch (arXiv) |
| `ji-2023-alignment` | Jiaming Ji et al. (2023), *AI Alignment: A Comprehensive Survey* | relata fetch (arXiv) |
| `kasirzadeh-gabriel-2023-conversation` | Atoosa Kasirzadeh & Iason Gabriel (2022), *In conversation with Artificial Intelligence: aligning language models with human values* | relata fetch (arXiv) |
| `kierans-2024-quantifying` | Aidan Kierans et al. (2024), *Quantifying Misalignment Between Agents: Towards a Sociotechnical Understanding of Alignment* | relata fetch (arXiv) |
| `kolt-2025-governing` | Noam Kolt (2025), *Governing AI Agents* | relata fetch (arXiv) |
| `klingefjord-2024-human` | Oliver Klingefjord et al. (2024), *What are human values, and how do we align AI to them?* | relata fetch (arXiv) |
| `korinek-balwit-2022-aligned` | Anton Korinek & Avital Balwit (2022), *Aligned with Whom? Direct and social goals for AI systems* | relata fetch (arXiv) |
| `kolt-2026-caputo` | Noam Kolt et al. (2026), *Legal Alignment for Safe and Ethical AI* | relata fetch (arXiv) |
| `lacroix-2026-relative` | Travis LaCroix (2026), *Relative Principals, Pluralistic Alignment, and the Structural Value Alignment Problem* | relata fetch (arXiv) |
| `leike-2018-scalable` | Jan Leike et al. (2018), *Scalable agent alignment via reward modeling: a research direction* | relata fetch (arXiv) |
| `mishra-2023-ai` | Abhilash Mishra (2023), *AI Alignment and Social Choice: Fundamental Limitations and Policy Implications* | relata fetch (arXiv) |
| `mitchell-agle-wood-1997-toward` | Mitchell et al. (1997), *Toward a Theory of Stakeholder Identification and Salience: Defining the Principle of Who and What Really Counts* | no origin URL recorded: copy downloaded 2026-10-06 by a law/economics research sub-agent of the ai-risk-mod... |
| `ngo-2022-alignment` | Richard Ngo et al. (2022), *The Alignment Problem from a Deep Learning Perspective* | relata fetch (arXiv) |
| `rfc-2020-8693` | Jones et al. (2020), *OAuth 2.0 Token Exchange (RFC 8693)* | https://www.rfc-editor.org/rfc/rfc8693.pdf |
| `riedl-desai-2025-agents` | Mark O. Riedl & Deven R. Desai (2025), *AI Agents and the Law* | relata fetch (arXiv) |
| `shavit-2023-practices` | Shavit et al. (2023), *Practices for Governing Agentic AI Systems* | https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf |
| `shen-2024-towards` | Hua Shen et al. (2024), *Position: Towards Bidirectional Human-AI Alignment* | relata fetch (arXiv) |
| `sorensen-2024-roadmap` | Taylor Sorensen et al. (2024), *A Roadmap to Pluralistic Alignment* | relata fetch (arXiv) |
| `w3c-2013-prov-dm` | Moreau & Missier (2013), *PROV-DM: The PROV Data Model* | https://www.w3.org/TR/prov-dm/ |
| `wallace-2024-instruction` | Eric Wallace et al. (2024), *The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions* | relata fetch (arXiv) |
| `yang-2026-multi-user` | Shu Yang et al. (2026), *Multi-User Large Language Model Agents* | relata fetch (arXiv) |
| `zhixuan-2024-beyond` | Tan Zhi-Xuan et al. (2024), *Beyond Preferences in AI Alignment* | relata fetch (arXiv) |
| `zhang-2026-many-tier` | Jingyu Zhang et al. (2026), *Many-Tier Instruction Hierarchy in LLM Agents* | relata fetch (arXiv) |
| `zverev-2024-separate` | Egor Zverev et al. (2024), *Can LLMs Separate Instructions From Data? And What Do We Even Mean By That?* | relata fetch (arXiv) |
| `askell-2021-general` | Amanda Askell et al. (2021), *A General Language Assistant as a Laboratory for Alignment* | relata fetch (arXiv) |

**Notes on particular entries.**
- `anthropic-2026-constitution`:
  - The title page says "Published January 21, 2026"; the spike's role-vocabulary report says 22 January.
  - It is an Anthropic document. It was added together with OpenAI's Model Spec, as item 7 of the spike's integration plan proposes, and the catalog's conflict-of-interest note applies to both.
- `openai-2026-model-spec` is the 2026-08-18 version, which `model-spec.openai.com` still served as current on 2026-10-08. The web page is the source of record.
- `anthropic-2025-transparency-framework` (July 2025, two pages) is not cited in the repo. I came across it while searching for FCF v1 and added it on judgment, as Anthropic's own proposal for SB 53-style frameworks. Drop it if it is noise.
- `meta-2025-frontier-ai-framework-feb` is the text Meta first published on 3 February 2025. The existing `meta-2025-frontier-ai-framework` is its 28 March re-upload under the same "v1.1" label. Zhu codes two of the re-upload's changes as material:
  - the scope narrows from "match or exceed" to "exceed";
  - the object of the non-release trigger changes from "a catastrophic outcome" to "a threat scenario".
- `xai-2025-rmf-draft-feb10` and `meta-2025-frontier-ai-framework-feb` exist only in the Internet Archive. Their `source` is the Wayback URL.
- **Present-day RSP sequence:** relata now holds v1.0, v2.0, v2.1, v2.2, v3.0, v3.1, v3.2, v3.3 and v3.4. No v1.1 exists (Zhu checked every changelog).
- **NVIDIA.**
  - `nvidia-2025-frontier` is still NVIDIA's only frontier framework. The file NVIDIA serves today has the same hash as relata's copy (Last-Modified 17 February 2025).
  - The one newer NVIDIA framework-type document is `ghosh-2025-safety`, an agentic safety and security framework (NVIDIA with Lakera, arXiv 2511.21990).
  - NVIDIA appears among the later signatories of the Seoul commitments (`dsit-2024-frontier-ai-safety-commitments`).
- **TC260 1.0:** only the English text is attached. The Chinese original's URL is in the entry note. `relata pdf` names the blob `pdfs/<key>.pdf`, which as far as I can tell means one document per entry.
- **Korea:** both texts are the official KLRI English translations; the Korean text is authoritative. Art. 24 of the Enforcement Decree sets the compute trigger for the Act's Art. 32 safety obligation.
- **`kolt-2026-caputo`** is *Legal Alignment for Safe and Ethical AI* (Kolt, Caputo et al.). The key names the second author, not a title word; I noticed only after creation.
- **`kasirzadeh-gabriel-2023-conversation`**: the `year` field is 2022 (arXiv v1), and the key says 2023, as the repo cites it. The note explains.

### Existing entries given a document

| Key | What was attached |
|---|---|
| `hadfield-menell-hadfield-2019-incomplete` | arXiv 1804.04268 preprint (`coverage: preprint`) |
| `aguirre-dempsey-surden-reiner-2020-ai-loyalty` | arXiv 2003.11157 preprint (`coverage: preprint`) |
| `benthall-shekman-2023-fiduciary` | arXiv 2308.02435 preprint (`coverage: preprint`) |

`relata fetch` had escalated all three: Unpaywall located copies, but the downloads failed.

## Looked for and already present

- **Anthropic:** FCF v2 (`anthropic-2026-frontier-compliance-framework-v2`) and the FCF announcement; RSP v2.2, v3.0 and v3.4; the March 2026 noncompliance policy; the Frontier Safety Roadmap (July 2026); both Risk Reports.
- **OpenAI:** Preparedness Framework v2 and the Frontier Governance Framework.
- **Google DeepMind:** FSF v1.0, v2.0, v3.0 and v3.1. No v3.2 or v4 was found.
- **xAI:** RMF of August 2025, FAIF of December 2025, FAIF of June 2026.
- **Others:**
  - Meta's Advanced AI Scaling Framework v2;
  - Microsoft's v1 and February 2026 frameworks;
  - Amazon's 2025 framework and September 2026 update;
  - Cohere v1.0, G42, Magic v1.0, NAVER's 2024 ASF and ASF 2.0;
  - Shanghai AI Lab v1.0;
  - NVIDIA's *Frontier AI Risk Assessment*.
- **Developers with no published framework:** two trackers (regulations.ai, 30 September; Vorp Labs, 12 July) list none for Mistral, Zhipu, Inflection, MiniMax, 01.AI, TII, DeepSeek, Alibaba, Moonshot or ByteDance. No developer besides Anthropic and OpenAI publishes a constitution or model spec of comparable kind.
- **Governments and intergovernmental bodies:**
  - **US:** EO 14365, EO 14409, NSPM-11, the White House legislative framework and the AI Action Plan.
  - **States:** NY S8828 and California SB 53.
  - **Agencies and reports:** DHS's roles framework, NIST AI 100-2e2025 (`vassilev-2025-adversarial`) and the California Report.
  - **International:** the G7 code, OECD HAIP v2, the OECD future-risks report, Perset et al., the UN High-level Advisory Body report, JAISI, the Canadian AISI pages, and IASR Key Updates 1 and 2.
  - **UK and EU:** ETSI EN 304 223, the Five Eyes and NCSC agentic guidance, DSIT's codes of practice, the AI Act, the Digital Omnibus, the GPAI Code, the Commission's GPAI guidelines and the serious-incident template.
- **Literature:**
  - Carroll et al. 2024;
  - Hubinger et al. 2019;
  - Shah et al. 2025;
  - Hammond et al. 2025;
  - Kasirzadeh & Gabriel 2025;
  - Sourbut et al. 2024;
  - Debenedetti et al. 2025 (CaMeL).
- **A key the repo cites but relata lacked:** the government-survey sub-agent swept the 244 keys cited in backticks across the repo and found one: `anthropic-2025-frontier-compliance-framework`, which `influx/thin-pass/` tried for FCF v1. It is still missing; see the next section.

## Could not get

- **Anthropic, *Frontier Compliance Framework* v1 (19 December 2025), and its revisions v1.1 (2 March 2026) and v1.2 (8 June 2026).** All three are known only from v2's changelog and the announcement post.
  - The FCF has only ever been hosted inside Anthropic's Vanta Trust Center (`trust.anthropic.com`), a JavaScript app with no public file URL.
  - I rendered the Trust Center with headless Chrome on 2026-10-08. It lists a single "Anthropic Frontier Compliance Framework" resource: v2, the copy already in relata. v1.1's own resource URL resolves to the same listing.
  - Zhu recorded the earlier versions as withdrawn from the Trust Center by 2026-09-02. The Internet Archive holds only app shells for `trust.anthropic.com/resources*` (Zhu's CDX search, 103 captures). The archive was partly offline when I tried, so I could not repeat that check.
  - A web search for mirrors found commentary that discusses v1, but no copy of it.
  - If v1 is needed as a primary, the remaining routes are to ask Anthropic, or to ask someone who downloaded it in December 2025.
  - The thin pass's dates before 2026-03-02 (v1.1) therefore rest on v2's changelog, not on v1's text.
- **OpenAI, "Towards Safety Cases for Frontier AI Training" (28 September 2026).** This is newer than Zhu's corpus and a plausible addition, but openai.com returns 403 to scripts and a Cloudflare challenge to headless Chrome. Earlier OpenAI pages in relata were captured with headless Chrome, so a later retry may work.

## Chose not to add

- **Same-label re-uploads** that Zhu codes as not material: Anthropic RSP v2.0 (1 November 2024) and v2.1 (1 April 2025), OpenAI PF v2 (15 April 2025 bytes), GDM FSF v2.0 (4 and 13 February 2025), Microsoft v1 (8 February 2025) and Magic (20 July 2024). Their differences are typography, table-of-contents lines, a link or a spelling.
- **xAI's 20 August 2025 RMF as first uploaded.** Its only difference from relata's 22 August copy is that "AISI" was removed from a past-tense list of collaborators. Add it if that mention matters.
- **Frontier Safety Roadmap, February 2026 snapshot**, and Anthropic's RSP redlines (v2.2, v3.1 to v3.4). The snapshot survives only as Wayback HTML, and the redlines are revision accounts rather than versions. Both are in Zhu's corpus.
- **NAVER's Korean-language texts.** They are translations of documents already in relata.
- **IBM's February 2025 safety and governance blog post.** It is a Seoul deliverable, not a frontier framework.
- **NY S.6953-B (the 2025 RAISE text).** S8828 repeals and re-adds Article 44-B, so it is superseded.
- **California SB 1047.** It was vetoed, and its lineage reaches the corpus through the California Report.
- **Statements with little risk content:** the Council of Europe Framework Convention, the Seoul Declaration and Ministerial Statement, the Paris summit statement, and China's Global AI Governance Action Plan (which TC260 2.0 covers).
- **Laws without risk content:** Japan's AI Promotion Act and India's AI Governance Guidelines. Both are promotion-oriented, and the repo does not use them.
- **EU guidance on Art. 73 serious incidents for high-risk systems.** It is not about general-purpose models, and the GPAI incident template is already in relata.
- **Material cited only by the spike's role-vocabulary report, as analogy:** the Uniform Directed Trust Act and the Maine Uniform Trust Code; the Model Context Protocol, A2A and AP2 specifications; and the IETF drafts (WIMSE AIMS, on-behalf-of). The protocol specifications and drafts change frequently and sit outside a risk model's sources. The scratchpad copies are temporary, so they will be lost if not added.
- **SEP entries, Arbital, NIST CSRC glossary pages, IEV and ERA term pages, and HSE's ALARP page.** These are reference pages cited for single definitions.
- **ISO/IEC 22989, 23894, 31000 and 31010, and IEC 31010.** These are paywalled. Only preview excerpts exist in the scratchpad.
- **Papers in the scratchpad that the repo does not cite:** South et al. 2025 (arXiv 2501.09674), Yang et al. *Hierarchical Alignment* (2604.09075), Syed et al. 2026 (2609.22712), Nguyen et al. on AI accountability (2410.04247), Pandit & Rintamäki (2501.14756) and Lee, Cooper & Grimmelmann 2023.
- **Press and commentary** (the catalog's Axios, Fortune and SAN rows). These are context rows, which the catalog marks as read through a web-fetch tool. I did not add them.

## Proposed for `source-catalog.md` (Joseph's call)

- **Upstream table.** Five of its rows now have keys and could carry them:
  - Seoul commitments: `dsit-2024-frontier-ai-safety-commitments`;
  - OECD incident definition: `oecd-2024-defining-ai-incidents`;
  - Greenblatt et al.: `greenblatt-2023-ai-control`;
  - METR: `metr-2023-rsp`;
  - Yampolskiy: `yampolskiy-2016-taxonomy`.

  They are still unread. They can be cited from the corpus once someone reads them.
- **The ANT-RSP, OAI-PF, META and xAI rows** could list the earlier versions now in relata, since the catalog says the template role "belongs to the series and its earlier versions". In particular:
  - `anthropic-2023-rsp-v1-0` through `anthropic-2026-rsp-v3-3`;
  - `openai-2023-preparedness-framework-beta`;
  - `meta-2025-frontier-ai-framework-feb`.
- **The ANT-FCF row** still reads "v1 Dec 19, 2025". It could say that v1 to v1.2 have been withdrawn and that v2 is the only primary.
- **Candidate new rows** (Influence groupings are a guess):
  - Anthropic's constitution and OpenAI's Model Spec, as major (developer governing documents), with the conflict-of-interest note (spike integration plan item 7);
  - the TC260 framework 2.0, as major (China's government framework; Shanghai AI Lab cites it);
  - Korea's Framework Act and Decree, as major (law; NAVER's ASF 2.0 is built on it);
  - IMDA's agentic framework v1.5, as supporting;
  - the FMF *Risk Taxonomy and Thresholds* report, as supporting (Microsoft's framework cites it);
  - EO 14110, as supporting or context. It is revoked, but it is the source of NIST 600-1's and 800-1's "dual-use foundation model" definitions.

## Conversion queue

All 106 keys were submitted with `relata prep … --background`.

- **At 01:50 UTC on 2026-10-09:** all 106 keys were in the shared queue, at the back of about 340 jobs (positions 234 to 339).
- Nothing of mine had converted yet. The single worker converts one document at a time, and documents that need OCR take ten minutes or more each.
- `relata prep list` shows progress. Once the queue drains, `relata show-markdown <key>` works on any of these entries.

## Notes for relata (feedback, not changes)

- **`relata ingest --help` runs ingest** instead of printing help. I ran it by accident at the start. It drained the spool and reported `promoted=0 rejected=0 needs-review=0 skipped=462`, so nothing changed. A `--help` that acts is easy to trip over.
- **`relata add` rejects some BibTeX.** It rejects single-line BibTeX that starts with whitespace, which is the form doi.org content negotiation returns. It also needs the citation key to equal the relata key; arXiv's export uses a different key. Neither is a problem once known.
- **arXiv's BibTeX export gives the latest revision's year.** An arXiv-sourced `add` therefore drifts from the year a work is usually cited by. This is worth knowing for any future bulk add.
- **`possible-duplicates` matches title substrings.** It flagged Bernheim & Whinston's *Common Agency* as a possible duplicate of Feng's *Decomposing Common Agency*.
- **There is no edit verb.** Corrections to entries just created went through `Relata::Entry#save`; a sanctioned verb would make that path visible.
- **One `relata prep --background` run stalled.** I called it with all 106 keys and stdin inherited from the agent's shell. It sat sleeping for more than nine minutes without enqueuing anything, and had no child processes.
  - The same keys, in batches of 25 with stdin closed (`</dev/null`), queued in seconds.
  - I did not find the cause. A read on stdin somewhere in the designator or cascade path is my guess, not a finding.
