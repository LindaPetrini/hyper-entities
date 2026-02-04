// ─── Page & Typography ───
#set page(
  paper: "a4",
  margin: (x: 2.5cm, y: 2.5cm),
  numbering: "1",
  header: context {
    if counter(page).get().first() > 1 [
      #set text(8pt, fill: luma(140))
      Hyper-Entities: Consensus Highlights
      #h(1fr)
      Foresight Institute
    ]
  },
)
#set text(font: "New Computer Modern", size: 10.5pt)
#set par(justify: true, leading: 0.65em)
#set heading(numbering: "1.")

// ─── Title Page ───
#v(4cm)
#align(center)[
  #text(28pt, weight: "bold")[Hyper-Entities]
  #v(4pt)
  #text(16pt, fill: luma(80))[Consensus Highlights Report]
  #v(1.5cm)
  #text(11pt, fill: luma(100))[
    Linda Petrini & Beatrice Erkers \
    Foresight Institute \
    January 2026
  ]
]
#pagebreak()

// ─── Table of Contents ───
#outline(indent: auto, depth: 2)
#pagebreak()

// ═══════════════════════════════════════════
= Introduction

== What Are Hyper-Entities?

A *hyper-entity* is a coherent, future-instantiated system that does not yet exist, but is treated as if it will; whose realization would create a new stable action space for humanity; and which already reorganizes coordination, investment, and narrative around its anticipated existence.

Three characteristics define a hyper-entity:

+ *Non-existent but treated as real* --- the system doesn't exist yet, but people act as if it will.
+ *Creates new action spaces* --- it would enable fundamentally new things humans can do.
+ *Pre-real effects* --- it already reorganizes coordination, investment, and narrative _now_.

Historical examples include the Internet (pre-1990s), which reorganized telecoms R&D, policy, and venture capital before widespread deployment; the Space Race (1950s--60s), where Moon missions organized national budgets and education systems before any launches; and AGI today, which reshapes AI research priorities, corporate strategies, and policy discussions despite not yet existing.

== Project Overview

This project set out to systematically identify, score, and curate hyper-entities emerging from the discourse around the Foresight Institute's research community. The source material comprises:

- *65 podcast transcripts* from the Foresight Institute podcast series, featuring researchers, technologists, and thinkers at the frontier of science and governance.
- *40 world-gallery submissions* from the Foresight Institute's Existential Hope project, presenting speculative visions of positive futures.
- *2 AI-pathways essays*, including Vitalik Buterin's d/acc framework and analysis of Tool AI approaches.
- *1 x-hope document* providing additional framing.

From this corpus, over 300 candidate hyper-entities were extracted, scored across three assessment stages, clustered thematically, and then curated through an independent review process by two researchers (Linda Petrini and Beatrice Erkers) to arrive at a final consensus list of 39 highlighted entities.

// ═══════════════════════════════════════════
= Methodology <methodology>

The methodology follows a multi-stage pipeline: extraction, scoring, clustering, and human curation.

== Stage 1: Hyper-Entity Qualification (max 27)

Each candidate is scored on 9 axes (0--3 per axis). A candidate must score *18 or above* to qualify as a hyper-entity. Scores of 12--17 are borderline and require strong justification.

#figure(
  table(
    columns: (auto, 1fr, 1fr, 1fr, 1fr),
    inset: 6pt,
    align: (left, left, left, left, left),
    fill: (col, row) => if row == 0 { luma(230) },
    [*Axis*], [*0*], [*1*], [*2*], [*3*],
    [Non-existence], [Already deployed], [Prototype exists], [Partial demos], [No instantiation],
    [Plausibility], [Fantasy], [Hand-wavy], [Credible theory], [Active scientific path],
    [Design specificity], [Vague aspiration], [Metaphor only], [Coarse architecture], [Detailed system model],
    [New action space], [Incremental], [Narrow new ability], [Broad new capability], [Entirely new verb],
    [Roadmap clarity], [None], [Wishful], [Research agenda], [Multi-stage roadmap],
    [Coordination gravity], [Solo interest], [Small niche], [Multiple orgs], [Global coordination],
    [Resource pull], [Trivial], [Some grants], [Serious capital], [Massive capital + talent],
    [Narrative centrality], [Ignored], [Peripheral], [Often referenced], [Justifies present actions],
    [Pre-real effects], [None], [Speculation], [Market/policy shifts], [Institutions reorganize],
  ),
  caption: [Stage 1 scoring rubric (9 axes, 0--3 each, max 27).],
)

