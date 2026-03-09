# Hyper-Entities V3: Spotlight Report

Linda Petrini  
Foresight Institute  
March 2026

---

## 1. Executive Summary

The term *hyper-entity* was coined by Michael Nielsen to describe systems that do not yet exist but are already reshaping how people coordinate, allocate capital, and construct shared narratives around their anticipated arrival. These are not speculative fictions. They are attractors — concepts sufficiently concrete and compelling that researchers, funders, and institutions organize real behavior around them before any working version exists. This report identifies and ranks 189 such candidates drawn from 109 sources, with the goal of helping funders, policymakers, and technologists direct attention toward the highest-leverage opportunities.

The analysis applies the d/acc framework developed by Vitalik Buterin, which evaluates entities across four overlapping properties: democratic (distributing power rather than concentrating it), decentralized (resistant to single points of control or failure), defensive (strengthening protective rather than offensive capabilities), and differential (accelerating beneficial technologies faster than harmful ones). Entities were also scored on transformative potential and actionability, producing a composite score that determined tier placement.

From 189 candidates, 19 were designated Tier 1 spotlight entities and 170 placed on a Tier 2 watch list. The spotlight entities represent the strongest combination of d/acc alignment, transformative potential, and near-term actionability. Leading this group are Community-Governed AI Mesh Systems (composite score 21), the Universal AI Learning UnCommons (20), and an AI cryptographic oracle with zero-knowledge IoT auditing and jury-DAO governance (19). Across all 189 entities, the average d/acc score was 9.5 out of 20, average transformative score 2.6 out of 5, and average Technology Readiness Level (TRL) 3.9 — placing the field, in aggregate, between proof-of-concept and early validation.

The largest thematic cluster is AI Safety, Alignment & Governance with 31 entities, followed by Scientific Research & Knowledge Infrastructure (25) and Education, Development & Human Flourishing (20). Decentralized & Democratic Institutions and AI-Mediated Deliberation & Collective Intelligence each contribute 18 entities, reflecting strong interest in governance architectures that can scale without centralizing control.

The most common bottleneck across the full dataset is coordination, affecting 76 of 189 entities. Regulatory uncertainty constrains 57, engineering challenges 24, and social acceptance barriers 13. Funding, despite its prominence in public discourse about emerging technology, ranks last as a primary bottleneck, cited for only 7 entities. This distribution suggests that the scarcest resource is not capital but the institutional infrastructure to align actors around shared standards, protocols, and governance frameworks.

Recommended primary actions reflect this: 68 entities most need sustained research, 58 require convening — bringing together the communities of practice that can establish norms and test coordination mechanisms — and 39 need advocacy to shift regulatory and political conditions. Only 17 are primarily in a build phase, and 7 are primarily funding-constrained.

All candidates were sourced from Existential Hope (existentialhope.com), the Foresight Institute's initiative cataloguing pathways to long-term human and civilizational flourishing, drawing on podcast transcripts, world gallery submissions, and AI pathways essays. Twenty-seven entities appeared in both this analysis and the prior v2 analysis, providing cross-version consensus on their significance.

---

## 2. Methodology

This report represents the third iteration of the Foresight Institute's hyper-entity pipeline, designated V3. The process moved through five sequential stages: extraction, deduplication, web research, scoring, and curation into tiers.

**Source extraction.** Candidate entities were extracted from 109 distinct sources hosted on or linked through Existential Hope. These fell into three categories: transcripts from the Existential Hope podcast series, submissions to the Foresight World Gallery, and essays contributed to the AI Pathways project. Extraction targeted named systems, protocols, institutions, or frameworks described as anticipated or proposed rather than fully operational.

**Deduplication.** Raw extraction produced substantial overlap, with the same concept appearing under variant names across sources. Candidates were deduplicated by concept rather than by label, collapsing near-synonyms into single entries and preserving the most descriptive name. This process reduced the candidate pool to 189 distinct entities.

**Web research.** Each deduplicated entity was researched to establish current development status, identify relevant actors, and assign a Technology Readiness Level on the standard 1–9 scale. The TRL distribution across the 189 entities skewed early-stage: 10 entities at TRL 1, 24 at TRL 2, 29 at TRL 3, 76 at TRL 4, 25 at TRL 5, 16 at TRL 6, 8 at TRL 7, and 1 at TRL 8. The modal TRL of 4 indicates that most candidates have demonstrated feasibility in laboratory or limited-context conditions but have not yet achieved validated prototypes.

**Scoring.** Each entity was scored on three dimensions. The d/acc score (0–20) assessed alignment with democratic, decentralized, defensive, and differential acceleration principles, with five points available per dimension. The transformative score (0–5) assessed potential to alter coordination, governance, or capability at civilizational scale. The actionability score (0–5) assessed whether concrete next steps exist and whether current actors can execute them. Composite scores summed d/acc and transformative dimensions. Scoring was performed by the Claude API (Anthropic) with human curation applied at the tiering and editorial stages to catch systematic errors and resolve ambiguous cases.

**Tiering.** Entities with composite scores of 14 or above were designated Tier 1 spotlight entities, yielding 19 candidates. The remaining 170 entities form the Tier 2 watch list. Twenty-seven entities appeared in both V3 and the prior V2 analysis, providing a cross-version consensus signal that was weighted positively in borderline cases. Primary bottleneck and recommended action type were assigned categorically rather than scored, based on the web research stage assessment of what currently constrains each entity's development.

---

## 3. Spotlight Entities (Tier 1)

The following 19 entities scored highest on our composite metric (d/acc alignment + transformative potential + actionability). Each represents a system that doesn't yet exist but is already shaping coordination and investment.

### Community-Governed AI Mesh Systems
**Decentralized & Democratic Institutions** | Composite: 21

Decentralized AI networks trained on locally governed data and stewarded by community trust circles rather than centralized corporate or state actors.

**How it works.** Local communities retain sovereignty over data used to train and fine-tune AI models, with governance handled by designated trust circles—particularly Indigenous and racialized community groups—operating under consent frameworks those communities define. A mesh architecture distributes both compute and decision-making authority across nodes, so no single actor controls the system. The three layers—federated learning, Indigenous data governance, and mesh networking—exist as mature separate components but have not yet been integrated into a unified operational system.

**Who's building toward this.** Flower (adap gmbh) and OpenMined (PySyft) provide production-grade federated learning infrastructure for distributed model training. The Global Indigenous Data Alliance stewards the CARE Principles, and Local Contexts supports Indigenous data sovereignty and cultural heritage protection in digital systems. Bittensor is building decentralized AI infrastructure with community-governed token incentives. No dedicated funding for an integrated system has been identified. **TRL: 4**—individual components are mature and deployed; full integration remains unbuilt.

**d/acc alignment.** This entity scores at the ceiling on Democratic (5/5) and Decentralized (5/5) dimensions, reflecting structural governance design that places decision-making authority with affected communities rather than extracting it upward. Defensive posture scores 4/5, as the architecture resists both corporate data capture and state surveillance by design.

> **What can someone do RIGHT NOW?** Convene a working group that puts Indigenous data governance leaders, federated learning developers (Flower, OpenMined), and mesh network operators in the same room to draft interoperability standards and shared governance protocols—this coordination work is the actual bottleneck, not missing technology. A funder could seed that process directly by commissioning a joint technical-governance scoping study across these currently siloed communities.

