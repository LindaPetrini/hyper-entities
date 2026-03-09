# Hyper-Entities V3: Spotlight Report

Linda Petrini  
Foresight Institute  
March 2026

---

## 1. Executive Summary

The term *[hyper-entity](https://www.existentialhope.com/podcasts/michael-nielsen-on-hyper-entities-tools-for-thought-and-wise-optimism)* was coined by Michael Nielsen to describe systems that do not yet exist but are already reshaping how people coordinate, allocate capital, and construct shared narratives around their anticipated arrival. These are not speculative fictions. They are attractors — specific enough that researchers, funders, and institutions start organizing around them before anything works. This report identifies and ranks 189 such candidates drawn from 109 sources, with the goal of helping funders, policymakers, and technologists figure out where to pay attention.

The analysis applies the [d/acc framework](https://vitalik.eth.limo/general/2023/11/27/techno_optimism.html) developed by Vitalik Buterin, which evaluates entities across four overlapping properties: democratic (distributing power rather than concentrating it), decentralized (resistant to single points of control or failure), defensive (strengthening protective over offensive capabilities), and differential (accelerating beneficial technologies faster than harmful ones). Entities were also scored on transformative potential and actionability, producing a composite score that determined tier placement.

From 189 candidates, 19 were designated Tier 1 spotlight entities and 170 placed on a Tier 2 watch list. The spotlight entities represent the strongest combination of d/acc alignment, transformative potential, and near-term actionability. Leading this group are Community-Governed AI Mesh Systems (composite score 21), the Universal AI Learning UnCommons (20), and an AI cryptographic oracle with zero-knowledge IoT auditing and jury-DAO governance (19). Across all 189 entities, the average d/acc score was 9.5 out of 20, average transformative score 2.6 out of 5, and average Technology Readiness Level (TRL) 3.9 — placing the field, in aggregate, between proof-of-concept and early validation.

The largest thematic cluster is AI Safety, Alignment & Governance with 31 entities, followed by Scientific Research & Knowledge Infrastructure (25) and Education, Development & Human Flourishing (20). Decentralized & Democratic Institutions and AI-Mediated Deliberation & Collective Intelligence each contribute 18 entities, reflecting how much energy is going into the question of whether governance can scale without centralizing control.

The most common bottleneck across the full dataset is coordination, affecting 76 of 189 entities. Regulatory uncertainty constrains 57, engineering challenges 24, and social acceptance barriers 13. Funding, despite its prominence in public discourse about emerging technology, ranks last as a primary bottleneck, cited for only 7 entities. This distribution suggests that the scarcest resource is not capital but institutional glue — shared standards, protocols, governance frameworks — that gets people pulling in the same direction.

Recommended primary actions reflect this: 68 entities most need sustained research, 58 require convening (bringing together the communities of practice that can establish norms and test coordination mechanisms), and 39 need advocacy to shift regulatory and political conditions. Only 17 are primarily in a build phase. Seven are primarily funding-constrained.

All candidates were sourced from [Existential Hope](https://www.existentialhope.com/) ([existentialhope.com](https://www.existentialhope.com/)), the [Foresight Institute](https://foresight.org/)'s initiative cataloguing pathways to long-term human and civilizational flourishing, drawing on [podcast transcripts](https://www.existentialhope.com/podcasts), [world gallery](https://worlds.existentialhope.com/) submissions, and [AI pathways](https://www.existentialhope.com/ai-pathways) essays. Twenty-seven entities appeared in both this analysis and the prior v2 analysis, giving us a consistency check between two rounds.

---

## 2. Methodology

This report represents the third iteration of the Foresight Institute's hyper-entity pipeline, designated V3. The pipeline has five stages: extraction, deduplication, web research, scoring, and curation into tiers.

**Source extraction.** Candidate entities were extracted from 109 distinct sources hosted on or linked through Existential Hope. These fell into three categories: transcripts from the Existential Hope podcast series, submissions to the Foresight World Gallery, and essays contributed to the AI Pathways project. Extraction targeted named systems, protocols, institutions, or frameworks described as anticipated or proposed rather than fully operational.

**Deduplication.** Raw extraction produced substantial overlap, with the same concept appearing under variant names across sources. Candidates were deduplicated by concept rather than by label, collapsing near-synonyms into single entries and preserving the most descriptive name. This process reduced the candidate pool to 189 distinct entities.

**Web research.** Each deduplicated entity was researched to establish current development status, identify relevant actors, and assign a Technology Readiness Level on the standard 1–9 scale. The distribution skewed early-stage, with a modal TRL of 4 and a range of 1–8. Most candidates have demonstrated feasibility in laboratory or limited-context conditions but have not yet achieved validated prototypes.

**Scoring.** Each entity was scored on three dimensions. The d/acc score (0–20) assessed alignment with democratic, decentralized, defensive, and differential acceleration principles, with five points available per dimension. The transformative score (0–5) captured how much it could change the way societies coordinate or govern. The actionability score (0–5) assessed whether concrete next steps exist and whether current actors can execute them. Composite scores summed d/acc and transformative dimensions. Scoring was performed by the Claude API (Anthropic); we reviewed results by hand at the tiering and editorial stages to catch systematic errors and resolve ambiguous cases.

**Tiering.** Entities with composite scores of 14 or above were designated Tier 1 spotlight entities, yielding 19 candidates. The remaining 170 entities form the Tier 2 watch list. Twenty-seven entities appeared in both V3 and the prior V2 analysis, giving us a consistency check that was weighted positively in borderline cases. Primary bottleneck and recommended action type were assigned categorically rather than scored, based on the web research stage assessment of what currently constrains each entity's development.

---

## 3. Spotlight Entities (Tier 1)

The following 19 entities scored highest on our composite metric (d/acc alignment + transformative potential + actionability). Each represents a system that doesn't yet exist but is already shaping coordination and investment.

### Community-Governed AI Mesh Systems
**Decentralized & Democratic Institutions** | Composite: 21

Decentralized AI networks trained on locally governed data and stewarded by community trust circles rather than centralized corporate or state actors.

**How it works.** Local communities retain sovereignty over data used to train and fine-tune AI models, with governance handled by designated trust circles (particularly Indigenous and racialized community groups) operating under consent frameworks those communities define. A [mesh architecture](https://en.wikipedia.org/wiki/Mesh_networking) distributes both compute and decision-making authority across nodes, so no single actor controls the system. [Flower](https://flower.ai) and [OpenMined](https://www.openmined.org) have proven [federated learning](https://en.wikipedia.org/wiki/Federated_learning) works. [GIDA](https://www.gida-global.org) has proven Indigenous data governance works. Mesh networks work. But nobody has tried to wire them together, partly because the governance conversations happen in completely different rooms from the engineering ones.

**Who's building toward this.** [Flower (adap gmbh)](https://flower.ai) and OpenMined ([PySyft](https://github.com/OpenMined/PySyft)) provide production-grade federated learning infrastructure for distributed model training. The [Global Indigenous Data Alliance](https://www.gida-global.org) stewards the [CARE Principles](https://en.wikipedia.org/wiki/CARE_Principles_for_Indigenous_Data_Governance), and [Local Contexts](https://localcontexts.org) supports Indigenous data sovereignty and cultural heritage protection in digital systems. [Bittensor](https://bittensor.com) is building decentralized AI infrastructure with community-governed token incentives. No dedicated funding for an integrated system has been identified. **TRL: 4**—individual components are mature and deployed; full integration remains unbuilt.

**d/acc alignment.** This entity scores at the ceiling on Democratic (5/5) and Decentralized (5/5) dimensions, reflecting structural governance design that places decision-making authority with affected communities rather than extracting it upward. Defensive posture scores 4/5, as the architecture resists both corporate data capture and state surveillance by design. Key research underpinning this space includes [FLOWER: A Friendly Federated Learning Framework](https://arxiv.org/abs/2007.14390) (2020), [The CARE Principles for Indigenous Data Governance](https://datascience.codata.org/articles/dsj-2020-043) (2019), and UNESCO's report on [Indigenous People-Centered AI](https://www.unesco.org/ethics-ai/en/articles/new-report-and-guidelines-indigenous-data-sovereignty-artificial-intelligence-developments) (2024). (Source: [the-living-rights-network](https://worlds.existentialhope.com/world/the-living-rights-network/))

> **What can someone do RIGHT NOW?** Convene a working group that puts Indigenous data governance leaders, federated learning developers (Flower, OpenMined), and mesh network operators in the same room to draft interoperability standards and shared governance protocols—this coordination work is the actual bottleneck, not missing technology. A funder could seed that process directly by commissioning a joint technical-governance scoping study across these currently siloed communities.

> "communities shaped by displacement, colonization, and exclusion are building decentralized, care-centered mesh networks. These relational systems are trained on locally governed data, stewarded by Indigenous and racialized trust circles, and guided by protocols rooted in consent, dignity, and interdependence—not control." — *Source: [the-living-rights-network](https://worlds.existentialhope.com/world/the-living-rights-network/)*

### Universal AI Learning UnCommons (UALU)
**Education, Development & Human Flourishing** | Composite: 20

A federated governance institution that develops, maintains, and audits AI education tools through multi-stakeholder councils including elders, learners, and ethicists.

**How it works.** UALU operates as a decentralized network of community nodes that co-create and oversee AI educational tools, with governance councils composed of elders, learners, technologists, and ethicists conducting regular audits and setting standards for bias mitigation and cultural appropriateness. The federated structure enables local adaptation while maintaining shared accountability frameworks across the network. Mozilla funds AI governance. The [African Union Commission](https://au.int/en/pressreleases/20240617/african-ministers-adopt-landmark-continental-artificial-intelligence-strategy) is building a continental AI strategy. [UNESCO](https://en.unesco.org/) sets ethics standards, including its [Recommendation on the Ethics of AI](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics) (2021). But none of them have binding enforcement mechanisms that give elder councils actual veto power over AI tools.

**Who's building toward this.** [Mozilla Foundation](https://www.mozillafoundation.org/en/internet-health/trustworthy-artificial-intelligence/) has committed $2.7M (2023) for its Responsible Computing Challenge across Kenya, India, and the US, and $1M (2025–2027) for its Democracy x AI Cohort. The African Union Commission is developing a Continental AI Strategy and Digital Education Strategy (2023–2028) through multi-stakeholder consultation. UNESCO is establishing AI ethics standards and competency frameworks for students and teachers. [AIGN](https://aign.global/ai-governance-framework/global-ai-governance-framework/education-ai-governance-framework/) is developing operational AI governance frameworks for schools and universities with audit mechanisms. [IDRC](https://idrc-crdi.ca/en/research-in-action/commitment-action-advancing-use-ai-education-africa) supports the EmpowerED initiative for responsible AI implementation in African education systems. The project sits at **TRL 3**—conceptual frameworks are mature, but no fully operational federated institution with formal elder council oversight exists at scale.

**d/acc alignment.** UALU scores highest on Democratic (5/5) and Defensive (5/5), reflecting its structural commitment to participatory oversight and harm mitigation through community-led auditing. Decentralization scores 4/5, grounded in the federated node architecture. Relevant publications include Mozilla's [Creating Trustworthy AI](https://assets.mofoprod.net/network/documents/Mozilla-Trustworthy_AI.pdf) (2020), the OECD's [Multi-stakeholder collaboration and co-creation: towards responsible application of AI in education](https://www.oecd.org/en/publications/oecd-digital-education-outlook-2023_c74f03de-en/full-report/multi-stakeholder-collaboration-and-co-creation-towards-responsible-application-of-ai-in-education_07fbbd0d.html) (2023), and [AI Governance in Higher Education](https://arxiv.org/html/2509.06176v1) (2025). (Source: [the-learning-uncommons-of-2035](https://worlds.existentialhope.com/world/the-learning-uncommons-of-2035/))

> **What can someone do RIGHT NOW?** A funder or institutional actor could convene a working group drawing on Mozilla, AIGN, UNESCO, and African Union representatives to design a pilot federated governance structure—the funding exists across these organizations but lacks a coordinating mechanism to integrate elder council participation with operational audit processes.

> "A federated, community-led network responsible for developing, maintaining, and auditing AI education tools. Overseen by councils including elders, learners, technologists, and ethicists to uphold justice and care." — *Source: [the-learning-uncommons-of-2035](https://worlds.existentialhope.com/world/the-learning-uncommons-of-2035/)*

### AI cryptographic oracle with zero-knowledge IoT auditing and jury-DAO
**Decentralized & Democratic Institutions** | Composite: 19

A fraud-resistance layer combining [zero-knowledge proofs](https://en.wikipedia.org/wiki/Zero-knowledge_proof) from IoT sensor data, AI anomaly detection, stake-slashing penalties, and a decentralized human jury for retroactive balance correction.

**How it works.** [IoT](https://en.wikipedia.org/wiki/Internet_of_things) devices generate zero-knowledge proofs of their sensor readings, letting a ledger verify data authenticity without exposing raw feeds that could be spoofed or fabricated. An AI layer monitors token-minting patterns for statistical anomalies, while actors caught cheating face quadratic slashing, penalties that scale super-linearly with stake size to neutralize "too-big-to-fail" manipulation. A randomly selected jury-DAO of token holders can then vote to retroactively adjust balances, placing a human override on top of automated enforcement.

**Who's building toward this.** [**RISC Zero**](https://www.risczero.com/) provides the zero-knowledge virtual machine for proof generation. [**Chainlink**](https://chain.link/) and [**API3**](https://api3.org/) supply decentralized oracle infrastructure. [**Kleros**](https://kleros.io/) has operated a live jury-DAO since 2018, handling 1,000+ cases. Slashing mechanisms are operational in [Ethereum proof-of-stake](https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/). The gap is not that nobody has the pieces but that nobody has tried to combine ZK-IoT with AI anomaly detection under DAO adjudication — the trust boundaries between these systems are undefined. TRL: 4; ZK-IoT proofs demonstrated on ESP32 microcontrollers at ~700ms.

**d/acc alignment.** Defensive scores highest at 5/5, reflecting the system's explicit design to detect and penalize fraud at multiple layers. Democratic and Decentralized both score 4/5, driven by the jury-DAO's human override capacity and the absence of any central arbiter. The research base includes [zk-IoT: Securing the Internet of Things with Zero-Knowledge Proofs on Blockchain Platforms](https://arxiv.org/html/2402.08322v2) (2024), [Detecting Anomalies in Blockchain Transactions using Machine Learning Classifiers and Explainability Analysis](https://arxiv.org/html/2401.03530v1) (2024), and [Anomaly Detection in Blockchain: A Systematic Review](https://www.mdpi.com/2076-3417/15/15/8330) (2025). (Source: [hybrid-market](https://worlds.existentialhope.com/world/hybrid-market/))

> **What can someone do RIGHT NOW?** A researcher or cryptoeconomics team could publish a formal integration specification—defining the trust boundaries, oracle assumptions, and incentive parameters needed to combine ZK-IoT proofs, AI anomaly detection, quadratic slashing, and DAO adjudication into a coherent system. A funder could convene Kleros, RISC Zero, and a blockchain ML group around a shared testnet deployment to resolve the coordination gap blocking production-scale validation.

> "A hard-fork deployed AI cryptographic oracles tied to sensor roots for zero-knowledge IoT based auditing, quadratic-stake slashing to take on 'too-big-to-fail' cheaters, and a jury-DAO to retro-adjust balances." — *Source: [hybrid-market](https://worlds.existentialhope.com/world/hybrid-market/)*

### Moral Trade
**AI-Mediated Deliberation & Collective Intelligence** | Composite: 18

A mechanism by which people or groups with different moral priorities swap concessions so that each gets more of what they care about than unilateral action would yield.

**How it works.** Moral trade applies the logic of economic exchange to ethical preferences: parties identify where their moral priorities are relatively cheap for the other side to accommodate, then negotiate exchanges that leave both better off by their own values. At civilizational scale, this could allow diverse moral communities to each achieve far more of their valued outcomes than competition or majority-rule permits, without requiring any single ethical framework to dominate. [Toby Ord](https://en.wikipedia.org/wiki/Toby_Ord) formalized the concept academically in his paper [Moral Trade](https://www.journals.uchicago.edu/doi/10.1086/682187) (2015); informal versions already occur in activist coalition bargaining and [effective altruism](https://en.wikipedia.org/wiki/Effective_altruism) cause prioritization.

**Who's building toward this.** The [Future of Humanity Institute](https://www.fhi.ox.ac.uk/) and University of Oxford provided the academic home for Toby Ord's foundational theoretical work. The [Effective Altruism](https://www.effectivealtruism.org/) community has explored small-scale applications through informal coordination on charitable donations across cause areas. No dedicated funding has been identified, and the concept sits at TRL 2—theorized and occasionally applied ad hoc, but without formal institutional infrastructure or governance mechanisms.

**d/acc alignment.** Moral trade scores highest on Democratic (5/5) and Decentralized (4/5) dimensions, reflecting its core design goal of enabling pluralistic coordination without imposing a dominant moral framework. Defensive and Differential scores are lower, as the concept addresses coordination rather than security or targeted acceleration. Recent work includes [Moral public goods are a big deal for whether we get a good future](https://forum.effectivealtruism.org/posts/L76qZhfvkediwXd6f/moral-public-goods-are-a-big-deal-for-whether-we-get-a-good) (2025) and a [Moral Trade Proposal with 95-100% Surplus](https://forum.effectivealtruism.org/posts/jvW6p5Hk2r4883tNT/moral-trade-proposal-with-95-100-surplus) (2024). (Source: [Fin Moorhouse](https://finmoorhouse.com/) — [fin-moorhouse-why-we-need-to-aim-higher-than-survival](https://www.existentialhope.com/podcasts/fin-moorhouse-why-we-need-to-aim-higher-than-survival))


> **What can someone do RIGHT NOW?** A researcher or funder could commission a systematic mapping of existing informal moral trade instances across activist coalitions, international negotiations, and EA cause prioritization to identify which coordination mechanisms succeeded and why. A builder with AI expertise could prototype a preference-elicitation and matching tool — the [fair-division](https://en.wikipedia.org/wiki/Fair_division) literature already has working algorithms ([Adjusted Winner](https://en.wikipedia.org/wiki/Adjusted_winner_procedure), [Spliddit](http://spliddit.org/)) that handle analogous problems — to help parties identify low-cost concessions across moral domains.

> "Let's say you really care that people abstain from eating meat, and I really care about people reducing their carbon footprint. Maybe it's not much of a cost for me to eliminate meat from my diet, and it's not much of a cost for you to offset your emissions. Then we have an opportunity for a deal where I eat less meat and you reduce your carbon footprint... if you scale it up to the level of a civilization, there are huge opportunities." — *Source: [podcasts](https://www.existentialhope.com/podcasts/fin-moorhouse-why-we-need-to-aim-higher-than-survival)*

### BCI Operating System (BCI-OS)
**Neurotechnology & Brain-Computer Interfaces** | Composite: 18

An open-source operating system layer for [brain-computer interfaces](https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface) that embeds agency evaluation, AI model compatibility, and privacy standards as core OS-level features.

**How it works.** BCI-OS sits between BCI hardware and applications, enforcing privacy protocols and agency evaluations at the OS level rather than delegating them to individual apps. Standardized model compatibility protocols enable interoperability across hardware manufacturers. An open-source governance structure and standards body maintain human-agency principles, with academic and industry pilots iteratively refining the system.

**Who's building toward this.** [OpenBCI](https://openbci.com/) provides open-source hardware and software platforms with community adoption but without unified privacy or agency frameworks. [AE Studio](https://www.ae.studio/brain-computer-interface) is developing agency-focused BCI tools including the Neurotech Development Kit, with neuroethical principles embedded in its approach. The [Future of Privacy Forum](https://fpf.org) is researching BCI-specific data protection standards, and the [IEEE Standards Association](https://standards.ieee.org/) published a 2024 Standards Roadmap for Neurotechnologies for Machine Interfacing covering sensing, feedback, and data management. No dedicated funding for a unified BCI-OS has been identified. TRL: 3.

**d/acc alignment.** BCI-OS scores highest on Defensive (5/5) and Democratic (4/5), reflecting its core architectural commitment to protecting user agency and neural data privacy, and its open-source governance model that distributes control away from any single manufacturer. Key references include [Enhancing the Security & Privacy of Wearable Brain-Computer Interfaces](https://arxiv.org/abs/2201.07711) (2022), the IEEE [Standards Roadmap: Neurotechnologies for Machine Interfacing](https://standards.ieee.org/) (2024), and the GAO report on [Brain-Computer Interfaces: Applications, Challenges, and Policy Options](https://www.gao.gov/products/gao-25-106952) (2025).


> **What can someone do RIGHT NOW?** A funder or institution could convene a working group pulling together OpenBCI, AE Studio, IEEE, FDA representatives, and privacy researchers to draft a governance charter and interoperability specification for BCI-OS. The fragmented ecosystem is the binding constraint, not technical readiness. That alone won't solve the problem, but right now these groups aren't even using the same vocabulary for agency evaluation, which makes everything downstream harder.

> "['The Open Source BCI Project: Create an open-source brain-computer interface (BCI) operating system to enhance human cognitive abilities and privacy in a TAI era.', 'Develop a privacy-preserving, open-source BCI operating system (BCI-OS) that enhances human cognitive abilities and safeguards human-agency in the TAI era. Integrated agency evaluations, model compatibility protocols, and robust data privacy standards in the BCI-OS.']" — *Source: Diogo de Lucena, Judd Rosenblatt, Mamun Miah*

### Tokenized neural data sharing with selective disclosure
**Neurotechnology & Brain-Computer Interfaces** | Composite: 17

Rather than broadcasting all neural data, the system segments and tokenizes different categories of neural output (emotional states, motor intentions, cognitive content), allowing users to grant or revoke access to specific tokens. Think OAuth scopes for your brain: share an emotional state with a therapist, keep everything else private. Existing healthcare privacy frameworks, including HIPAA and Montana's neuro-rights law, provide the regulatory scaffolding on which such an architecture would sit (see [Regulating neural data processing in the age of BCIs](https://journals.sagepub.com/doi/10.1177/20552076251326123), 2025; [A Framework for Preserving Privacy and Cybersecurity in BCI Applications](https://arxiv.org/abs/2209.09653), 2022; and [Chilean Supreme Court ruling on the protection of brain activity](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1330439/full), 2024). The concept was discussed in a [podcast with Mary Lou Jepsen](https://www.existentialhope.com/podcasts/mary-lou-jepsen-a-handheld-device-to-defeat-cancer) on Existential Hope.

**Who's building toward this.** The [Neurorights Foundation](https://www.neurorightsfoundation.org) drives advocacy and state-level legislation for neural data privacy. The [Future of Privacy Forum](https://fpf.org) produces research and guidance on BCI privacy frameworks. [Columbia University's Neurotechnology Center](https://www.columbia.edu) works on neurorights and data protection frameworks. No funding for this specific architecture has been documented. **TRL: 2** — regulatory concepts exist and are codified in Colorado, California, Montana, and Chile's constitutional protections, but no BCI system with tokenized selective-disclosure has been deployed or demonstrated.

**d/acc alignment.** This scores highest on Defensive (5/5) and Democratic empowerment (4/5), reflecting its core function as a user-controlled protection against involuntary neural data exposure. Decentralization scores lower (2/5) because current implementations rely on centralized regulatory and institutional frameworks.


> **What can someone do RIGHT NOW?** Policy advocates and legal researchers should push for federal technical standards that define granular consent mechanisms for neural data—without unified specifications, companies have no regulatory incentive to build tokenized architectures. Organizations with healthcare IT expertise could draft model technical standards bridging existing OAuth-style access control frameworks to BCI data streams, giving regulators concrete language to adopt.

> "I think it'll be tokenized, basically. You'll let certain parts of what you want to share out, and you'll keep what you want as your innermost thoughts to yourself. Or perhaps you'll have relationships where you wish to share your innermost thoughts." — *Source: [podcasts](https://www.existentialhope.com/podcasts/mary-lou-jepsen-a-handheld-device-to-defeat-cancer)*

### Civic Systems Co-Op
**AI Safety, Alignment & Governance** | Composite: 17

A global open-source consortium that develops and maintains ethical AI tools for municipal and community governance.

**How it works.** Member cities and communities contribute to and draw from a shared repository of AI governance tools, with the consortium setting ethical standards and maintaining transparent decision logs. Governance is distributed across member organizations rather than controlled by a single vendor or government, keeping systems adaptable to local needs. [DPGA](https://digitalpublicgoods.xyz/) has a registry of 150+ [open-source](https://en.wikipedia.org/wiki/Open-source_software) governance tools but no shared development infrastructure. [OGP](https://www.opengovpartnership.org/) has the political relationships but no technical platform. [OpenGov](https://opengov.com/) has the platform but locks cities into a proprietary vendor. A [cooperative](https://en.wikipedia.org/wiki/Cooperative) model would sit between these, combining what each has without the constraints each imposes.

**Who's building toward this.** The [**Digital Public Goods Alliance**](https://digitalpublicgoods.xyz/) (UN-endorsed) maintains a registry of 150+ open-source governance solutions and provides the closest structural analog to a coordinating body. The [**Open Government Partnership**](https://www.opengovpartnership.org/) promotes transparency and accountability frameworks across local and national governments. [**OpenGov**](https://opengov.com/) demonstrates commercial viability with AI-enabled tools for budgeting, permitting, and public engagement across 2,000+ US communities. The [**Open Knowledge Foundation**](https://okfn.org/) develops open-source standards and civic tech tools as a DPGA member. No dedicated funding for a unified consortium has been identified. TRL: 5 — field-tested components exist, but a true cooperative with distributed member control remains at prototype stage. Recent research highlights both the opportunity and the gap: see OGP's [Artificial Intelligence and Open Government: Local Perspectives](https://www.opengovpartnership.org/documents/artificial-intelligence-and-open-government-local-perspectives-2025/) (2025) and [Building Accountable AI in Government](https://www.opengovpartnership.org/stories/building-accountable-artificial-intelligence-in-government-a-practical-reform-agenda/) (2025). The concept originates from the [Commons Cloud](https://worlds.existentialhope.com/world/the-commons-cloud/) scenario on Existential Hope.

**d/acc alignment.** Democratic (4/5), Decentralized (4/5), and Defensive (4/5) scores are all strong, reflecting the model's emphasis on distributed control, member accountability, and protection against vendor lock-in. Differential impact scores lower (2/5) because the mechanism operates within [civic tech](https://en.wikipedia.org/wiki/Civic_technology) rather than across multiple domains.


> **What can someone do RIGHT NOW?** If DPGA won't convene this, a city coalition should just start drafting a consortium charter and contribution model with two or three willing municipalities. The interoperability requirements across current municipal AI deployments need mapping to define the technical baseline a shared repository would need to meet. Waiting for a top-down coordination mandate hasn't worked so far.

> "The Civic Systems Co-Op: a global open-source consortium maintaining ethical, adaptable AI systems for cities and communities." — *Source: [the-commons-cloud](https://worlds.existentialhope.com/world/the-commons-cloud/)*

### Interbeing Forum
**Decentralized & Democratic Institutions** | Composite: 17

> "The Interbeing Forum is a rotating assembly of stewards from across bioregions. It includes people, yes, but also guardians (advised by digital twins) for rivers, soils, and future generations. It oversees the Commonsense Accord and safeguards the integrity of the digital twin ecosystem." — *Source: [the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences](https://worlds.existentialhope.com/world/the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences/)*

A rotating [bioregional](https://en.wikipedia.org/wiki/Bioregionalism) assembly that grants formal representation to ecosystems and future generations through human guardians advised by [digital twin](https://en.wikipedia.org/wiki/Digital_twin) data.

**How it works.** Stewards selected on a rotating basis from bioregions govern through a binding accord, preventing any single faction from entrenching power. Designated guardians speak for non-human entities (rivers, soils) and for future generations, with their positions informed by real-time ecological data from digital twin systems. The assembly also audits that digital infrastructure directly, ensuring it remains a tool of democratic participation rather than centralized control.

**Who's building toward this.** [bioregional.agency](https://lina.community/projects/8e9dd1ac-2b08-4136-9680-d365de3de61b/) (Austria, co-founded 2025 by Gordon Selbach and Jakob Travnik) is piloting bioregional assembly practices; [Resilience.Earth](https://resilience.earth/) is developing distributed decision-making and adaptive governance tools for bioregional communities; [Department of Bioregion / CascadiaNow!](https://cascadiabioregion.org/) has advanced bioregional education across the Cascadia region since 2005; and the [Ozark Area Community Congress](https://cascadiabioregion.org/ozarks-bioregion) has operated a rotating, consensus-based bioregional assembly in the Ozarks since 1980. No dedicated funding has been identified for the integrated Interbeing Forum model. TRL: 3. The Ozark Area Community Congress has run a rotating bioregional assembly since 1980, but without ecosystem guardianship. New Zealand's [Whanganui River](https://en.wikipedia.org/wiki/Environmental_personhood#New_Zealand) has [legal personhood](https://en.wikipedia.org/wiki/Environmental_personhood), but without a bioregional assembly. Nobody has tried both at once. Key research framing the opportunity includes [Where are you at? Re-engaging bioregional ideas](https://compass.onlinelibrary.wiley.com/doi/full/10.1111/gec3.12722) (2023), [Cyber-governance of the natural world: digital twins in environmental governance](https://www.sciencedirect.com/science/article/pii/S2589811625000424) (2025), and [Digital Collaborative Mechanism of Ecological Governance Based on Digital Twin](https://www.mdpi.com/2673-4591/120/1/32) (2026).

**d/acc alignment.** Democratic and Decentralized dimensions both score 4/5, reflecting the rotating stewardship structure and formal power-sharing across bioregions that structurally resists capture. Differential scores lowest (2/5), as the model does not yet create new civilizational action space beyond the governance domain.


> **What can someone do RIGHT NOW?** Legal advocates and policy researchers should work to establish or extend ecosystem legal personhood frameworks, building on New Zealand's Whanganui River precedent and Wales's [Future Generations Commissioner](https://en.wikipedia.org/wiki/Future_Generations_Commissioner_for_Wales), into cross-jurisdictional bioregional contexts. Connecting existing practitioners (OACC, bioregional.agency) with environmental digital twin researchers would accelerate the governance integration that no institution has yet achieved.

### Interoperable Governance Protocol Stack
**Decentralized & Democratic Institutions** | Composite: 16

A shared technical and governance protocol layer that allows citizens to port [digital identities](https://en.wikipedia.org/wiki/Digital_identity), benefits, and credentials across distinct federated city-state systems, and enables AI systems across those jurisdictions to align resource allocation and crisis modeling.

The protocol stack defines common standards for digital identity, benefits entitlements, and credentials so that any compliant local system can read and honor records issued by another. During crises, federated AI systems across jurisdictions share resource allocation decisions and logistics data in a machine-readable format. Governance modules are deliberately modular: jurisdictions can adopt the stack without surrendering local policy autonomy.

The [**OpenID Foundation**](https://openid.net/) completed a [real-world multi-region interoperability demonstration](https://openid.net/openid-foundation-demonstrates-real-world-interoperabiity-of-new-digital-identity-standards/) in May 2025. [**W3C**](https://www.w3.org/) maintains [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-1.1/) and [Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/) standards. The [**Trust Over IP Foundation**](https://www.trustoverip.org/) is developing governance frameworks for decentralized digital trust, and [**GovStack**](https://govstack.global/) is assembling modular government building blocks covering identity, payments, and data exchange. Core identity standards are in production pilots across the EU, UK, Switzerland, Japan, and California, but the combined benefits-portability-plus-AI-crisis-coordination system remains at prototype stage. TRL: 4. Relevant research includes [Interoperable Architecture for Digital Identity Delegation for AI Agents with Blockchain Integration](https://arxiv.org/pdf/2601.14982) (2026) and [Disaster Management in the Era of Agentic AI Systems: A Vision for Federated Crisis Response](https://www.arxiv.org/pdf/2510.16034) (2025).

**d/acc alignment.** Decentralized (4/5) and Defensive (4/5) are the strongest dimensions: the modular architecture preserves jurisdictional autonomy while the crisis coordination capability directly reduces harm from disasters. Democratic alignment (3/5) reflects meaningful but incomplete citizen-facing benefits, and Differential (2/5) is low because the underlying technologies are established rather than frontier.


> **What can someone do RIGHT NOW?** Convene a working group that brings together municipal governments, standards bodies, and emergency management agencies to draft a model mutual-recognition agreement for cross-jurisdictional verifiable credentials — starting with a bilateral pilot between two willing cities. Engaging regulators early to establish shared legal frameworks for benefits eligibility translation matters more than any technical work right now, because regulatory fragmentation is the primary bottleneck.

> "A coalition of federated city-states launches the first interoperable governance protocol stack, allowing citizens to carry digital IDs, benefits, and credentials between different local systems. When severe flooding hits multiple jurisdictions, modular governance systems coordinate relief in hours instead of weeks, sharing resources and logistics seamlessly across local and regional levels." — *Source: N/A*

### Comprehensive AI Services (Drexler)
**AI Safety, Alignment & Governance** | Composite: 16

An architecture of many narrow, domain-limited superhuman AIs that interact competitively rather than a single general [superintelligence](https://en.wikipedia.org/wiki/Superintelligence), achieving safety through structural narrowness.

**How it works.** Rather than building one general-purpose superintelligent system, AI capabilities are deliberately partitioned into domain-specific services that are superhuman within their lane but architecturally prevented from generalizing beyond it. The resulting ecology of competing specialized systems provides checks analogous to market competition or ecological balance, making unilateral takeover or unexpected generalization structurally difficult. Can you wire together narrow AIs without accidentally building a general one? That's the core unsolved question. Safety here comes from the architecture itself, not from aligning a single powerful agent.

**Who's building toward this.** No organization is deliberately implementing CAIS as a unified design paradigm. The [Future of Humanity Institute](https://www.fhi.ox.ac.uk) at the University of Oxford published [K. Eric Drexler](https://en.wikipedia.org/wiki/K._Eric_Drexler)'s foundational 2019 technical report, [*Reframing Superintelligence*](https://www.fhi.ox.ac.uk/publications/reframing-superintelligence-comprehensive-ai-services-as-general-intelligence-technical-report-2019-1-k-eric-drexler/), which remains the primary articulation of the framework. Individual narrow superhuman AIs—[AlphaFold](https://en.wikipedia.org/wiki/AlphaFold), chess engines—demonstrate isolated components, but without architectural enforcement of narrowness or a competitive service ecology. No dedicated funding has been identified. TRL: 2. The concept was discussed in a [podcast with Nathan Labenz](https://www.cognitiverevolution.ai/)][SKIP(https://www.existentialhope.com/podcasts/nathan-labenz-what-are-the-best-case-scenarios-for-ai) on Existential Hope.

**d/acc alignment.** CAIS scores highest on Decentralized (4/5) and Defensive (4/5), reflecting its structural resistance to power concentration and its safety-by-design approach. The low Differential score (2/5) reflects the absence of any implementation pathway that would accelerate this approach relative to general-purpose foundation models.


> **What can someone do RIGHT NOW?** Who funds the [formal verification](https://en.wikipedia.org/wiki/Formal_verification) work? The core unsolved problem is whether service composition across domain-limited AIs can be architecturally bounded to prevent emergent generalization. On the policy side, a regulatory proposal requiring capability partitioning disclosures for frontier model developers would create the coordination infrastructure the CAIS model currently lacks entirely.

> "It's safety through narrowness. It's not to say that the AIs aren't really good at what they do—they could be superhuman at what they do—but in the same way that we have superhuman chess players that can only play chess, and we have superhuman protein folding AIs that can only fold protein, you don't really have to worry that that's going to do something surprising... I think that would be a really good design decision if we could manage it: to have AIs that are potentially superhuman in their domain but are in a pretty fundamental way limited to their domain so they don't do an end-run around whatever guardrails we've put in place." — *Source: [podcasts](https://www.existentialhope.com/podcasts/nathan-labenz-what-are-the-best-case-scenarios-for-ai)*

### Attack Dog DAO for Climate
**Ecological & Regenerative Systems** | Composite: 16

A [DAO](https://en.wikipedia.org/wiki/Decentralized_autonomous_organization) that funds and coordinates environmental litigation on behalf of legally-recognized natural entities, financed through tokenized litigation investment. The idea was [proposed in a conversation about combining crypto mechanisms with climate action](https://www.existentialhope.com/podcasts/trent-mcconaghy-from-starships-to-tokens-pioneering-futures).

**How it works.** Natural bodies granted [legal personhood](https://scholars.unh.edu/unh_lr/vol17/iss2/13/)—rivers, lakes—become plaintiffs in lawsuits against polluters. A DAO pools capital from investors through tokenized litigation finance mechanisms, funding those cases and returning proceeds to investors when litigation succeeds. Investors profit when the lawsuits win. The lawsuits win when polluters lose. That's the whole trick. The [movement to grant legal personhood to nature is growing](https://theconversation.com/granting-legal-personhood-to-nature-is-a-growing-movement-can-it-stem-biodiversity-loss-227336), expanding the potential plaintiff pool.

**Who's building toward this.** The closest attempt was Aristata Capital, which explored climate litigation finance but stopped short of DAO governance or tokenization. Adjacent work is underway from several directions. [**Ryval**](https://www.ryval.io) pioneered [tokenized litigation finance](https://arbitrationblog.kluwerarbitration.com/2022/03/16/litigation-finance-and-crypto-tokens-how-a-blockchain-startup-seeks-to-create-financing-marketplaces-for-disputes/) via Initial Litigation Offerings on blockchain, completing its first ILO in October 2021. [**LawCoin**](https://www.lawcoin.io) tokenizes litigation finance deals on [Ethereum](https://en.wikipedia.org/wiki/Ethereum) for institutional investors. [**MediCoin**](https://www.medicoin.io) has tokenized attorney fee interests specifically in environmental litigation, including [PFAS](https://en.wikipedia.org/wiki/Per-_and_polyfluoroalkyl_substances) cases. [**ClientEarth**](https://www.clientearth.org), the environmental law firm, has inspired litigation finance focused on climate cases through Aristata Capital. No known entity has combined environmental personhood, DAO governance, and tokenized litigation finance into a deployed system. TRL: 3. Funding: none identified for an integrated implementation.

**d/acc alignment.** The concept scores highest on democratic distribution (4/5) and defensive posture (4/5)—it distributes access to legal enforcement mechanisms and directly counters harmful actors—while decentralization is constrained (3/5) by guardian bottlenecks and DAO liability exposure under current law.


> **What can someone do RIGHT NOW?** If ClientEarth or a similar environmental law firm won't pilot a DAO-governed litigation fund, a crypto-native legal team should just build one and let courts sort out the liability questions — the precedent-setting value alone justifies the risk. Separately, engaging securities regulators on the classification of tokenized litigation interests would unblock retail investor participation.

> "One approach is creating an attack dog DAO (Decentralized Autonomous Organization) for climate, similar to the Electronic Frontier Foundation but focused on environmental issues. This DAO could sue on behalf of natural bodies, like rivers or lakes, that have been granted legal personhood. It would leverage litigation finance, where people can invest in these legal battles." — *Source: [podcasts](https://www.existentialhope.com/podcasts/trent-mcconaghy-from-starships-to-tokens-pioneering-futures)*

### Wisdom DAO
**Decentralized & Democratic Institutions** | Composite: 16

A decentralized autonomous organization where human citizens and AI systems jointly propose, deliberate, and vote on governance policy using weighted voting and [blockchain](https://en.wikipedia.org/wiki/Blockchain) transparency. The concept originates from the [Sadvipra AI world-building scenario](https://worlds.existentialhope.com/world/worldbuilding-course-worldbuilding-toolbox-world-entry-page-world-gallery-x-twitter-instagram-medium-bookmark-sadvipra-ai/).

**How it works.** Citizens use personal AI assistants (Citizen-AI) to parse proposals and cast informed votes recorded on a blockchain ledger. A second AI layer aggregates votes into policy drafts. Humans still ratify, but execution runs on [smart contracts](https://en.wikipedia.org/wiki/Smart_contract), removing the usual discretionary window between "approved" and "implemented."

**Who's building toward this.** [Near Foundation](https://near.org) is developing AI-powered delegates and the Pulse sentiment-tracking tool for DAO governance. [SingularityNET](https://singularitynet.io) operates a decentralized AI coordination platform using blockchain for service governance and privacy-preserving datasets. [Aragon](https://aragon.org) provides DAO infrastructure and tooling, while [MakerDAO](https://makerdao.com) demonstrates on-chain token-based governance at meaningful scale. No dedicated funding for integrated human-AI hybrid governance DAOs has been identified. **TRL: 4** — AI agents have been [tested against 3,383 real proposals](https://arxiv.org/html/2510.21117v2) with 97% alignment to historical human decisions, and simulations show a 40% participation increase, but no production deployment at city or national scale exists. Recent research includes a [stepwise development framework for AI-driven DAOs](https://arxiv.org/html/2511.08641v1) and a study on [democratic governance through DAO-based deliberation](https://www.nature.com/articles/s41598-026-40180-8).

**d/acc alignment.** Democratic (4/5) and Decentralized (4/5) are the strongest dimensions, reflecting the system's core design: distributed decision-making authority shared between citizens and AI rather than concentrated in bureaucratic institutions. Defensive scores lower (3/5) because the system's resilience against manipulation and adversarial voting remains unproven at scale.


> **What can someone do RIGHT NOW?** Researchers should publish comparative studies of existing DAO governance pilots—particularly Near Foundation's Pulse deployments—to build the empirical record regulators need to draft workable legal frameworks. Policy advocates should engage directly with [EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act) implementation bodies and [NIST](https://www.nist.gov/artificial-intelligence) to push for explicit guidance on AI-assisted voting systems before legal ambiguity freezes further development.

> "Wisdom DAO – Citizens & AIs co-create policy. By 2035, governance shifted from centralized bureaucracy to decentralized wisdom guided by Sadvipra AI and DAOs. People co-create policy with personal AIs, corruption drops through blockchain transparency, and decisions align with dharma." — *Source: [worldbuilding-course-worldbuilding-toolbox-world-entry-page-world-gallery-x-twitter-instagram-medium-bookmark-sadvipra-ai](https://worlds.existentialhope.com/world/worldbuilding-course-worldbuilding-toolbox-world-entry-page-world-gallery-x-twitter-instagram-medium-bookmark-sadvipra-ai/)*

### Accord of Watersheds
**International Governance & Coordination** | Composite: 16

An international treaty framework that organizes political cooperation around [watershed](https://en.wikipedia.org/wiki/Watershed) and bioregional boundaries rather than national borders, envisioned in the [2035 Rewild scenario](https://worlds.existentialhope.com/world/2035-rewild/).

**How it works.** Signatory parties—nations, Indigenous governments, and regional bodies—agree to coordinate resource use, conservation, and conflict resolution according to the boundaries and health of shared watersheds. Governance bodies are constituted around river basins or bioregions, with binding obligations tied to ecological indicators rather than national interest. Dispute resolution and resource allocation follow hydrological logic rather than political boundaries.

**Who's building toward this.** The [**International Joint Commission (IJC)**](https://ijc.org) has operated transboundary [watershed governance](https://en.wikipedia.org/wiki/Watershed_management) between Canada and the US since 1909, with its [International Watersheds Initiative](https://ijc.org/en/quarter-century-international-watersheds-initiative) (est. 1998) pioneering ecosystem-centered management with Indigenous participation. The [**Mekong River Commission (MRC)**](https://www.mrcmekong.org/) coordinates four nations using [integrated water resources management](https://en.wikipedia.org/wiki/Integrated_water_resources_management) across the Mekong Basin. The [**International Network of Basin Organizations (INBO)**](https://www.inbo-news.org/) supports 120+ river basin organizations globally. The [**Cascadia Department of Bioregion**](https://cascadiabioregion.org/) is developing bioregional governance frameworks across the Pacific Northwest, while [**Resilience.Earth**](https://resilience.earth/) delivers [bioregional governance training](https://ecolise.eu/wp-content/uploads/2025/03/Bioregional-Governance-Training-Guide.pdf) in Asia-Pacific. No dedicated funding for a unified treaty framework has been identified. TRL: 6—operational regional structures exist, but a binding global framework remains conceptual.

**d/acc alignment.** Scores highest on democratic inclusion (4/5) and defensive orientation (4/5), reflecting its emphasis on multi-stakeholder governance and ecological protection over extractive national interest. Decentralization scores moderate (3/5) because watershed bodies, while sub-national in logic, still require centralized treaty architecture to function. For further context, see "[Human Watershed: The Emerging Politics of Bioregional Democracy](https://www.kosmosjournal.org/article/human-watershed-the-emerging-politics-of-bioregional-democracy/)" (2024).


> **What can someone do RIGHT NOW?** Legal advocates and international law scholars can draft model treaty language that converts existing watershed commission frameworks—IJC, MRC—into a replicable binding instrument with enforceable ecological indicators. Policy advocates with access to [UN Environment Assembly](https://www.unep.org/environmentassembly/) or [CBD](https://en.wikipedia.org/wiki/Convention_on_Biological_Diversity) processes should push for a formal resolution recognizing bioregional governance as a legitimate basis for transboundary treaty obligations.

> "The Accord of Watersheds—a treaty system where ecosystems, not nations, are the organizing principle of cooperation." — *Source: [2035-rewild](https://worlds.existentialhope.com/world/2035-rewild/)*

### DAO-governed open innovation platform for TLM documentation and training data
**Decentralized & Democratic Institutions** | Composite: 16

A [DAO](https://en.wikipedia.org/wiki/Decentralized_autonomous_organization)-based governance structure that mandates open-source documentation and community-sourced feedback loops for translation model development and adaptation, as envisioned in [La Langue de la Prévoyance](https://worlds.existentialhope.com/world/la-langue-de-la-prvoyance/).

**How it works.** [Smart-contract](https://en.wikipedia.org/wiki/Smart_contract)-based voting gives communities formal decision-making power over how [translation language model](https://en.wikipedia.org/wiki/Language_model) (TLM) training data is collected, labeled, and updated. [Open innovation](https://en.wikipedia.org/wiki/Open_innovation) platforms serve as the interface for submitting feedback, flagging bias, and proposing model adaptations. Governance rules enforced through the DAO prevent proprietary capture, keeping models and documentation publicly accessible.

**Who's building toward this.** [Hugging Face](https://huggingface.co) hosts over 1,000 community-contributed translation models but has no governance layer for community decision-making over those models. [Mozilla Common Voice](https://commonvoice.mozilla.org) crowdsources multilingual voice data but doesn't give contributors formal control over how it's used. [Ocean Protocol](https://oceanprotocol.com) provides decentralized data exchange with DAO governance and tokenized data assets. [Aragon](https://aragon.org) supplies DAO governance frameworks and is exploring [AI-DAO integration](https://blog.aragon.org/ai-daos-the-future-of-daos-powered-by-artificial-intelligence/). The missing link is connecting contributor governance to model development decisions. Overall TRL: 3. Relevant research includes work on [governance of DAOs that produce open source software](https://www.sciencedirect.com/science/article/pii/S2096720923000416) and a [stepwise development framework for AI-driven DAOs](https://arxiv.org/html/2511.08641).

**d/acc alignment.** Democratic (4/5) and Decentralized (4/5) are the strongest dimensions, reflecting the core design intent to distribute control over model development away from proprietary actors and toward affected communities. Defensive scores lower (3/5) because the system's protective value depends on successful implementation that has not yet been demonstrated at scale.


> **What can someone do RIGHT NOW?** Convene a working group that brings together Hugging Face contributors, Ocean Protocol governance participants, and multilingual community organizations to design and pilot a DAO governance layer specifically for a production translation model — starting with a bounded language pair to test coordination mechanisms before scaling. A funder could seed this pilot by commissioning a governance design sprint that maps smart-contract voting to concrete model update decisions.

> "Decentralized Autonomous Organizations (DAOs) ensure open access to TLM documentation and training data so that communities drive decision-making on model adaptations. Open innovation platforms source community feedback to further transparency and interoperability." — *Source: [la-langue-de-la-prvoyance](https://worlds.existentialhope.com/world/la-langue-de-la-prvoyance/)*

### Watershed Parliaments
**Decentralized & Democratic Institutions** | Composite: 16

[Bioregional](https://en.wikipedia.org/wiki/Bioregionalism) governance bodies organized around watershed boundaries rather than political borders, incorporating ecological feedback into formal decision-making. The concept appears in the [Mycelial Democracy scenario](https://worlds.existentialhope.com/world/mycelial-democracy/).

**How it works.** Governance jurisdiction is defined by hydrological catchment areas, replacing nation-state and municipal lines with boundaries that match the actual movement of water and the ecosystems it sustains. Decision-making bodies include designated representatives for ecosystem interests alongside human citizens. Before adoption, proposals must pass multi-generational impact assessments covering all species within the watershed.

**Who's building toward this.** The [**Murray-Darling Basin Authority**](https://www.mdba.gov.au/) (Australia) manages integrated water resources across a major watershed with Indigenous representation and multi-stakeholder governance. The [**Susquehanna River Basin Commission**](https://www.srbc.gov/) and [**Interstate Commission on the Potomac River Basin**](https://www.potomacriver.org/) coordinate water management across multi-state jurisdictions in North America. The [**Cascadia Department of Bioregion**](https://cascadiabioregion.org/) advocates for watershed-based political restructuring, aligned with the vision of "[bioregional democracy](https://www.kosmosjournal.org/article/human-watershed-the-emerging-politics-of-bioregional-democracy/)" as an emerging political form. New Zealand's [Whanganui River](https://en.wikipedia.org/wiki/Environmental_personhood#New_Zealand), granted [legal personhood](https://en.wikipedia.org/wiki/Environmental_personhood) in 2017, remains the clearest proof-of-concept for ecosystem rights integration. No dedicated funding was identified. TRL: 4 — operational governance structures exist at watershed scale, but full ecosystem representation and multi-generational impact assessment mechanisms remain largely theoretical.

**d/acc alignment.** **Watershed Parliaments** score highest on Democratic (4/5) and Defensive (4/5), reflecting their potential to distribute political power along ecological lines and build long-term resilience against resource conflicts. Decentralization scores lower (3/5) because existing implementations remain embedded within nation-state structures rather than replacing them. For a broader framing, see "[Bioregionalism: A Model for a Self-Sufficient and Democratic Economy](https://earth.org/bioregionalism/)" (2021).


> **What can someone do RIGHT NOW?** If the Whanganui River legal personhood model can't be expanded into binding governance frameworks in other jurisdictions, watershed parliaments remain a thought experiment. Advocates and legal scholars should focus there first. Separately, a comparative study of existing river basin commissions would identify which governance features actually transfer to full bioregional authority structures.

> "Watershed Parliaments replace geopolitical boundaries with bioregional governance aligned with natural water systems. These institutions integrate human decision-making with ecological feedback, where voting rights extend to ecosystem representatives and decisions must demonstrate positive impacts across seven generations of all life forms within the watershed." — *Source: [mycelial-democracy](https://worlds.existentialhope.com/world/mycelial-democracy/)*

### Digital Twins for Communities and Ecosystems
**AI-Mediated Deliberation & Collective Intelligence** | Composite: 16

Real-time digital models of communities and ecosystems that enable participatory future simulation with locally-owned data.

**How it works.** Sensor networks and continuous data feeds update digital models of local ecological and social conditions, allowing stakeholders to run simulations of policy or environmental decisions before implementing them. Critically, communities retain ownership of their data rather than ceding it to centralized platforms. Outputs can inform governance bodies, including representatives for non-human entities such as rivers.

**Who's building toward this.** The [**Singapore Land Authority**](https://www.sla.gov.sg/) built [Virtual Singapore](https://en.wikipedia.org/wiki/Virtual_Singapore), the first country-scale urban [digital twin](https://en.wikipedia.org/wiki/Digital_twin), operational since 2022 following a $73M investment over 2012–2017. The [**Alan Turing Institute**](https://www.turing.ac.uk/research/research-projects/ecosystems-digital-twins) is developing methodology for scalable digital twin ecosystems and national digital twin infrastructure. [**Northeastern University's Boston Area Research Initiative (BARI)**](https://www.northeastern.edu/) is building Fora.ai, a participatory modeling platform for community-led digital twins in green infrastructure planning (see "[Enhancing digital twin technology with community-led, science-driven participatory modeling](https://journals.sagepub.com/doi/10.1177/23998083251323671)," 2025). [**The Nature Conservancy and Esri**](https://www.esri.com/about/newsroom/blog/open-science-environmental-digital-twin) are developing environmental digital twins for ecosystem monitoring, including the Point Conception project. TRL sits at 5: urban digital twin components are mature, but participatory governance integrated with community [data sovereignty](https://en.wikipedia.org/wiki/Data_sovereignty) at scale remains in prototype phase. Broader framing appears in "[Digital twins and the digital logics of biodiversity](https://journals.sagepub.com/doi/full/10.1177/03063127241236809)" (2024) and "[City Digital Twin Concepts: A Vision for Community Participation](https://www.researchgate.net/publication/359184358_City_Digital_Twin_Concepts_A_Vision_for_Community_Participation)" (2022). The concept originates from the [Commonsense Accord world](https://worlds.existentialhope.com/world/the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences/).

**d/acc alignment.** This entity scores highest on democratic (4/5) and defensive (4/5) dimensions, reflecting its potential to distribute simulation capacity to communities and reduce harm from uninformed governance decisions. Decentralization scores 3/5 because data sovereignty frameworks and community-owned infrastructure remain partially realized rather than structurally embedded.


> **What can someone do RIGHT NOW?** Funding a structured pilot that combines Fora.ai-style participatory modeling with a community data ownership agreement and an operational sensor network would move this from conceptual integration to demonstrated production system. Singapore proved national-scale digital twins work; Fora.ai proved participatory modeling works; GDPR and Indigenous data governance proved data sovereignty frameworks work. The gap is that urban planners, data sovereignty practitioners, and sensor network operators don't attend the same conferences.

> "Digital twins reflect the real-time state of communities and ecosystems. They help people simulate futures, explore consequences, and make decisions guided by care, memory, and shared responsibility. Every community and citizen holds its own data as a form of digital sovereignty." — *Source: [the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences](https://worlds.existentialhope.com/world/the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences/)*

### Loyal AI Assistance (Fiduciary AI Assistance)
**AI Safety, Alignment & Governance** | Composite: 15

> **What can someone do RIGHT NOW?** Legal scholars, policy advocates, and AI governance organizations should push for regulatory frameworks that define and enforce fiduciary duty standards for AI assistants. This is the explicit gating factor for commercial adoption. Connecting existing legal instruments like [UETA](https://en.wikipedia.org/wiki/Uniform_Electronic_Transactions_Act) to AI agent accountability, and building coalitions that pressure regulators to establish compliance mechanisms, would move this from research artifact to deployable standard.

A personal AI system explicitly designed to serve the individual user's goals rather than platform or advertiser interests, functioning more like a [fiduciary](https://en.wikipedia.org/wiki/Fiduciary) than a product. A loyal AI assistant would know the user deeply enough to genuinely assist rather than manipulate, with no third-party incentives embedded in its objective function. Unlike Siri or Alexa, which are structurally oriented toward platform revenue and data monetization, a fiduciary AI would operate under a duty of loyalty and care analogous to legal fiduciary relationships.

The [Montreal AI Ethics Institute](https://montrealethics.ai/) has developed research and design frameworks for fiduciary AI systems (see "[Designing Fiduciary Artificial Intelligence](https://dl.acm.org/doi/fullHtml/10.1145/3617694.3623230)," 2023). [Consumer Reports Innovation](https://innovation.consumerreports.org/) is exploring personal AI agents operating under fiduciary duty principles, detailed in "[Empowering Consumers with Personal AI Agents](https://innovation.consumerreports.org/empowering-consumers-with-personal-ai-agents-legal-foundations-and-design-considerations/)" (2025). The [Alignment Research Center](https://alignment.anthropic.com/) contributes relevant user-centric alignment research. Legal foundations are explored in "[Fiduciary Principles in AI: Utilizing the Duty of Loyalty](https://www.bu.edu/law/files/2023/09/Fiduciary-paper.pdf)" (2023). No dedicated external funding has been documented. **TRL 3** — published design methodologies and legal frameworks exist, but no commercial deployment has occurred. The concept emerged from a podcast discussion with [Anthony Aguirre](https://en.wikipedia.org/wiki/Anthony_Aguirre) [on worldbuilding](https://www.existentialhope.com/podcasts/anthony-aguirre-anna-yelizarova-on-worldbuilding).

**d/acc alignment.** Scores highest on Democratic control (4/5) and Defensive posture (4/5), reflecting its core purpose of returning AI agency to individuals and protecting users from manipulative system design. Decentralization and differential acceleration scores are weaker (2/5 each).


> "One of the things that came out of the augmented intelligence summit was fiduciary AI assistance. I have been calling them loyal AI assistance. There is a loyal AI system that doesn't have selfish interests and works to advance your goals and interests." — *Source: [podcasts](https://www.existentialhope.com/podcasts/anthony-aguirre-anna-yelizarova-on-worldbuilding)*

### The Global Deliberation Coordinator
**AI-Mediated Deliberation & Collective Intelligence** | Composite: 15

A platform institution designed to coordinate global deliberative processes and collective decision-making specifically around AI governance.

**How it works.** The institution establishes structured coordination infrastructure that convenes global stakeholders—states, civil society, technical experts—for deliberative discussions on AI governance, enabling collective decisions that cross national and organizational boundaries. Unlike existing expert bodies, the model centers inclusive participation and [deliberative](https://en.wikipedia.org/wiki/Deliberative_democracy) legitimacy rather than top-down technical guidance. AI tools support multilingual, asynchronous deliberation at scale across time zones and cultures.

**Who's building toward this.** The **UN [Global Dialogue on AI Governance](https://www.un.org/global-dialogue-ai-governance/en)** (launched August 2025) provides the most operational foundation, offering an inclusive state-and-stakeholder platform. [**AI4Deliberation**](https://cordis.europa.eu/project/id/101178806) ([Horizon Europe](https://en.wikipedia.org/wiki/Horizon_Europe), €2,999,500) is building AI-enabled deliberative toolkits for governments. [**Connected by Data**](https://connectedbydata.org/resources/global-deliberation-ai) is researching independent global assembly designs for AI governance. [**AI & Democracy Foundation**](https://aidemocracyfoundation.org/) focuses on deliberative processes for AI alignment. [**Metagov**](https://metagov.org/) develops digital self-governance infrastructure. TRL sits at 4: pilots are proven, but no unified global coordination architecture exists yet. Key publications include "[Global AI Governance: Where the Challenge is the Solution](https://arxiv.org/pdf/2503.04766)" (2025), "[Global Citizen Deliberation on Artificial Intelligence: Options and design considerations](https://connectedbydata.org/resources/global-deliberation-ai)" (2024), and the "[Governing AI for Humanity](https://www.un.org/sites/un2.un.org/files/governing_ai_for_humanity_final_report_en.pdf)" UN High-Level Advisory Body Final Report (2024).

**d/acc alignment.** Democratic (4/5) and Defensive (4/5) are the strongest dimensions—this entity directly addresses who gets a voice in AI governance decisions and builds resilience against unilateral capture of those decisions. Decentralized and Differential scores (2/5 each) reflect that coordination infrastructure, by design, requires some centralization.


> **What can someone do RIGHT NOW?** Use the UN Global Dialogue on AI Governance as a convening anchor: fund Connected by Data or Metagov to translate their global assembly design research into a concrete coordination architecture proposal, then pressure-test it with delegations from the 118 currently excluded countries before the next major AI governance summit.

> "The Global Deliberation Coordinator (Hackathon shared second place): Focuses on establishing a platform for global discussions and decision-making on AI and other pressing issues." — *Source: N/A*

### Epistemic stack
**Scientific Research & Knowledge Infrastructure** | Composite: 14

> "There is no reason why, when reading a newspaper article about something, you shouldn't be able to trace back: where did that quote come from, or where did this piece of information come from? How do I know whether to trust this?... We should be able to have a stack we can follow all the way from the high level back down to the raw ingredients, and then figure out how much we trust each of those steps." — *Source: [podcasts](https://www.existentialhope.com/podcasts/anthony-aguirre-tools-or-agents-choosing-our-ai-future)*

A citation and [provenance](https://en.wikipedia.org/wiki/Provenance) system for all information, from newspaper articles to social media claims, that lets users trace any assertion back to its raw data sources, with trust scores based on historical accuracy of each link in the chain.

**How it works.** Every piece of information carries machine-readable provenance metadata linking it to its source, analogous to academic citations but applied universally. AI tools help users traverse this chain from a high-level claim down to raw data, which can be cryptographically signed by hardware [secure enclaves](https://en.wikipedia.org/wiki/Trusted_execution_environment). Each node in the chain (person, outlet, inference step) accumulates a reliability record based on past accuracy, giving users a principled basis for assessing any given claim.

**Who's building toward this.** The [Coalition for Content Provenance and Authenticity (C2PA)](https://c2pa.org/) released its open technical standard in 2022, with adoption now spanning camera makers, news outlets, and platforms. The [Content Authenticity Initiative (CAI)](https://contentauthenticity.org/) develops open-source tooling within that coalition. [X's Community Notes](https://communitynotes.x.com/) operates crowdsourced fact-checking at scale with 133,000+ contributors. [Numbers Protocol](https://captureapp.xyz/) integrates C2PA provenance data with blockchain for immutable asset tracking. No dedicated funding for a unified epistemic stack has been identified. TRL: 4—components exist in isolation; end-to-end integration from raw sensor data through inference to published claims with per-node trust scoring remains unbuilt. The vision is articulated in "[A Full Epistemic Stack: Knowledge Commons for the 21st Century](https://www.oliversourbut.net/p/a-full-epistemic-stack)" (2025), while related challenges are examined in "[The Provenance Problem: LLMs and the Breakdown of Citation Norms](https://arxiv.org/abs/2509.13365)" (2025) and "[Architecting Trust in Artificial Epistemic Agents](https://arxiv.org/html/2603.02960)" (2025). The concept draws from a podcast discussion with [Anthony Aguirre](https://en.wikipedia.org/wiki/Anthony_Aguirre) on [choosing our AI future](https://www.existentialhope.com/podcasts/anthony-aguirre-tools-or-agents-choosing-our-ai-future).

**d/acc alignment.** Defensive scores highest (4/5) because accurate provenance directly counters manipulation and misinformation at the infrastructure level. Democratic scores 3/5, reflecting the system's potential to equalize access to source-level verification across users and institutions.


> **What can someone do RIGHT NOW?** Who convenes C2PA, the academic citation graph projects, and platform trust-and-safety teams to define a shared metadata schema? That's the missing piece. The technology for media provenance, inference-step logging, and per-node accuracy scoring exists in fragments across these communities. A funded convening body with a concrete interoperability mandate could close the gap faster than any single technical project.


---

## 4. Watch List (Tier 2)

The remaining 170 entities form the watch list — systems worth tracking but not yet meeting the composite score threshold for spotlight treatment.

| Name | Group | d/acc | Trans. | Bottleneck | Action | TRL | Source |
|------|-------|-------|--------|------------|--------|-----|-----|
| **AI Fiduciaries** | AI Safety, Alignment & Governance | 17/20 | 3/5 | Coordination | Convene | 5 | |
| **Liberal/Popperian AGI Education Framework** | AI Safety, Alignment & Governance | 15/20 | 4/5 | Physics | Research | 1 | [david-deutsch-on-beauty-knowle](https://www.existentialhope.com/podcasts/david-deutsch-on-beauty-knowledge-and-progress) |
| **Privacy-Preserving Global Regulatory Markets for AI Verif...** | AI Safety, Alignment & Governance | 16/20 | 3/5 | Coordination | Convene | 3 | [emilia-javorsky-the-future-of-](https://www.existentialhope.com/podcasts/emilia-javorsky-the-future-of-ai-bioengineering-and-human-empathy) |
| **LexNodes** | Decentralized & Democratic Institutions | 16/20 | 3/5 | Regulation | Advocate | 4 | [lexcommons-the-open-law-societ](https://worlds.existentialhope.com/world/lexcommons-the-open-law-society/) |
| **Viotopia** | Education, Development & Human Flouri... | 13/20 | 4/5 | Coordination | Research | 1 | [fin-moorhouse-why-we-need-to-a](https://www.existentialhope.com/podcasts/fin-moorhouse-why-we-need-to-aim-higher-than-survival) |
| **Continuity Guild** | Education, Development & Human Flouri... | 15/20 | 2/5 | Coordination | Convene | 5 | [threadtime](https://worlds.existentialhope.com/world/threadtime/) |
| **BioEcho Mesh** | Ecological & Regenerative Systems | 14/20 | 2/5 | Coordination | Convene | 6 | [2035-rewild](https://worlds.existentialhope.com/world/2035-rewild/) |
| **Cognitive Field Resonators (CFRs)** | Scientific Research & Knowledge Infra... | 15/20 | 1/5 | Physics | Research | 1 | [harmonic-futures-a-2035-of-coh](https://worlds.existentialhope.com/world/harmonic-futures-a-2035-of-coherence-not-convenience/) |
| **The Mnemosyne Assembly** | AI Safety, Alignment & Governance | 13/20 | 3/5 | Coordination | Convene | 3 | [harmonic-futures-a-2035-of-coh](https://worlds.existentialhope.com/world/harmonic-futures-a-2035-of-coherence-not-convenience/) |
| **Translation Language Models (TLMs) with citizen-owned tra...** | AI-Mediated Deliberation & Collective... | 13/20 | 3/5 | Coordination | Build | 4 | [la-langue-de-la-prvoyance](https://worlds.existentialhope.com/world/la-langue-de-la-prvoyance/) |
| **Open Cognition Ledger** | Decentralized & Democratic Institutions | 13/20 | 3/5 | Coordination | Convene | 4 | [symbiotic-wisdom](https://worlds.existentialhope.com/world/symbiotic-wisdom/) |
| **Polymesh Civic Ledger** | Decentralized & Democratic Institutions | 13/20 | 3/5 | Coordination | Research | 4 | [symbiotic-wisdom](https://worlds.existentialhope.com/world/symbiotic-wisdom/) |
| **Living Rights Network** | Decentralized & Democratic Institutions | 13/20 | 3/5 | Coordination | Convene | 4 | [the-living-rights-network](https://worlds.existentialhope.com/world/the-living-rights-network/) |
| **The Collective of Inner Weavers** | AI Safety, Alignment & Governance | 13/20 | 3/5 | Funding | Fund | 4 | [veliona-the-world-of-unfolding](https://worlds.existentialhope.com/world/veliona-the-world-of-unfolding-minds/) |
| **Federated Procurement Platforms** | Economic Systems & Resource Distribution | 13/20 | 2/5 | Coordination | Convene | 5 | |
| **contextual autonomy** | AI Safety, Alignment & Governance | 12/20 | 3/5 | Coordination | Convene | 4 | |
| **Publishing for Machines (machine-readable scientific publ...** | Scientific Research & Knowledge Infra... | 12/20 | 3/5 | Social Acceptance | Convene | 4 | [andrew-white-building-an-ai-sc](https://www.existentialhope.com/podcasts/andrew-white-building-an-ai-scientist-to-automate-discovery) |
| **De novo designed universal flu vaccines (Neil King / Bake...** | Biotech, Medicine & Life Extension | 12/20 | 3/5 | Regulation | Advocate | 6 | [david-baker-using-ai-for-scien](https://www.existentialhope.com/podcasts/david-baker-using-ai-for-science-to-solve-humanitys-biggest-problems) |
| **Computational models for infectious disease spread and va...** | Biotech, Medicine & Life Extension | 12/20 | 3/5 | Coordination | Convene | 7 | [pablos-holman-on-creating-tech](https://www.existentialhope.com/podcasts/pablos-holman-on-creating-technology-that-actually-matters) |
| **AI-Democratic Institutions for Decentralized Governance** | Decentralized & Democratic Institutions | 12/20 | 3/5 | Social Acceptance | Research | 4 | [worldbuilding-special-3rd-plac](https://www.existentialhope.com/podcasts/worldbuilding-special-3rd-place-floratech) |
| **Crowdfunded Independent Longevity AI Research Program** | Nanotechnology & Advanced Manufacturing | 13/20 | 2/5 | Coordination | Convene | 4 | [a-hope-for-human-immortality](https://worlds.existentialhope.com/world/a-hope-for-human-immortality/) |
| **Hybrid Market impact bond ledger** | Economic Systems & Resource Distribution | 12/20 | 3/5 | Regulation | Advocate | 5 | [hybrid-market](https://worlds.existentialhope.com/world/hybrid-market/) |
| **Isolated Societies Research Institute** | Scientific Research & Knowledge Infra... | 13/20 | 2/5 | Funding | Research | 3 | [self-sustaining-isolated-socie](https://worlds.existentialhope.com/world/self-sustaining-isolated-societies/) |
| **Mandatory Open-Source AI Release Policy** | AI Safety, Alignment & Governance | 12/20 | 3/5 | Regulation | Advocate | 2 | [sustainable-abundance](https://worlds.existentialhope.com/world/sustainable-abundance/) |
| **Loom Studios** | Decentralized & Democratic Institutions | 12/20 | 3/5 | Coordination | Research | 4 | [symphora](https://worlds.existentialhope.com/world/symphora/) |
| **The Common Knowledge Generator** | Scientific Research & Knowledge Infra... | 12/20 | 3/5 | Coordination | Convene | 4 | |
| **The Delphi Collaboration Protocol** | AI-Mediated Deliberation & Collective... | 13/20 | 2/5 | Coordination | Build | 4 | |
| **The Scenario Planning Institution** | AI Safety, Alignment & Governance | 12/20 | 3/5 | Coordination | Convene | 4 | |
| **Flourishing Certification** | Education, Development & Human Flouri... | 12/20 | 3/5 | Coordination | Convene | 3 | |
| **TAI Horizon Scanner** | AI Safety, Alignment & Governance | 12/20 | 3/5 | Coordination | Convene | 4 | |
| **Lean FRO (interactive theorem proving infrastructure for ...** | Scientific Research & Knowledge Infra... | 11/20 | 3/5 | Engineering | Build | 6 | [adam-marblestone-solving-scien](https://www.existentialhope.com/podcasts/adam-marblestone-solving-sciences-biggest-gaps) |
| **Large-scale AI-mediated deliberation system** | AI-Mediated Deliberation & Collective... | 11/20 | 3/5 | Engineering | Build | 5 | [anthony-aguirre-tools-or-agent](https://www.existentialhope.com/podcasts/anthony-aguirre-tools-or-agents-choosing-our-ai-future) |
| **Reputational Market** | Economic Systems & Resource Distribution | 11/20 | 3/5 | Coordination | Research | 3 | [kristian-rnn-the-darwinian-tra](https://www.existentialhope.com/podcasts/kristian-rnn-the-darwinian-trap-that-explains-our-world) |
| **Learning Observatories** | AI Safety, Alignment & Governance | 11/20 | 3/5 | Coordination | Convene | 4 | [niklas-lundblad-how-ai-can-acc](https://www.existentialhope.com/podcasts/niklas-lundblad-how-ai-can-accelerate-science-its-own-adoption) |
| **Deep Fision borehole nuclear reactor** | Energy, Environment & Planetary Systems | 11/20 | 3/5 | Regulation | Build | 4 | [pablos-holman-on-creating-tech](https://www.existentialhope.com/podcasts/pablos-holman-on-creating-technology-that-actually-matters) |
| **Values-as-modality parametrization across AI systems** | AI Safety, Alignment & Governance | 11/20 | 3/5 | Coordination | Research | 2 | [richard-mallah-how-aligned-ai-](https://www.existentialhope.com/podcasts/richard-mallah-how-aligned-ai-could-help-us-create-a-flourishing-future) |
| **Parallel lightly-regulated childminder category (France)** | Education, Development & Human Flouri... | 12/20 | 2/5 | Regulation | Research | 7 | [sam-bowman-whats-holding-back-](https://www.existentialhope.com/podcasts/sam-bowman-whats-holding-back-progress-and-how-to-fix-it) |
| **Orare - AI-powered Futarchy governance system** | AI-Mediated Deliberation & Collective... | 11/20 | 3/5 | Social Acceptance | Advocate | 4 | [worldbuilding-special-1st-plac](https://www.existentialhope.com/podcasts/worldbuilding-special-1st-place-cities-of-orare) |
| **VOICE (Voice for Open Source Information and Community En...** | AI-Mediated Deliberation & Collective... | 11/20 | 3/5 | Social Acceptance | Research | 4 | [worldbuilding-special-2nd-plac](https://www.existentialhope.com/podcasts/worldbuilding-special-2nd-place-rising-choir) |
| **Global Personhood Token / Trust-of-Personhood Standard** | International Governance & Coordination | 11/20 | 3/5 | Regulation | Advocate | 6 | [worldbuilding-special-2nd-plac](https://www.existentialhope.com/podcasts/worldbuilding-special-2nd-place-rising-choir) |
| **LexCommons** | Decentralized & Democratic Institutions | 12/20 | 2/5 | Regulation | Research | 5 | [lexcommons-the-open-law-societ](https://worlds.existentialhope.com/world/lexcommons-the-open-law-society/) |
| **The Welcome Circle** | Education, Development & Human Flouri... | 12/20 | 2/5 | Coordination | Convene | 2 | [planet-joy](https://worlds.existentialhope.com/world/planet-joy/) |
| **RaízMental Global** | Biotech, Medicine & Life Extension | 11/20 | 3/5 | Regulation | Convene | 4 | [razmental-emotional-healing-ec](https://worlds.existentialhope.com/world/razmental-emotional-healing-ecosystems/) |
| **Ethical AI Tutors** | Education, Development & Human Flouri... | 11/20 | 3/5 | Coordination | Convene | 5 | [the-learning-uncommons-of-2035](https://worlds.existentialhope.com/world/the-learning-uncommons-of-2035/) |
| **Safety-Netted DAOs** | Decentralized & Democratic Institutions | 11/20 | 2/5 | Engineering | Build | 2 | |
| **AGI Liability Safe Harbor Framework** | AI Safety, Alignment & Governance | 10/20 | 3/5 | Regulation | Research | 1 | |
| **Multiplicity.ai** | AI-Mediated Deliberation & Collective... | 11/20 | 2/5 | Engineering | Build | 7 | [andrew-critch-what-agi-might-l](https://www.existentialhope.com/podcasts/andrew-critch-what-agi-might-look-like-in-practice) |
| **Futarchy** | Decentralized & Democratic Institutions | 10/20 | 3/5 | Social Acceptance | Build | 4 | [david-duvenaud-exploring-the-c](https://www.existentialhope.com/podcasts/david-duvenaud-exploring-the-cruxes-and-possibilities-of-post-agi-futures) |
| **Active smart fabric with autonomous environmental response** | Nanotechnology & Advanced Manufacturing | 11/20 | 2/5 | Engineering | Research | 3 | [david-leigh-exploring-the-poss](https://www.existentialhope.com/podcasts/david-leigh-exploring-the-possibilities-of-nanotechnology) |
| **Integration of Brain Preservation into the Medical System** | Biotech, Medicine & Life Extension | 11/20 | 2/5 | Regulation | Advocate | 3 | [dr-ariel-zeleznikow-johnston-t](https://www.existentialhope.com/podcasts/dr-ariel-zeleznikow-johnston-the-future-loves-you) |
| **Imagination Annotated (book series)** | Education, Development & Human Flouri... | 11/20 | 2/5 | Coordination | Convene | 6 | [ed-finn-how-science-fiction-ca](https://www.existentialhope.com/podcasts/ed-finn-how-science-fiction-can-inspire-real-world-innovation) |
| **Author Personal Knowledge Graph / Writing Corpus Utility** | Scientific Research & Knowledge Infra... | 11/20 | 2/5 | Engineering | Build | 5 | [jim-oshaughnessy-on-investing-](https://www.existentialhope.com/podcasts/jim-oshaughnessy-on-investing-in-infinite-human-potential) |
| **Artificial General Wisdom** | AI Safety, Alignment & Governance | 10/20 | 3/5 | Coordination | Research | 2 | [liv-boeree-game-theory-moloch-](https://www.existentialhope.com/podcasts/liv-boeree-game-theory-moloch-our-hopeful-future) |
| **Componentized architectures optimized for inner alignment...** | AI Safety, Alignment & Governance | 10/20 | 3/5 | Coordination | Research | 2 | [richard-mallah-how-aligned-ai-](https://www.existentialhope.com/podcasts/richard-mallah-how-aligned-ai-could-help-us-create-a-flourishing-future) |
| **Neighborhood opt-in upzoning with land value capture** | Decentralized & Democratic Institutions | 11/20 | 2/5 | Regulation | Research | 4 | [sam-bowman-whats-holding-back-](https://www.existentialhope.com/podcasts/sam-bowman-whats-holding-back-progress-and-how-to-fix-it) |
| **Kacha's Global Symbiosis Council (GSC)** | International Governance & Coordination | 10/20 | 3/5 | Coordination | Convene | 4 | [2035-the-era-of-sentient-symbi](https://worlds.existentialhope.com/world/2035-the-era-of-sentient-symbiosis-and-human-ai-flourishment/) |
| **Guardian Network** | International Governance & Coordination | 11/20 | 2/5 | Coordination | Convene | 4 | [edusafe](https://worlds.existentialhope.com/world/edusafe/) |
| **Decentralized community-built AI systems** | Decentralized & Democratic Institutions | 10/20 | 3/5 | Coordination | Convene | 5 | [new-world-in-the-making](https://worlds.existentialhope.com/world/new-world-in-the-making/) |
| **Bio-Responsive AI Interfaces** | Neurotechnology & Brain-Computer Inte... | 11/20 | 2/5 | Coordination | Convene | 4 | [planet-joy](https://worlds.existentialhope.com/world/planet-joy/) |
| **Open-source AI-powered research funding and knowledge pla...** | Scientific Research & Knowledge Infra... | 10/20 | 3/5 | Regulation | Advocate | 4 | [potentia](https://worlds.existentialhope.com/world/potentia/) |
| **Interplanetary Cooperative** | International Governance & Coordination | 11/20 | 2/5 | Regulation | Advocate | 2 | [resilient-planetary-settlement](https://worlds.existentialhope.com/world/resilient-planetary-settlements/) |
| **Civic Loom** | AI-Mediated Deliberation & Collective... | 11/20 | 2/5 | Coordination | Research | 5 | [symphora](https://worlds.existentialhope.com/world/symphora/) |
| **AI-powered participatory policy simulation platform** | AI-Mediated Deliberation & Collective... | 10/20 | 3/5 | Social Acceptance | Convene | 5 | [the-commons-cloud](https://worlds.existentialhope.com/world/the-commons-cloud/) |
| **The Flourishing Foundation** | Education, Development & Human Flouri... | 11/20 | 2/5 | Regulation | Advocate | 5 | |
| **The Evals for Evals Institute** | AI Safety, Alignment & Governance | 10/20 | 3/5 | Coordination | Convene | 3 | |
| **The World Convention on Transformative Artificial Intelli...** | International Governance & Coordination | 11/20 | 2/5 | Coordination | Convene | 4 | |
| **Global Deliberation as a Service (GDaaS)** | AI-Mediated Deliberation & Collective... | 10/20 | 3/5 | Coordination | Convene | 4 | |
| **World Convention on Transformative Artificial Intelligenc...** | International Governance & Coordination | 10/20 | 3/5 | Coordination | Research | 2 | |
| **Tool AI for Tool AI** | AI Safety, Alignment & Governance | 9/20 | 3/5 | Engineering | Build | 4 | |
| **NotADoctor.ai medical record serialization and RCT search** | Biotech, Medicine & Life Extension | 10/20 | 2/5 | Engineering | Research | 6 | [andrew-critch-what-agi-might-l](https://www.existentialhope.com/podcasts/andrew-critch-what-agi-might-look-like-in-practice) |
| **AI-mediated conflict resolution tool (retorsion/disgorgem...** | AI-Mediated Deliberation & Collective... | 10/20 | 2/5 | Regulation | Research | 4 | [andrew-critch-what-agi-might-l](https://www.existentialhope.com/podcasts/andrew-critch-what-agi-might-look-like-in-practice) |
| **Aviary** | Scientific Research & Knowledge Infra... | 10/20 | 2/5 | Social Acceptance | Build | 6 | [andrew-white-building-an-ai-sc](https://www.existentialhope.com/podcasts/andrew-white-building-an-ai-scientist-to-automate-discovery) |
| **Windfall Clause** | Economic Systems & Resource Distribution | 10/20 | 2/5 | Coordination | Convene | 2 | [anthony-aguirre-anna-yelizarov](https://www.existentialhope.com/podcasts/anthony-aguirre-anna-yelizarova-on-worldbuilding) |
| **Project Hieroglyph** | Education, Development & Human Flouri... | 9/20 | 3/5 | Funding | Fund | 4 | [ed-finn-how-science-fiction-ca](https://www.existentialhope.com/podcasts/ed-finn-how-science-fiction-can-inspire-real-world-innovation) |
| **Provably Safe AGI via Formal Verification** | AI Safety, Alignment & Governance | 9/20 | 3/5 | Engineering | Research | 3 | [gus-docker-beyond-survival-env](https://www.existentialhope.com/podcasts/gus-docker-beyond-survival-envisioning-a-technologically-enhanced-utopia) |
| **Closed-loop gene therapy for seizure suppression via acti...** | Biotech, Medicine & Life Extension | 9/20 | 3/5 | Regulation | Fund | 4 | [jacques-carolan-the-future-of-](https://www.existentialhope.com/podcasts/jacques-carolan-the-future-of-brain-health) |
| **AI underwriting / mandatory insurance for AI systems** | AI Safety, Alignment & Governance | 9/20 | 3/5 | Regulation | Advocate | 4 | [nathan-labenz-what-are-the-bes](https://www.existentialhope.com/podcasts/nathan-labenz-what-are-the-best-case-scenarios-for-ai) |
| **Self-Improving System Prompt for Continuous AI Capability...** | AI Safety, Alignment & Governance | 10/20 | 2/5 | Engineering | Build | 4 | [niklas-lundblad-how-ai-can-acc](https://www.existentialhope.com/podcasts/niklas-lundblad-how-ai-can-accelerate-science-its-own-adoption) |
| **Multicriteria safety architecture with explicit precedenc...** | AI Safety, Alignment & Governance | 9/20 | 3/5 | Engineering | Research | 1 | [richard-mallah-how-aligned-ai-](https://www.existentialhope.com/podcasts/richard-mallah-how-aligned-ai-could-help-us-create-a-flourishing-future) |
| **Blockchain-based Universal Self-Actualization Income** | Economic Systems & Resource Distribution | 10/20 | 2/5 | Regulation | Research | 3 | [trent-mcconaghy-from-starships](https://www.existentialhope.com/podcasts/trent-mcconaghy-from-starships-to-tokens-pioneering-futures) |
| **International Council of Life Extension** | Biotech, Medicine & Life Extension | 10/20 | 2/5 | Regulation | Advocate | 4 | [a-hope-for-human-immortality](https://worlds.existentialhope.com/world/a-hope-for-human-immortality/) |
| **Ecological Balance Council** | Ecological & Regenerative Systems | 10/20 | 2/5 | Coordination | Convene | 2 | [green-renaissance](https://worlds.existentialhope.com/world/green-renaissance/) |
| **Adaptive Wearable Tech** | Biotech, Medicine & Life Extension | 9/20 | 3/5 | Regulation | Build | 7 | [human-centric-technology](https://worlds.existentialhope.com/world/human-centric-technology/) |
| **Human-Tech Council** | AI Safety, Alignment & Governance | 10/20 | 2/5 | Coordination | Convene | 4 | [human-centric-technology](https://worlds.existentialhope.com/world/human-centric-technology/) |
| **Global Learning Collective** | Education, Development & Human Flouri... | 9/20 | 3/5 | Coordination | Convene | 6 | [lumina-the-world-illuminated-b](https://worlds.existentialhope.com/world/lumina-the-world-illuminated-by-unleashed-human-brilliance/) |
| **Emotional Coach (Empathetic Neuro-AI)** | Neurotechnology & Brain-Computer Inte... | 9/20 | 3/5 | Regulation | Research | 4 | [razmental-emotional-healing-ec](https://worlds.existentialhope.com/world/razmental-emotional-healing-ecosystems/) |
| **Regenerative Biospheres** | Ecological & Regenerative Systems | 9/20 | 3/5 | Engineering | Research | 5 | [resilient-planetary-settlement](https://worlds.existentialhope.com/world/resilient-planetary-settlements/) |
| **AI Alignment Markets** | AI Safety, Alignment & Governance | 10/20 | 2/5 | Coordination | Research | 3 | [the-symbiotic-age](https://worlds.existentialhope.com/world/the-symbiotic-age/) |
| **Global AI Alignment Commission (GAAC)** | International Governance & Coordination | 9/20 | 3/5 | Coordination | Convene | 2 | [the-symbiotic-age](https://worlds.existentialhope.com/world/the-symbiotic-age/) |
| **Extracellular vesicle-based blood diagnostics for tissue-...** | Biotech, Medicine & Life Extension | 9/20 | 2/5 | Coordination | Convene | 3 | [amy-proal-rethinking-chronic-d](https://www.existentialhope.com/podcasts/amy-proal-rethinking-chronic-disease) |
| **Protein-based nanomachines for in vivo tissue repair and ...** | Biotech, Medicine & Life Extension | 8/20 | 3/5 | Engineering | Research | 3 | [david-baker-using-ai-for-scien](https://www.existentialhope.com/podcasts/david-baker-using-ai-for-science-to-solve-humanitys-biggest-problems) |
| **Biohybrid living DBS electrode (neuron-based implant inte...** | Neurotechnology & Brain-Computer Inte... | 8/20 | 3/5 | Engineering | Research | 3 | [jacques-carolan-the-future-of-](https://www.existentialhope.com/podcasts/jacques-carolan-the-future-of-brain-health) |
| **Chemputer / Chemputation programming language** | Nanotechnology & Advanced Manufacturing | 8/20 | 3/5 | Social Acceptance | Advocate | 7 | [lee-cronin-catalyzing-progress](https://www.existentialhope.com/podcasts/lee-cronin-catalyzing-progress-through-chemistry) |
| **Openwater universal diagnostic/therapeutic device** | Biotech, Medicine & Life Extension | 8/20 | 3/5 | Regulation | Fund | 4 | [mary-lou-jepsen-a-handheld-dev](https://www.existentialhope.com/podcasts/mary-lou-jepsen-a-handheld-device-to-defeat-cancer) |
| **AI-driven forking narrative / interactive scenario conten...** | AI-Mediated Deliberation & Collective... | 8/20 | 3/5 | Social Acceptance | Build | 5 | [nathan-labenz-what-are-the-bes](https://www.existentialhope.com/podcasts/nathan-labenz-what-are-the-best-case-scenarios-for-ai) |
| **Agent Contract Declaration Requirement** | AI Safety, Alignment & Governance | 9/20 | 2/5 | Coordination | Convene | 2 | [niklas-lundblad-how-ai-can-acc](https://www.existentialhope.com/podcasts/niklas-lundblad-how-ai-can-accelerate-science-its-own-adoption) |
| **Spectrum from environmental safety to metagenic safety** | AI Safety, Alignment & Governance | 9/20 | 2/5 | Engineering | Research | 1 | [richard-mallah-how-aligned-ai-](https://www.existentialhope.com/podcasts/richard-mallah-how-aligned-ai-could-help-us-create-a-flourishing-future) |
| **Bounded AI Agents** | AI Safety, Alignment & Governance | 9/20 | 2/5 | Coordination | Research | 5 | [worldbuilding-special-3rd-plac](https://www.existentialhope.com/podcasts/worldbuilding-special-3rd-place-floratech) |
| **BTC Trust Grid** | Economic Systems & Resource Distribution | 9/20 | 2/5 | Regulation | Advocate | 4 | [worldbuilding-course-worldbuil](https://worlds.existentialhope.com/world/worldbuilding-course-worldbuilding-toolbox-world-entry-page-world-gallery-x-twitter-instagram-medium-bookmark-sadvipra-ai/) |
| **Global Fungal Biology Research Initiative (Big Tech + Pau...** | Biotech, Medicine & Life Extension | 9/20 | 2/5 | Coordination | Convene | 3 | [fungi-terra](https://worlds.existentialhope.com/world/fungi-terra/) |
| **Biophilic Architecture** | Ecological & Regenerative Systems | 9/20 | 2/5 | Funding | Fund | 7 | [green-renaissance](https://worlds.existentialhope.com/world/green-renaissance/) |
| **Urban Sustainability Network** | Energy, Environment & Planetary Systems | 9/20 | 2/5 | Regulation | Advocate | 7 | [harmonized-urban-ecosystems](https://worlds.existentialhope.com/world/harmonized-urban-ecosystems/) |
| **AI Market Intermediaries** | Economic Systems & Resource Distribution | 8/20 | 3/5 | Coordination | Convene | 4 | [the-more-beautiful-world-our-h](https://worlds.existentialhope.com/world/the-more-beautiful-world-our-hearts-know-is-possible/) |
| **The Indefinite Lifespan** | Biotech, Medicine & Life Extension | 8/20 | 3/5 | Regulation | Advocate | 4 | [the-world-of-equal-opportunity](https://worlds.existentialhope.com/world/the-world-of-equal-opportunity-for-sentient-beings-living-the-indefinite-lifespan-immortally/) |
| **Memory Looms** | Education, Development & Human Flouri... | 10/20 | 1/5 | Physics | Research | 1 | [threadtime](https://worlds.existentialhope.com/world/threadtime/) |
| **World Cultural Exchange Forum** | International Governance & Coordination | 9/20 | 2/5 | Coordination | Convene | 6 | [unity-through-diversity](https://worlds.existentialhope.com/world/unity-through-diversity/) |
| **TimeLike / SECHI (Simulation-Enabled Cooperative Human In...** | AI-Mediated Deliberation & Collective... | 7/20 | 4/5 | Coordination | Research | 3 | |
| **Request for Evaluation (RfE) Protocol** | AI Safety, Alignment & Governance | 9/20 | 2/5 | Coordination | Convene | 1 | |
| **Focused Research Organizations (FROs)** | Scientific Research & Knowledge Infra... | 7/20 | 3/5 | Funding | Fund | 5 | [adam-marblestone-solving-scien](https://www.existentialhope.com/podcasts/adam-marblestone-solving-sciences-biggest-gaps) |
| **Vagus nerve microbiome characterization study** | Biotech, Medicine & Life Extension | 8/20 | 2/5 | Coordination | Research | 3 | [amy-proal-rethinking-chronic-d](https://www.existentialhope.com/podcasts/amy-proal-rethinking-chronic-disease) |
| **AI-driven drug repurposing pipeline (AMD/Ripasudil discov...** | Biotech, Medicine & Life Extension | 7/20 | 3/5 | Regulation | Research | 5 | [andrew-white-building-an-ai-sc](https://www.existentialhope.com/podcasts/andrew-white-building-an-ai-scientist-to-automate-discovery) |
| **Universal Constructor** | Nanotechnology & Advanced Manufacturing | 6/20 | 4/5 | Physics | Research | 1 | [david-deutsch-on-beauty-knowle](https://www.existentialhope.com/podcasts/david-deutsch-on-beauty-knowledge-and-progress) |
| **Bell Labs Systems Engineer Role** | Scientific Research & Knowledge Infra... | 8/20 | 2/5 | Coordination | Convene | 4 | [eric-gilliam-what-history-can-](https://www.existentialhope.com/podcasts/eric-gilliam-what-history-can-teach-us-about-doing-better-science) |
| **Meditation-State Detection Model** | Neurotechnology & Brain-Computer Inte... | 9/20 | 1/5 | Engineering | Research | 4 | [gus-docker-beyond-survival-env](https://www.existentialhope.com/podcasts/gus-docker-beyond-survival-envisioning-a-technologically-enhanced-utopia) |
| **Vertis Solus space-based solar power array** | Energy, Environment & Planetary Systems | 7/20 | 3/5 | Engineering | Research | 4 | [pablos-holman-on-creating-tech](https://www.existentialhope.com/podcasts/pablos-holman-on-creating-technology-that-actually-matters) |
| **Computer-controlled sail cargo ship** | Energy, Environment & Planetary Systems | 7/20 | 3/5 | Regulation | Advocate | 6 | [pablos-holman-on-creating-tech](https://www.existentialhope.com/podcasts/pablos-holman-on-creating-technology-that-actually-matters) |
| **Fire-the-CEO Decision Market** | Economic Systems & Resource Distribution | 8/20 | 2/5 | Regulation | Advocate | 3 | [robin-hanson-on-futurism-his-b](https://www.existentialhope.com/podcasts/robin-hanson-on-futurism-his-best-career-advice) |
| **Planetary-Scale Intelligence** | Ecological & Regenerative Systems | 7/20 | 3/5 | Coordination | Research | 2 | [sara-walker-unraveling-lifes-b](https://www.existentialhope.com/podcasts/sara-walker-unraveling-lifes-beginnings-with-the-cosmic-perspective) |
| **NanoSync – Regenerative Nanotechnology** | Biotech, Medicine & Life Extension | 7/20 | 3/5 | Physics | Research | 2 | [elysium](https://worlds.existentialhope.com/world/elysium/) |
| **Institute for Life Extension (ILE)** | Biotech, Medicine & Life Extension | 7/20 | 3/5 | Regulation | Advocate | 4 | [elysium](https://worlds.existentialhope.com/world/elysium/) |
| **Urban AI systems** | Energy, Environment & Planetary Systems | 7/20 | 3/5 | Coordination | Convene | 6 | [harmonized-urban-ecosystems](https://worlds.existentialhope.com/world/harmonized-urban-ecosystems/) |
| **AI-Managed Childhood Development Centers** | Education, Development & Human Flouri... | 7/20 | 3/5 | Regulation | Research | 4 | [harmony-haven](https://worlds.existentialhope.com/world/harmony-haven/) |
| **Predictive AI System for R&D Funding Allocation** | Scientific Research & Knowledge Infra... | 7/20 | 3/5 | Regulation | Advocate | 4 | [innovation-nation](https://worlds.existentialhope.com/world/innovation-nation/) |
| **Lifelong AI Guardians** | Education, Development & Human Flouri... | 8/20 | 2/5 | Regulation | Advocate | 4 | [kidtopia](https://worlds.existentialhope.com/world/kidtopia/) |
| **Earth UBI** | Economic Systems & Resource Distribution | 8/20 | 2/5 | Coordination | Convene | 2 | [protopia-peace-project](https://worlds.existentialhope.com/world/protopia-peace-project/) |
| **Jurisdictional Routers** | International Governance & Coordination | 8/20 | 1/5 | Regulation | Research | 3 | |
| **Pareto-Optimal Negotiation Bots** | AI-Mediated Deliberation & Collective... | 7/20 | 2/5 | Social Acceptance | Advocate | 7 | |
| **LitQA3 (high-recall literature evaluation benchmark)** | Scientific Research & Knowledge Infra... | 7/20 | 2/5 | Engineering | Build | 4 | [andrew-white-building-an-ai-sc](https://www.existentialhope.com/podcasts/andrew-white-building-an-ai-scientist-to-automate-discovery) |
| **LLM Historical Forecasting Benchmark** | Scientific Research & Knowledge Infra... | 7/20 | 2/5 | Engineering | Research | 3 | [david-duvenaud-exploring-the-c](https://www.existentialhope.com/podcasts/david-duvenaud-exploring-the-cruxes-and-possibilities-of-post-agi-futures) |
| **BBN-style Applied R&D Contractor (New BBNs)** | Scientific Research & Knowledge Infra... | 6/20 | 3/5 | Coordination | Fund | 5 | [eric-gilliam-what-history-can-](https://www.existentialhope.com/podcasts/eric-gilliam-what-history-can-teach-us-about-doing-better-science) |
| **Closed-loop ultrasound brain-state readout and mood modul...** | Neurotechnology & Brain-Computer Inte... | 6/20 | 3/5 | Regulation | Research | 5 | [jacques-carolan-the-future-of-](https://www.existentialhope.com/podcasts/jacques-carolan-the-future-of-brain-health) |
| **Massively scalable intravascular or CSF-routed neural int...** | Neurotechnology & Brain-Computer Inte... | 6/20 | 3/5 | Regulation | Advocate | 5 | [jacques-carolan-the-future-of-](https://www.existentialhope.com/podcasts/jacques-carolan-the-future-of-brain-health) |
| **Continuous AI-Driven Book Marketing Matchmaker** | Economic Systems & Resource Distribution | 7/20 | 2/5 | Engineering | Build | 6 | [jim-oshaughnessy-on-investing-](https://www.existentialhope.com/podcasts/jim-oshaughnessy-on-investing-in-infinite-human-potential) |
| **Child Equity Stake Fund (US Birth Endowment)** | Economic Systems & Resource Distribution | 7/20 | 2/5 | Social Acceptance | Advocate | 8 | [jim-oshaughnessy-on-investing-](https://www.existentialhope.com/podcasts/jim-oshaughnessy-on-investing-in-infinite-human-potential) |
| **Onerofex (collective AI-mediated dreaming experience)** | AI-Mediated Deliberation & Collective... | 7/20 | 2/5 | Regulation | Research | 4 | [ken-liu-what-ai-reveals-about-](https://www.existentialhope.com/podcasts/ken-liu-what-ai-reveals-about-humanity) |
| **Atheoretical Science via Massive Sensor Networks and AI P...** | Scientific Research & Knowledge Infra... | 6/20 | 3/5 | Coordination | Research | 3 | [niklas-lundblad-how-ai-can-acc](https://www.existentialhope.com/podcasts/niklas-lundblad-how-ai-can-accelerate-science-its-own-adoption) |
| **Parallel Federal Science Funding System with Mandatory In...** | Scientific Research & Knowledge Infra... | 6/20 | 3/5 | Funding | Advocate | 2 | [stuart-buck-what-is-good-scien](https://www.existentialhope.com/podcasts/stuart-buck-what-is-good-science) |
| **Global Childhood Development Authority (GCDA)** | Education, Development & Human Flouri... | 7/20 | 2/5 | Coordination | Convene | 4 | [harmony-haven](https://worlds.existentialhope.com/world/harmony-haven/) |
| **The Children's Movement** | Education, Development & Human Flouri... | 6/20 | 3/5 | Funding | Convene | 4 | [kidtopia](https://worlds.existentialhope.com/world/kidtopia/) |
| **Neural-Adaptive Learning AI** | Neurotechnology & Brain-Computer Inte... | 7/20 | 2/5 | Regulation | Advocate | 4 | [lumina-the-world-illuminated-b](https://worlds.existentialhope.com/world/lumina-the-world-illuminated-by-unleashed-human-brilliance/) |
| **Bitcoin-funded renewable energy cooperatives** | Energy, Environment & Planetary Systems | 7/20 | 2/5 | Regulation | Advocate | 5 | [new-world-in-the-making](https://worlds.existentialhope.com/world/new-world-in-the-making/) |
| **Ecosystem-responsive AI management system** | Ecological & Regenerative Systems | 7/20 | 2/5 | Regulation | Advocate | 4 | [potentia](https://worlds.existentialhope.com/world/potentia/) |
| **GAI (Global AI Board)** | AI Safety, Alignment & Governance | 7/20 | 2/5 | Coordination | Convene | 4 | [sustainable-abundance](https://worlds.existentialhope.com/world/sustainable-abundance/) |
| **United Nations Biosphere Geoengineering and AI Governance...** | International Governance & Coordination | 7/20 | 2/5 | Coordination | Convene | 2 | [the-world-of-equal-opportunity](https://worlds.existentialhope.com/world/the-world-of-equal-opportunity-for-sentient-beings-living-the-indefinite-lifespan-immortally/) |
| **Little AI Robots (emotional decision-support chatbots)** | Education, Development & Human Flouri... | 7/20 | 2/5 | Regulation | Research | 6 | [uniqualia](https://worlds.existentialhope.com/world/uniqualia/) |
| **Consolidated Intelligence Council** | International Governance & Coordination | 7/20 | 2/5 | Coordination | Research | 4 | [unified-peace](https://worlds.existentialhope.com/world/unified-peace/) |
| **Neural Harmony Interface** | Neurotechnology & Brain-Computer Inte... | 6/20 | 3/5 | Regulation | Research | 4 | [veliona-the-world-of-unfolding](https://worlds.existentialhope.com/world/veliona-the-world-of-unfolding-minds/) |
| **Bio-templated microchips via implosion fabrication** | Nanotechnology & Advanced Manufacturing | 5/20 | 3/5 | Engineering | Research | 3 | [adam-marblestone-solving-scien](https://www.existentialhope.com/podcasts/adam-marblestone-solving-sciences-biggest-gaps) |
| **Programmable synthetic molecular robots for chemical synt...** | Nanotechnology & Advanced Manufacturing | 5/20 | 3/5 | Physics | Research | 3 | [david-leigh-exploring-the-poss](https://www.existentialhope.com/podcasts/david-leigh-exploring-the-possibilities-of-nanotechnology) |
| **Aldehyde-Stabilized Cryopreservation** | Biotech, Medicine & Life Extension | 6/20 | 2/5 | Regulation | Research | 4 | [dr-ariel-zeleznikow-johnston-t](https://www.existentialhope.com/podcasts/dr-ariel-zeleznikow-johnston-the-future-loves-you) |
| **AI-powered blog aggregator with conversational interface** | Education, Development & Human Flouri... | 7/20 | 1/5 | Engineering | Build | 6 | [eli-dourado-on-accelerating-pr](https://www.existentialhope.com/podcasts/eli-dourado-on-accelerating-progress) |
| **EgoLets** | AI-Mediated Deliberation & Collective... | 5/20 | 3/5 | Regulation | Advocate | 4 | [ken-liu-what-ai-reveals-about-](https://www.existentialhope.com/podcasts/ken-liu-what-ai-reveals-about-humanity) |
| **Chemical substrate computation / chemical consciousness** | Scientific Research & Knowledge Infra... | 5/20 | 3/5 | Physics | Research | 2 | [lee-cronin-catalyzing-progress](https://www.existentialhope.com/podcasts/lee-cronin-catalyzing-progress-through-chemistry) |
| **Alexa Gentia (machine-negotiated agent legal structures)** | AI Safety, Alignment & Governance | 6/20 | 2/5 | Regulation | Research | 4 | [niklas-lundblad-how-ai-can-acc](https://www.existentialhope.com/podcasts/niklas-lundblad-how-ai-can-accelerate-science-its-own-adoption) |
| **Origin of Life Evolutionary Engine (chemical space search...** | Scientific Research & Knowledge Infra... | 5/20 | 3/5 | Physics | Research | 4 | [sara-walker-unraveling-lifes-b](https://www.existentialhope.com/podcasts/sara-walker-unraveling-lifes-beginnings-with-the-cosmic-perspective) |
| **Assembly Theory** | Scientific Research & Knowledge Infra... | 6/20 | 2/5 | Physics | Research | 4 | [sara-walker-unraveling-lifes-b](https://www.existentialhope.com/podcasts/sara-walker-unraveling-lifes-beginnings-with-the-cosmic-perspective) |
| **National Science and Technology Foresight Agency (NSTFA)** | Scientific Research & Knowledge Infra... | 6/20 | 2/5 | Coordination | Convene | 4 | [innovation-nation](https://worlds.existentialhope.com/world/innovation-nation/) |
| **Minimum-payload terraforming nanomachine for Mars** | Nanotechnology & Advanced Manufacturing | 3/20 | 4/5 | Physics | Research | 2 | [lee-cronin-catalyzing-progress](https://www.existentialhope.com/podcasts/lee-cronin-catalyzing-progress-through-chemistry) |
| **Microbial Interaction Simulation AI (Anthropic-built)** | Scientific Research & Knowledge Infra... | 5/20 | 2/5 | Engineering | Research | 4 | [fungi-terra](https://worlds.existentialhope.com/world/fungi-terra/) |
| **Institute for Human Perplexity** | Scientific Research & Knowledge Infra... | 5/20 | 2/5 | Coordination | Research | 2 | [uniqualia](https://worlds.existentialhope.com/world/uniqualia/) |
| **Gene Drives for Wild Animal Suffering Reduction** | Ecological & Regenerative Systems | 2/20 | 4/5 | Regulation | Convene | 4 | [david-pearce-a-future-without-](https://www.existentialhope.com/podcasts/david-pearce-a-future-without-suffering) |
| **Focused Philanthropic Bet Modeled on Warren Weaver / Rock...** | Scientific Research & Knowledge Infra... | 3/20 | 3/5 | Social Acceptance | Advocate | 6 | [eric-gilliam-what-history-can-](https://www.existentialhope.com/podcasts/eric-gilliam-what-history-can-teach-us-about-doing-better-science) |
| **Jurisdictional Arbitrage Special Economic Zones for BCI R...** | Neurotechnology & Brain-Computer Inte... | 4/20 | 2/5 | Regulation | Advocate | 5 | [trent-mcconaghy-from-starships](https://www.existentialhope.com/podcasts/trent-mcconaghy-from-starships-to-tokens-pioneering-futures) |
| **Affective and Socio-Emotional Atmospheric Reading System** | Education, Development & Human Flouri... | 4/20 | 2/5 | Social Acceptance | Advocate | 5 | [edusafe](https://worlds.existentialhope.com/world/edusafe/) |
| **AI-driven individualized peace education system** | Education, Development & Human Flouri... | 4/20 | 2/5 | Regulation | Research | 4 | [unified-peace](https://worlds.existentialhope.com/world/unified-peace/) |
| **Elective Cryonic Suspension at Peak Vitality ('Kyasia')** | Biotech, Medicine & Life Extension | 4/20 | 1/5 | Regulation | Advocate | 2 | [david-pearce-a-future-without-](https://www.existentialhope.com/podcasts/david-pearce-a-future-without-suffering) |
| **Earth AI** | Economic Systems & Resource Distribution | 3/20 | 2/5 | Coordination | Research | 4 | [protopia-peace-project](https://worlds.existentialhope.com/world/protopia-peace-project/) |
| **Neural Linguistic Interfaces** | Neurotechnology & Brain-Computer Inte... | 2/20 | 3/5 | Engineering | Research | 4 | [unity-through-diversity](https://worlds.existentialhope.com/world/unity-through-diversity/) |
| **Phenomenal Binding-Based Sentient AI Architecture** | Neurotechnology & Brain-Computer Inte... | 1/20 | 3/5 | Physics | Research | 1 | [david-pearce-a-future-without-](https://www.existentialhope.com/podcasts/david-pearce-a-future-without-suffering) |
| **Grabby Aliens Three-Parameter Model** | Scientific Research & Knowledge Infra... | 0/20 | 2/5 | Physics | Research | 4 | [robin-hanson-on-futurism-his-b](https://www.existentialhope.com/podcasts/robin-hanson-on-futurism-his-best-career-advice) |

---

## 5. How to Get Involved

### Fund (7 entities)
Working concepts exist but lack capital to scale.

**Watch list** (7 entities):
- The Collective of Inner Weavers (Bottleneck: Funding)
- [Project Hieroglyph](https://hieroglyph.asu.edu/) (Bottleneck: Funding)
- Closed-loop gene therapy for seizure suppression via activity-sensing potassium-channel upregulation (Bottleneck: Regulation)
- [Openwater](https://www.openwater.health/) universal diagnostic/therapeutic device (Bottleneck: Regulation)
- [Biophilic Architecture](https://en.wikipedia.org/wiki/Biophilic_design) (Bottleneck: Funding)
- [Focused Research Organizations (FROs)](https://www.convergentresearch.org/about-fros) (Bottleneck: Funding)
- [BBN](https://en.wikipedia.org/wiki/Raytheon_BBN)-style Applied R&D Contractor (New BBNs) (Bottleneck: Coordination)

### Build (17 entities)
The research is done and the path is clear. What's missing is engineering teams to build it.

**Watch list** (17 entities):
- Translation Language Models (TLMs) with citizen-owned training databases (Bottleneck: Coordination)
- The [Delphi](https://en.wikipedia.org/wiki/Delphi_method) Collaboration Protocol (Bottleneck: Coordination)
- [Lean FRO](https://lean-lang.org/) (interactive theorem proving infrastructure for mathematics and AI) (Bottleneck: Engineering)
- Large-scale AI-mediated deliberation system (Bottleneck: Engineering)
- [Deep Fission](https://deepfission.com/) borehole nuclear reactor (Bottleneck: Regulation)
- Safety-Netted [DAOs](https://en.wikipedia.org/wiki/Decentralized_autonomous_organization) (Bottleneck: Engineering)
- [Multiplicity.ai](https://themultiplicity.ai/) (Bottleneck: Engineering)
- [Futarchy](https://en.wikipedia.org/wiki/Futarchy) (Bottleneck: Social Acceptance)
- Author Personal Knowledge Graph / Writing Corpus Utility (Bottleneck: Engineering)
- Tool AI for Tool AI (Bottleneck: Engineering)
- *...and 7 more*

### Research (68 entities)
Promising directions that need more investigation before they're ready for deployment.

**Spotlight:**
- [**AI cryptographic oracle with zero-knowledge IoT auditing and jury-DAO**](#ai-cryptographic-oracle-with-zero-knowledge-iot-auditing-and-jury-dao) — A fraud-resistance layer combining [zero-knowledge proofs](https://en.wikipedia.org/wiki/Zero-knowledge_proof) from IoT sensor data, AI anomaly detection, stake-slashing penalties, and a decentralized human jury for retroactive balance correction. (Bottleneck: Coordination)
- [**Moral Trade**](#moral-trade) — A mechanism by which people or groups with different moral priorities swap concessions so that each gets more of what they care about than unilateral action would yield. Concept originated by [Toby Ord](https://en.wikipedia.org/wiki/Toby_Ord). (Bottleneck: Coordination)
- [**Comprehensive AI Services (Drexler)**](#comprehensive-ai-services-drexler) — An architecture of many narrow, domain-limited superhuman AIs that interact competitively rather than a single general superintelligence, achieving safety through structural narrowness. Based on [Eric Drexler's framework](https://www.fhi.ox.ac.uk/wp-content/uploads/Reframing_Superintelligence_FHI-TR-2019-1.1-1.pdf). (Bottleneck: Coordination)
- [**Wisdom DAO**](#wisdom-dao) — A [decentralized autonomous organization](https://en.wikipedia.org/wiki/Decentralized_autonomous_organization) where human citizens and AI systems jointly propose, deliberate, and vote on governance policy using weighted voting and [blockchain](https://en.wikipedia.org/wiki/Blockchain) transparency. (Bottleneck: Regulation)

**Watch list** (64 entities):
- Liberal/Popperian AGI Education Framework (Bottleneck: Physics)
- Viotopia (Bottleneck: Coordination)
- Cognitive Field Resonators (CFRs) (Bottleneck: Physics)
- Polymesh Civic Ledger (Bottleneck: Coordination)
- AI-Democratic Institutions for Decentralized Governance (Bottleneck: Social Acceptance)
- Isolated Societies Research Institute (Bottleneck: Funding)
- Loom Studios (Bottleneck: Coordination)
- Reputational Market (Bottleneck: Coordination)
- Values-as-modality parametrization across AI systems (Bottleneck: Coordination)
- Parallel lightly-regulated childminder category (France) (Bottleneck: Regulation)
- *...and 54 more*

### Advocate (39 entities)
These need policy changes, regulatory frameworks, or public support to move forward.

**Spotlight:**
- [**Tokenized neural data sharing with selective disclosure**](#tokenized-neural-data-sharing-with-selective-disclosure) — A privacy architecture for [BCI](https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface) systems in which neural data is tokenized so users can selectively disclose specific streams of thought or brain state while retaining others as private. (Bottleneck: Regulation)
- [**Interbeing Forum**](#interbeing-forum) — A rotating bioregional assembly that grants formal representation to ecosystems and future generations through human guardians advised by [digital twin](https://en.wikipedia.org/wiki/Digital_twin) data. (Bottleneck: Regulation)
- [**Attack Dog DAO for Climate**](#attack-dog-dao-for-climate) — A DAO that funds and coordinates environmental litigation on behalf of legally-recognized natural entities, financed through tokenized litigation investment. (Bottleneck: Regulation)
- [**Accord of Watersheds**](#accord-of-watersheds) — An international treaty framework that organizes political cooperation around [watershed](https://en.wikipedia.org/wiki/Drainage_basin) and bioregional boundaries rather than national borders. (Bottleneck: Regulation)
- [**Watershed Parliaments**](#watershed-parliaments) — Bioregional governance bodies organized around watershed boundaries rather than political borders, incorporating ecological feedback into formal decision-making. (Bottleneck: Regulation)
- [**Loyal AI Assistance (Fiduciary AI Assistance)**](#loyal-ai-assistance-fiduciary-ai-assistance) — A personal AI system explicitly designed to be loyal to the individual user's goals rather than to platform or advertiser interests, contrasted with current assistants like Siri or Alexa. Based on [fiduciary AI principles](https://arxiv.org/abs/2308.02435). (Bottleneck: Regulation)

**Watch list** (33 entities):
- [LexDAO](https://lexdao.org/) (Bottleneck: Regulation)
- De novo designed universal flu vaccines ([Neil King](https://www.ipd.uw.edu/) / [Baker Lab](https://www.bakerlab.org/) platform) (Bottleneck: Regulation)
- Hybrid Market impact bond ledger (Bottleneck: Regulation)
- Mandatory Open-Source AI Release Policy (Bottleneck: Regulation)
- [Orare](https://orare.world/) - AI-powered Futarchy governance system (Bottleneck: Social Acceptance)
- Global Personhood Token / Trust-of-Personhood Standard (Bottleneck: Regulation)
- Integration of [Brain Preservation](https://www.brainpreservation.org/) into the Medical System (Bottleneck: Regulation)
- Open-source AI-powered research funding and knowledge platform (Bottleneck: Regulation)
- Interplanetary Cooperative (Bottleneck: Regulation)
- The Flourishing Foundation (Bottleneck: Regulation)
- *...and 23 more*

### Convene (58 entities)
The pieces exist separately — what's missing is coordination between stakeholders.

**Spotlight:**
- [**Community-Governed AI Mesh Systems**](#community-governed-ai-mesh-systems) — Decentralized AI networks trained on locally governed data and stewarded by community trust circles rather than centralized corporate or state actors. (Bottleneck: Coordination)
- [**Universal AI Learning UnCommons (UALU)**](#universal-ai-learning-uncommons-ualu) — A federated governance institution that develops, maintains, and audits AI education tools through multi-stakeholder councils including elders, learners, and ethicists. (Bottleneck: Coordination)
- [**BCI Operating System (BCI-OS)**](#bci-operating-system-bci-os) — An open-source operating system layer for [brain-computer interfaces](https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface) that embeds agency evaluation, AI model compatibility, and privacy standards as core OS-level features. (Bottleneck: Coordination)
- [**Civic Systems Co-Op**](#civic-systems-co-op) — A global open-source consortium that develops and maintains ethical AI tools for municipal and community governance. (Bottleneck: Coordination)
- [**Interoperable Governance Protocol Stack**](#interoperable-governance-protocol-stack) — A shared technical and governance protocol layer that allows citizens to port digital identities, benefits, and credentials across distinct federated city-state systems, and enables AI systems across those jurisdictions to align resource allocation and crisis modeling. (Bottleneck: Regulation)
- [**DAO-governed open innovation platform for TLM documentation and training data**](#dao-governed-open-innovation-platform-for-tlm-documentation-and-training-data) — A DAO-based governance structure that mandates open-source documentation and community-sourced feedback loops for translation model development and adaptation. (Bottleneck: Coordination)
- [**Digital Twins for Communities and Ecosystems**](#digital-twins-for-communities-and-ecosystems) — Real-time [digital models](https://en.wikipedia.org/wiki/Digital_twin) of communities and ecosystems that enable participatory future simulation with locally-owned data. (Bottleneck: Coordination)
- [**The Global Deliberation Coordinator**](#the-global-deliberation-coordinator) — A platform institution designed to coordinate global [deliberative processes](https://en.wikipedia.org/wiki/Deliberative_democracy) and collective decision-making specifically around AI governance. (Bottleneck: Coordination)
- [**Epistemic stack**](#epistemic-stack) — A citation and provenance system for all information—from newspaper articles to social media claims—that lets users trace any assertion back to its raw data sources, with trust scores based on historical accuracy of each link in the chain. (Bottleneck: Coordination)

**Watch list** (49 entities):
- [AI Fiduciaries](https://arxiv.org/abs/2308.02435) (Bottleneck: Coordination)
- Privacy-Preserving Global Regulatory Markets for AI Verification (Bottleneck: Coordination)
- Continuity Guild (Bottleneck: Coordination)
- BioEcho Mesh (Bottleneck: Coordination)
- The Mnemosyne Assembly (Bottleneck: Coordination)
- Open Cognition Ledger (Bottleneck: Coordination)
- Living Rights Network (Bottleneck: Coordination)
- [Federated Procurement Platforms](https://en.wikipedia.org/wiki/OpenProcurement) (Bottleneck: Coordination)
- contextual autonomy (Bottleneck: Coordination)
- Publishing for Machines (machine-readable scientific publishing framework) (Bottleneck: Social Acceptance)
- *...and 39 more*


---

## 6. Appendix: Scoring Details

Full scoring breakdown for all Tier 1 entities.

### Community-Governed AI Mesh Systems
**Composite: 21** | Group: Decentralized & Democratic Institutions | TRL: 4 | v2 consensus: No

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 5/5 | Governance explicitly handled by designated community trust circles (Indigenous and racialized groups) with consent frameworks defining access and use protocols. Decision-making authority distribut... |
| d/acc: Decentralized | 5/5 | Mesh architecture explicitly distributes both compute and decision-making authority locally with no single node controlling the system. Federated learning frameworks (Flower, PySyft) enable distrib... |
| d/acc: Defensive | 4/5 | System protects community data sovereignty and prevents extraction by centralized actors. Preserves privacy through federated learning (data stays local). Defends against colonization patterns thro... |
| d/acc: Differential | 3/5 | Accelerates defensive capabilities (data sovereignty, privacy-preserving training, distributed governance) relative to centralized AI extraction models. However, research data does not substantivel... |
| **d/acc Total** | **17/20** | Strong d/acc alignment on democratic and decentralized dimensions with clear evidence. Defensive posture evident but not exclusively defensive. Differential advantage claimed but not empirically demonstrated in source material. |
| Transformative | 4/5 | If fully implemented and adopted at scale, this would transform multiple fields: (1) AI governance—replacing corporate/state-centric models with community-governed alternatives; (2) Indigenous data so |
| Bottleneck | Coordination | Research data identifies 'integration complexity: combining three distinct technical and governance layers requires solving interoperability challenges that no current platform addresses' and 'governa |
| Action | Convene | Given that technical components exist separately (federated learning frameworks mature, Indigenous governance principles established, mesh networks operational) but lack integration, the immediate act |

### Universal AI Learning UnCommons (UALU)
**Composite: 20** | Group: Education, Development & Human Flourishing | TRL: 3 | v2 consensus: Yes

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 5/5 | UALU explicitly distributes decision-making power through 'governance councils composed of diverse stakeholders—elders, learners, technologists, ethicists' with 'co-creation and oversight' mechanis... |
| d/acc: Decentralized | 4/5 | Described as 'decentralised network of community nodes, each contributing to co-creation' with 'federated structure' allowing 'local adaptation while maintaining shared accountability frameworks.' ... |
| d/acc: Defensive | 5/5 | UALU's core function is auditing, bias mitigation, and cultural appropriateness oversight—purely protective mechanisms. No offensive capabilities described. Focus on 'justice and care' and preventi... |
| d/acc: Differential | 3/5 | UALU accelerates defensive AI governance (auditing, bias detection, ethical oversight) relative to uncontrolled AI deployment. However, research data shows 'most existing initiatives focus on top-d... |
| **d/acc Total** | **17/20** |  |
| Transformative | 3/5 | UALU transforms the AI education governance field by institutionalizing elder/community council oversight and federated accountability—currently absent at scale. Research confirms 'formal elder/commun |
| Bottleneck | Coordination | Research data explicitly identifies 'Institutional fragmentation—no existing federated model integrates elder councils, learners, ethicists, and technologists with formal accountability mechanisms' an |
| Action | Convene | Given TRL 3 status, existing partial analogues (Mozilla, African Union, UNESCO, AIGN), and identified coordination barriers, immediate action should be convening multi-stakeholder working groups to de |

### AI cryptographic oracle with zero-knowledge IoT auditing and jury-DAO
**Composite: 19** | Group: Decentralized & Democratic Institutions | TRL: 4 | v2 consensus: No

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 4/5 | Jury-DAO component explicitly enables 'randomly selected jury-DAO of token holders can vote to retroactively adjust balances,' distributing fraud adjudication decisions across decentralized human p... |
| d/acc: Decentralized | 4/5 | System eliminates single points of failure through: (1) distributed IoT sensor network generating proofs, (2) decentralized AI anomaly detection layer, (3) jury-DAO replacing centralized arbiters, ... |
| d/acc: Defensive | 5/5 | Purely defensive architecture: zero-knowledge proofs protect sensor data from spoofing, AI anomaly detection identifies fraudulent claims, quadratic slashing deters cheating, jury-DAO provides huma... |
| d/acc: Differential | 3/5 | Moderately differential: ZK-IoT proofs and AI anomaly detection advance defensive fraud detection faster than attackers can generate undetectable false claims. However, differential advantage is no... |
| **d/acc Total** | **16/20** |  |
| Transformative | 3/5 | Transforms a field (blockchain fraud detection and governance): Combines four previously separate components (ZK-IoT, AI anomaly detection, quadratic slashing, jury-DAO) into integrated fraud-resistan |
| Bottleneck | Coordination | N/A |
| Action | Research | N/A |

### Moral Trade
**Composite: 18** | Group: AI-Mediated Deliberation & Collective Intelligence | TRL: 2 | v2 consensus: Yes

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 5/5 | Moral trade explicitly distributes decision-making power by allowing diverse groups with different moral priorities to negotiate outcomes rather than having any single moral view dominate. Source s... |
| d/acc: Decentralized | 4/5 | The mechanism is inherently decentralized—it operates through bilateral/multilateral negotiation between parties rather than centralized authority. However, at civilizational scale, some coordinati... |
| d/acc: Defensive | 3/5 | Moral trade is primarily a coordination mechanism rather than inherently defensive or offensive. It enables peaceful resolution of moral disagreements through negotiation rather than competition or... |
| d/acc: Differential | 2/5 | No evidence in source material addresses differential acceleration of defensive vs. offensive capabilities. Moral trade is a coordination/negotiation framework that could theoretically be applied t... |
| **d/acc Total** | **14/20** |  |
| Transformative | 4/5 | Moral trade has potential to transform multiple fields by enabling civilizational-scale coordination across diverse moral communities. Source describes 'huge opportunities' at civilization scale and n |
| Bottleneck | Coordination | N/A |
| Action | Research | N/A |

### BCI Operating System (BCI-OS)
**Composite: 18** | Group: Neurotechnology & Brain-Computer Interfaces | TRL: 3 | v2 consensus: No

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 4/5 | Open-source governance structure with standards body explicitly designed to maintain human-agency principles. Source states 'open-source governance structure and standards body are created to maint... |
| d/acc: Decentralized | 3/5 | OS-level architecture reduces single points of failure by enforcing privacy and agency at the platform layer rather than leaving it to individual applications. Open-source model enables distributed... |
| d/acc: Defensive | 5/5 | Purely defensive in posture: embeds privacy protocols, agency evaluation, and consent mechanisms at OS level to protect users from unauthorized neural data access. Source emphasizes 'safeguards hum... |
| d/acc: Differential | 3/5 | Moderately differential: privacy and agency protections embedded at OS level could slow malicious actors' ability to exploit BCIs compared to fragmented landscape where each app handles security in... |
| **d/acc Total** | **15/20** | Strong on democratic governance intent and defensive posture; moderate on decentralization and differential advantage. |
| Transformative | 3/5 | Transforms a field (neurotechnology/BCI development). BCI-OS would fundamentally restructure how BCIs are developed, deployed, and governed by establishing privacy and agency as architectural requirem |
| Bottleneck | Coordination | Research data explicitly identifies 'fragmented BCI ecosystem: hardware manufacturers, software developers, and application creators operate independently without standardized interfaces or governance |
| Action | Convene | TRL 3 status with proof-of-concept work at AE Studio and OpenBCI indicates technical feasibility is not the immediate constraint. Funding is not identified as a barrier. The critical next step is conv |

### Tokenized neural data sharing with selective disclosure
**Composite: 17** | Group: Neurotechnology & Brain-Computer Interfaces | TRL: 2 | v2 consensus: No

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 4/5 | Tokenized selective disclosure directly distributes decision-making power to individual users over their own neural data. Users can 'grant or revoke access to specific tokens' and choose 'what you ... |
| d/acc: Decentralized | 2/5 | The architecture itself is user-centric but relies on regulatory frameworks (HIPAA, state laws) and consent management systems that are inherently centralized or platform-mediated. No evidence of p... |
| d/acc: Defensive | 5/5 | This is purely defensive: it protects neural data privacy by limiting exposure, enabling users to withhold sensitive cognitive content, and preventing unauthorized access to specific thought stream... |
| d/acc: Differential | 3/5 | The architecture favors defense by enabling granular privacy controls that are difficult for attackers to circumvent without user consent. However, the research data notes 're-identification even f... |
| **d/acc Total** | **14/20** | Strong on democratic empowerment and defensive posture; moderate on decentralization and differential advantage. |
| Transformative | 3/5 | This transforms the field of neural data governance and BCI ethics. It moves from binary consent models (share all or nothing) to granular, user-controlled access control, fundamentally changing how n |
| Bottleneck | Regulation | While regulatory frameworks exist (Montana, Colorado, California, Chile), they treat neural data as sensitive information without implementing granular tokenized mechanisms. Research data explicitly s |
| Action | Advocate | TRL 2 indicates proof-of-concept stage. No funding barriers are documented. The immediate action is regulatory: advocate for unified federal standards and technical specifications for tokenized neural |

### Civic Systems Co-Op
**Composite: 17** | Group: AI Safety, Alignment & Governance | TRL: 5 | v2 consensus: No

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 4/5 | Mechanism explicitly states 'distributed across member organizations rather than controlled by a single vendor or government' and 'member cities and communities contribute to and draw from a shared... |
| d/acc: Decentralized | 4/5 | Design eliminates single vendor or government control point. Research data confirms 'no unified global open-source consortium exists' currently, but the proposed model distributes maintenance and g... |
| d/acc: Defensive | 4/5 | Explicitly framed around 'ethical AI tools' with 'transparent decision logs' and 'ethical standards.' Purpose is governance transparency and accountability, not offensive capability. Open-source mo... |
| d/acc: Differential | 2/5 | No evidence in source material that this accelerates defensive AI development faster than offensive. The mechanism focuses on governance transparency and ethical standards for municipal use cases, ... |
| **d/acc Total** | **14/20** |  |
| Transformative | 3/5 | Transforms the municipal AI governance field by shifting from vendor-controlled (OpenGov serving 2,000+ communities) or loosely federated registries (DPGA with 150+ tools) to a unified cooperative mod |
| Bottleneck | Coordination | N/A |
| Action | Convene | N/A |

### Interbeing Forum
**Composite: 17** | Group: Decentralized & Democratic Institutions | TRL: 3 | v2 consensus: No

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 4/5 | Rotating steward selection from bioregions prevents power entrenchment. Formal representation granted to non-human entities and future generations through designated guardians. Decision-making weig... |
| d/acc: Decentralized | 4/5 | Bioregional structure distributes authority across geographic regions rather than centralizing in nation-states. Rotating basis prevents single points of control. Multiple precedents (OACC since 19... |
| d/acc: Defensive | 4/5 | Explicitly protective: safeguards ecosystem integrity, represents future generations, audits digital infrastructure for integrity. Designed to constrain rather than expand extractive capacity. Over... |
| d/acc: Differential | 2/5 | Digital twin technology could accelerate defensive monitoring and decision-making, but research data shows digital twins are 'in prototype/pilot phase' with 'no integrated system' yet existing. The... |
| **d/acc Total** | **14/20** |  |
| Transformative | 3/5 | Transforms a field (environmental governance and bioregional decision-making). Combines three existing but separate precedents (legal personhood for ecosystems, future generations representation, citi |
| Bottleneck | Regulation | N/A |
| Action | Advocate | N/A |

### Interoperable Governance Protocol Stack
**Composite: 16** | Group: Decentralized & Democratic Institutions | TRL: 4 | v2 consensus: Yes

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 3/5 | Protocol stack enables citizens to port identities and benefits across systems, increasing individual agency. However, decision-making power remains with jurisdictional authorities who implement th... |
| d/acc: Decentralized | 4/5 | Architecture explicitly designed as federated with modular governance components. No single point of control: 'any compliant local system can read and honor records issued by another.' Multiple jur... |
| d/acc: Defensive | 4/5 | System is fundamentally protective: enables crisis response, resource sharing, and citizen benefit access without requiring data centralization. Designed to preserve jurisdictional autonomy while e... |
| d/acc: Differential | 2/5 | Limited evidence of differential acceleration. The protocol stack itself is defensive (coordination, not weaponization), but research data shows 'federated learning frameworks for privacy-preservin... |
| **d/acc Total** | **13/20** |  |
| Transformative | 3/5 | Transforms a field (emergency response and cross-jurisdictional governance coordination). Evidence: enables 'relief in hours instead of weeks' and 'seamless resource sharing across local and regional  |
| Bottleneck | Regulation | N/A |
| Action | Convene | N/A |

### Comprehensive AI Services (Drexler)
**Composite: 16** | Group: AI Safety, Alignment & Governance | TRL: 2 | v2 consensus: No

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 3/5 | CAIS distributes decision-making across multiple competing specialized systems rather than concentrating it in a single superintelligence. The 'ecology of competing specialized systems' provides ch... |
| d/acc: Decentralized | 4/5 | The architecture explicitly eliminates single points of failure by partitioning capabilities into domain-specific services. Source states 'structural narrowness' prevents 'unilateral takeover,' and... |
| d/acc: Defensive | 4/5 | CAIS is explicitly framed as a safety architecture: 'safety through narrowness' and 'guardrails we've put in place.' Architectural constraints prevent systems from doing 'end-runs around' safety me... |
| d/acc: Differential | 2/5 | CAIS could accelerate defensive capabilities by making uncontrolled generalization structurally difficult. However, research data notes 'foundation models may have undermined some CAIS assumptions'... |
| **d/acc Total** | **13/20** |  |
| Transformative | 3/5 | CAIS transforms AI safety discourse and the conceptual framing of superintelligence (field-level impact). It offers a fundamentally different architectural paradigm for organizing AI systems. However, |
| Bottleneck | Coordination | N/A |
| Action | Research | N/A |

### Attack Dog DAO for Climate
**Composite: 16** | Group: Ecological & Regenerative Systems | TRL: 3 | v2 consensus: No

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 4/5 | DAO structure inherently distributes governance via token-holder voting. Source describes 'decentralized governance' as core mechanism. However, evidence shows no actual implementation, so democrat... |
| d/acc: Decentralized | 3/5 | DAO component reduces single points of failure in capital pooling and decision-making. However, research data identifies critical centralization risks: 'courts have deemed DAOs general partnerships... |
| d/acc: Defensive | 4/5 | Mechanism is fundamentally defensive: funding litigation against polluters and harmful actors to protect natural entities. Creates market deterrent against environmental harm rather than enabling n... |
| d/acc: Differential | 2/5 | Weak differential advantage. While litigation finance creates defensive incentives, it does not accelerate defensive technology faster than offensive technology. Polluters can equally access litiga... |
| **d/acc Total** | **13/20** | Strong on democratic distribution and defensive posture; moderate on decentralization due to liability and guardian bottlenecks; weak on differential advantage. |
| Transformative | 3/5 | Transforms a field (environmental law and climate litigation). Creates new market mechanism linking financial incentives to environmental protection via legal personhood frameworks. Combines three pre |
| Bottleneck | Regulation | Research data identifies three unresolved regulatory barriers: (1) 'Legal uncertainty around DAO liability...creates structural risk'; (2) 'Environmental personhood frameworks lack standardized liabil |
| Action | Advocate | Immediate action should target regulatory clarity and legal framework development. Funding or building would encounter insurmountable legal barriers. Research is ongoing (publications cited). Advocacy |

### Wisdom DAO
**Composite: 16** | Group: Decentralized & Democratic Institutions | TRL: 4 | v2 consensus: No

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 4/5 | Mechanism explicitly distributes decision-making to citizens via personal AI assistants and weighted voting. All citizens can propose and vote on governance policy. Research data shows 40% particip... |
| d/acc: Decentralized | 4/5 | Built on blockchain ledger with smart contract enforcement, eliminating centralized bureaucratic gatekeepers. DAO infrastructure (Aragon, MakerDAO precedents) demonstrates technical feasibility of ... |
| d/acc: Defensive | 3/5 | Mechanism is primarily defensive: reduces corruption through transparency, prevents centralized power concentration, and uses smart contracts to enforce decisions rather than enable unilateral acti... |
| d/acc: Differential | 2/5 | Mechanism accelerates defensive governance infrastructure (transparency, distributed decision-making, corruption reduction). However, research data shows AI agents generate voting recommendations w... |
| **d/acc Total** | **13/20** |  |
| Transformative | 3/5 | Transforms governance field by shifting from centralized bureaucracy to hybrid human-AI decentralized decision-making. Research demonstrates 97% alignment with historical decisions and 40% participati |
| Bottleneck | Regulation | N/A |
| Action | Research | N/A |

### Accord of Watersheds
**Composite: 16** | Group: International Governance & Coordination | TRL: 6 | v2 consensus: No

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 4/5 | Mechanism explicitly includes 'nations, Indigenous governments, and regional bodies' as signatory parties with multi-stakeholder coordination. IJC and MRC implementations demonstrate 'multi-stakeho... |
| d/acc: Decentralized | 3/5 | Distributes authority from national capitals to watershed-based governance bodies, reducing single points of control. However, research data shows 'fragmented form across multiple regional implemen... |
| d/acc: Defensive | 4/5 | Framework is explicitly defensive: 'protect rather than attack,' focused on 'conservation and conflict resolution,' 'resource allocation follow hydrological logic,' and 'ecosystem-centered governan... |
| d/acc: Differential | 2/5 | No evidence in source material that this framework accelerates defensive technology faster than offensive technology. The mechanism focuses on governance structure and resource coordination, not te... |
| **d/acc Total** | **13/20** | Strong on democratic inclusion and defensive orientation; moderate on decentralization and weak on differential acceleration. |
| Transformative | 3/5 | Transforms a field (environmental governance and international law). Shifts organizing principle from national borders to ecological boundaries—a fundamental reframing of how transnational cooperation |
| Bottleneck | Regulation | TRL 6 indicates operational governance structures exist, but 'a comprehensive international treaty framework...remains at conceptual stage.' Barriers section identifies 'entrenched national sovereignt |
| Action | Advocate | Given TRL 6 status with existing implementations (IJC, MRC) and pilot projects (Cascadia, Amazon, Asia-Pacific), the immediate need is advocacy to formalize fragmented implementations into unified tre |

### DAO-governed open innovation platform for TLM documentation and training data
**Composite: 16** | Group: Decentralized & Democratic Institutions | TRL: 3 | v2 consensus: No

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 4/5 | DAO-based governance with smart-contract voting gives communities 'formal decision-making power over how TLM training data is collected, labeled, and updated.' Open innovation platforms enable comm... |
| d/acc: Decentralized | 4/5 | DAO structure eliminates single proprietary entity control; 'prevents proprietary capture of the models' through distributed governance. Smart-contract enforcement is inherently decentralized. Howe... |
| d/acc: Defensive | 3/5 | The mechanism is primarily defensive: it protects against proprietary capture, prevents bias through community oversight, and enforces transparency via open-source requirements. However, it is not ... |
| d/acc: Differential | 2/5 | The entity accelerates defensive capabilities (transparency, distributed control, bias detection) but does not explicitly accelerate defensive tech faster than offensive tech. Research data shows n... |
| **d/acc Total** | **13/20** |  |
| Transformative | 3/5 | This entity transforms a field (translation model development and AI governance). It shifts the paradigm from proprietary, centralized model development to community-governed, open-source alternatives |
| Bottleneck | Coordination | N/A |
| Action | Convene | N/A |

### Watershed Parliaments
**Composite: 16** | Group: Decentralized & Democratic Institutions | TRL: 4 | v2 consensus: No

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 4/5 | Mechanism explicitly includes 'designated representatives for ecosystem interests alongside human citizens' and 'multi-stakeholder participation' in existing implementations (MDBA, SRBC, ICPRB). Ho... |
| d/acc: Decentralized | 3/5 | Watershed-based organization reduces dependence on nation-state political boundaries as single points of control. Research data shows 'fragmented form through river basin organizations' that 'coord... |
| d/acc: Defensive | 4/5 | The mechanism is explicitly defensive: 'Proposals must pass multi-generational impact assessments covering all species within the watershed before adoption' and decisions must 'demonstrate positive... |
| d/acc: Differential | 2/5 | No evidence in provided materials regarding acceleration of defensive versus offensive technologies. The mechanism focuses on governance structure and decision-making processes rather than technolo... |
| **d/acc Total** | **13/20** |  |
| Transformative | 3/5 | Watershed Parliaments would transform the field of governance and environmental management by fundamentally reorganizing political jurisdiction around ecological rather than geopolitical boundaries. T |
| Bottleneck | Regulation | N/A |
| Action | Advocate | N/A |

### Digital Twins for Communities and Ecosystems
**Composite: 16** | Group: AI-Mediated Deliberation & Collective Intelligence | TRL: 5 | v2 consensus: Yes

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 4/5 | Mechanism explicitly enables 'participatory future simulation' and 'participatory governance bodies including representatives for non-human entities.' Citizens retain decision-making power through ... |
| d/acc: Decentralized | 3/5 | Communities and citizens 'retain ownership of their data' and hold 'digital sovereignty' rather than ceding to centralized platforms. However, sensor networks and models still require coordination ... |
| d/acc: Defensive | 4/5 | Mechanism is fundamentally defensive: enables simulation of consequences before implementation, protects community data ownership against centralized platform capture, and supports informed governa... |
| d/acc: Differential | 2/5 | No evidence in source material that this accelerates defensive technology faster than offensive technology. Digital twin technology is dual-use (Singapore's system used for 'disaster management' bu... |
| **d/acc Total** | **13/20** | Strong on democratic and defensive dimensions, moderate on decentralization, weak on differential advantage. |
| Transformative | 3/5 | Transforms a field (environmental governance and urban planning). Digital twins with genuine participatory governance and community data ownership would fundamentally reshape how communities make deci |
| Bottleneck | Coordination | Research data identifies multiple barriers but coordination emerges as primary: 'integration at scale remains in prototype/pilot phase,' 'combining community data ownership with real-time sensor netwo |
| Action | Convene | Given mature component technologies (digital twins operational, data sovereignty frameworks exist) and identified coordination barriers, immediate action should be convening stakeholders across techno |

### Loyal AI Assistance (Fiduciary AI Assistance)
**Composite: 15** | Group: AI Safety, Alignment & Governance | TRL: 3 | v2 consensus: Yes

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 4/5 | System explicitly designed to 'remain in control' with user maintaining decision-making authority. Contrasts with current assistants that prioritize platform interests over user goals. Fiduciary du... |
| d/acc: Decentralized | 2/5 | While individual users gain control over their personal AI system, the research data does not describe distributed architecture or reduced single points of failure. Each user would have their own l... |
| d/acc: Defensive | 4/5 | System is explicitly defensive in posture: designed to protect user interests against manipulation, data monetization, and advertiser influence. Mechanism emphasizes 'no selfish or third-party inte... |
| d/acc: Differential | 2/5 | While fiduciary AI is defensive in nature, research data provides no evidence that it accelerates defensive capabilities faster than offensive ones. The technology remains conceptual; no comparativ... |
| **d/acc Total** | **12/20** | Strong on democratic control and defensive posture; weaker on decentralization and differential acceleration. |
| Transformative | 3/5 | Transforms the field of AI assistance design by reorienting incentive structures from platform/advertiser interests to user interests. Establishes new legal and design frameworks (fiduciary duty) appl |
| Bottleneck | Regulation | Research data explicitly identifies 'regulatory and legal uncertainty' as primary barrier: 'fiduciary frameworks remain underdeveloped for AI, with no clear enforcement mechanisms or standards for com |
| Action | Advocate | TRL 3 status indicates research phase is mature (published frameworks, design methodologies, institutional research). Funding exists through research institutions. Primary need is regulatory pathway d |

### The Global Deliberation Coordinator
**Composite: 15** | Group: AI-Mediated Deliberation & Collective Intelligence | TRL: 4 | v2 consensus: Yes

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 4/5 | Platform explicitly designed to 'convene global stakeholders for deliberative discussions' and coordinate 'collective decision-making across national and organizational boundaries.' UN Global Dialo... |
| d/acc: Decentralized | 2/5 | Proposed as a 'platform institution' and 'coordination infrastructure,' which implies centralized convening function. Research shows existing implementations (AI4Deliberation, Global Dialogue) oper... |
| d/acc: Defensive | 4/5 | Mechanism focuses on deliberative processes for collective decision-making on AI governance—inherently defensive in posture (governance, coordination, alignment rather than capability acceleration)... |
| d/acc: Differential | 2/5 | Deliberation coordination accelerates defensive governance capacity (policy alignment, stakeholder consensus). However, research data provides no evidence this specifically accelerates defensive te... |
| **d/acc Total** | **12/20** |  |
| Transformative | 3/5 | Transforms the field of AI governance by shifting from fragmented national/regional approaches to coordinated global deliberative infrastructure. Research demonstrates this addresses a critical gap: c |
| Bottleneck | Coordination | Research explicitly identifies 'representation and coordination gaps: 118 countries (mainly Global South) remain excluded from major AI governance initiatives, and hundreds of incompatible governance  |
| Action | Convene | Given TRL 4 status with multiple pilot projects proven viable, and coordination as primary bottleneck, immediate action should focus on convening stakeholders to design unified coordination architectu |

### Epistemic stack
**Composite: 14** | Group: Scientific Research & Knowledge Infrastructure | TRL: 4 | v2 consensus: Yes

| Dimension | Score | Evidence |
|-----------|-------|----------|
| d/acc: Democratic | 3/5 | Community Notes demonstrates crowdsourced fact-checking with 133,000+ contributors, distributing verification power. However, only 11% of submitted notes reach 'helpful' status, indicating gatekeep... |
| d/acc: Decentralized | 2/5 | C2PA and blockchain-based systems (Numbers Protocol/Capture) add cryptographic and immutability layers, reducing single points of failure for provenance records. However, research data explicitly n... |
| d/acc: Defensive | 4/5 | The epistemic stack is fundamentally defensive: it aims to protect users from misinformation by enabling verification and trust assessment rather than generating false claims. The mechanism traces ... |
| d/acc: Differential | 2/5 | The system could theoretically accelerate defensive capabilities (verification, trust assessment) relative to offensive ones (disinformation creation). However, research data provides no evidence t... |
| **d/acc Total** | **11/20** |  |
| Transformative | 3/5 | The epistemic stack would transform the information verification field by creating a unified, traceable provenance system from raw data through inference to published claims. Research data shows 'no u |
| Bottleneck | Coordination | N/A |
| Action | Convene | N/A |