== Stage 2: Technology Impact Assessment (max 70)

Qualified entities are assessed on 14 dimensions (0--5 each) measuring potential impact and risk. Higher scores indicate greater magnitude of effect --- not necessarily positive.

#figure(
  table(
    columns: (auto, 1fr),
    inset: 6pt,
    align: (left, left),
    fill: (col, row) => if row == 0 { luma(230) },
    [*Dimension*], [*What is scored*],
    [Capability Discontinuity], [New powers unlocked (incremental ... phase change)],
    [Cross-Domain Reach], [How many sectors it touches],
    [Scalability], [Speed and cost of global spread],
    [Autonomy], [Operates without ongoing human control],
    [Composability], [Can be embedded everywhere],
    [Feedback Intensity], [Strength of self-reinforcing loops],
    [Irreversibility], [Difficulty of rollback once deployed],
    [Power Concentration], [Centralizes leverage],
    [Externality Magnitude], [Size of spillovers],
    [Misuse Asymmetry], [Harm vs.\ benefit ratio],
    [Governance Lag], [Gap vs.\ existing institutions],
    [Narrative Lock-In], [Inevitable story it enforces],
    [Path Dependency], [Futures foreclosed],
    [Human Agency Impact], [Effect on human choice],
  ),
  caption: [Stage 2 technology assessment dimensions (14 axes, 0--5 each, max 70).],
)

== Stage 3: d/acc Values Alignment (max 20)

Based on Vitalik Buterin's d/acc framework (Defensive / Decentralized / Democratic / Differential Acceleration), this stage evaluates whether a hyper-entity aligns with values that promote human flourishing, resilience, and freedom. Each entity is scored on 4 dimensions (0--5 each).

#figure(
  table(
    columns: (auto, 1fr),
    inset: 6pt,
    align: (left, left),
    fill: (col, row) => if row == 0 { luma(230) },
    [*Dimension*], [*What is scored*],
    [Democratic], [Enables collective decision-making vs.\ concentrates decisions in elites],
    [Decentralized], [Distributes power broadly vs.\ creates single points of control],
    [Defensive], [Favors protection over harm; defense-favoring],
    [Differential], [Creates positive asymmetries; improves defense and freedom],
  ),
  caption: [Stage 3: d/acc values alignment (4 dimensions, 0--5 each, max 20).],
)

== Curation Process

After automated extraction and scoring, the entities were presented to two independent researchers through a review interface:

+ *Independent shortlisting*: Linda and Beatrice each independently reviewed the full set of scored entities and starred those they considered most significant. Linda selected 88 entities; Beatrice selected 67.
+ *Overlap identification*: 26 entities were starred by _both_ reviewers (20.2% overlap rate), forming the core consensus set.
+ *Cross-review voting*: Each reviewer then reviewed the other's unique picks via a voting interface, voting Yes on entities they also found compelling. Linda voted Yes on 8 of Beatrice's unique picks; Beatrice voted Yes on 5 of Linda's unique picks.
+ *Final list*: The resulting 39 entities (26 shared + 8 Linda's Yes + 5 Beatrice's Yes) constitute the consensus highlights presented in this report.

// ═══════════════════════════════════════════
= Consensus Entities <entities>

The 39 consensus entities are presented below, organized into three tiers: shared picks (starred by both reviewers), Linda's Yes picks (from Beatrice's unique list), and Beatrice's Yes picks (from Linda's unique list). Within each tier, entities are grouped by thematic cluster.

== Shared Picks (26)
_Starred independently by both Linda and Beatrice._

=== Coordination & AI-Enabled

*Mind Uploading Infrastructure* \
Technological systems enabling gradual human consciousness transfer to digital platforms, with complex social and infrastructural considerations for maintaining uploaded minds. \
#text(size: 9pt, fill: luma(100))[d/acc: 8/20 #h(1em) Tech: 56/70]

=== Ecosystem & Open

*LexCommons* \
A global, open-source legal system powered by smart contracts, AI legal agents, and decentralized governance. It transforms law from a closed, institutional practice to an open, participatory, and technologically mediated global commons. \
#text(size: 9pt, fill: luma(100))[d/acc: 18/20 #h(1em) Tech: 57/70]

=== Energy & Clean

*Deep Fision Micro Nuclear Reactors* \
A small, factory-producible nuclear reactor designed to be buried a mile underground, providing localized, safe, and clean energy. Designed to be mass-manufactured like automobiles, with each reactor about the size of a Toyota. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: 47/70]