> "communities shaped by displacement, colonization, and exclusion are building decentralized, care-centered mesh networks. These relational systems are trained on locally governed data, stewarded by Indigenous and racialized trust circles, and guided by protocols rooted in consent, dignity, and interdependence—not control." — *Source: [the-living-rights-network](https://worlds.existentialhope.com/world/the-living-rights-network/)*

### Universal AI Learning UnCommons (UALU)
**Education, Development & Human Flourishing** | Composite: 20

A federated governance institution that develops, maintains, and audits AI education tools through multi-stakeholder councils including elders, learners, and ethicists.

**How it works.** UALU operates as a decentralized network of community nodes that co-create and oversee AI educational tools, with governance councils composed of elders, learners, technologists, and ethicists conducting regular audits and setting standards for bias mitigation and cultural appropriateness. The federated structure enables local adaptation while maintaining shared accountability frameworks across the network. This model addresses a documented gap: no existing institution formally integrates elder and community council oversight of AI tools with binding enforcement mechanisms.

**Who's building toward this.** Mozilla Foundation has committed $2.7M (2023) for its Responsible Computing Challenge across Kenya, India, and the US, and $1M (2025–2027) for its Democracy x AI Cohort. The African Union Commission is developing a Continental AI Strategy and Digital Education Strategy (2023–2028) through multi-stakeholder consultation. UNESCO is establishing AI ethics standards and competency frameworks for students and teachers. AIGN is developing operational AI governance frameworks for schools and universities with audit mechanisms. IDRC supports the EmpowerED initiative for responsible AI implementation in African education systems. The project sits at **TRL 3**—conceptual frameworks are mature, but no fully operational federated institution with formal elder council oversight exists at scale.

**d/acc alignment.** UALU scores highest on Democratic (5/5) and Defensive (5/5), reflecting its structural commitment to participatory oversight and harm mitigation through community-led auditing. Decentralization scores 4/5, grounded in the federated node architecture.

> **What can someone do RIGHT NOW?** A funder or institutional actor could convene a working group drawing on Mozilla, AIGN, UNESCO, and African Union representatives to design a pilot federated governance structure—the funding exists across these organizations but lacks a coordinating mechanism to integrate elder council participation with operational audit processes.

> "A federated, community-led network responsible for developing, maintaining, and auditing AI education tools. Overseen by councils including elders, learners, technologists, and ethicists to uphold justice and care." — *Source: [the-learning-uncommons-of-2035](https://worlds.existentialhope.com/world/the-learning-uncommons-of-2035/)*

### AI cryptographic oracle with zero-knowledge IoT auditing and jury-DAO
**Decentralized & Democratic Institutions** | Composite: 19

A fraud-resistance layer combining zero-knowledge proofs from IoT sensor data, AI anomaly detection, stake-slashing penalties, and a decentralized human jury for retroactive balance correction.

**How it works.** IoT devices generate zero-knowledge proofs of their sensor readings, letting a ledger verify data authenticity without exposing raw feeds that could be spoofed or fabricated. An AI layer monitors token-minting patterns for statistical anomalies, while actors caught cheating face quadratic slashing—penalties that scale super-linearly with stake size to neutralize "too-big-to-fail" manipulation. A randomly selected jury-DAO of token holders can then vote to retroactively adjust balances, placing a human override on top of automated enforcement.

**Who's building toward this.** The component stack is real but unintegrated: **RISC Zero** provides the zero-knowledge virtual machine for proof generation; **Chainlink** and **API3** supply decentralized oracle infrastructure; **Kleros** has operated a live jury-DAO since 2018, handling 1,000+ cases. Slashing mechanisms are operational in Ethereum proof-of-stake. No known funding has been identified for a fully integrated system. TRL: 4—ZK-IoT proofs demonstrated on ESP32 microcontrollers at ~700ms; full integration with AI anomaly detection and retroactive DAO adjudication has not reached production.

**d/acc alignment.** Defensive scores highest at 5/5, reflecting the system's explicit design to detect and penalize fraud at multiple layers. Democratic and Decentralized both score 4/5, driven by the jury-DAO's human override capacity and the absence of any central arbiter.

> **What can someone do RIGHT NOW?** A researcher or cryptoeconomics team could publish a formal integration specification—defining the trust boundaries, oracle assumptions, and incentive parameters needed to combine ZK-IoT proofs, AI anomaly detection, quadratic slashing, and DAO adjudication into a coherent system. A funder could convene Kleros, RISC Zero, and a blockchain ML group around a shared testnet deployment to resolve the coordination gap blocking production-scale validation.

> "A hard-fork deployed AI cryptographic oracles tied to sensor roots for zero-knowledge IoT based auditing, quadratic-stake slashing to take on 'too-big-to-fail' cheaters, and a jury-DAO to retro-adjust balances." — *Source: [hybrid-market](https://worlds.existentialhope.com/world/hybrid-market/)*

### Moral Trade
**AI-Mediated Deliberation & Collective Intelligence** | Composite: 18

A mechanism by which people or groups with different moral priorities swap concessions so that each gets more of what they care about than unilateral action would yield.

**How it works.** Moral trade applies the logic of economic exchange to ethical preferences: parties identify where their moral priorities are relatively cheap for the other side to accommodate, then negotiate exchanges that leave both better off by their own values. At civilizational scale, this could allow diverse moral communities to each achieve far more of their valued outcomes than competition or majority-rule permits, without requiring any single ethical framework to dominate. Toby Ord formalized the concept academically in 2015; informal versions already occur in activist coalition bargaining and effective altruism cause prioritization.

**Who's building toward this.** The Future of Humanity Institute and University of Oxford provided the academic home for Toby Ord's foundational theoretical work. The Effective Altruism community has explored small-scale applications through informal coordination on charitable donations across cause areas. No dedicated funding has been identified, and the concept sits at TRL 2—theorized and occasionally applied ad hoc, but without formal institutional infrastructure or governance mechanisms.

**d/acc alignment.** Moral trade scores highest on Democratic (5/5) and Decentralized (4/5) dimensions, reflecting its core design goal of enabling pluralistic coordination without imposing a dominant moral framework. Defensive and Differential scores are lower, as the concept addresses coordination rather than security or targeted acceleration.

> **What can someone do RIGHT NOW?** A researcher or funder could commission a systematic mapping of existing informal moral trade instances—across activist coalitions, international negotiations, and EA cause prioritization—to identify which coordination mechanisms succeeded and why. A builder with AI expertise could prototype a preference-elicitation and matching tool that helps parties identify low-cost concessions across moral domains, directly attacking the measurement and trust barriers that keep this at TRL 2.

> "Let's say you really care that people abstain from eating meat, and I really care about people reducing their carbon footprint. Maybe it's not much of a cost for me to eliminate meat from my diet, and it's not much of a cost for you to offset your emissions. Then we have an opportunity for a deal where I eat less meat and you reduce your carbon footprint... if you scale it up to the level of a civilization, there are huge opportunities." — *Source: [podcasts](https://www.existentialhope.com/podcasts/fin-moorhouse-why-we-need-to-aim-higher-than-survival)*

### BCI Operating System (BCI-OS)
**Neurotechnology & Brain-Computer Interfaces** | Composite: 18

An open-source operating system layer for brain-computer interfaces that embeds agency evaluation, AI model compatibility, and privacy standards as core OS-level features.

**How it works.** BCI-OS sits between BCI hardware and applications, enforcing privacy protocols and agency evaluations at the OS level rather than delegating them to individual apps. Standardized model compatibility protocols enable interoperability across hardware manufacturers. An open-source governance structure and standards body maintain human-agency principles, with academic and industry pilots iteratively refining the system.

**Who's building toward this.** OpenBCI provides open-source hardware and software platforms with community adoption but without unified privacy or agency frameworks. AE Studio is developing agency-focused BCI tools including the Neurotech Development Kit, with neuroethical principles embedded in its approach. The Future of Privacy Forum is researching BCI-specific data protection standards, and the IEEE Standards Association published a 2024 Standards Roadmap for Neurotechnologies for Machine Interfacing covering sensing, feedback, and data management. No dedicated funding for a unified BCI-OS has been identified. TRL: 3.

**d/acc alignment.** BCI-OS scores highest on Defensive (5/5) and Democratic (4/5), reflecting its core architectural commitment to protecting user agency and neural data privacy, and its open-source governance model that distributes control away from any single manufacturer.

> **What can someone do RIGHT NOW?** A funder or institution could convene a working group pulling together OpenBCI, AE Studio, IEEE, FDA representatives, and privacy researchers to draft a governance charter and interoperability specification for BCI-OS—the fragmented ecosystem is the binding constraint, not technical readiness. Hosting a structured multi-stakeholder workshop with a concrete deliverable (a draft standards framework) would directly address the coordination bottleneck.

> "['The Open Source BCI Project: Create an open-source brain-computer interface (BCI) operating system to enhance human cognitive abilities and privacy in a TAI era.', 'Develop a privacy-preserving, open-source BCI operating system (BCI-OS) that enhances human cognitive abilities and safeguards human-agency in the TAI era. Integrated agency evaluations, model compatibility protocols, and robust data privacy standards in the BCI-OS.']" — *Source: Diogo de Lucena, Judd Rosenblatt, Mamun Miah*

### Tokenized neural data sharing with selective disclosure
**Neurotechnology & Brain-Computer Interfaces** | Composite: 17

A privacy architecture for BCI systems in which neural data is tokenized so users can selectively disclose specific streams of thought or brain state while retaining others as private.

**How it works.** Rather than broadcasting all neural data, the system segments and tokenizes different categories of neural output—emotional states, motor intentions, cognitive content—allowing users to grant or revoke access to specific tokens, analogous to OAuth scopes. A user could share an emotional state with a therapist while keeping other cognitive content private. Existing healthcare privacy frameworks, including HIPAA and Montana's neuro-rights law, provide the regulatory scaffolding on which such an architecture would sit.

**Who's building toward this.** The Neurorights Foundation drives advocacy and state-level legislation for neural data privacy. The Future of Privacy Forum produces research and guidance on BCI privacy frameworks. Columbia University's Neurotechnology Center works on neurorights and data protection frameworks. No funding for this specific architecture has been documented. **TRL: 2** — regulatory concepts exist and are codified in Colorado, California, Montana, and Chile's constitutional protections, but no BCI system with tokenized selective-disclosure has been deployed or demonstrated.

**d/acc alignment.** This scores highest on Defensive (5/5) and Democratic empowerment (4/5), reflecting its core function as a user-controlled protection against involuntary neural data exposure. Decentralization scores lower (2/5) because current implementations rely on centralized regulatory and institutional frameworks.

> **What can someone do RIGHT NOW?** Policy advocates and legal researchers should push for federal technical standards that define granular consent mechanisms for neural data—without unified specifications, companies have no regulatory incentive to build tokenized architectures. Organizations with healthcare IT expertise could draft model technical standards bridging existing OAuth-style access control frameworks to BCI data streams, giving regulators concrete language to adopt.

> "I think it'll be tokenized, basically. You'll let certain parts of what you want to share out, and you'll keep what you want as your innermost thoughts to yourself. Or perhaps you'll have relationships where you wish to share your innermost thoughts." — *Source: [podcasts](https://www.existentialhope.com/podcasts/mary-lou-jepsen-a-handheld-device-to-defeat-cancer)*

### Civic Systems Co-Op
**AI Safety, Alignment & Governance** | Composite: 17

A global open-source consortium that develops and maintains ethical AI tools for municipal and community governance.

**How it works.** Member cities and communities contribute to and draw from a shared repository of AI governance tools, with the consortium setting ethical standards and maintaining transparent decision logs. Governance is distributed across member organizations rather than controlled by a single vendor or government, keeping systems adaptable to local needs. This cooperative model sits between the proprietary vendor approach (OpenGov's 2,000+ community platform) and loose federated registries like the Digital Public Goods Alliance.

**Who's building toward this.** The **Digital Public Goods Alliance** (UN-endorsed) maintains a registry of 150+ open-source governance solutions and provides the closest structural analog to a coordinating body. The **Open Government Partnership** promotes transparency and accountability frameworks across local and national governments. **OpenGov** demonstrates commercial viability with AI-enabled tools for budgeting, permitting, and public engagement across 2,000+ US communities. The **Open Knowledge Foundation** develops open-source standards and civic tech tools as a DPGA member. No dedicated funding for a unified consortium has been identified. TRL: 5 — field-tested components exist, but a true cooperative with distributed member control remains at prototype stage.

**d/acc alignment.** Democratic (4/5), Decentralized (4/5), and Defensive (4/5) scores are all strong, reflecting the model's emphasis on distributed control, member accountability, and protection against vendor lock-in. Differential impact scores lower (2/5) because the mechanism operates within civic tech rather than across multiple domains.

> **What can someone do RIGHT NOW?** A foundation or civic technology funder could convene the Digital Public Goods Alliance, Open Government Partnership, and two or three member cities to draft a formal consortium charter and contribution model, directly addressing the coordination gap that prevents existing fragmented initiatives from coalescing. A researcher could map interoperability requirements across current municipal AI deployments to define the technical baseline a shared repository would need to meet.

> "The Civic Systems Co-Op: a global open-source consortium maintaining ethical, adaptable AI systems for cities and communities." — *Source: [the-commons-cloud](https://worlds.existentialhope.com/world/the-commons-cloud/)*

### Interbeing Forum
**Decentralized & Democratic Institutions** | Composite: 17

A rotating bioregional assembly that grants formal representation to ecosystems and future generations through human guardians advised by digital twin data.

**How it works.** Stewards selected on a rotating basis from bioregions govern through a binding accord, preventing any single faction from entrenching power. Designated guardians speak for non-human entities—rivers, soils—and for future generations, with their positions informed by real-time ecological data from digital twin systems. The assembly also audits that digital infrastructure directly, ensuring it remains a tool of democratic participation rather than centralized control.

**Who's building toward this.** bioregional.agency (Austria, co-founded 2025 by Gordon Selbach and Jakob Travnik) is piloting bioregional assembly practices; Resilience.Earth is developing distributed decision-making and adaptive governance tools for bioregional communities; Department of Bioregion / CascadiaNow! has advanced bioregional education across the Cascadia region since 2005; and the Ozark Area Community Congress has operated a rotating, consensus-based bioregional assembly in the Ozarks since 1980. No dedicated funding has been identified for the integrated Interbeing Forum model. TRL: 3—component precedents exist, but no institution yet combines rotating bioregional representation, ecosystem guardianship, and digital twin advisory in a single body.

**d/acc alignment.** Democratic and Decentralized dimensions both score 4/5, reflecting the rotating stewardship structure and formal power-sharing across bioregions that structurally resists capture. Differential scores lowest (2/5), as the model does not yet create new civilizational action space beyond the governance domain.

> **What can someone do RIGHT NOW?** Legal advocates and policy researchers should work to establish or extend ecosystem legal personhood frameworks—building on New Zealand's Whanganui River precedent and Wales's Future Generations Commissioner—into cross-jurisdictional bioregional contexts. Connecting existing practitioners (OACC, bioregional.agency) with environmental digital twin researchers would accelerate the governance integration that no institution has yet achieved.

> "The Interbeing Forum is a rotating assembly of stewards from across bioregions. It includes people, yes, but also guardians (advised by digital twins) for rivers, soils, and future generations. It oversees the Commonsense Accord and safeguards the integrity of the digital twin ecosystem." — *Source: [the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences](https://worlds.existentialhope.com/world/the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences/)*

### Interoperable Governance Protocol Stack
**Decentralized & Democratic Institutions** | Composite: 16

A shared technical and governance protocol layer that allows citizens to port digital identities, benefits, and credentials across distinct federated city-state systems, and enables AI systems across those jurisdictions to align resource allocation and crisis modeling.

**How it works.** The protocol stack defines common standards for digital identity, benefits entitlements, and credentials so that any compliant local system can read and honor records issued by another. During crises, federated AI systems across jurisdictions share resource allocation decisions, risk assessments, and logistics data in a machine-readable, interoperable format. Governance modules are deliberately modular, allowing jurisdictions to adopt the stack without surrendering local policy autonomy while the protocol layer handles translation between differing local implementations.

**Who's building toward this.** The **OpenID Foundation** is developing OpenID for Verifiable Credentials interoperability specifications, with a real-world multi-region demonstration completed in May 2025. **W3C** maintains the Decentralized Identifiers (DIDs) and Verifiable Credentials standards that form the identity backbone. The **Trust Over IP Foundation** is developing governance frameworks for decentralized digital trust infrastructure, and **GovStack** is assembling modular government digital building blocks covering identity, payments, and data exchange. No dedicated funding for the integrated stack has been identified. TRL: 4 — core identity standards are in production pilots across the EU, UK, Switzerland, Japan, and California, but the combined benefits-portability-plus-AI-crisis-coordination system remains at prototype stage.

**d/acc alignment.** Decentralized (4/5) and Defensive (4/5) are the strongest dimensions: the modular architecture preserves jurisdictional autonomy while the crisis coordination capability directly reduces harm from disasters. Democratic alignment (3/5) reflects meaningful but incomplete citizen-facing benefits, and Differential (2/5) is low because the underlying technologies are established rather than frontier.

> **What can someone do RIGHT NOW?** Convene a working group that brings together municipal governments, standards bodies, and emergency management agencies to draft a model mutual-recognition agreement for cross-jurisdictional verifiable credentials — starting with a bilateral pilot between two willing cities. Engaging regulators early to establish shared legal frameworks for benefits eligibility translation is the single highest-leverage action given that regulatory fragmentation, not technical readiness, is the primary bottleneck.

> "A coalition of federated city-states launches the first interoperable governance protocol stack, allowing citizens to carry digital IDs, benefits, and credentials between different local systems. When severe flooding hits multiple jurisdictions, modular governance systems coordinate relief in hours instead of weeks, sharing resources and logistics seamlessly across local and regional levels." — *Source: N/A*

### Comprehensive AI Services (Drexler)
**AI Safety, Alignment & Governance** | Composite: 16

An architecture of many narrow, domain-limited superhuman AIs that interact competitively rather than a single general superintelligence, achieving safety through structural narrowness.

**How it works.** Rather than building one general-purpose superintelligent system, AI capabilities are deliberately partitioned into domain-specific services that are superhuman within their lane but architecturally prevented from generalizing beyond it. The resulting ecology of competing specialized systems provides checks analogous to market competition or ecological balance, making unilateral takeover or unexpected generalization structurally difficult. Crucially, safety is not achieved through alignment of a single powerful agent but through the architecture itself.

**Who's building toward this.** No organization is deliberately implementing CAIS as a unified design paradigm. The Future of Humanity Institute at the University of Oxford published Drexler's foundational 2019 technical report, *Reframing Superintelligence*, which remains the primary articulation of the framework. Individual narrow superhuman AIs—AlphaFold, chess engines—demonstrate isolated components, but without architectural enforcement of narrowness or a competitive service ecology. No dedicated funding has been identified. TRL: 2.

**d/acc alignment.** CAIS scores highest on Decentralized (4/5) and Defensive (4/5), reflecting its structural resistance to power concentration and its safety-by-design approach. The low Differential score (2/5) reflects the absence of any implementation pathway that would accelerate this approach relative to general-purpose foundation models.

> **What can someone do RIGHT NOW?** A researcher or funder could commission formal technical work on the core unsolved problem: whether service composition across domain-limited AIs can be architecturally bounded to prevent emergent generalization. A policy advocate could draft a regulatory proposal requiring capability partitioning disclosures for frontier model developers, creating the coordination infrastructure the CAIS model currently lacks entirely.

> "It's safety through narrowness. It's not to say that the AIs aren't really good at what they do—they could be superhuman at what they do—but in the same way that we have superhuman chess players that can only play chess, and we have superhuman protein folding AIs that can only fold protein, you don't really have to worry that that's going to do something surprising... I think that would be a really good design decision if we could manage it: to have AIs that are potentially superhuman in their domain but are in a pretty fundamental way limited to their domain so they don't do an end-run around whatever guardrails we've put in place." — *Source: [podcasts](https://www.existentialhope.com/podcasts/nathan-labenz-what-are-the-best-case-scenarios-for-ai)*

### Attack Dog DAO for Climate
**Ecological & Regenerative Systems** | Composite: 16

A DAO that funds and coordinates environmental litigation on behalf of legally-recognized natural entities, financed through tokenized litigation investment.

**How it works.** Natural bodies granted legal personhood—rivers, lakes—become plaintiffs in lawsuits against polluters. A DAO pools capital from investors through tokenized litigation finance mechanisms, funding those cases and returning proceeds to investors when litigation succeeds. This creates a direct market incentive to deter environmental harm: profit motive and ecological protection become structurally aligned.

**Who's building toward this.** No single organization has assembled all three components, but adjacent work is underway. **Ryval** pioneered tokenized litigation finance via Initial Litigation Offerings on blockchain, completing its first ILO in October 2021. **LawCoin** tokenizes litigation finance deals on Ethereum for institutional investors. **MediCoin** has tokenized attorney fee interests specifically in environmental litigation, including PFAS cases. **ClientEarth**, the environmental law firm, has inspired litigation finance focused on climate cases through Aristata Capital. No known entity has combined environmental personhood, DAO governance, and tokenized litigation finance into a deployed system. TRL: 3. Funding: none identified for an integrated implementation.

**d/acc alignment.** The concept scores highest on democratic distribution (4/5) and defensive posture (4/5)—it distributes access to legal enforcement mechanisms and directly counters harmful actors—while decentralization is constrained (3/5) by guardian bottlenecks and DAO liability exposure under current law.

> **What can someone do RIGHT NOW?** Advocates and legal scholars should push for standardized environmental personhood frameworks across jurisdictions and clarity on DAO liability structures—these are the blocking conditions, not engineering gaps. Engaging securities regulators on the classification of tokenized litigation interests would directly unblock retail investor participation and cross-border enforcement.

> "One approach is creating an attack dog DAO (Decentralized Autonomous Organization) for climate, similar to the Electronic Frontier Foundation but focused on environmental issues. This DAO could sue on behalf of natural bodies, like rivers or lakes, that have been granted legal personhood. It would leverage litigation finance, where people can invest in these legal battles." — *Source: [podcasts](https://www.existentialhope.com/podcasts/trent-mcconaghy-from-starships-to-tokens-pioneering-futures)*

### Wisdom DAO
**Decentralized & Democratic Institutions** | Composite: 16

A decentralized autonomous organization where human citizens and AI systems jointly propose, deliberate, and vote on governance policy using weighted voting and blockchain transparency.

**How it works.** Citizens use personal AI assistants (Citizen-AI) to parse proposals and cast informed votes recorded on a blockchain ledger. A Wisdom Aggregator AI synthesizes inputs across the participant pool into coherent policy recommendations, which humans then ratify. Smart contracts enforce decisions automatically, removing discretionary points where corruption typically enters.

**Who's building toward this.** Near Foundation is developing AI-powered delegates and the Pulse sentiment-tracking tool for DAO governance. SingularityNET operates a decentralized AI coordination platform using blockchain for service governance and privacy-preserving datasets. Aragon provides DAO infrastructure and tooling, while MakerDAO demonstrates on-chain token-based governance at meaningful scale. No dedicated funding for integrated human-AI hybrid governance DAOs has been identified. **TRL: 4** — AI agents have been tested against 3,383 real proposals with 97% alignment to historical human decisions, and simulations show a 40% participation increase, but no production deployment at city or national scale exists.

**d/acc alignment.** Democratic (4/5) and Decentralized (4/5) are the strongest dimensions, reflecting the system's core design: distributed decision-making authority shared between citizens and AI rather than concentrated in bureaucratic institutions. Defensive scores lower (3/5) because the system's resilience against manipulation and adversarial voting remains unproven at scale.

> **What can someone do RIGHT NOW?** Researchers should publish comparative studies of existing DAO governance pilots—particularly Near Foundation's Pulse deployments—to build the empirical record regulators need to draft workable legal frameworks. Policy advocates should engage directly with EU AI Act implementation bodies and NIST to push for explicit guidance on AI-assisted voting systems before legal ambiguity freezes further development.

> "Wisdom DAO – Citizens & AIs co-create policy. By 2035, governance shifted from centralized bureaucracy to decentralized wisdom guided by Sadvipra AI and DAOs. People co-create policy with personal AIs, corruption drops through blockchain transparency, and decisions align with dharma." — *Source: [worldbuilding-course-worldbuilding-toolbox-world-entry-page-world-gallery-x-twitter-instagram-medium-bookmark-sadvipra-ai](https://worlds.existentialhope.com/world/worldbuilding-course-worldbuilding-toolbox-world-entry-page-world-gallery-x-twitter-instagram-medium-bookmark-sadvipra-ai/)*

### Accord of Watersheds
**International Governance & Coordination** | Composite: 16

An international treaty framework that organizes political cooperation around watershed and bioregional boundaries rather than national borders.

**How it works.** Signatory parties—nations, Indigenous governments, and regional bodies—agree to coordinate resource use, conservation, and conflict resolution according to the boundaries and health of shared watersheds. Governance bodies are constituted around river basins or bioregions, with binding obligations tied to ecological indicators rather than national interest. Dispute resolution and resource allocation follow hydrological logic: the river basin, not the border, determines jurisdiction.

**Who's building toward this.** The **International Joint Commission (IJC)** has operated transboundary watershed governance between Canada and the US since 1909, with its International Watersheds Initiative (est. 1998) pioneering ecosystem-centered management with Indigenous participation. The **Mekong River Commission (MRC)** coordinates four nations using integrated water resources management across the Mekong Basin. The **International Network of Basin Organizations (INBO)** supports 120+ river basin organizations globally. The **Cascadia Department of Bioregion** is developing bioregional governance frameworks across the Pacific Northwest, while **Resilience.Earth** delivers bioregional governance training in Asia-Pacific. No dedicated funding for a unified treaty framework has been identified. TRL: 6—operational regional structures exist, but a binding global framework remains conceptual.

**d/acc alignment.** Scores highest on democratic inclusion (4/5) and defensive orientation (4/5), reflecting its emphasis on multi-stakeholder governance and ecological protection over extractive national interest. Decentralization scores moderate (3/5) because watershed bodies, while sub-national in logic, still require centralized treaty architecture to function.

> **What can someone do RIGHT NOW?** Legal advocates and international law scholars can draft model treaty language that converts existing watershed commission frameworks—IJC, MRC—into a replicable binding instrument with enforceable ecological indicators. Policy advocates with access to UN Environment Assembly or CBD processes should push for a formal resolution recognizing bioregional governance as a legitimate basis for transboundary treaty obligations.

> "The Accord of Watersheds—a treaty system where ecosystems, not nations, are the organizing principle of cooperation." — *Source: [2035-rewild](https://worlds.existentialhope.com/world/2035-rewild/)*

### DAO-governed open innovation platform for TLM documentation and training data
**Decentralized & Democratic Institutions** | Composite: 16

A DAO-based governance structure that mandates open-source documentation and community-sourced feedback loops for translation model development and adaptation.

**How it works.** Smart-contract-based voting gives communities formal decision-making power over how translation language model (TLM) training data is collected, labeled, and updated. Open innovation platforms serve as the interface for submitting feedback, flagging bias, and proposing model adaptations. Governance rules enforced through the DAO prevent proprietary capture, keeping models and documentation publicly accessible.

**Who's building toward this.** No single organization has yet integrated all components at production scale, but several are building the necessary infrastructure. Hugging Face hosts over 1,000 community-contributed translation models (TRL 4–5). Mozilla Common Voice crowdsources multilingual voice data through community-driven collection (TRL 4). Ocean Protocol provides decentralized data exchange with DAO governance and tokenized data assets (TRL 3–4). Aragon supplies DAO governance frameworks and is exploring AI-DAO integration. No dedicated funding for the integrated system has been identified. Overall TRL: 3.

**d/acc alignment.** Democratic (4/5) and Decentralized (4/5) are the strongest dimensions, reflecting the core design intent to distribute control over model development away from proprietary actors and toward affected communities. Defensive scores lower (3/5) because the system's protective value depends on successful implementation that has not yet been demonstrated at scale.

> **What can someone do RIGHT NOW?** Convene a working group that brings together Hugging Face contributors, Ocean Protocol governance participants, and multilingual community organizations to design and pilot a DAO governance layer specifically for a production translation model — starting with a bounded language pair to test coordination mechanisms before scaling. A funder could seed this pilot by commissioning a governance design sprint that maps smart-contract voting to concrete model update decisions.

> "Decentralized Autonomous Organizations (DAOs) ensure open access to TLM documentation and training data so that communities drive decision-making on model adaptations. Open innovation platforms source community feedback to further transparency and interoperability." — *Source: [la-langue-de-la-prvoyance](https://worlds.existentialhope.com/world/la-langue-de-la-prvoyance/)*

### Watershed Parliaments
**Decentralized & Democratic Institutions** | Composite: 16

Bioregional governance bodies organized around watershed boundaries rather than political borders, incorporating ecological feedback into formal decision-making.

**How it works.** Governance jurisdiction is defined by hydrological catchment areas, replacing nation-state and municipal lines with boundaries that match the actual movement of water and the ecosystems it sustains. Decision-making bodies include designated representatives for ecosystem interests alongside human citizens. Before adoption, proposals must pass multi-generational impact assessments covering all species within the watershed.

**Who's building toward this.** The **Murray-Darling Basin Authority** (Australia) manages integrated water resources across a major watershed with Indigenous representation and multi-stakeholder governance. The **Susquehanna River Basin Commission** and **Interstate Commission on the Potomac River Basin** coordinate water management across multi-state jurisdictions in North America. The **Cascadia Department of Bioregion** advocates for watershed-based political restructuring. New Zealand's Whanganui River, granted legal personhood in 2017, remains the clearest proof-of-concept for ecosystem rights integration. No dedicated funding was identified. TRL: 4 — operational governance structures exist at watershed scale, but full ecosystem representation and multi-generational impact assessment mechanisms remain largely theoretical.

**d/acc alignment.** Watershed Parliaments score highest on Democratic (4/5) and Defensive (4/5), reflecting their potential to distribute political power along ecological lines and build long-term resilience against resource conflicts. Decentralization scores lower (3/5) because existing implementations remain embedded within nation-state structures rather than replacing them.

> **What can someone do RIGHT NOW?** Advocates and legal scholars can work to expand the Whanganui River legal personhood model into binding governance frameworks in other jurisdictions, building the regulatory precedents that watershed parliaments require. Researchers can document and compare existing river basin commissions to identify which governance features are most transferable to full bioregional authority structures.

> "Watershed Parliaments replace geopolitical boundaries with bioregional governance aligned with natural water systems. These institutions integrate human decision-making with ecological feedback, where voting rights extend to ecosystem representatives and decisions must demonstrate positive impacts across seven generations of all life forms within the watershed." — *Source: [mycelial-democracy](https://worlds.existentialhope.com/world/mycelial-democracy/)*

### Digital Twins for Communities and Ecosystems
**AI-Mediated Deliberation & Collective Intelligence** | Composite: 16

Real-time digital models of communities and ecosystems that enable participatory future simulation with locally-owned data.

**How it works.** Sensor networks and continuous data feeds update digital models of local ecological and social conditions, allowing stakeholders to run simulations of policy or environmental decisions before implementing them. Critically, communities retain ownership of their data rather than ceding it to centralized platforms. Outputs can inform governance bodies, including representatives for non-human entities such as rivers.

**Who's building toward this.** The **Singapore Land Authority** built Virtual Singapore, the first country-scale urban digital twin, operational since 2022 following a $73M investment over 2012–2017. The **Alan Turing Institute** is developing methodology for scalable digital twin ecosystems and national digital twin infrastructure. **Northeastern University's Boston Area Research Initiative (BARI)** is building Fora.ai, a participatory modeling platform for community-led digital twins in green infrastructure planning. **The Nature Conservancy and Esri** are developing environmental digital twins for ecosystem monitoring, including the Point Conception project. TRL sits at 5: urban digital twin components are mature, but participatory governance integrated with community data sovereignty at scale remains in prototype phase.

**d/acc alignment.** This entity scores highest on democratic (4/5) and defensive (4/5) dimensions, reflecting its potential to distribute simulation capacity to communities and reduce harm from uninformed governance decisions. Decentralization scores 3/5 because data sovereignty frameworks and community-owned infrastructure remain partially realized rather than structurally embedded.

> **What can someone do RIGHT NOW?** Convene a working group that connects existing digital twin operators (urban planning, ecological monitoring), data sovereignty practitioners (Indigenous data governance initiatives, GDPR implementers), and community organizations already using participatory planning tools—the component technologies exist and the primary gap is institutional coordination to integrate them. Funding a structured pilot that combines Fora.ai-style participatory modeling with a community data ownership agreement and an operational sensor network would move this from conceptual integration to demonstrated production system.

> "Digital twins reflect the real-time state of communities and ecosystems. They help people simulate futures, explore consequences, and make decisions guided by care, memory, and shared responsibility. Every community and citizen holds its own data as a form of digital sovereignty." — *Source: [the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences](https://worlds.existentialhope.com/world/the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences/)*

### Loyal AI Assistance (Fiduciary AI Assistance)
**AI Safety, Alignment & Governance** | Composite: 15

A personal AI system explicitly designed to serve the individual user's goals rather than platform or advertiser interests — functioning more like a fiduciary than a product.

**How it works.** A loyal AI assistant would know the user deeply enough to genuinely assist rather than manipulate, with no third-party incentives embedded in its objective function. Unlike Siri or Alexa, which are structurally oriented toward platform revenue and data monetization, a fiduciary AI would operate under a duty of loyalty and care analogous to legal fiduciary relationships. The same architecture could scale from helping individuals navigate everyday information dynamics to assisting researchers with complex scientific problems.

**Who's building toward this.** The Montreal AI Ethics Institute has developed research and design frameworks for fiduciary AI systems. Consumer Reports Innovation is exploring personal AI agents operating under fiduciary duty principles. The Alignment Research Center contributes relevant user-centric alignment research. No dedicated external funding has been documented. **TRL 3** — published design methodologies and legal frameworks exist, but no commercial deployment has occurred.

**d/acc alignment.** Scores highest on Democratic control (4/5) and Defensive posture (4/5), reflecting its core purpose of returning AI agency to individuals and protecting users from manipulative system design. Decentralization and differential acceleration scores are weaker (2/5 each), as the concept does not inherently restructure AI infrastructure or accelerate capabilities differentially.

> **What can someone do RIGHT NOW?** Legal scholars, policy advocates, and AI governance organizations should push for regulatory frameworks that define and enforce fiduciary duty standards for AI assistants — this is the explicit gating factor for commercial adoption. Connecting existing legal instruments like UETA to AI agent accountability, and building coalitions that pressure regulators to establish compliance mechanisms, would move this from research artifact to deployable standard.

> "One of the things that came out of the augmented intelligence summit was fiduciary AI assistance. I have been calling them loyal AI assistance. There is a loyal AI system that doesn't have selfish interests and works to advance your goals and interests." — *Source: [podcasts](https://www.existentialhope.com/podcasts/anthony-aguirre-anna-yelizarova-on-worldbuilding)*

### The Global Deliberation Coordinator
**AI-Mediated Deliberation & Collective Intelligence** | Composite: 15

A platform institution designed to coordinate global deliberative processes and collective decision-making specifically around AI governance.

**How it works.** The institution establishes structured coordination infrastructure that convenes global stakeholders—states, civil society, technical experts—for deliberative discussions on AI governance, enabling collective decisions that cross national and organizational boundaries. Unlike existing expert bodies, the model centers inclusive participation and deliberative legitimacy rather than top-down technical guidance. AI tools support multilingual, asynchronous deliberation at scale across time zones and cultures.

**Who's building toward this.** The **UN Global Dialogue on AI Governance** (launched August 2025) provides the most operational foundation, offering an inclusive state-and-stakeholder platform. **AI4Deliberation** (Horizon Europe, €2,999,500) is building AI-enabled deliberative toolkits for governments. **Connected by Data** is researching independent global assembly designs for AI governance. **AI & Democracy Foundation** focuses on deliberative processes for AI alignment. **Metagov** develops digital self-governance infrastructure. TRL sits at 4: pilots are proven, but no unified global coordination architecture exists yet.

**d/acc alignment.** Democratic (4/5) and Defensive (4/5) are the strongest dimensions—this entity directly addresses who gets a voice in AI governance decisions and builds resilience against unilateral capture of those decisions. Decentralized and Differential scores (2/5 each) reflect that coordination infrastructure, by design, requires some centralization.

> **What can someone do RIGHT NOW?** Use the UN Global Dialogue on AI Governance as a convening anchor: fund Connected by Data or Metagov to translate their global assembly design research into a concrete coordination architecture proposal, then pressure-test it with delegations from the 118 currently excluded countries before the next major AI governance summit.

> "The Global Deliberation Coordinator (Hackathon shared second place): Focuses on establishing a platform for global discussions and decision-making on AI and other pressing issues." — *Source: N/A*

### Epistemic stack
**Scientific Research & Knowledge Infrastructure** | Composite: 14

A citation and provenance system for all information—from newspaper articles to social media claims—that lets users trace any assertion back to its raw data sources, with trust scores based on historical accuracy of each link in the chain.

**How it works.** Every piece of information carries machine-readable provenance metadata linking it to its source, analogous to academic citations but applied universally. AI tools help users traverse this chain from a high-level claim down to raw data, which can be cryptographically signed by hardware secure enclaves. Each node in the chain—person, outlet, inference step—accumulates a reliability record based on past accuracy, giving users a principled basis for assessing any given claim.

**Who's building toward this.** The Coalition for Content Provenance and Authenticity (C2PA) released its open technical standard in 2022, with adoption now spanning camera makers, news outlets, and platforms. The Content Authenticity Initiative (CAI) develops open-source tooling within that coalition. X's Community Notes operates crowdsourced fact-checking at scale with 133,000+ contributors. Numbers Protocol integrates C2PA provenance data with blockchain for immutable asset tracking. No dedicated funding for a unified epistemic stack has been identified. TRL: 4—components exist in isolation; end-to-end integration from raw sensor data through inference to published claims with per-node trust scoring remains unbuilt.

**d/acc alignment.** Defensive scores highest (4/5) because accurate provenance directly counters manipulation and misinformation at the infrastructure level. Democratic scores 3/5, reflecting the system's potential to equalize access to source-level verification across users and institutions.

> **What can someone do RIGHT NOW?** Convene a working group spanning C2PA, academic citation graph projects, and platform trust-and-safety teams to define a shared metadata schema that bridges media provenance, inference-step logging, and per-node accuracy scoring. The core bottleneck is coordination, not technology—a funded convening body with a concrete interoperability mandate could close the gap between existing partial implementations faster than any single technical project.

> "There is no reason why, when reading a newspaper article about something, you shouldn't be able to trace back: where did that quote come from, or where did this piece of information come from? How do I know whether to trust this?... We should be able to have a stack we can follow all the way from the high level back down to the raw ingredients, and then figure out how much we trust each of those steps." — *Source: [podcasts](https://www.existentialhope.com/podcasts/anthony-aguirre-tools-or-agents-choosing-our-ai-future)*


---

## 4. Watch List (Tier 2)

The remaining 170 entities form the watch list — systems worth tracking but not yet meeting the composite score threshold for spotlight treatment.

| Name | Group | d/acc | Trans. | Bottleneck | Action | TRL |
|------|-------|-------|--------|------------|--------|-----|
| AI Fiduciaries | AI Safety, Alignment & Governance | 17/20 | 3/5 | Coordination | Convene | 5 |
| Liberal/Popperian AGI Education Framework | AI Safety, Alignment & Governance | 15/20 | 4/5 | Physics | Research | 1 |
| Privacy-Preserving Global Regulatory Markets for AI Verif... | AI Safety, Alignment & Governance | 16/20 | 3/5 | Coordination | Convene | 3 |
| LexNodes | Decentralized & Democratic Institutions | 16/20 | 3/5 | Regulation | Advocate | 4 |
| Viotopia | Education, Development & Human Flouri... | 13/20 | 4/5 | Coordination | Research | 1 |
| Continuity Guild | Education, Development & Human Flouri... | 15/20 | 2/5 | Coordination | Convene | 5 |
| BioEcho Mesh | Ecological & Regenerative Systems | 14/20 | 2/5 | Coordination | Convene | 6 |
| Cognitive Field Resonators (CFRs) | Scientific Research & Knowledge Infra... | 15/20 | 1/5 | Physics | Research | 1 |
| The Mnemosyne Assembly | AI Safety, Alignment & Governance | 13/20 | 3/5 | Coordination | Convene | 3 |
| Translation Language Models (TLMs) with citizen-owned tra... | AI-Mediated Deliberation & Collective... | 13/20 | 3/5 | Coordination | Build | 4 |
| Open Cognition Ledger | Decentralized & Democratic Institutions | 13/20 | 3/5 | Coordination | Convene | 4 |
| Polymesh Civic Ledger | Decentralized & Democratic Institutions | 13/20 | 3/5 | Coordination | Research | 4 |
| Living Rights Network | Decentralized & Democratic Institutions | 13/20 | 3/5 | Coordination | Convene | 4 |
| The Collective of Inner Weavers | AI Safety, Alignment & Governance | 13/20 | 3/5 | Funding | Fund | 4 |
| Federated Procurement Platforms | Economic Systems & Resource Distribution | 13/20 | 2/5 | Coordination | Convene | 5 |
| contextual autonomy | AI Safety, Alignment & Governance | 12/20 | 3/5 | Coordination | Convene | 4 |
| Publishing for Machines (machine-readable scientific publ... | Scientific Research & Knowledge Infra... | 12/20 | 3/5 | Social Acceptance | Convene | 4 |
| De novo designed universal flu vaccines (Neil King / Bake... | Biotech, Medicine & Life Extension | 12/20 | 3/5 | Regulation | Advocate | 6 |
| Computational models for infectious disease spread and va... | Biotech, Medicine & Life Extension | 12/20 | 3/5 | Coordination | Convene | 7 |
| AI-Democratic Institutions for Decentralized Governance | Decentralized & Democratic Institutions | 12/20 | 3/5 | Social Acceptance | Research | 4 |
| Crowdfunded Independent Longevity AI Research Program | Nanotechnology & Advanced Manufacturing | 13/20 | 2/5 | Coordination | Convene | 4 |
| Hybrid Market impact bond ledger | Economic Systems & Resource Distribution | 12/20 | 3/5 | Regulation | Advocate | 5 |
| Isolated Societies Research Institute | Scientific Research & Knowledge Infra... | 13/20 | 2/5 | Funding | Research | 3 |
| Mandatory Open-Source AI Release Policy | AI Safety, Alignment & Governance | 12/20 | 3/5 | Regulation | Advocate | 2 |
| Loom Studios | Decentralized & Democratic Institutions | 12/20 | 3/5 | Coordination | Research | 4 |
| The Common Knowledge Generator | Scientific Research & Knowledge Infra... | 12/20 | 3/5 | Coordination | Convene | 4 |
| The Delphi Collaboration Protocol | AI-Mediated Deliberation & Collective... | 13/20 | 2/5 | Coordination | Build | 4 |
| The Scenario Planning Institution | AI Safety, Alignment & Governance | 12/20 | 3/5 | Coordination | Convene | 4 |
| Flourishing Certification | Education, Development & Human Flouri... | 12/20 | 3/5 | Coordination | Convene | 3 |
| TAI Horizon Scanner | AI Safety, Alignment & Governance | 12/20 | 3/5 | Coordination | Convene | 4 |
| Lean FRO (interactive theorem proving infrastructure for ... | Scientific Research & Knowledge Infra... | 11/20 | 3/5 | Engineering | Build | 6 |
| Large-scale AI-mediated deliberation system | AI-Mediated Deliberation & Collective... | 11/20 | 3/5 | Engineering | Build | 5 |
| Reputational Market | Economic Systems & Resource Distribution | 11/20 | 3/5 | Coordination | Research | 3 |
| Learning Observatories | AI Safety, Alignment & Governance | 11/20 | 3/5 | Coordination | Convene | 4 |
| Deep Fision borehole nuclear reactor | Energy, Environment & Planetary Systems | 11/20 | 3/5 | Regulation | Build | 4 |
| Values-as-modality parametrization across AI systems | AI Safety, Alignment & Governance | 11/20 | 3/5 | Coordination | Research | 2 |
| Parallel lightly-regulated childminder category (France) | Education, Development & Human Flouri... | 12/20 | 2/5 | Regulation | Research | 7 |
| Orare - AI-powered Futarchy governance system | AI-Mediated Deliberation & Collective... | 11/20 | 3/5 | Social Acceptance | Advocate | 4 |
| VOICE (Voice for Open Source Information and Community En... | AI-Mediated Deliberation & Collective... | 11/20 | 3/5 | Social Acceptance | Research | 4 |
| Global Personhood Token / Trust-of-Personhood Standard | International Governance & Coordination | 11/20 | 3/5 | Regulation | Advocate | 6 |
| LexCommons | Decentralized & Democratic Institutions | 12/20 | 2/5 | Regulation | Research | 5 |
| The Welcome Circle | Education, Development & Human Flouri... | 12/20 | 2/5 | Coordination | Convene | 2 |
| RaízMental Global | Biotech, Medicine & Life Extension | 11/20 | 3/5 | Regulation | Convene | 4 |
| Ethical AI Tutors | Education, Development & Human Flouri... | 11/20 | 3/5 | Coordination | Convene | 5 |
| Safety-Netted DAOs | Decentralized & Democratic Institutions | 11/20 | 2/5 | Engineering | Build | 2 |
| AGI Liability Safe Harbor Framework | AI Safety, Alignment & Governance | 10/20 | 3/5 | Regulation | Research | 1 |
| Multiplicity.ai | AI-Mediated Deliberation & Collective... | 11/20 | 2/5 | Engineering | Build | 7 |
| Futarchy | Decentralized & Democratic Institutions | 10/20 | 3/5 | Social Acceptance | Build | 4 |
| Active smart fabric with autonomous environmental response | Nanotechnology & Advanced Manufacturing | 11/20 | 2/5 | Engineering | Research | 3 |
| Integration of Brain Preservation into the Medical System | Biotech, Medicine & Life Extension | 11/20 | 2/5 | Regulation | Advocate | 3 |
| Imagination Annotated (book series) | Education, Development & Human Flouri... | 11/20 | 2/5 | Coordination | Convene | 6 |
| Author Personal Knowledge Graph / Writing Corpus Utility | Scientific Research & Knowledge Infra... | 11/20 | 2/5 | Engineering | Build | 5 |
| Artificial General Wisdom | AI Safety, Alignment & Governance | 10/20 | 3/5 | Coordination | Research | 2 |
| Componentized architectures optimized for inner alignment... | AI Safety, Alignment & Governance | 10/20 | 3/5 | Coordination | Research | 2 |
| Neighborhood opt-in upzoning with land value capture | Decentralized & Democratic Institutions | 11/20 | 2/5 | Regulation | Research | 4 |
| Kacha's Global Symbiosis Council (GSC) | International Governance & Coordination | 10/20 | 3/5 | Coordination | Convene | 4 |
| Guardian Network | International Governance & Coordination | 11/20 | 2/5 | Coordination | Convene | 4 |
| Decentralized community-built AI systems | Decentralized & Democratic Institutions | 10/20 | 3/5 | Coordination | Convene | 5 |
| Bio-Responsive AI Interfaces | Neurotechnology & Brain-Computer Inte... | 11/20 | 2/5 | Coordination | Convene | 4 |
| Open-source AI-powered research funding and knowledge pla... | Scientific Research & Knowledge Infra... | 10/20 | 3/5 | Regulation | Advocate | 4 |
| Interplanetary Cooperative | International Governance & Coordination | 11/20 | 2/5 | Regulation | Advocate | 2 |
| Civic Loom | AI-Mediated Deliberation & Collective... | 11/20 | 2/5 | Coordination | Research | 5 |
| AI-powered participatory policy simulation platform | AI-Mediated Deliberation & Collective... | 10/20 | 3/5 | Social Acceptance | Convene | 5 |
| The Flourishing Foundation | Education, Development & Human Flouri... | 11/20 | 2/5 | Regulation | Advocate | 5 |
| The Evals for Evals Institute | AI Safety, Alignment & Governance | 10/20 | 3/5 | Coordination | Convene | 3 |
| The World Convention on Transformative Artificial Intelli... | International Governance & Coordination | 11/20 | 2/5 | Coordination | Convene | 4 |
| Global Deliberation as a Service (GDaaS) | AI-Mediated Deliberation & Collective... | 10/20 | 3/5 | Coordination | Convene | 4 |
| World Convention on Transformative Artificial Intelligenc... | International Governance & Coordination | 10/20 | 3/5 | Coordination | Research | 2 |
| Tool AI for Tool AI | AI Safety, Alignment & Governance | 9/20 | 3/5 | Engineering | Build | 4 |
| NotADoctor.ai medical record serialization and RCT search | Biotech, Medicine & Life Extension | 10/20 | 2/5 | Engineering | Research | 6 |
| AI-mediated conflict resolution tool (retorsion/disgorgem... | AI-Mediated Deliberation & Collective... | 10/20 | 2/5 | Regulation | Research | 4 |
| Aviary | Scientific Research & Knowledge Infra... | 10/20 | 2/5 | Social Acceptance | Build | 6 |
| Windfall Clause | Economic Systems & Resource Distribution | 10/20 | 2/5 | Coordination | Convene | 2 |
| Project Hieroglyph | Education, Development & Human Flouri... | 9/20 | 3/5 | Funding | Fund | 4 |
| Provably Safe AGI via Formal Verification | AI Safety, Alignment & Governance | 9/20 | 3/5 | Engineering | Research | 3 |
| Closed-loop gene therapy for seizure suppression via acti... | Biotech, Medicine & Life Extension | 9/20 | 3/5 | Regulation | Fund | 4 |
| AI underwriting / mandatory insurance for AI systems | AI Safety, Alignment & Governance | 9/20 | 3/5 | Regulation | Advocate | 4 |
| Self-Improving System Prompt for Continuous AI Capability... | AI Safety, Alignment & Governance | 10/20 | 2/5 | Engineering | Build | 4 |
| Multicriteria safety architecture with explicit precedenc... | AI Safety, Alignment & Governance | 9/20 | 3/5 | Engineering | Research | 1 |
| Blockchain-based Universal Self-Actualization Income | Economic Systems & Resource Distribution | 10/20 | 2/5 | Regulation | Research | 3 |
| International Council of Life Extension | Biotech, Medicine & Life Extension | 10/20 | 2/5 | Regulation | Advocate | 4 |
| Ecological Balance Council | Ecological & Regenerative Systems | 10/20 | 2/5 | Coordination | Convene | 2 |
| Adaptive Wearable Tech | Biotech, Medicine & Life Extension | 9/20 | 3/5 | Regulation | Build | 7 |
| Human-Tech Council | AI Safety, Alignment & Governance | 10/20 | 2/5 | Coordination | Convene | 4 |
| Global Learning Collective | Education, Development & Human Flouri... | 9/20 | 3/5 | Coordination | Convene | 6 |
| Emotional Coach (Empathetic Neuro-AI) | Neurotechnology & Brain-Computer Inte... | 9/20 | 3/5 | Regulation | Research | 4 |
| Regenerative Biospheres | Ecological & Regenerative Systems | 9/20 | 3/5 | Engineering | Research | 5 |
| AI Alignment Markets | AI Safety, Alignment & Governance | 10/20 | 2/5 | Coordination | Research | 3 |
| Global AI Alignment Commission (GAAC) | International Governance & Coordination | 9/20 | 3/5 | Coordination | Convene | 2 |
| Extracellular vesicle-based blood diagnostics for tissue-... | Biotech, Medicine & Life Extension | 9/20 | 2/5 | Coordination | Convene | 3 |
| Protein-based nanomachines for in vivo tissue repair and ... | Biotech, Medicine & Life Extension | 8/20 | 3/5 | Engineering | Research | 3 |
| Biohybrid living DBS electrode (neuron-based implant inte... | Neurotechnology & Brain-Computer Inte... | 8/20 | 3/5 | Engineering | Research | 3 |
| Chemputer / Chemputation programming language | Nanotechnology & Advanced Manufacturing | 8/20 | 3/5 | Social Acceptance | Advocate | 7 |
| Openwater universal diagnostic/therapeutic device | Biotech, Medicine & Life Extension | 8/20 | 3/5 | Regulation | Fund | 4 |
| AI-driven forking narrative / interactive scenario conten... | AI-Mediated Deliberation & Collective... | 8/20 | 3/5 | Social Acceptance | Build | 5 |
| Agent Contract Declaration Requirement | AI Safety, Alignment & Governance | 9/20 | 2/5 | Coordination | Convene | 2 |
| Spectrum from environmental safety to metagenic safety | AI Safety, Alignment & Governance | 9/20 | 2/5 | Engineering | Research | 1 |
| Bounded AI Agents | AI Safety, Alignment & Governance | 9/20 | 2/5 | Coordination | Research | 5 |
| BTC Trust Grid | Economic Systems & Resource Distribution | 9/20 | 2/5 | Regulation | Advocate | 4 |
| Global Fungal Biology Research Initiative (Big Tech + Pau... | Biotech, Medicine & Life Extension | 9/20 | 2/5 | Coordination | Convene | 3 |
| Biophilic Architecture | Ecological & Regenerative Systems | 9/20 | 2/5 | Funding | Fund | 7 |
| Urban Sustainability Network | Energy, Environment & Planetary Systems | 9/20 | 2/5 | Regulation | Advocate | 7 |
| AI Market Intermediaries | Economic Systems & Resource Distribution | 8/20 | 3/5 | Coordination | Convene | 4 |
| The Indefinite Lifespan | Biotech, Medicine & Life Extension | 8/20 | 3/5 | Regulation | Advocate | 4 |
| Memory Looms | Education, Development & Human Flouri... | 10/20 | 1/5 | Physics | Research | 1 |
| World Cultural Exchange Forum | International Governance & Coordination | 9/20 | 2/5 | Coordination | Convene | 6 |
| TimeLike / SECHI (Simulation-Enabled Cooperative Human In... | AI-Mediated Deliberation & Collective... | 7/20 | 4/5 | Coordination | Research | 3 |
| Request for Evaluation (RfE) Protocol | AI Safety, Alignment & Governance | 9/20 | 2/5 | Coordination | Convene | 1 |
| Focused Research Organizations (FROs) | Scientific Research & Knowledge Infra... | 7/20 | 3/5 | Funding | Fund | 5 |
| Vagus nerve microbiome characterization study | Biotech, Medicine & Life Extension | 8/20 | 2/5 | Coordination | Research | 3 |
| AI-driven drug repurposing pipeline (AMD/Ripasudil discov... | Biotech, Medicine & Life Extension | 7/20 | 3/5 | Regulation | Research | 5 |
| Universal Constructor | Nanotechnology & Advanced Manufacturing | 6/20 | 4/5 | Physics | Research | 1 |
| Bell Labs Systems Engineer Role | Scientific Research & Knowledge Infra... | 8/20 | 2/5 | Coordination | Convene | 4 |
| Meditation-State Detection Model | Neurotechnology & Brain-Computer Inte... | 9/20 | 1/5 | Engineering | Research | 4 |
| Vertis Solus space-based solar power array | Energy, Environment & Planetary Systems | 7/20 | 3/5 | Engineering | Research | 4 |
| Computer-controlled sail cargo ship | Energy, Environment & Planetary Systems | 7/20 | 3/5 | Regulation | Advocate | 6 |
| Fire-the-CEO Decision Market | Economic Systems & Resource Distribution | 8/20 | 2/5 | Regulation | Advocate | 3 |
| Planetary-Scale Intelligence | Ecological & Regenerative Systems | 7/20 | 3/5 | Coordination | Research | 2 |
| NanoSync – Regenerative Nanotechnology | Biotech, Medicine & Life Extension | 7/20 | 3/5 | Physics | Research | 2 |
| Institute for Life Extension (ILE) | Biotech, Medicine & Life Extension | 7/20 | 3/5 | Regulation | Advocate | 4 |
| Urban AI systems | Energy, Environment & Planetary Systems | 7/20 | 3/5 | Coordination | Convene | 6 |
| AI-Managed Childhood Development Centers | Education, Development & Human Flouri... | 7/20 | 3/5 | Regulation | Research | 4 |
| Predictive AI System for R&D Funding Allocation | Scientific Research & Knowledge Infra... | 7/20 | 3/5 | Regulation | Advocate | 4 |
| Lifelong AI Guardians | Education, Development & Human Flouri... | 8/20 | 2/5 | Regulation | Advocate | 4 |
| Earth UBI | Economic Systems & Resource Distribution | 8/20 | 2/5 | Coordination | Convene | 2 |
| Jurisdictional Routers | International Governance & Coordination | 8/20 | 1/5 | Regulation | Research | 3 |
| Pareto-Optimal Negotiation Bots | AI-Mediated Deliberation & Collective... | 7/20 | 2/5 | Social Acceptance | Advocate | 7 |
| LitQA3 (high-recall literature evaluation benchmark) | Scientific Research & Knowledge Infra... | 7/20 | 2/5 | Engineering | Build | 4 |
| LLM Historical Forecasting Benchmark | Scientific Research & Knowledge Infra... | 7/20 | 2/5 | Engineering | Research | 3 |
| BBN-style Applied R&D Contractor (New BBNs) | Scientific Research & Knowledge Infra... | 6/20 | 3/5 | Coordination | Fund | 5 |
| Closed-loop ultrasound brain-state readout and mood modul... | Neurotechnology & Brain-Computer Inte... | 6/20 | 3/5 | Regulation | Research | 5 |
| Massively scalable intravascular or CSF-routed neural int... | Neurotechnology & Brain-Computer Inte... | 6/20 | 3/5 | Regulation | Advocate | 5 |
| Continuous AI-Driven Book Marketing Matchmaker | Economic Systems & Resource Distribution | 7/20 | 2/5 | Engineering | Build | 6 |
| Child Equity Stake Fund (US Birth Endowment) | Economic Systems & Resource Distribution | 7/20 | 2/5 | Social Acceptance | Advocate | 8 |
| Onerofex (collective AI-mediated dreaming experience) | AI-Mediated Deliberation & Collective... | 7/20 | 2/5 | Regulation | Research | 4 |
| Atheoretical Science via Massive Sensor Networks and AI P... | Scientific Research & Knowledge Infra... | 6/20 | 3/5 | Coordination | Research | 3 |
| Parallel Federal Science Funding System with Mandatory In... | Scientific Research & Knowledge Infra... | 6/20 | 3/5 | Funding | Advocate | 2 |
| Global Childhood Development Authority (GCDA) | Education, Development & Human Flouri... | 7/20 | 2/5 | Coordination | Convene | 4 |
| The Children's Movement | Education, Development & Human Flouri... | 6/20 | 3/5 | Funding | Convene | 4 |
| Neural-Adaptive Learning AI | Neurotechnology & Brain-Computer Inte... | 7/20 | 2/5 | Regulation | Advocate | 4 |
| Bitcoin-funded renewable energy cooperatives | Energy, Environment & Planetary Systems | 7/20 | 2/5 | Regulation | Advocate | 5 |
| Ecosystem-responsive AI management system | Ecological & Regenerative Systems | 7/20 | 2/5 | Regulation | Advocate | 4 |
| GAI (Global AI Board) | AI Safety, Alignment & Governance | 7/20 | 2/5 | Coordination | Convene | 4 |
| United Nations Biosphere Geoengineering and AI Governance... | International Governance & Coordination | 7/20 | 2/5 | Coordination | Convene | 2 |
| Little AI Robots (emotional decision-support chatbots) | Education, Development & Human Flouri... | 7/20 | 2/5 | Regulation | Research | 6 |
| Consolidated Intelligence Council | International Governance & Coordination | 7/20 | 2/5 | Coordination | Research | 4 |
| Neural Harmony Interface | Neurotechnology & Brain-Computer Inte... | 6/20 | 3/5 | Regulation | Research | 4 |
| Bio-templated microchips via implosion fabrication | Nanotechnology & Advanced Manufacturing | 5/20 | 3/5 | Engineering | Research | 3 |
| Programmable synthetic molecular robots for chemical synt... | Nanotechnology & Advanced Manufacturing | 5/20 | 3/5 | Physics | Research | 3 |
| Aldehyde-Stabilized Cryopreservation | Biotech, Medicine & Life Extension | 6/20 | 2/5 | Regulation | Research | 4 |
| AI-powered blog aggregator with conversational interface | Education, Development & Human Flouri... | 7/20 | 1/5 | Engineering | Build | 6 |
| EgoLets | AI-Mediated Deliberation & Collective... | 5/20 | 3/5 | Regulation | Advocate | 4 |
| Chemical substrate computation / chemical consciousness | Scientific Research & Knowledge Infra... | 5/20 | 3/5 | Physics | Research | 2 |
| Alexa Gentia (machine-negotiated agent legal structures) | AI Safety, Alignment & Governance | 6/20 | 2/5 | Regulation | Research | 4 |
| Origin of Life Evolutionary Engine (chemical space search... | Scientific Research & Knowledge Infra... | 5/20 | 3/5 | Physics | Research | 4 |
| Assembly Theory | Scientific Research & Knowledge Infra... | 6/20 | 2/5 | Physics | Research | 4 |
| National Science and Technology Foresight Agency (NSTFA) | Scientific Research & Knowledge Infra... | 6/20 | 2/5 | Coordination | Convene | 4 |
| Minimum-payload terraforming nanomachine for Mars | Nanotechnology & Advanced Manufacturing | 3/20 | 4/5 | Physics | Research | 2 |
| Microbial Interaction Simulation AI (Anthropic-built) | Scientific Research & Knowledge Infra... | 5/20 | 2/5 | Engineering | Research | 4 |
| Institute for Human Perplexity | Scientific Research & Knowledge Infra... | 5/20 | 2/5 | Coordination | Research | 2 |
| Gene Drives for Wild Animal Suffering Reduction | Ecological & Regenerative Systems | 2/20 | 4/5 | Regulation | Convene | 4 |
| Focused Philanthropic Bet Modeled on Warren Weaver / Rock... | Scientific Research & Knowledge Infra... | 3/20 | 3/5 | Social Acceptance | Advocate | 6 |
| Jurisdictional Arbitrage Special Economic Zones for BCI R... | Neurotechnology & Brain-Computer Inte... | 4/20 | 2/5 | Regulation | Advocate | 5 |
| Affective and Socio-Emotional Atmospheric Reading System | Education, Development & Human Flouri... | 4/20 | 2/5 | Social Acceptance | Advocate | 5 |
| AI-driven individualized peace education system | Education, Development & Human Flouri... | 4/20 | 2/5 | Regulation | Research | 4 |
| Elective Cryonic Suspension at Peak Vitality ('Kyasia') | Biotech, Medicine & Life Extension | 4/20 | 1/5 | Regulation | Advocate | 2 |
| Earth AI | Economic Systems & Resource Distribution | 3/20 | 2/5 | Coordination | Research | 4 |
| Neural Linguistic Interfaces | Neurotechnology & Brain-Computer Inte... | 2/20 | 3/5 | Engineering | Research | 4 |
| Phenomenal Binding-Based Sentient AI Architecture | Neurotechnology & Brain-Computer Inte... | 1/20 | 3/5 | Physics | Research | 1 |
| Grabby Aliens Three-Parameter Model | Scientific Research & Knowledge Infra... | 0/20 | 2/5 | Physics | Research | 4 |

---

## 5. How to Get Involved

### Fund (7 entities)
These entities have working concepts but need capital to scale. The bottleneck is money, not ideas.

**Watch list** (7 entities):
- The Collective of Inner Weavers (Bottleneck: Funding)
- Project Hieroglyph (Bottleneck: Funding)
- Closed-loop gene therapy for seizure suppression via activity-sensing potassium-channel upregulation (Bottleneck: Regulation)
- Openwater universal diagnostic/therapeutic device (Bottleneck: Regulation)
- Biophilic Architecture (Bottleneck: Funding)
- Focused Research Organizations (FROs) (Bottleneck: Funding)
- BBN-style Applied R&D Contractor (New BBNs) (Bottleneck: Coordination)

### Build (17 entities)
The research is done, the path is clear — these need engineering teams and implementation effort.

**Watch list** (17 entities):
- Translation Language Models (TLMs) with citizen-owned training databases (Bottleneck: Coordination)
- The Delphi Collaboration Protocol (Bottleneck: Coordination)
- Lean FRO (interactive theorem proving infrastructure for mathematics and AI) (Bottleneck: Engineering)
- Large-scale AI-mediated deliberation system (Bottleneck: Engineering)
- Deep Fision borehole nuclear reactor (Bottleneck: Regulation)
- Safety-Netted DAOs (Bottleneck: Engineering)
- Multiplicity.ai (Bottleneck: Engineering)
- Futarchy (Bottleneck: Social Acceptance)
- Author Personal Knowledge Graph / Writing Corpus Utility (Bottleneck: Engineering)
- Tool AI for Tool AI (Bottleneck: Engineering)
- *...and 7 more*

### Research (68 entities)
Promising directions that need more investigation before they're ready for deployment.

**Spotlight:**
- **AI cryptographic oracle with zero-knowledge IoT auditing and jury-DAO** — A fraud-resistance layer combining zero-knowledge proofs from IoT sensor data, AI anomaly detection, stake-slashing penalties, and a decentralized human jury for retroactive balance correction. (Bottleneck: Coordination)
- **Moral Trade** — A mechanism by which people or groups with different moral priorities swap concessions so that each gets more of what they care about than unilateral action would yield. (Bottleneck: Coordination)
- **Comprehensive AI Services (Drexler)** — An architecture of many narrow, domain-limited superhuman AIs that interact competitively rather than a single general superintelligence, achieving safety through structural narrowness. (Bottleneck: Coordination)
- **Wisdom DAO** — A decentralized autonomous organization where human citizens and AI systems jointly propose, deliberate, and vote on governance policy using weighted voting and blockchain transparency. (Bottleneck: Regulation)

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
- **Tokenized neural data sharing with selective disclosure** — A privacy architecture for BCI systems in which neural data is tokenized so users can selectively disclose specific streams of thought or brain state while retaining others as private. (Bottleneck: Regulation)
- **Interbeing Forum** — A rotating bioregional assembly that grants formal representation to ecosystems and future generations through human guardians advised by digital twin data. (Bottleneck: Regulation)
- **Attack Dog DAO for Climate** — A DAO that funds and coordinates environmental litigation on behalf of legally-recognized natural entities, financed through tokenized litigation investment. (Bottleneck: Regulation)
- **Accord of Watersheds** — An international treaty framework that organizes political cooperation around watershed and bioregional boundaries rather than national borders. (Bottleneck: Regulation)
- **Watershed Parliaments** — Bioregional governance bodies organized around watershed boundaries rather than political borders, incorporating ecological feedback into formal decision-making. (Bottleneck: Regulation)
- **Loyal AI Assistance (Fiduciary AI Assistance)** — A personal AI system explicitly designed to be loyal to the individual user's goals rather than to platform or advertiser interests, contrasted with current assistants like Siri or Alexa. (Bottleneck: Regulation)

**Watch list** (33 entities):
- LexNodes (Bottleneck: Regulation)
- De novo designed universal flu vaccines (Neil King / Baker Lab platform) (Bottleneck: Regulation)
- Hybrid Market impact bond ledger (Bottleneck: Regulation)
- Mandatory Open-Source AI Release Policy (Bottleneck: Regulation)
- Orare - AI-powered Futarchy governance system (Bottleneck: Social Acceptance)
- Global Personhood Token / Trust-of-Personhood Standard (Bottleneck: Regulation)
- Integration of Brain Preservation into the Medical System (Bottleneck: Regulation)
- Open-source AI-powered research funding and knowledge platform (Bottleneck: Regulation)
- Interplanetary Cooperative (Bottleneck: Regulation)
- The Flourishing Foundation (Bottleneck: Regulation)
- *...and 23 more*

### Convene (58 entities)
The pieces exist separately — what's missing is coordination between stakeholders.

**Spotlight:**
- **Community-Governed AI Mesh Systems** — Decentralized AI networks trained on locally governed data and stewarded by community trust circles rather than centralized corporate or state actors. (Bottleneck: Coordination)
- **Universal AI Learning UnCommons (UALU)** — A federated governance institution that develops, maintains, and audits AI education tools through multi-stakeholder councils including elders, learners, and ethicists. (Bottleneck: Coordination)
- **BCI Operating System (BCI-OS)** — An open-source operating system layer for brain-computer interfaces that embeds agency evaluation, AI model compatibility, and privacy standards as core OS-level features. (Bottleneck: Coordination)
- **Civic Systems Co-Op** — A global open-source consortium that develops and maintains ethical AI tools for municipal and community governance. (Bottleneck: Coordination)
- **Interoperable Governance Protocol Stack** — A shared technical and governance protocol layer that allows citizens to port digital identities, benefits, and credentials across distinct federated city-state systems, and enables AI systems across those jurisdictions to align resource allocation and crisis modeling. (Bottleneck: Regulation)
- **DAO-governed open innovation platform for TLM documentation and training data** — A DAO-based governance structure that mandates open-source documentation and community-sourced feedback loops for translation model development and adaptation. (Bottleneck: Coordination)
- **Digital Twins for Communities and Ecosystems** — Real-time digital models of communities and ecosystems that enable participatory future simulation with locally-owned data. (Bottleneck: Coordination)
- **The Global Deliberation Coordinator** — A platform institution designed to coordinate global deliberative processes and collective decision-making specifically around AI governance. (Bottleneck: Coordination)
- **Epistemic stack** — A citation and provenance system for all information—from newspaper articles to social media claims—that lets users trace any assertion back to its raw data sources, with trust scores based on historical accuracy of each link in the chain. (Bottleneck: Coordination)

**Watch list** (49 entities):
- AI Fiduciaries (Bottleneck: Coordination)
- Privacy-Preserving Global Regulatory Markets for AI Verification (Bottleneck: Coordination)
- Continuity Guild (Bottleneck: Coordination)
- BioEcho Mesh (Bottleneck: Coordination)
- The Mnemosyne Assembly (Bottleneck: Coordination)
- Open Cognition Ledger (Bottleneck: Coordination)
- Living Rights Network (Bottleneck: Coordination)
- Federated Procurement Platforms (Bottleneck: Coordination)
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