=== Epistemic & Stack

*Epistemic Stack* \
A comprehensive information verification and tracing system that allows users to follow the provenance of information from high-level claims down to raw data sources, enabling more robust trust and understanding. \
#text(size: 9pt, fill: luma(100))[d/acc: 17/20 #h(1em) Tech: 44/70]

*Distributed Zero-Knowledge Security Systems* \
A networked cybersecurity infrastructure using advanced cryptographic techniques to protect critical communications and industrial control networks, with distributed threat intelligence and quantum-resistant encryption. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: 47/70]

*Epistemic Infrastructure for Truth Verification* \
A systematic approach to determining truth and trust in an AI-mediated information ecosystem, involving precise citation, consensus mechanisms, and algorithmic truth assessment. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: 53/70]

=== Global & Molecular

*End-User Programming Ecosystem* \
A democratized software creation environment where non-technical individuals can design, modify, and generate custom software tailored to their specific needs using AI-enhanced tools. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: 54/70]

*Fiduciary AI Assistance* \
A system of AI assistants designed to be fundamentally loyal to individual human users, helping them navigate complex problems and daily life while respecting their goals and interests. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: N/A]

=== Governance

*AI-Assisted Epistemological Enhancement System* \
A technological and methodological approach using AI to improve human reasoning, forecasting, truth-discovery, and collaborative deliberation, leveraging AI capabilities to enhance human cognitive processes and decision-making. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: 54/70]

*Prediction Markets as Decision Support Systems* \
An advanced institutional technology for transforming crowd intelligence into actionable decision-making tools for organizations, moving beyond current crypto-based betting platforms to create sophisticated advisory systems. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: 44/70]

*Digital Twin Ecosystem* \
A comprehensive system of real-time digital representations of communities and ecosystems that enable collective decision-making, simulation, and shared responsibility, providing new infrastructure for understanding and managing complex social and ecological systems. \
#text(size: 9pt, fill: luma(100))[d/acc: 15/20 #h(1em) Tech: 55/70]

*EgoLets (Personal AI Assistants)* \
Personalized AI systems that capture individual thinking patterns and decision-making styles, functioning as specialized "little versions of your ego" across different life domains. \
#text(size: 9pt, fill: luma(100))[d/acc: 15/20 #h(1em) Tech: 48/70]

*Global Deliberation Coordinator (GDaaS)* \
A pioneering institution that combines traditional deliberative democratic processes with AI-powered tools to enable rapid, cost-effective, and accessible global decision-making on critical challenges. \
#text(size: 9pt, fill: luma(100))[d/acc: 15/20 #h(1em) Tech: 52/70]

=== Governance & Global

*Digital Mind Governance Systems* \
A future institutional and ethical framework for managing, protecting, and regulating digital minds as potential moral patients with rights, voting capabilities, and social standing. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: 53/70]

=== Governance & Platform

*Competitive Governance Protocol Stack* \
An interoperable digital governance system allowing citizens to participate in multiple overlapping jurisdictions, with portable digital identities and the ability to switch between governance networks based on performance. \
#text(size: 9pt, fill: luma(100))[d/acc: 18/20 #h(1em) Tech: 57/70]

=== Interfaces & Brain

*Translation Language Models (TLMs)* \
A multipurpose linguistic technology that enables rapid translation and understanding across languages, dialects, and technical domains, democratizing knowledge work by breaking down communication barriers. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: 53/70]

*Atomically Precise Manufacturing / Molecular Machine Systems* \
A technological system enabling precise manipulation of matter at the atomic scale, potentially revolutionizing manufacturing, environmental control, and product creation. \
#text(size: 9pt, fill: luma(100))[d/acc: 13/20 #h(1em) Tech: 57/70]

*Immune-Computer Interface* \
A transformative technological system that enables direct, high-bandwidth communication between human immune systems and computational technologies, allowing for dynamic biological monitoring, intervention, and enhancement. \
#text(size: 9pt, fill: luma(100))[d/acc: 13/20 #h(1em) Tech: 58/70]

*Universal Constructor* \
A hypothetical machine capable of being programmed to construct virtually anything within the laws of physics, fundamentally transforming human labor and production by eliminating physical toil and enabling exponential self-replication. \
#text(size: 9pt, fill: luma(100))[d/acc: 13/20 #h(1em) Tech: N/A]

*Human Superintelligence via Brain-Computer Interfaces (BCI)* \
A technological system that enhances human cognitive capabilities through direct neural interfaces, enabling humans to compete with and potentially transcend artificial intelligence, fundamentally expanding human potential for understanding and exploring the universe. \
#text(size: 9pt, fill: luma(100))[d/acc: 12/20 #h(1em) Tech: 60/70]

=== Learning & Adaptive

*Universal AI Learning UnCommons (UALU)* \
A federated, community-led network for developing and maintaining AI educational tools, governed by diverse councils including elders, learners, technologists, and ethicists to ensure just and caring educational infrastructure. \
#text(size: 9pt, fill: luma(100))[d/acc: 17/20 #h(1em) Tech: 44/70]

*De-escalatory Self-Defense Mediation Tool* \
An AI-powered mediation platform designed to resolve conflicts through progressive strategies of win-win negotiation, restoration, and proportional consequence, aimed at reducing escalation in interpersonal, organizational, and international disputes. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: N/A]

=== Markets

*Reputational Markets* \
A decentralized global coordination mechanism that uses prediction markets to assess and incentivize responsible behavior across complex supply chains, creating a dynamic reputation scoring system that encourages collective accountability for long-term human values. \
#text(size: 9pt, fill: luma(100))[d/acc: 17/20 #h(1em) Tech: 51/70]

=== Science & Research

*Automated Scientific Publishing Ecosystem for Machine Consumers* \
A reimagined scientific publishing system designed primarily for AI systems to consume, process, and contribute to scientific knowledge, with radically different latency, format, and peer review mechanisms. \
#text(size: 9pt, fill: luma(100))[d/acc: 18/20 #h(1em) Tech: 60/70]

*Atheoretical Science AI* \
A radically new scientific methodology where AI explores massive sensor network data without pre-existing theoretical frameworks, discovering useful patterns and mechanisms through pure exploration and pattern recognition. \
#text(size: 9pt, fill: luma(100))[d/acc: 13/20 #h(1em) Tech: N/A]

*Chemputing (Chemical Computing)* \
A systematic approach to programming chemical reactions using standardized hardware and a specialized programming language, enabling reliable molecular transformations and potentially revolutionizing drug discovery, materials science, and computational chemistry. \
#text(size: 9pt, fill: luma(100))[d/acc: 13/20 #h(1em) Tech: 44/70]

#pagebreak()

== Linda's Yes Picks (8)
_Entities from Beatrice's unique list that Linda voted Yes on._

=== Economic & Universal

*Climate Adaptation Jurisdictional Arbitrage* \
A strategic approach to creating special economic zones and new cities optimized for climate migration, leveraging legal and economic frameworks to proactively manage population displacement caused by environmental changes. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: N/A]

=== Ecosystem & Tool

*Lifelong AI Guardians* \
Privacy-preserving AI systems that monitor and support children's holistic development, providing personalized guidance across multiple life domains and connecting different stakeholders through intelligent, empathetic monitoring. \
#text(size: 9pt, fill: luma(100))[d/acc: 13/20 #h(1em) Tech: 49/70]

=== Emotional & Urban

*Empathetic Neuro-AI Emotional Coaching System* \
An AI-driven emotional support ecosystem that provides personalized, real-time therapeutic interventions through neural signal analysis and adaptive AI companions that prevent emotional crises and promote healing. \
#text(size: 9pt, fill: luma(100))[d/acc: 13/20 #h(1em) Tech: 48/70]

=== Global & Molecular

*Protein Design for Global Challenges* \
A comprehensive approach to using engineered proteins to solve critical global problems across sustainability, health, climate, and technology domains --- designing novel proteins that can break down pollutants, capture carbon, create new medical treatments, and integrate biological systems with inorganic materials. \
#text(size: 9pt, fill: luma(100))[d/acc: 13/20 #h(1em) Tech: 53/70]

=== Governance & Global

*Moral Trade Civilization* \
A future societal model where ethical preferences can be systematically traded, allowing diverse moral perspectives to achieve mutually beneficial outcomes and maximize collective value alignment. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: N/A]

=== Governance & Platform

*Habermas Machines* \
An AI system designed to support group deliberation by generating and refining collective statements, aiming to help diverse groups reach consensus through advanced language processing. \
#text(size: 9pt, fill: luma(100))[d/acc: 15/20 #h(1em) Tech: 42/70]

=== Interfaces & Brain

*Expanded Moral Circle Technologies* \
Neurotechnological and communication systems enabling dramatically enhanced empathy, understanding, and moral perception across different forms of consciousness. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: N/A]

=== Science & Research

*Origin of Life Experimental Platform* \
A chemical search engine designed to systematically explore molecular space to generate novel life forms, treating the origin of life as a fundamental physics problem that can be experimentally investigated. \
#text(size: 9pt, fill: luma(100))[d/acc: 10/20 #h(1em) Tech: 46/70]

#pagebreak()

== Beatrice's Yes Picks (5)
_Entities from Linda's unique list that Beatrice voted Yes on._

=== Energy & Clean

*Decentralized Adaptive Energy Network* \
An AI-optimized, decentralized energy network with dynamic routing, local energy production, and intelligent demand prediction, transforming traditional centralized energy distribution models. \
#text(size: 9pt, fill: luma(100))[d/acc: 18/20 #h(1em) Tech: 51/70]

=== Epistemic & Stack

*Gevulot (Privacy Infrastructure)* \
A fine-grained privacy control system where individuals can dynamically set permissions for data capture and sharing about themselves, fundamentally restructuring information privacy. \
#text(size: 9pt, fill: luma(100))[d/acc: 18/20 #h(1em) Tech: N/A]

=== Interfaces & Brain

*Whole Brain Emulation* \
A technological approach to creating digital replicas of human brains through advanced scanning and simulation technologies, potentially enabling preservation of human cognitive capabilities in digital form. \
#text(size: 9pt, fill: luma(100))[d/acc: 8/20 #h(1em) Tech: N/A]

=== Markets

*Futarchy (Governance by Prediction Markets)* \
A novel governance system where societal values are democratically determined, but specific policy implementations are selected through prediction markets that objectively forecast outcomes. \
#text(size: 9pt, fill: luma(100))[d/acc: 16/20 #h(1em) Tech: N/A]

=== Science & Research

*Decentralized Scientific Collaboration Infrastructure* \
A new scientific ecosystem with federated research networks, multi-track career systems, and AI-enabled collaborative platforms that fundamentally transform how knowledge is produced, validated, and attributed. \
#text(size: 9pt, fill: luma(100))[d/acc: 18/20 #h(1em) Tech: 53/70]

#pagebreak()

// ═══════════════════════════════════════════
= Conclusion

The 39 hyper-entities identified in this report represent a curated map of futures that are already shaping the present. Though none of these systems fully exist yet, each is generating real coordination effects --- redirecting research agendas, attracting capital, spawning prototypes, and anchoring the narratives through which institutions and individuals make decisions today.

Several patterns emerge from the consensus list:

- *Governance and collective intelligence dominate.* The largest cluster of highlighted entities concerns new mechanisms for decision-making at scale --- prediction markets, deliberative AI, competitive jurisdictions, and reputation systems. This reflects a shared intuition that the bottleneck for beneficial futures is not primarily technological but coordinational.

- *Epistemic infrastructure is a recurring theme.* Multiple entities address the problem of trust, truth, and provenance in an AI-saturated information environment. The Epistemic Stack, truth verification systems, and zero-knowledge security all point toward a felt need for new foundations of shared knowledge.

- *Brain interfaces and molecular manufacturing appear as high-risk, high-reward frontiers.* Entities like Human Superintelligence via BCI, Immune-Computer Interfaces, and Atomically Precise Manufacturing score high on technology impact but lower on d/acc alignment, signaling areas where the potential for transformative benefit coexists with significant governance challenges.

- *d/acc alignment varies widely.* Scores range from 8/20 (Mind Uploading Infrastructure, Whole Brain Emulation) to 18/20 (Competitive Governance Protocol Stack, Gevulot, Decentralized Adaptive Energy Network). This spread is itself informative: the entities that most excite researchers are not uniformly safe or decentralized, and the ones that score highest on values alignment are not always the most technologically mature.

- *The cross-review process surfaced complementary perspectives.* Linda's Yes picks from Beatrice's list leaned toward moral and emotional dimensions (Expanded Moral Circle Technologies, Empathetic Neuro-AI, Moral Trade Civilization), while Beatrice's Yes picks from Linda's list emphasized decentralized infrastructure (Gevulot, Decentralized Energy, Decentralized Science). The voting mechanism proved effective at capturing entities that a single reviewer might overlook.

This report is a starting point, not a final ranking. The hyper-entities listed here are not predictions --- they are attractors, pulling present-day activity into alignment with possible futures. The value of identifying them lies not in forecasting which will arrive first, but in making visible the coordination patterns they are already creating, and in asking whether those patterns lead where we want to go.
