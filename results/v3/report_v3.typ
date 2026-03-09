#set document(title: "Hyper-Entities V3: Spotlight Report", author: "Linda Petrini")
#set page(margin: 1in, numbering: "1")
#set text(font: "Helvetica", size: 11pt, lang: "en")
#set par(justify: true, leading: 0.65em)
#set heading(numbering: none)
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  text(size: 20pt, weight: "bold", it.body)
  v(0.5em)
}
#show heading.where(level: 2): it => {
  v(1em)
  text(size: 16pt, weight: "bold", it.body)
  v(0.3em)
}
#show heading.where(level: 3): it => {
  v(0.8em)
  text(size: 13pt, weight: "bold", it.body)
  v(0.2em)
}
#show link: it => {
  set text(fill: rgb("#1a5276"))
  underline(it)
}

// Title page
#align(center + horizon)[
  #text(size: 28pt, weight: "bold")[Hyper-Entities V3:\ Spotlight Report]
  #v(1.5em)
  #text(size: 14pt)[Linda Petrini]
  #v(0.5em)
  #text(size: 12pt)[Foresight Institute]
  #v(0.5em)
  #text(size: 12pt)[March 2026]
]
#pagebreak()

// Table of Contents
#outline(title: "Table of Contents", indent: 1.5em, depth: 2)
#pagebreak()

// Body
= Hyper-Entities V3: Spotlight Report


Linda Petrini & Beatrice Erkers
Foresight Institute
March 2026

#line(length: 100%, stroke: 0.5pt + luma(180))


== 1. Executive Summary


The term _#link("https://www.existentialhope.com/podcasts/michael-nielsen-on-hyper-entities-tools-for-thought-and-wise-optimism")[hyper-entity]_ was coined by Michael Nielsen to describe systems that do not yet exist but are already reshaping how people coordinate, allocate capital, and construct shared narratives around their anticipated arrival. These are not speculative fictions. They are attractors — specific enough that researchers, funders, and institutions start organizing around them before anything works. This report identifies and ranks 189 such candidates drawn from 109 sources, with the goal of helping funders, policymakers, and technologists figure out where to pay attention.

The analysis applies the #link("https://vitalik.eth.limo/general/2023/11/27/techno_optimism.html")[d/acc framework] developed by Vitalik Buterin, which evaluates entities across four overlapping properties: democratic (distributing power rather than concentrating it), decentralized (resistant to single points of control or failure), defensive (strengthening protective over offensive capabilities), and differential (accelerating beneficial technologies faster than harmful ones). Entities were also scored on transformative potential and actionability, producing a composite score that determined tier placement.

From 189 candidates, 19 were designated Tier 1 spotlight entities and 170 placed on a Tier 2 watch list. The spotlight entities represent the strongest combination of d/acc alignment, transformative potential, and near-term actionability. Leading this group are Community-Governed AI Mesh Systems (composite score 21), the Universal AI Learning UnCommons (20), and an AI cryptographic oracle with zero-knowledge IoT auditing and jury-DAO governance (19). Across all 189 entities, the average d/acc score was 9.5 out of 20, average transformative score 2.6 out of 5, and average Technology Readiness Level (TRL) 3.9 — placing the field, in aggregate, between proof-of-concept and early validation.

The largest thematic cluster is AI Safety, Alignment & Governance with 31 entities, followed by Scientific Research & Knowledge Infrastructure (25) and Education, Development & Human Flourishing (20). Decentralized & Democratic Institutions and AI-Mediated Deliberation & Collective Intelligence each contribute 18 entities, reflecting how much energy is going into the question of whether governance can scale without centralizing control.

The most common bottleneck across the full dataset is coordination, affecting 76 of 189 entities. Regulatory uncertainty constrains 57, engineering challenges 24, and social acceptance barriers 13. Funding, despite its prominence in public discourse about emerging technology, ranks last as a primary bottleneck, cited for only 7 entities. This distribution suggests that the scarcest resource is not capital but institutional glue — shared standards, protocols, governance frameworks — that gets people pulling in the same direction.

Recommended primary actions reflect this: 68 entities most need sustained research, 58 require convening (bringing together the communities of practice that can establish norms and test coordination mechanisms), and 39 need advocacy to shift regulatory and political conditions. Only 17 are primarily in a build phase. Seven are primarily funding-constrained.

All candidates were sourced from #link("https://www.existentialhope.com/")[Existential Hope] (#link("https://www.existentialhope.com/")[existentialhope.com]), the #link("https://foresight.org/")[Foresight Institute]'s initiative cataloguing pathways to long-term human and civilizational flourishing, drawing on #link("https://www.existentialhope.com/podcasts")[podcast transcripts], #link("https://worlds.existentialhope.com/")[world gallery] submissions, and #link("https://www.existentialhope.com/ai-pathways")[AI pathways] essays. Twenty-seven entities appeared in both this analysis and the prior v2 analysis, giving us a consistency check between two rounds.

#line(length: 100%, stroke: 0.5pt + luma(180))


== 2. Introduction


=== What Are Hyper-Entities?


A hyper-entity is a coherent, future-instantiated system that does not yet exist, but is treated as if it will; whose realization would create a new stable action space for humanity; and which already reorganizes coordination, investment, and narrative around its anticipated existence. The term was coined by #link("https://michaelnielsen.org/")[Michael Nielsen], whose broader definition informed this project's more operationally focused criteria.

Nielsen's emphasis was on the design dimension — hyper-entities as orienting visions that carry new affordances, requiring genuine imagination and depth of understanding to conceive. This project adds an operational criterion: that the entity's anticipated existence is already causally active, reshaping coordination and investment before any prototype exists.

Three characteristics define a hyper-entity:

+ _Not yet deployed_ — exists only as concept, early fragments, or shared anticipation — not as a functioning system at scale.
+ _Transformatively novel_ — would enable fundamentally new things humans can do, not just improve on existing capabilities.
+ _Already causally active_ — its anticipated existence reorganizes coordination, investment, and narrative now, before any prototype exists. This is the key distinguishing feature: a hyper-entity has causal force through expectation alone.

Historical examples include the Internet (pre-1990s), which reorganized telecoms R&D, policy, and venture capital before widespread deployment; the Space Race (1950s-60s), where Moon missions organized national budgets and education systems before any launches; and AGI today, which reshapes AI research priorities, corporate strategies, and policy discussions despite not yet existing.

=== Project Overview


This project set out to systematically identify, score, and curate hyper-entities emerging from the discourse around the #link("https://www.existentialhope.com/")[Existential Hope] community. The source material comprises:

- 65 podcast transcripts from the #link("https://www.existentialhope.com/podcasts")[Existential Hope podcast] by the #link("https://foresight.org/")[Foresight Institute]
- 41 #link("https://worlds.existentialhope.com/")[world gallery] submissions from Existential Hope
- 3 #link("https://www.existentialhope.com/ai-pathways")[AI pathways] essays, including #link("https://en.wikipedia.org/wiki/Vitalik_Buterin")[Vitalik Buterin]'s #link("https://vitalik.eth.limo/general/2023/11/27/techno_optimism.html")[d/acc framework] and its 2025 update

From this corpus, over 300 candidate hyper-entities were extracted, scored across three assessment dimensions, deduplicated, researched via web search, and curated to arrive at a final list of 189 distinct entities, with 19 highlighted as Tier 1 spotlight entities.

=== Why This Matters: The AGI Crowding-Out Problem


If you follow technology discourse in 2026, you might reasonably conclude that artificial general intelligence is the only future worth preparing for. In 2024, over \$252 billion in corporate investment flowed into AI and AGI companies. In 2025, AI startups alone raised \$211 billion in venture capital, an 85% year-over-year increase. Major governments have appointed AI safety czars. CEOs casually discuss "the arrival of superintelligence" in quarterly earnings calls.

This isn't inherently wrong — AGI could indeed be transformative. But this concentration creates what economists call a crowding-out effect: when one opportunity dominates attention and capital, other valuable investments get systematically underfunded.

This project attempts to answer a different question: not "what hyper-entity is most likely to arrive?" but "which ones should we be naming, funding, and building toward, given the kind of future we actually want?"

Our research identifies 189 such entities, ranging from planetary-scale governance systems to new tools for collective decision-making, from programmable biology to infrastructure for shared truth. Many score highly on metrics that should matter to rational funders: broad benefit distribution, downside protection, and resilience to political shifts.

Yet they receive fragmentary attention. Consider epistemic infrastructure — systems designed to help communities establish shared facts and navigate information disorders. By our analysis, projects in this space align strongly with human values and address urgent coordination failures. The same pattern repeats across governance innovation, distributed energy systems, and open science infrastructure.

This imbalance carries real costs. First, many of these overlooked systems represent critical infrastructure for human flourishing regardless of AGI timelines. Whether artificial superintelligence arrives in 2030 or 2080, we'll still need tools for democratic legitimacy, ways to manage synthetic biology safely, and governance protocols that prevent technological lock-in.

Second, several entities on our list would actually help society navigate AGI's arrival more safely. Better epistemic infrastructure means clearer public deliberation about AI governance. Advanced collective intelligence systems could help coordinate complex international AI safety regimes. We're underfunding the very tools we'd need to handle the future we're investing so heavily in creating.

The argument here isn't anti-AGI. It's closer to portfolio theory applied to civilizational bets: under genuine uncertainty, concentration in a single scenario carries real risk. Infrastructure that creates value across many possible futures — not just one — seems worth naming, even if the allocation decisions belong to others.

#line(length: 100%, stroke: 0.5pt + luma(180))


== 3. Key Findings


=== The Landscape: d/acc Alignment vs. Transformative Potential


The scatter plot below positions all 189 entities by their d/acc values alignment score (x-axis) and transformative potential (y-axis). Point size reflects the composite score; color indicates thematic group.

!#link("scatter_plot_v3.svg")[Scatter plot: d/acc alignment vs transformative potential]

The upper-right quadrant — high transformative potential and strong d/acc alignment — contains the systems most worth prioritizing: those that could change how societies coordinate while distributing power rather than concentrating it. This is where we find _Community-Governed AI Mesh Systems_, the _Universal AI Learning UnCommons_, and _Moral Trade_.

The upper-left quadrant highlights transformative systems with weaker d/acc alignment — powerful but potentially centralizing. Several neurotechnology entities fall here, reflecting BCIs' enormous potential alongside unresolved questions about who controls neural data.

Most entities cluster in the mid-range of both axes, indicating meaningful but not yet paradigm-shifting systems that are still in early development stages.

=== Maturity Distribution


#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*TRL Range*],
  table.cell[*Description*],
  table.cell[*Count*],
  table.cell[1-2],
  table.cell[Conceptual / early research],
  table.cell[34],
  table.cell[3-4],
  table.cell[Proof of concept / early validation],
  table.cell[105],
  table.cell[5-6],
  table.cell[Prototype / operational in limited context],
  table.cell[41],
  table.cell[7-8],
  table.cell[Near deployment],
  table.cell[9],
)


The average TRL of 3.9 places the field, in aggregate, between proof-of-concept and early validation. This is not a list of things almost ready to ship — it is a map of things that need patient capital and sustained attention.

=== Bottleneck and Action Distribution


The most common bottleneck is coordination (76 entities), followed by regulation (57), engineering (24), social acceptance (13), and funding (7). That funding ranks last challenges the common assumption that emerging technology primarily needs more capital. The scarcest resource appears to be institutional glue — shared standards, protocols, and governance frameworks.

Recommended actions mirror this: 68 entities most need research, 58 need convening, 39 need advocacy, 17 need building, and 7 need funding.

#line(length: 100%, stroke: 0.5pt + luma(180))


== 4. Spotlight Entities (Tier 1)


The following 19 entities scored highest on our composite metric (d/acc alignment + transformative potential + actionability). Each represents a system that doesn't yet exist but is already shaping coordination and investment.

=== Community-Governed AI Mesh Systems

_Decentralized & Democratic Institutions_ | Composite: 21

Decentralized AI networks trained on locally governed data and stewarded by community trust circles rather than centralized corporate or state actors.

_How it works._ Local communities retain sovereignty over data used to train and fine-tune AI models, with governance handled by designated trust circles (particularly Indigenous and racialized community groups) operating under consent frameworks those communities define. A #link("https://en.wikipedia.org/wiki/Mesh_networking")[mesh architecture] distributes both compute and decision-making authority across nodes, so no single actor controls the system. #link("https://flower.ai")[Flower] and #link("https://www.openmined.org")[OpenMined] have proven #link("https://en.wikipedia.org/wiki/Federated_learning")[federated learning] works. #link("https://www.gida-global.org")[GIDA] has proven Indigenous data governance works. Mesh networks work. But nobody has tried to wire them together, partly because the governance conversations happen in completely different rooms from the engineering ones.

_Who's building toward this._ #link("https://flower.ai")[Flower (adap gmbh)] and OpenMined (#link("https://github.com/OpenMined/PySyft")[PySyft]) provide production-grade federated learning infrastructure for distributed model training. The #link("https://www.gida-global.org")[Global Indigenous Data Alliance] stewards the #link("https://en.wikipedia.org/wiki/CARE_Principles_for_Indigenous_Data_Governance")[CARE Principles], and #link("https://localcontexts.org")[Local Contexts] supports Indigenous data sovereignty and cultural heritage protection in digital systems. #link("https://bittensor.com")[Bittensor] is building decentralized AI infrastructure with community-governed token incentives. No dedicated funding for an integrated system has been identified. _TRL: 4_—individual components are mature and deployed; full integration remains unbuilt.

_d/acc alignment._ This entity scores at the ceiling on Democratic (5/5) and Decentralized (5/5) dimensions, reflecting structural governance design that places decision-making authority with affected communities rather than extracting it upward. Defensive posture scores 4/5, as the architecture resists both corporate data capture and state surveillance by design. Key research underpinning this space includes #link("https://arxiv.org/abs/2007.14390")[FLOWER: A Friendly Federated Learning Framework] (2020), #link("https://datascience.codata.org/articles/dsj-2020-043")[The CARE Principles for Indigenous Data Governance] (2019), and UNESCO's report on #link("https://www.unesco.org/ethics-ai/en/articles/new-report-and-guidelines-indigenous-data-sovereignty-artificial-intelligence-developments")[Indigenous People-Centered AI] (2024). (Source: #link("https://worlds.existentialhope.com/world/the-living-rights-network/")[the-living-rights-network])

#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ Convene a working group that puts Indigenous data governance leaders, federated learning developers (Flower, OpenMined), and mesh network operators in the same room to draft interoperability standards and shared governance protocols—this coordination work is the actual bottleneck, not missing technology. A funder could seed that process directly by commissioning a joint technical-governance scoping study across these currently siloed communities.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["communities shaped by displacement, colonization, and exclusion are building decentralized, care-centered mesh networks. These relational systems are trained on locally governed data, stewarded by Indigenous and racialized trust circles, and guided by protocols rooted in consent, dignity, and interdependence—not control." — _Source: #link("https://worlds.existentialhope.com/world/the-living-rights-network/")[the-living-rights-network]_]


=== Universal AI Learning UnCommons (UALU)

_Education, Development & Human Flourishing_ | Composite: 20

A federated governance institution that develops, maintains, and audits AI education tools through multi-stakeholder councils including elders, learners, and ethicists.

_How it works._ UALU operates as a decentralized network of community nodes that co-create and oversee AI educational tools, with governance councils composed of elders, learners, technologists, and ethicists conducting regular audits and setting standards for bias mitigation and cultural appropriateness. The federated structure enables local adaptation while maintaining shared accountability frameworks across the network. #link("https://en.wikipedia.org/wiki/Mozilla")[Mozilla] funds AI governance. The #link("https://au.int/en/pressreleases/20240617/african-ministers-adopt-landmark-continental-artificial-intelligence-strategy")[African Union Commission] is building a continental AI strategy. #link("https://en.unesco.org/")[UNESCO] sets ethics standards, including its #link("https://www.unesco.org/en/artificial-intelligence/recommendation-ethics")[Recommendation on the Ethics of AI] (2021). But none of them have binding enforcement mechanisms that give elder councils actual veto power over AI tools.

_Who's building toward this._ #link("https://www.mozillafoundation.org/en/internet-health/trustworthy-artificial-intelligence/")[Mozilla Foundation] has committed \$2.7M (2023) for its Responsible Computing Challenge across Kenya, India, and the US, and \$1M (2025–2027) for its Democracy x AI Cohort. The African Union Commission is developing a Continental AI Strategy and Digital Education Strategy (2023–2028) through multi-stakeholder consultation. UNESCO is establishing AI ethics standards and competency frameworks for students and teachers. #link("https://aign.global/ai-governance-framework/global-ai-governance-framework/education-ai-governance-framework/")[AIGN] is developing operational AI governance frameworks for schools and universities with audit mechanisms. #link("https://idrc-crdi.ca/en/research-in-action/commitment-action-advancing-use-ai-education-africa")[IDRC] supports the EmpowerED initiative for responsible AI implementation in African education systems. The project sits at _TRL 3_—conceptual frameworks are mature, but no fully operational federated institution with formal elder council oversight exists at scale.

_d/acc alignment._ UALU scores highest on Democratic (5/5) and Defensive (5/5), reflecting its structural commitment to participatory oversight and harm mitigation through community-led auditing. Decentralization scores 4/5, grounded in the federated node architecture. Relevant publications include Mozilla's #link("https://assets.mofoprod.net/network/documents/Mozilla-Trustworthy_AI.pdf")[Creating Trustworthy AI] (2020), the OECD's #link("https://www.oecd.org/en/publications/oecd-digital-education-outlook-2023_c74f03de-en/full-report/multi-stakeholder-collaboration-and-co-creation-towards-responsible-application-of-ai-in-education_07fbbd0d.html")[Multi-stakeholder collaboration and co-creation: towards responsible application of AI in education] (2023), and #link("https://arxiv.org/html/2509.06176v1")[AI Governance in Higher Education] (2025). (Source: #link("https://worlds.existentialhope.com/world/the-learning-uncommons-of-2035/")[the-learning-uncommons-of-2035])

#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ A funder or institutional actor could convene a working group drawing on Mozilla, AIGN, UNESCO, and African Union representatives to design a pilot federated governance structure—the funding exists across these organizations but lacks a coordinating mechanism to integrate elder council participation with operational audit processes.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["A federated, community-led network responsible for developing, maintaining, and auditing AI education tools. Overseen by councils including elders, learners, technologists, and ethicists to uphold justice and care." — _Source: #link("https://worlds.existentialhope.com/world/the-learning-uncommons-of-2035/")[the-learning-uncommons-of-2035]_]


=== AI cryptographic oracle with zero-knowledge IoT auditing and jury-DAO

_Decentralized & Democratic Institutions_ | Composite: 19

A fraud-resistance layer combining #link("https://en.wikipedia.org/wiki/Zero-knowledge_proof")[zero-knowledge proofs] from IoT sensor data, AI anomaly detection, stake-slashing penalties, and a decentralized human jury for retroactive balance correction.

_How it works._ #link("https://en.wikipedia.org/wiki/Internet_of_things")[IoT] devices generate zero-knowledge proofs of their sensor readings, letting a ledger verify data authenticity without exposing raw feeds that could be spoofed or fabricated. An AI layer monitors token-minting patterns for statistical anomalies, while actors caught cheating face quadratic slashing, penalties that scale super-linearly with stake size to neutralize "too-big-to-fail" manipulation. A randomly selected jury-DAO of token holders can then vote to retroactively adjust balances, placing a human override on top of automated enforcement.

_Who's building toward this._ #link("https://www.risczero.com/")[_RISC Zero_] provides the zero-knowledge virtual machine for proof generation. #link("https://chain.link/")[_Chainlink_] and #link("https://api3.org/")[_API3_] supply decentralized #link("https://en.wikipedia.org/wiki/Blockchain_oracle")[oracle] infrastructure. #link("https://kleros.io/")[_Kleros_] has operated a live jury-DAO since 2018, handling 1,000+ cases. Slashing mechanisms are operational in #link("https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/")[Ethereum proof-of-stake]. The gap is not that nobody has the pieces but that nobody has tried to combine ZK-IoT with AI anomaly detection under DAO adjudication — the trust boundaries between these systems are undefined. TRL: 4; ZK-IoT proofs demonstrated on #link("https://en.wikipedia.org/wiki/ESP32")[ESP32] microcontrollers at ~700ms.

_d/acc alignment._ Defensive scores highest at 5/5, reflecting the system's explicit design to detect and penalize fraud at multiple layers. Democratic and Decentralized both score 4/5, driven by the jury-DAO's human override capacity and the absence of any central arbiter. The research base includes #link("https://arxiv.org/html/2402.08322v2")[zk-IoT: Securing the Internet of Things with Zero-Knowledge Proofs on Blockchain Platforms] (2024), #link("https://arxiv.org/html/2401.03530v1")[Detecting Anomalies in Blockchain Transactions using Machine Learning Classifiers and Explainability Analysis] (2024), and #link("https://www.mdpi.com/2076-3417/15/15/8330")[Anomaly Detection in Blockchain: A Systematic Review] (2025). (Source: #link("https://worlds.existentialhope.com/world/hybrid-market/")[hybrid-market])

#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ A researcher or cryptoeconomics team could publish a formal integration specification—defining the trust boundaries, oracle assumptions, and incentive parameters needed to combine ZK-IoT proofs, AI anomaly detection, quadratic slashing, and DAO adjudication into a coherent system. A funder could convene Kleros, RISC Zero, and a blockchain ML group around a shared testnet deployment to resolve the coordination gap blocking production-scale validation.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["A hard-fork deployed AI cryptographic oracles tied to sensor roots for zero-knowledge IoT based auditing, quadratic-stake slashing to take on 'too-big-to-fail' cheaters, and a jury-DAO to retro-adjust balances." — _Source: #link("https://worlds.existentialhope.com/world/hybrid-market/")[hybrid-market]_]


=== Moral Trade

_AI-Mediated Deliberation & Collective Intelligence_ | Composite: 18

A mechanism by which people or groups with different moral priorities swap concessions so that each gets more of what they care about than unilateral action would yield.

_How it works._ Moral trade applies the logic of economic exchange to ethical preferences: parties identify where their moral priorities are relatively cheap for the other side to accommodate, then negotiate exchanges that leave both better off by their own values. At civilizational scale, this could allow diverse moral communities to each achieve far more of their valued outcomes than competition or majority-rule permits, without requiring any single ethical framework to dominate. #link("https://en.wikipedia.org/wiki/Toby_Ord")[Toby Ord] formalized the concept academically in his paper #link("https://www.journals.uchicago.edu/doi/10.1086/682187")[Moral Trade] (2015); informal versions already occur in activist coalition bargaining and #link("https://en.wikipedia.org/wiki/Effective_altruism")[effective altruism] cause prioritization.

_Who's building toward this._ The #link("https://www.fhi.ox.ac.uk/")[Future of Humanity Institute] and #link("https://en.wikipedia.org/wiki/University_of_Oxford")[University of Oxford] provided the academic home for Toby Ord's foundational theoretical work. The #link("https://www.effectivealtruism.org/")[Effective Altruism] community has explored small-scale applications through informal coordination on charitable donations across cause areas. No dedicated funding has been identified, and the concept sits at TRL 2—theorized and occasionally applied ad hoc, but without formal institutional infrastructure or governance mechanisms.

_d/acc alignment._ Moral trade scores highest on Democratic (5/5) and Decentralized (4/5) dimensions, reflecting its core design goal of enabling pluralistic coordination without imposing a dominant moral framework. Defensive and Differential scores are lower, as the concept addresses coordination rather than security or targeted acceleration. Recent work includes #link("https://forum.effectivealtruism.org/posts/L76qZhfvkediwXd6f/moral-public-goods-are-a-big-deal-for-whether-we-get-a-good")[Moral public goods are a big deal for whether we get a good future] (2025) and a #link("https://forum.effectivealtruism.org/posts/jvW6p5Hk2r4883tNT/moral-trade-proposal-with-95-100-surplus")[Moral Trade Proposal with 95-100% Surplus] (2024). (Source: #link("https://finmoorhouse.com/")[Fin Moorhouse] — #link("https://www.existentialhope.com/podcasts/fin-moorhouse-why-we-need-to-aim-higher-than-survival")[fin-moorhouse-why-we-need-to-aim-higher-than-survival])


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ A researcher or funder could commission a systematic mapping of existing informal moral trade instances across activist coalitions, international negotiations, and EA cause prioritization to identify which coordination mechanisms succeeded and why. A builder with AI expertise could prototype a preference-elicitation and matching tool — the #link("https://en.wikipedia.org/wiki/Fair_division")[fair-division] literature already has working algorithms (#link("https://en.wikipedia.org/wiki/Adjusted_winner_procedure")[Adjusted Winner], #link("http://spliddit.org/")[Spliddit]) that handle analogous problems — to help parties identify low-cost concessions across moral domains.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["Let's say you really care that people abstain from eating meat, and I really care about people reducing their carbon footprint. Maybe it's not much of a cost for me to eliminate meat from my diet, and it's not much of a cost for you to offset your emissions. Then we have an opportunity for a deal where I eat less meat and you reduce your carbon footprint... if you scale it up to the level of a civilization, there are huge opportunities." — _Source: #link("https://www.existentialhope.com/podcasts/fin-moorhouse-why-we-need-to-aim-higher-than-survival")[podcasts]_]


=== BCI Operating System (BCI-OS)

_Neurotechnology & Brain-Computer Interfaces_ | Composite: 18

An open-source operating system layer for #link("https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface")[brain-computer interfaces] that embeds agency evaluation, AI model compatibility, and privacy standards as core OS-level features.

_How it works._ BCI-OS sits between BCI hardware and applications, enforcing privacy protocols and agency evaluations at the OS level rather than delegating them to individual apps. Standardized model compatibility protocols enable interoperability across hardware manufacturers. An open-source governance structure and standards body maintain human-agency principles, with academic and industry pilots iteratively refining the system.

_Who's building toward this._ #link("https://openbci.com/")[OpenBCI] provides open-source hardware and software platforms with community adoption but without unified privacy or agency frameworks. #link("https://www.ae.studio/brain-computer-interface")[AE Studio] is developing agency-focused BCI tools including the Neurotech Development Kit, with neuroethical principles embedded in its approach. The #link("https://fpf.org")[Future of Privacy Forum] is researching BCI-specific data protection standards, and the #link("https://standards.ieee.org/")[IEEE Standards Association] published a 2024 Standards Roadmap for Neurotechnologies for Machine Interfacing covering sensing, feedback, and data management. No dedicated funding for a unified BCI-OS has been identified. TRL: 3.

_d/acc alignment._ BCI-OS scores highest on Defensive (5/5) and Democratic (4/5), reflecting its core architectural commitment to protecting user agency and neural data privacy, and its open-source governance model that distributes control away from any single manufacturer. Key references include #link("https://arxiv.org/abs/2201.07711")[Enhancing the Security & Privacy of Wearable Brain-Computer Interfaces] (2022), the IEEE #link("https://standards.ieee.org/wp-content/uploads/import/documents/presentations/ieee-neurotech-for-bmi-standards-roadmap.pdf")[Standards Roadmap: Neurotechnologies for Machine Interfacing] (2024), and the GAO report on #link("https://www.gao.gov/products/gao-25-106952")[Brain-Computer Interfaces: Applications, Challenges, and Policy Options] (2025).


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ A funder or institution could convene a working group pulling together OpenBCI, AE Studio, IEEE, #link("https://en.wikipedia.org/wiki/Food_and_Drug_Administration")[FDA] representatives, and privacy researchers to draft a governance charter and interoperability specification for BCI-OS. The fragmented ecosystem is the binding constraint, not technical readiness. That alone won't solve the problem, but right now these groups aren't even using the same vocabulary for agency evaluation, which makes everything downstream harder.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["['The Open Source BCI Project: Create an open-source brain-computer interface (BCI) operating system to enhance human cognitive abilities and privacy in a TAI era.', 'Develop a privacy-preserving, open-source BCI operating system (BCI-OS) that enhances human cognitive abilities and safeguards human-agency in the TAI era. Integrated agency evaluations, model compatibility protocols, and robust data privacy standards in the BCI-OS.']" — _Source: Diogo de Lucena, Judd Rosenblatt, Mamun Miah_]


=== Tokenized neural data sharing with selective disclosure

_Neurotechnology & Brain-Computer Interfaces_ | Composite: 17

Rather than broadcasting all neural data, the system segments and tokenizes different categories of neural output (emotional states, motor intentions, cognitive content), allowing users to grant or revoke access to specific tokens — a form of #link("https://en.wikipedia.org/wiki/Selective_disclosure")[selective disclosure]. Think #link("https://en.wikipedia.org/wiki/OAuth")[OAuth] scopes for your brain: share an emotional state with a therapist, keep everything else private. Existing healthcare privacy frameworks, including #link("https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act")[HIPAA] and #link("https://leg.mt.gov/bills/2025/billpdf/SB0163.pdf")[Montana's neuro-rights law], provide the regulatory scaffolding on which such an architecture would sit (see #link("https://journals.sagepub.com/doi/10.1177/20552076251326123")[Regulating neural data processing in the age of BCIs], 2025; #link("https://arxiv.org/abs/2209.09653")[A Framework for Preserving Privacy and Cybersecurity in BCI Applications], 2022; and #link("https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1330439/full")[Chilean Supreme Court ruling on the protection of brain activity], 2024). The concept was discussed in a #link("https://www.existentialhope.com/podcasts/mary-lou-jepsen-a-handheld-device-to-defeat-cancer")[podcast] with #link("https://en.wikipedia.org/wiki/Mary_Lou_Jepsen")[Mary Lou Jepsen] on Existential Hope.

_Who's building toward this._ The #link("https://www.neurorightsfoundation.org")[Neurorights Foundation] drives advocacy and state-level legislation for neural data privacy. The #link("https://fpf.org")[Future of Privacy Forum] produces research and guidance on BCI privacy frameworks. #link("https://zuckermaninstitute.columbia.edu/neurotechnology-center")[Columbia University's Neurotechnology Center], led by #link("https://en.wikipedia.org/wiki/Rafael_Yuste")[Rafael Yuste], works on neurorights and data protection frameworks. No funding for this specific architecture has been documented. _TRL: 2_ — regulatory concepts exist and are codified in #link("https://leg.colorado.gov/bills/hb24-1058")[Colorado], California, Montana, and #link("https://www.jurist.org/news/2021/10/chile-becomes-first-country-to-pass-neuro-rights-law/")[Chile's constitutional protections], but no BCI system with tokenized selective-disclosure has been deployed or demonstrated.

_d/acc alignment._ This scores highest on Defensive (5/5) and Democratic empowerment (4/5), reflecting its core function as a user-controlled protection against involuntary neural data exposure. Decentralization scores lower (2/5) because current implementations rely on centralized regulatory and institutional frameworks.


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ Policy advocates and legal researchers should push for federal technical standards that define granular consent mechanisms for neural data—without unified specifications, companies have no regulatory incentive to build tokenized architectures. Organizations with healthcare IT expertise could draft model technical standards bridging existing OAuth-style access control frameworks to BCI data streams, giving regulators concrete language to adopt.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["I think it'll be tokenized, basically. You'll let certain parts of what you want to share out, and you'll keep what you want as your innermost thoughts to yourself. Or perhaps you'll have relationships where you wish to share your innermost thoughts." — _Source: #link("https://www.existentialhope.com/podcasts/mary-lou-jepsen-a-handheld-device-to-defeat-cancer")[podcasts]_]


=== Civic Systems Co-Op

_AI Safety, Alignment & Governance_ | Composite: 17

A global open-source consortium that develops and maintains ethical AI tools for municipal and community governance.

_How it works._ Member cities and communities contribute to and draw from a shared repository of AI governance tools, with the consortium setting ethical standards and maintaining transparent decision logs. Governance is distributed across member organizations rather than controlled by a single vendor or government, keeping systems adaptable to local needs. #link("https://digitalpublicgoods.xyz/")[DPGA] has a registry of 150+ #link("https://en.wikipedia.org/wiki/Open-source_software")[open-source] governance tools but no shared development infrastructure. #link("https://www.opengovpartnership.org/")[OGP] has the political relationships but no technical platform. #link("https://opengov.com/")[OpenGov] has the platform but locks cities into a proprietary vendor. A #link("https://en.wikipedia.org/wiki/Cooperative")[cooperative] model would sit between these, combining what each has without the constraints each imposes.

_Who's building toward this._ The #link("https://digitalpublicgoods.xyz/")[_Digital Public Goods Alliance_] (UN-endorsed) maintains a registry of 150+ open-source governance solutions and provides the closest structural analog to a coordinating body. The #link("https://www.opengovpartnership.org/")[_Open Government Partnership_] promotes transparency and accountability frameworks across local and national governments. #link("https://opengov.com/")[_OpenGov_] demonstrates commercial viability with AI-enabled tools for budgeting, permitting, and public engagement across 2,000+ US communities. The #link("https://okfn.org/")[_Open Knowledge Foundation_] develops open-source standards and civic tech tools as a DPGA member. No dedicated funding for a unified consortium has been identified. TRL: 5 — field-tested components exist, but a true cooperative with distributed member control remains at prototype stage. Recent research highlights both the opportunity and the gap: see OGP's #link("https://www.opengovpartnership.org/documents/artificial-intelligence-and-open-government-local-perspectives-2025/")[Artificial Intelligence and Open Government: Local Perspectives] (2025) and #link("https://www.opengovpartnership.org/stories/building-accountable-artificial-intelligence-in-government-a-practical-reform-agenda/")[Building Accountable AI in Government] (2025). The concept originates from the #link("https://worlds.existentialhope.com/world/the-commons-cloud/")[Commons Cloud] scenario on Existential Hope.

_d/acc alignment._ Democratic (4/5), Decentralized (4/5), and Defensive (4/5) scores are all strong, reflecting the model's emphasis on distributed control, member accountability, and protection against vendor lock-in. Differential impact scores lower (2/5) because the mechanism operates within #link("https://en.wikipedia.org/wiki/Civic_technology")[civic tech] rather than across multiple domains.


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ If DPGA won't convene this, a city coalition should just start drafting a consortium charter and contribution model with two or three willing municipalities. The interoperability requirements across current municipal AI deployments need mapping to define the technical baseline a shared repository would need to meet. Waiting for a top-down coordination mandate hasn't worked so far.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["The Civic Systems Co-Op: a global open-source consortium maintaining ethical, adaptable AI systems for cities and communities." — _Source: #link("https://worlds.existentialhope.com/world/the-commons-cloud/")[the-commons-cloud]_]


=== Interbeing Forum

_Decentralized & Democratic Institutions_ | Composite: 17

#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["The Interbeing Forum is a rotating assembly of stewards from across bioregions. It includes people, yes, but also guardians (advised by digital twins) for rivers, soils, and future generations. It oversees the Commonsense Accord and safeguards the integrity of the digital twin ecosystem." — _Source: #link("https://worlds.existentialhope.com/world/the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences/")[the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences]_]


A rotating #link("https://en.wikipedia.org/wiki/Bioregionalism")[bioregional] assembly that grants formal representation to ecosystems and future generations through human guardians advised by #link("https://en.wikipedia.org/wiki/Digital_twin")[digital twin] data.

_How it works._ Stewards selected on a rotating basis from bioregions govern through a binding accord, preventing any single faction from entrenching power. Designated guardians speak for non-human entities (rivers, soils) and for future generations, with their positions informed by real-time ecological data from digital twin systems. The assembly also audits that digital infrastructure directly, ensuring it remains a tool of democratic participation rather than centralized control.

_Who's building toward this._ #link("https://lina.community/projects/8e9dd1ac-2b08-4136-9680-d365de3de61b/")[bioregional.agency] (Austria, co-founded 2025 by Gordon Selbach and Jakob Travnik) is piloting bioregional assembly practices; #link("https://resilience.earth/")[Resilience.Earth] is developing distributed decision-making and adaptive governance tools for bioregional communities; #link("https://cascadiabioregion.org/")[Department of Bioregion / CascadiaNow!] has advanced bioregional education across the Cascadia region since 2005; and the #link("https://cascadiabioregion.org/ozarks-bioregion")[Ozark Area Community Congress] has operated a rotating, consensus-based bioregional assembly in the Ozarks since 1980. No dedicated funding has been identified for the integrated _Interbeing Forum_ model. TRL: 3. The Ozark Area Community Congress has run a rotating bioregional assembly since 1980, but without ecosystem guardianship. New Zealand's #link("https://en.wikipedia.org/wiki/Environmental_personhood#New_Zealand")[Whanganui River] has #link("https://en.wikipedia.org/wiki/Environmental_personhood")[legal personhood], but without a bioregional assembly. Nobody has tried both at once. Key research framing the opportunity includes #link("https://compass.onlinelibrary.wiley.com/doi/full/10.1111/gec3.12722")[Where are you at? Re-engaging bioregional ideas] (2023), #link("https://www.sciencedirect.com/science/article/pii/S2589811625000424")[Cyber-governance of the natural world: digital twins in environmental governance] (2025), and #link("https://www.mdpi.com/2673-4591/120/1/32")[Digital Collaborative Mechanism of Ecological Governance Based on Digital Twin] (2026).

_d/acc alignment._ Democratic and Decentralized dimensions both score 4/5, reflecting the rotating stewardship structure and formal power-sharing across bioregions that structurally resists capture. Differential scores lowest (2/5), as the model does not yet create new civilizational action space beyond the governance domain.


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ Legal advocates and policy researchers should work to establish or extend ecosystem legal personhood frameworks, building on New Zealand's Whanganui River precedent and Wales's #link("https://en.wikipedia.org/wiki/Future_Generations_Commissioner_for_Wales")[Future Generations Commissioner], into cross-jurisdictional bioregional contexts. Connecting existing practitioners (OACC, bioregional.agency) with environmental digital twin researchers would accelerate the governance integration that no institution has yet achieved.]


=== Interoperable Governance Protocol Stack

_Decentralized & Democratic Institutions_ | Composite: 16

A shared technical and governance protocol layer that allows citizens to port #link("https://en.wikipedia.org/wiki/Digital_identity")[digital identities], benefits, and credentials across distinct federated city-state systems, and enables AI systems across those jurisdictions to align resource allocation and crisis modeling.

The protocol stack defines common standards for digital identity, benefits entitlements, and credentials so that any compliant local system can read and honor records issued by another. During crises, federated AI systems across jurisdictions share resource allocation decisions and logistics data in a machine-readable format. Governance modules are deliberately modular: jurisdictions can adopt the stack without surrendering local policy autonomy.

The #link("https://openid.net/")[_OpenID Foundation_] completed a #link("https://openid.net/openid-foundation-demonstrates-real-world-interoperabiity-of-new-digital-identity-standards/")[real-world multi-region interoperability demonstration] in May 2025. #link("https://www.w3.org/")[_W3C_] maintains #link("https://www.w3.org/TR/did-1.1/")[Decentralized Identifiers (DIDs)] and #link("https://www.w3.org/TR/vc-data-model-2.0/")[Verifiable Credentials] standards. The #link("https://www.trustoverip.org/")[_Trust Over IP Foundation_] is developing governance frameworks for decentralized digital trust, and #link("https://govstack.global/")[_GovStack_] is assembling modular government building blocks covering identity, payments, and data exchange. Core identity standards are in production pilots across the EU, UK, Switzerland, Japan, and California, but the combined benefits-portability-plus-AI-crisis-coordination system remains at prototype stage. TRL: 4. Relevant research includes #link("https://arxiv.org/pdf/2601.14982")[Interoperable Architecture for Digital Identity Delegation for AI Agents with Blockchain Integration] (2026) and #link("https://www.arxiv.org/pdf/2510.16034")[Disaster Management in the Era of Agentic AI Systems: A Vision for Federated Crisis Response] (2025).

_d/acc alignment._ Decentralized (4/5) and Defensive (4/5) are the strongest dimensions: the modular architecture preserves jurisdictional autonomy while the crisis coordination capability directly reduces harm from disasters. Democratic alignment (3/5) reflects meaningful but incomplete citizen-facing benefits, and Differential (2/5) is low because the underlying technologies are established rather than frontier.


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ Convene a working group that brings together municipal governments, standards bodies, and emergency management agencies to draft a model mutual-recognition agreement for cross-jurisdictional verifiable credentials — starting with a bilateral pilot between two willing cities. Engaging regulators early to establish shared legal frameworks for benefits eligibility translation matters more than any technical work right now, because regulatory fragmentation is the primary bottleneck.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["A coalition of federated city-states launches the first interoperable governance protocol stack, allowing citizens to carry digital IDs, benefits, and credentials between different local systems. When severe flooding hits multiple jurisdictions, modular governance systems coordinate relief in hours instead of weeks, sharing resources and logistics seamlessly across local and regional levels." — _Source: N/A_]


=== Comprehensive AI Services (Drexler)

_AI Safety, Alignment & Governance_ | Composite: 16

An architecture of many narrow, domain-limited superhuman AIs that interact competitively rather than a single general #link("https://en.wikipedia.org/wiki/Superintelligence")[superintelligence], achieving safety through structural narrowness.

_How it works._ Rather than building one general-purpose superintelligent system, AI capabilities are deliberately partitioned into domain-specific services that are superhuman within their lane but architecturally prevented from generalizing beyond it. The resulting ecology of competing specialized systems provides checks analogous to market competition or ecological balance, making unilateral takeover or unexpected generalization structurally difficult. Can you wire together narrow AIs without accidentally building a general one? That's the core unsolved question. Safety here comes from the architecture itself, not from aligning a single powerful agent.

_Who's building toward this._ No organization is deliberately implementing CAIS as a unified design paradigm. The #link("https://www.fhi.ox.ac.uk")[Future of Humanity Institute] at the University of Oxford published #link("https://en.wikipedia.org/wiki/K._Eric_Drexler")[K. Eric Drexler]'s foundational 2019 technical report, #link("https://www.fhi.ox.ac.uk/publications/reframing-superintelligence-comprehensive-ai-services-as-general-intelligence-technical-report-2019-1-k-eric-drexler/")[_Reframing Superintelligence_], which remains the primary articulation of the framework. Individual narrow superhuman AIs—#link("https://en.wikipedia.org/wiki/AlphaFold")[AlphaFold], chess engines—demonstrate isolated components, but without architectural enforcement of narrowness or a competitive service ecology. No dedicated funding has been identified. TRL: 2. The concept was discussed in a #link("https://www.existentialhope.com/podcasts/nathan-labenz-what-are-the-best-case-scenarios-for-ai")[podcast with Nathan Labenz] on Existential Hope.

_d/acc alignment._ CAIS scores highest on Decentralized (4/5) and Defensive (4/5), reflecting its structural resistance to power concentration and its safety-by-design approach. The low Differential score (2/5) reflects the absence of any implementation pathway that would accelerate this approach relative to general-purpose foundation models.


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ Who funds the #link("https://en.wikipedia.org/wiki/Formal_verification")[formal verification] work? The core unsolved problem is whether service composition across domain-limited AIs can be architecturally bounded to prevent emergent generalization. On the policy side, a regulatory proposal requiring capability partitioning disclosures for frontier model developers would create the coordination infrastructure the CAIS model currently lacks entirely.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["It's safety through narrowness. It's not to say that the AIs aren't really good at what they do—they could be superhuman at what they do—but in the same way that we have superhuman chess players that can only play chess, and we have superhuman protein folding AIs that can only fold protein, you don't really have to worry that that's going to do something surprising... I think that would be a really good design decision if we could manage it: to have AIs that are potentially superhuman in their domain but are in a pretty fundamental way limited to their domain so they don't do an end-run around whatever guardrails we've put in place." — _Source: #link("https://www.existentialhope.com/podcasts/nathan-labenz-what-are-the-best-case-scenarios-for-ai")[podcasts]_]


=== Attack Dog DAO for Climate

_Ecological & Regenerative Systems_ | Composite: 16

A #link("https://en.wikipedia.org/wiki/Decentralized_autonomous_organization")[DAO] that funds and coordinates environmental litigation on behalf of legally-recognized natural entities, financed through tokenized litigation investment. The idea was #link("https://www.existentialhope.com/podcasts/trent-mcconaghy-from-starships-to-tokens-pioneering-futures")[proposed in a conversation about combining crypto mechanisms with climate action].

_How it works._ Natural bodies granted #link("https://scholars.unh.edu/unh_lr/vol17/iss2/13/")[legal personhood]—rivers, lakes—become plaintiffs in lawsuits against polluters. A DAO pools capital from investors through tokenized litigation finance mechanisms, funding those cases and returning proceeds to investors when litigation succeeds. Investors profit when the lawsuits win. The lawsuits win when polluters lose. That's the whole trick. The #link("https://theconversation.com/granting-legal-personhood-to-nature-is-a-growing-movement-can-it-stem-biodiversity-loss-227336")[movement to grant legal personhood to nature is growing], expanding the potential plaintiff pool.

_Who's building toward this._ The closest attempt was Aristata Capital, which explored climate litigation finance but stopped short of DAO governance or tokenization. Adjacent work is underway from several directions. #link("https://www.ryval.io")[_Ryval_] pioneered #link("https://arbitrationblog.kluwerarbitration.com/2022/03/16/litigation-finance-and-crypto-tokens-how-a-blockchain-startup-seeks-to-create-financing-marketplaces-for-disputes/")[tokenized litigation finance] via Initial Litigation Offerings on blockchain, completing its first ILO in October 2021. #link("https://www.lawcoin.io")[_LawCoin_] tokenizes litigation finance deals on #link("https://en.wikipedia.org/wiki/Ethereum")[Ethereum] for institutional investors. #link("https://www.medicoin.io")[_MediCoin_] has tokenized attorney fee interests specifically in environmental litigation, including #link("https://en.wikipedia.org/wiki/Per-_and_polyfluoroalkyl_substances")[PFAS] cases. #link("https://www.clientearth.org")[_ClientEarth_], the environmental law firm, has inspired litigation finance focused on climate cases through Aristata Capital. No known entity has combined environmental personhood, DAO governance, and tokenized litigation finance into a deployed system. TRL: 3. Funding: none identified for an integrated implementation.

_d/acc alignment._ The concept scores highest on democratic distribution (4/5) and defensive posture (4/5)—it distributes access to legal enforcement mechanisms and directly counters harmful actors—while decentralization is constrained (3/5) by guardian bottlenecks and DAO liability exposure under current law.


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ If ClientEarth or a similar environmental law firm won't pilot a DAO-governed litigation fund, a crypto-native legal team should just build one and let courts sort out the liability questions — the precedent-setting value alone justifies the risk. Separately, engaging securities regulators on the classification of tokenized litigation interests would unblock retail investor participation.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["One approach is creating an attack dog DAO (Decentralized Autonomous Organization) for climate, similar to the Electronic Frontier Foundation but focused on environmental issues. This DAO could sue on behalf of natural bodies, like rivers or lakes, that have been granted legal personhood. It would leverage litigation finance, where people can invest in these legal battles." — _Source: #link("https://www.existentialhope.com/podcasts/trent-mcconaghy-from-starships-to-tokens-pioneering-futures")[podcasts]_]


=== Wisdom DAO

_Decentralized & Democratic Institutions_ | Composite: 16

A #link("https://en.wikipedia.org/wiki/Decentralized_autonomous_organization")[decentralized autonomous organization] where human citizens and AI systems jointly propose, deliberate, and vote on governance policy using weighted voting and #link("https://en.wikipedia.org/wiki/Blockchain")[blockchain] transparency. The concept originates from the #link("https://worlds.existentialhope.com/world/worldbuilding-course-worldbuilding-toolbox-world-entry-page-world-gallery-x-twitter-instagram-medium-bookmark-sadvipra-ai/")[Sadvipra AI world-building scenario].

_How it works._ Citizens use personal AI assistants (Citizen-AI) to parse proposals and cast informed votes recorded on a blockchain ledger. A second AI layer aggregates votes into policy drafts. Humans still ratify, but execution runs on #link("https://en.wikipedia.org/wiki/Smart_contract")[smart contracts], removing the usual discretionary window between "approved" and "implemented."

_Who's building toward this._ #link("https://near.org")[Near Foundation] is developing AI-powered delegates and the Pulse sentiment-tracking tool for DAO governance. #link("https://singularitynet.io")[SingularityNET] operates a decentralized AI coordination platform using blockchain for service governance and privacy-preserving datasets. #link("https://aragon.org")[Aragon] provides DAO infrastructure and tooling, while #link("https://makerdao.com")[MakerDAO] demonstrates on-chain token-based governance at meaningful scale. No dedicated funding for integrated human-AI hybrid governance DAOs has been identified. _TRL: 4_ — AI agents have been #link("https://arxiv.org/html/2510.21117v2")[tested against 3,383 real proposals] with 97% alignment to historical human decisions, and simulations show a 40% participation increase, but no production deployment at city or national scale exists. Recent research includes a #link("https://arxiv.org/html/2511.08641v1")[stepwise development framework for AI-driven DAOs] and a study on #link("https://www.nature.com/articles/s41598-026-40180-8")[democratic governance through DAO-based deliberation].

_d/acc alignment._ Democratic (4/5) and Decentralized (4/5) are the strongest dimensions, reflecting the system's core design: distributed decision-making authority shared between citizens and AI rather than concentrated in bureaucratic institutions. Defensive scores lower (3/5) because the system's resilience against manipulation and adversarial voting remains unproven at scale.


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ Researchers should publish comparative studies of existing DAO governance pilots—particularly Near Foundation's Pulse deployments—to build the empirical record regulators need to draft workable legal frameworks. Policy advocates should engage directly with #link("https://en.wikipedia.org/wiki/Artificial_Intelligence_Act")[EU AI Act] implementation bodies and #link("https://www.nist.gov/artificial-intelligence")[NIST] to push for explicit guidance on AI-assisted voting systems before legal ambiguity freezes further development.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["Wisdom DAO – Citizens & AIs co-create policy. By 2035, governance shifted from centralized bureaucracy to decentralized wisdom guided by Sadvipra AI and DAOs. People co-create policy with personal AIs, corruption drops through blockchain transparency, and decisions align with dharma." — _Source: #link("https://worlds.existentialhope.com/world/worldbuilding-course-worldbuilding-toolbox-world-entry-page-world-gallery-x-twitter-instagram-medium-bookmark-sadvipra-ai/")[worldbuilding-course-worldbuilding-toolbox-world-entry-page-world-gallery-x-twitter-instagram-medium-bookmark-sadvipra-ai]_]


=== Accord of Watersheds

_International Governance & Coordination_ | Composite: 16

An international treaty framework that organizes political cooperation around #link("https://en.wikipedia.org/wiki/Watershed")[watershed] and bioregional boundaries rather than national borders, envisioned in the #link("https://worlds.existentialhope.com/world/2035-rewild/")[2035 Rewild scenario].

_How it works._ Signatory parties—nations, Indigenous governments, and regional bodies—agree to coordinate resource use, conservation, and conflict resolution according to the boundaries and health of shared watersheds. Governance bodies are constituted around #link("https://en.wikipedia.org/wiki/Drainage_basin")[river basins] or bioregions, with binding obligations tied to ecological indicators rather than national interest. Dispute resolution and resource allocation follow hydrological logic rather than political boundaries.

_Who's building toward this._ The #link("https://ijc.org")[_International Joint Commission (IJC)_] has operated transboundary #link("https://en.wikipedia.org/wiki/Watershed_management")[watershed governance] between Canada and the US since 1909, with its #link("https://ijc.org/en/quarter-century-international-watersheds-initiative")[International Watersheds Initiative] (est. 1998) pioneering ecosystem-centered management with Indigenous participation. The #link("https://www.mrcmekong.org/")[_Mekong River Commission (MRC)_] coordinates four nations using #link("https://en.wikipedia.org/wiki/Integrated_water_resources_management")[integrated water resources management] across the Mekong Basin. The #link("https://www.inbo-news.org/")[_International Network of Basin Organizations (INBO)_] supports 120+ river basin organizations globally. The #link("https://cascadiabioregion.org/")[_Cascadia Department of Bioregion_] is developing bioregional governance frameworks across the Pacific Northwest, while #link("https://resilience.earth/")[_Resilience.Earth_] delivers #link("https://ecolise.eu/wp-content/uploads/2025/03/Bioregional-Governance-Training-Guide.pdf")[bioregional governance training] in Asia-Pacific. No dedicated funding for a unified treaty framework has been identified. TRL: 6—operational regional structures exist, but a binding global framework remains conceptual.

_d/acc alignment._ Scores highest on democratic inclusion (4/5) and defensive orientation (4/5), reflecting its emphasis on multi-stakeholder governance and ecological protection over extractive national interest. Decentralization scores moderate (3/5) because watershed bodies, while sub-national in logic, still require centralized treaty architecture to function. For further context, see "#link("https://www.kosmosjournal.org/article/human-watershed-the-emerging-politics-of-bioregional-democracy/")[Human Watershed: The Emerging Politics of Bioregional Democracy]" (2024).


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ Legal advocates and international law scholars can draft model treaty language that converts existing watershed commission frameworks—IJC, MRC—into a replicable binding instrument with enforceable ecological indicators. Policy advocates with access to #link("https://www.unep.org/environmentassembly/")[UN Environment Assembly] or #link("https://en.wikipedia.org/wiki/Convention_on_Biological_Diversity")[CBD] processes should push for a formal resolution recognizing bioregional governance as a legitimate basis for transboundary treaty obligations.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["The Accord of Watersheds—a treaty system where ecosystems, not nations, are the organizing principle of cooperation." — _Source: #link("https://worlds.existentialhope.com/world/2035-rewild/")[2035-rewild]_]


=== DAO-governed open innovation platform for TLM documentation and training data

_Decentralized & Democratic Institutions_ | Composite: 16

A #link("https://en.wikipedia.org/wiki/Decentralized_autonomous_organization")[DAO]-based governance structure that mandates open-source documentation and community-sourced feedback loops for translation model development and adaptation, as envisioned in #link("https://worlds.existentialhope.com/world/la-langue-de-la-prvoyance/")[La Langue de la Prévoyance].

_How it works._ #link("https://en.wikipedia.org/wiki/Smart_contract")[Smart-contract]-based voting gives communities formal decision-making power over how #link("https://en.wikipedia.org/wiki/Language_model")[translation language model] (TLM) training data is collected, labeled, and updated. #link("https://en.wikipedia.org/wiki/Open_innovation")[Open innovation] platforms serve as the interface for submitting feedback, flagging bias, and proposing model adaptations. Governance rules enforced through the DAO prevent proprietary capture, keeping models and documentation publicly accessible.

_Who's building toward this._ #link("https://huggingface.co")[Hugging Face] hosts over 1,000 community-contributed translation models but has no governance layer for community decision-making over those models. #link("https://commonvoice.mozilla.org")[Mozilla Common Voice] crowdsources multilingual voice data but doesn't give contributors formal control over how it's used. #link("https://oceanprotocol.com")[Ocean Protocol] provides decentralized data exchange with DAO governance and tokenized data assets. #link("https://aragon.org")[Aragon] supplies DAO governance frameworks and is exploring #link("https://blog.aragon.org/ai-daos-the-future-of-daos-powered-by-artificial-intelligence/")[AI-DAO integration]. The missing link is connecting contributor governance to model development decisions. Overall TRL: 3. Relevant research includes work on #link("https://www.sciencedirect.com/science/article/pii/S2096720923000416")[governance of DAOs that produce open source software] and a #link("https://arxiv.org/html/2511.08641")[stepwise development framework for AI-driven DAOs].

_d/acc alignment._ Democratic (4/5) and Decentralized (4/5) are the strongest dimensions, reflecting the core design intent to distribute control over model development away from proprietary actors and toward affected communities. Defensive scores lower (3/5) because the system's protective value depends on successful implementation that has not yet been demonstrated at scale.


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ Convene a working group that brings together Hugging Face contributors, Ocean Protocol governance participants, and multilingual community organizations to design and pilot a DAO governance layer specifically for a production translation model — starting with a bounded language pair to test coordination mechanisms before scaling. A funder could seed this pilot by commissioning a governance design sprint that maps smart-contract voting to concrete model update decisions.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["Decentralized Autonomous Organizations (DAOs) ensure open access to TLM documentation and training data so that communities drive decision-making on model adaptations. Open innovation platforms source community feedback to further transparency and interoperability." — _Source: #link("https://worlds.existentialhope.com/world/la-langue-de-la-prvoyance/")[la-langue-de-la-prvoyance]_]


=== Watershed Parliaments

_Decentralized & Democratic Institutions_ | Composite: 16

#link("https://en.wikipedia.org/wiki/Bioregionalism")[Bioregional] governance bodies organized around watershed boundaries rather than political borders, incorporating ecological feedback into formal decision-making. The concept appears in the #link("https://worlds.existentialhope.com/world/mycelial-democracy/")[Mycelial Democracy scenario].

_How it works._ Governance jurisdiction is defined by hydrological catchment areas, replacing nation-state and municipal lines with boundaries that match the actual movement of water and the ecosystems it sustains. Decision-making bodies include designated representatives for ecosystem interests alongside human citizens. Before adoption, proposals must pass multi-generational impact assessments covering all species within the watershed.

_Who's building toward this._ The #link("https://www.mdba.gov.au/")[_Murray-Darling Basin Authority_] (Australia) manages integrated water resources across a major watershed with Indigenous representation and multi-stakeholder governance. The #link("https://www.srbc.gov/")[_Susquehanna River Basin Commission_] and #link("https://www.potomacriver.org/")[_Interstate Commission on the Potomac River Basin_] coordinate water management across multi-state jurisdictions in North America. The #link("https://cascadiabioregion.org/")[_Cascadia Department of Bioregion_] advocates for watershed-based political restructuring, aligned with the vision of "#link("https://www.kosmosjournal.org/article/human-watershed-the-emerging-politics-of-bioregional-democracy/")[bioregional democracy]" as an emerging political form. New Zealand's #link("https://en.wikipedia.org/wiki/Environmental_personhood#New_Zealand")[Whanganui River], granted #link("https://en.wikipedia.org/wiki/Environmental_personhood")[legal personhood] in 2017, remains the clearest proof-of-concept for ecosystem rights integration. No dedicated funding was identified. TRL: 4 — operational governance structures exist at watershed scale, but full ecosystem representation and multi-generational impact assessment mechanisms remain largely theoretical.

_d/acc alignment._ _Watershed Parliaments_ score highest on Democratic (4/5) and Defensive (4/5), reflecting their potential to distribute political power along ecological lines and build long-term resilience against resource conflicts. Decentralization scores lower (3/5) because existing implementations remain embedded within nation-state structures rather than replacing them. For a broader framing, see "#link("https://earth.org/bioregionalism/")[Bioregionalism: A Model for a Self-Sufficient and Democratic Economy]" (2021).


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ If the Whanganui River legal personhood model can't be expanded into binding governance frameworks in other jurisdictions, watershed parliaments remain a thought experiment. Advocates and legal scholars should focus there first. Separately, a comparative study of existing river basin commissions would identify which governance features actually transfer to full bioregional authority structures.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["Watershed Parliaments replace geopolitical boundaries with bioregional governance aligned with natural water systems. These institutions integrate human decision-making with ecological feedback, where voting rights extend to ecosystem representatives and decisions must demonstrate positive impacts across seven generations of all life forms within the watershed." — _Source: #link("https://worlds.existentialhope.com/world/mycelial-democracy/")[mycelial-democracy]_]


=== Digital Twins for Communities and Ecosystems

_AI-Mediated Deliberation & Collective Intelligence_ | Composite: 16

Real-time digital models of communities and ecosystems that enable participatory future simulation with locally-owned data.

_How it works._ Sensor networks and continuous data feeds update digital models of local ecological and social conditions, allowing stakeholders to run simulations of policy or environmental decisions before implementing them. Critically, communities retain ownership of their data rather than ceding it to centralized platforms. Outputs can inform governance bodies, including representatives for non-human entities such as rivers.

_Who's building toward this._ The #link("https://www.sla.gov.sg/")[_Singapore Land Authority_] built #link("https://en.wikipedia.org/wiki/Virtual_Singapore")[Virtual Singapore], the first country-scale urban #link("https://en.wikipedia.org/wiki/Digital_twin")[digital twin], operational since 2022 following a \$73M investment over 2012–2017. The #link("https://www.turing.ac.uk/research/research-projects/ecosystems-digital-twins")[_Alan Turing Institute_] is developing methodology for scalable digital twin ecosystems and national digital twin infrastructure. #link("https://www.northeastern.edu/")[_Northeastern University's Boston Area Research Initiative (BARI)_] is building Fora.ai, a participatory modeling platform for community-led digital twins in green infrastructure planning (see "#link("https://journals.sagepub.com/doi/10.1177/23998083251323671")[Enhancing digital twin technology with community-led, science-driven participatory modeling]," 2025). #link("https://www.esri.com/about/newsroom/blog/open-science-environmental-digital-twin")[_The Nature Conservancy and Esri_] are developing environmental digital twins for ecosystem monitoring, including the Point Conception project. TRL sits at 5: urban digital twin components are mature, but participatory governance integrated with community #link("https://en.wikipedia.org/wiki/Data_sovereignty")[data sovereignty] at scale remains in prototype phase. Broader framing appears in "#link("https://journals.sagepub.com/doi/full/10.1177/03063127241236809")[Digital twins and the digital logics of biodiversity]" (2024) and "#link("https://www.researchgate.net/publication/359184358_City_Digital_Twin_Concepts_A_Vision_for_Community_Participation")[City Digital Twin Concepts: A Vision for Community Participation]" (2022). The concept originates from the #link("https://worlds.existentialhope.com/world/the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences/")[Commonsense Accord world].

_d/acc alignment._ This entity scores highest on democratic (4/5) and defensive (4/5) dimensions, reflecting its potential to distribute simulation capacity to communities and reduce harm from uninformed governance decisions. Decentralization scores 3/5 because data sovereignty frameworks and community-owned infrastructure remain partially realized rather than structurally embedded.


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ Funding a structured pilot that combines Fora.ai-style participatory modeling with a community data ownership agreement and an operational sensor network would move this from conceptual integration to demonstrated production system. Singapore proved national-scale digital twins work; Fora.ai proved participatory modeling works; GDPR and Indigenous data governance proved data sovereignty frameworks work. The gap is that urban planners, data sovereignty practitioners, and sensor network operators don't attend the same conferences.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["Digital twins reflect the real-time state of communities and ecosystems. They help people simulate futures, explore consequences, and make decisions guided by care, memory, and shared responsibility. Every community and citizen holds its own data as a form of digital sovereignty." — _Source: #link("https://worlds.existentialhope.com/world/the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences/")[the-commonsense-accord-collectively-stewarding-the-world-across-time-and-across-differences]_]


=== Loyal AI Assistance (Fiduciary AI Assistance)

_AI Safety, Alignment & Governance_ | Composite: 15

#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ Legal scholars, policy advocates, and AI governance organizations should push for regulatory frameworks that define and enforce fiduciary duty standards for AI assistants. This is the explicit gating factor for commercial adoption. Connecting existing legal instruments like #link("https://en.wikipedia.org/wiki/Uniform_Electronic_Transactions_Act")[UETA] to AI agent accountability, and building coalitions that pressure regulators to establish compliance mechanisms, would move this from research artifact to deployable standard.]


A personal AI system explicitly designed to serve the individual user's goals rather than platform or advertiser interests, functioning more like a #link("https://en.wikipedia.org/wiki/Fiduciary")[fiduciary] than a product. A loyal AI assistant would know the user deeply enough to genuinely assist rather than manipulate, with no third-party incentives embedded in its objective function. Unlike Siri or Alexa, which are structurally oriented toward platform revenue and data monetization, a fiduciary AI would operate under a duty of loyalty and care analogous to legal fiduciary relationships.

The #link("https://montrealethics.ai/")[Montreal AI Ethics Institute] has developed research and design frameworks for fiduciary AI systems (see "#link("https://dl.acm.org/doi/fullHtml/10.1145/3617694.3623230")[Designing Fiduciary Artificial Intelligence]," 2023). #link("https://innovation.consumerreports.org/")[Consumer Reports Innovation] is exploring personal AI agents operating under fiduciary duty principles, detailed in "#link("https://innovation.consumerreports.org/empowering-consumers-with-personal-ai-agents-legal-foundations-and-design-considerations/")[Empowering Consumers with Personal AI Agents]" (2025). The #link("https://alignment.anthropic.com/")[Alignment Research Center] contributes relevant user-centric alignment research. Legal foundations are explored in "#link("https://www.bu.edu/law/files/2023/09/Fiduciary-paper.pdf")[Fiduciary Principles in AI: Utilizing the Duty of Loyalty]" (2023). No dedicated external funding has been documented. _TRL 3_ — published design methodologies and legal frameworks exist, but no commercial deployment has occurred. The concept emerged from a podcast discussion with #link("https://en.wikipedia.org/wiki/Anthony_Aguirre")[Anthony Aguirre] #link("https://www.existentialhope.com/podcasts/anthony-aguirre-anna-yelizarova-on-worldbuilding")[on worldbuilding].

_d/acc alignment._ Scores highest on Democratic control (4/5) and Defensive posture (4/5), reflecting its core purpose of returning AI agency to individuals and protecting users from manipulative system design. Decentralization and differential acceleration scores are weaker (2/5 each).


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["One of the things that came out of the augmented intelligence summit was fiduciary AI assistance. I have been calling them loyal AI assistance. There is a loyal AI system that doesn't have selfish interests and works to advance your goals and interests." — _Source: #link("https://www.existentialhope.com/podcasts/anthony-aguirre-anna-yelizarova-on-worldbuilding")[podcasts]_]


=== The Global Deliberation Coordinator

_AI-Mediated Deliberation & Collective Intelligence_ | Composite: 15

A platform institution designed to coordinate global deliberative processes and collective decision-making specifically around AI governance.

_How it works._ The institution establishes structured coordination infrastructure that convenes global stakeholders—states, civil society, technical experts—for deliberative discussions on AI governance, enabling collective decisions that cross national and organizational boundaries. Unlike existing expert bodies, the model centers inclusive participation and #link("https://en.wikipedia.org/wiki/Deliberative_democracy")[deliberative] legitimacy rather than top-down technical guidance. AI tools support multilingual, asynchronous deliberation at scale across time zones and cultures.

_Who's building toward this._ The _UN #link("https://www.un.org/global-dialogue-ai-governance/en")[Global Dialogue on AI Governance]_ (launched August 2025) provides the most operational foundation, offering an inclusive state-and-stakeholder platform. #link("https://cordis.europa.eu/project/id/101178806")[_AI4Deliberation_] (#link("https://en.wikipedia.org/wiki/Horizon_Europe")[Horizon Europe], €2,999,500) is building AI-enabled deliberative toolkits for governments. #link("https://connectedbydata.org/resources/global-deliberation-ai")[_Connected by Data_] is researching independent global assembly designs for AI governance. #link("https://aidemocracyfoundation.org/")[_AI & Democracy Foundation_] focuses on deliberative processes for AI alignment. #link("https://metagov.org/")[_Metagov_] develops digital self-governance infrastructure. TRL sits at 4: pilots are proven, but no unified global coordination architecture exists yet. Key publications include "#link("https://arxiv.org/pdf/2503.04766")[Global AI Governance: Where the Challenge is the Solution]" (2025), "#link("https://connectedbydata.org/resources/global-deliberation-ai")[Global Citizen Deliberation on Artificial Intelligence: Options and design considerations]" (2024), and the "#link("https://www.un.org/sites/un2.un.org/files/governing_ai_for_humanity_final_report_en.pdf")[Governing AI for Humanity]" UN High-Level Advisory Body Final Report (2024).

_d/acc alignment._ Democratic (4/5) and Defensive (4/5) are the strongest dimensions—this entity directly addresses who gets a voice in AI governance decisions and builds resilience against unilateral capture of those decisions. Decentralized and Differential scores (2/5 each) reflect that coordination infrastructure, by design, requires some centralization.


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ Use the UN Global Dialogue on AI Governance as a convening anchor: fund Connected by Data or Metagov to translate their global assembly design research into a concrete coordination architecture proposal, then pressure-test it with delegations from the 118 currently excluded countries before the next major AI governance summit.]


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["The Global Deliberation Coordinator (Hackathon shared second place): Focuses on establishing a platform for global discussions and decision-making on AI and other pressing issues." — _Source: N/A_]


=== Epistemic stack

_Scientific Research & Knowledge Infrastructure_ | Composite: 14

#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)["There is no reason why, when reading a newspaper article about something, you shouldn't be able to trace back: where did that quote come from, or where did this piece of information come from? How do I know whether to trust this?... We should be able to have a stack we can follow all the way from the high level back down to the raw ingredients, and then figure out how much we trust each of those steps." — _Source: #link("https://www.existentialhope.com/podcasts/anthony-aguirre-tools-or-agents-choosing-our-ai-future")[podcasts]_]


A citation and #link("https://en.wikipedia.org/wiki/Provenance")[provenance] system for all information, from newspaper articles to social media claims, that lets users trace any assertion back to its raw data sources, with trust scores based on historical accuracy of each link in the chain.

_How it works._ Every piece of information carries machine-readable provenance metadata linking it to its source, analogous to academic citations but applied universally. AI tools help users traverse this chain from a high-level claim down to raw data, which can be cryptographically signed by hardware #link("https://en.wikipedia.org/wiki/Trusted_execution_environment")[secure enclaves]. Each node in the chain (person, outlet, inference step) accumulates a reliability record based on past accuracy, giving users a principled basis for assessing any given claim.

_Who's building toward this._ The #link("https://c2pa.org/")[Coalition for Content Provenance and Authenticity (C2PA)] released its open technical standard in 2022, with adoption now spanning camera makers, news outlets, and platforms. The #link("https://contentauthenticity.org/")[Content Authenticity Initiative (CAI)] develops open-source tooling within that coalition. #link("https://communitynotes.x.com/")[X's Community Notes] operates crowdsourced fact-checking at scale with 133,000+ contributors. #link("https://captureapp.xyz/")[Numbers Protocol] integrates C2PA provenance data with blockchain for immutable asset tracking. No dedicated funding for a unified epistemic stack has been identified. TRL: 4—components exist in isolation; end-to-end integration from raw sensor data through inference to published claims with per-node trust scoring remains unbuilt. The vision is articulated in "#link("https://www.oliversourbut.net/p/a-full-epistemic-stack")[A Full Epistemic Stack: Knowledge Commons for the 21st Century]" (2025), while related challenges are examined in "#link("https://arxiv.org/abs/2509.13365")[The Provenance Problem: LLMs and the Breakdown of Citation Norms]" (2025) and "#link("https://arxiv.org/html/2603.02960")[Architecting Trust in Artificial Epistemic Agents]" (2025). The concept draws from a podcast discussion with #link("https://en.wikipedia.org/wiki/Anthony_Aguirre")[Anthony Aguirre] on #link("https://www.existentialhope.com/podcasts/anthony-aguirre-tools-or-agents-choosing-our-ai-future")[choosing our AI future].

_d/acc alignment._ Defensive scores highest (4/5) because accurate provenance directly counters manipulation and misinformation at the infrastructure level. Democratic scores 3/5, reflecting the system's potential to equalize access to source-level verification across users and institutions.


#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[_What can someone do RIGHT NOW?_ Who convenes C2PA, the academic citation graph projects, and platform trust-and-safety teams to define a shared metadata schema? That's the missing piece. The technology for media provenance, inference-step logging, and per-node accuracy scoring exists in fragments across these communities. A funded convening body with a concrete interoperability mandate could close the gap faster than any single technical project.]



#line(length: 100%, stroke: 0.5pt + luma(180))


== 5. Watch List (Tier 2)


The remaining 170 entities form the watch list — systems worth tracking but not yet meeting the composite score threshold for spotlight treatment.

#table(columns: (auto, auto, auto, auto, auto, auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Name*],
  table.cell[*Group*],
  table.cell[*d/acc*],
  table.cell[*Trans.*],
  table.cell[*Bottleneck*],
  table.cell[*Action*],
  table.cell[*TRL*],
  table.cell[*Source*],
  table.cell[_AI Fiduciaries_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[17/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[5],
  table.cell[],
  table.cell[_Liberal/Popperian AGI Education Framework_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[15/20],
  table.cell[4/5],
  table.cell[Physics],
  table.cell[Research],
  table.cell[1],
  table.cell[#link("https://www.existentialhope.com/podcasts/david-deutsch-on-beauty-knowledge-and-progress")[david-deutsch-on-beauty-knowle]],
  table.cell[_Privacy-Preserving Global Regulatory Markets for AI Verif..._],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[16/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/emilia-javorsky-the-future-of-ai-bioengineering-and-human-empathy")[emilia-javorsky-the-future-of-]],
  table.cell[_LexNodes_],
  table.cell[Decentralized & Democratic Institutions],
  table.cell[16/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/lexcommons-the-open-law-society/")[lexcommons-the-open-law-societ]],
  table.cell[_Viotopia_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[13/20],
  table.cell[4/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[1],
  table.cell[#link("https://www.existentialhope.com/podcasts/fin-moorhouse-why-we-need-to-aim-higher-than-survival")[fin-moorhouse-why-we-need-to-a]],
  table.cell[_Continuity Guild_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[15/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[5],
  table.cell[#link("https://worlds.existentialhope.com/world/threadtime/")[threadtime]],
  table.cell[_BioEcho Mesh_],
  table.cell[Ecological & Regenerative Systems],
  table.cell[14/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[6],
  table.cell[#link("https://worlds.existentialhope.com/world/2035-rewild/")[2035-rewild]],
  table.cell[_Cognitive Field Resonators (CFRs)_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[15/20],
  table.cell[1/5],
  table.cell[Physics],
  table.cell[Research],
  table.cell[1],
  table.cell[#link("https://worlds.existentialhope.com/world/harmonic-futures-a-2035-of-coherence-not-convenience/")[harmonic-futures-a-2035-of-coh]],
  table.cell[_The Mnemosyne Assembly_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[13/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[3],
  table.cell[#link("https://worlds.existentialhope.com/world/harmonic-futures-a-2035-of-coherence-not-convenience/")[harmonic-futures-a-2035-of-coh]],
  table.cell[_Translation Language Models (TLMs) with citizen-owned tra..._],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[13/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Build],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/la-langue-de-la-prvoyance/")[la-langue-de-la-prvoyance]],
  table.cell[_Open Cognition Ledger_],
  table.cell[Decentralized & Democratic Institutions],
  table.cell[13/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/symbiotic-wisdom/")[symbiotic-wisdom]],
  table.cell[_Polymesh Civic Ledger_],
  table.cell[Decentralized & Democratic Institutions],
  table.cell[13/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/symbiotic-wisdom/")[symbiotic-wisdom]],
  table.cell[_Living Rights Network_],
  table.cell[Decentralized & Democratic Institutions],
  table.cell[13/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/the-living-rights-network/")[the-living-rights-network]],
  table.cell[_The Collective of Inner Weavers_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[13/20],
  table.cell[3/5],
  table.cell[Funding],
  table.cell[Fund],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/veliona-the-world-of-unfolding-minds/")[veliona-the-world-of-unfolding]],
  table.cell[_Federated Procurement Platforms_],
  table.cell[Economic Systems & Resource Distribution],
  table.cell[13/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[5],
  table.cell[],
  table.cell[_contextual autonomy_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[12/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[],
  table.cell[_Publishing for Machines (machine-readable scientific publ..._],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[12/20],
  table.cell[3/5],
  table.cell[Social Acceptance],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/andrew-white-building-an-ai-scientist-to-automate-discovery")[andrew-white-building-an-ai-sc]],
  table.cell[_De novo designed universal flu vaccines (Neil King / Bake..._],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[12/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[6],
  table.cell[#link("https://www.existentialhope.com/podcasts/david-baker-using-ai-for-science-to-solve-humanitys-biggest-problems")[david-baker-using-ai-for-scien]],
  table.cell[_Computational models for infectious disease spread and va..._],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[12/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[7],
  table.cell[#link("https://www.existentialhope.com/podcasts/pablos-holman-on-creating-technology-that-actually-matters")[pablos-holman-on-creating-tech]],
  table.cell[_AI-Democratic Institutions for Decentralized Governance_],
  table.cell[Decentralized & Democratic Institutions],
  table.cell[12/20],
  table.cell[3/5],
  table.cell[Social Acceptance],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/worldbuilding-special-3rd-place-floratech")[worldbuilding-special-3rd-plac]],
  table.cell[_Crowdfunded Independent Longevity AI Research Program_],
  table.cell[Nanotechnology & Advanced Manufacturing],
  table.cell[13/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/a-hope-for-human-immortality/")[a-hope-for-human-immortality]],
  table.cell[_Hybrid Market impact bond ledger_],
  table.cell[Economic Systems & Resource Distribution],
  table.cell[12/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[5],
  table.cell[#link("https://worlds.existentialhope.com/world/hybrid-market/")[hybrid-market]],
  table.cell[_Isolated Societies Research Institute_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[13/20],
  table.cell[2/5],
  table.cell[Funding],
  table.cell[Research],
  table.cell[3],
  table.cell[#link("https://worlds.existentialhope.com/world/self-sustaining-isolated-societies/")[self-sustaining-isolated-socie]],
  table.cell[_Mandatory Open-Source AI Release Policy_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[12/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[2],
  table.cell[#link("https://worlds.existentialhope.com/world/sustainable-abundance/")[sustainable-abundance]],
  table.cell[_Loom Studios_],
  table.cell[Decentralized & Democratic Institutions],
  table.cell[12/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/symphora/")[symphora]],
  table.cell[_The Common Knowledge Generator_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[12/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[],
  table.cell[_The Delphi Collaboration Protocol_],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[13/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Build],
  table.cell[4],
  table.cell[],
  table.cell[_The Scenario Planning Institution_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[12/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[],
  table.cell[_Flourishing Certification_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[12/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[3],
  table.cell[],
  table.cell[_TAI Horizon Scanner_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[12/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[],
  table.cell[_Lean FRO (interactive theorem proving infrastructure for ..._],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[11/20],
  table.cell[3/5],
  table.cell[Engineering],
  table.cell[Build],
  table.cell[6],
  table.cell[#link("https://www.existentialhope.com/podcasts/adam-marblestone-solving-sciences-biggest-gaps")[adam-marblestone-solving-scien]],
  table.cell[_Large-scale AI-mediated deliberation system_],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[11/20],
  table.cell[3/5],
  table.cell[Engineering],
  table.cell[Build],
  table.cell[5],
  table.cell[#link("https://www.existentialhope.com/podcasts/anthony-aguirre-tools-or-agents-choosing-our-ai-future")[anthony-aguirre-tools-or-agent]],
  table.cell[_Reputational Market_],
  table.cell[Economic Systems & Resource Distribution],
  table.cell[11/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/kristian-rnn-the-darwinian-trap-that-explains-our-world")[kristian-rnn-the-darwinian-tra]],
  table.cell[_Learning Observatories_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[11/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/niklas-lundblad-how-ai-can-accelerate-science-its-own-adoption")[niklas-lundblad-how-ai-can-acc]],
  table.cell[_Deep Fision borehole nuclear reactor_],
  table.cell[Energy, Environment & Planetary Systems],
  table.cell[11/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Build],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/pablos-holman-on-creating-technology-that-actually-matters")[pablos-holman-on-creating-tech]],
  table.cell[_Values-as-modality parametrization across AI systems_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[11/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[2],
  table.cell[#link("https://www.existentialhope.com/podcasts/richard-mallah-how-aligned-ai-could-help-us-create-a-flourishing-future")[richard-mallah-how-aligned-ai-]],
  table.cell[_Parallel lightly-regulated childminder category (France)_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[12/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[7],
  table.cell[#link("https://www.existentialhope.com/podcasts/sam-bowman-whats-holding-back-progress-and-how-to-fix-it")[sam-bowman-whats-holding-back-]],
  table.cell[_Orare - AI-powered Futarchy governance system_],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[11/20],
  table.cell[3/5],
  table.cell[Social Acceptance],
  table.cell[Advocate],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/worldbuilding-special-1st-place-cities-of-orare")[worldbuilding-special-1st-plac]],
  table.cell[_VOICE (Voice for Open Source Information and Community En..._],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[11/20],
  table.cell[3/5],
  table.cell[Social Acceptance],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/worldbuilding-special-2nd-place-rising-choir")[worldbuilding-special-2nd-plac]],
  table.cell[_Global Personhood Token / Trust-of-Personhood Standard_],
  table.cell[International Governance & Coordination],
  table.cell[11/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[6],
  table.cell[#link("https://www.existentialhope.com/podcasts/worldbuilding-special-2nd-place-rising-choir")[worldbuilding-special-2nd-plac]],
  table.cell[_LexCommons_],
  table.cell[Decentralized & Democratic Institutions],
  table.cell[12/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[5],
  table.cell[#link("https://worlds.existentialhope.com/world/lexcommons-the-open-law-society/")[lexcommons-the-open-law-societ]],
  table.cell[_The Welcome Circle_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[12/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[2],
  table.cell[#link("https://worlds.existentialhope.com/world/planet-joy/")[planet-joy]],
  table.cell[_RaízMental Global_],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[11/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/razmental-emotional-healing-ecosystems/")[razmental-emotional-healing-ec]],
  table.cell[_Ethical AI Tutors_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[11/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[5],
  table.cell[#link("https://worlds.existentialhope.com/world/the-learning-uncommons-of-2035/")[the-learning-uncommons-of-2035]],
  table.cell[_Safety-Netted DAOs_],
  table.cell[Decentralized & Democratic Institutions],
  table.cell[11/20],
  table.cell[2/5],
  table.cell[Engineering],
  table.cell[Build],
  table.cell[2],
  table.cell[],
  table.cell[_AGI Liability Safe Harbor Framework_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[10/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[1],
  table.cell[],
  table.cell[_Multiplicity.ai_],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[11/20],
  table.cell[2/5],
  table.cell[Engineering],
  table.cell[Build],
  table.cell[7],
  table.cell[#link("https://www.existentialhope.com/podcasts/andrew-critch-what-agi-might-look-like-in-practice")[andrew-critch-what-agi-might-l]],
  table.cell[_Futarchy_],
  table.cell[Decentralized & Democratic Institutions],
  table.cell[10/20],
  table.cell[3/5],
  table.cell[Social Acceptance],
  table.cell[Build],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/david-duvenaud-exploring-the-cruxes-and-possibilities-of-post-agi-futures")[david-duvenaud-exploring-the-c]],
  table.cell[_Active smart fabric with autonomous environmental response_],
  table.cell[Nanotechnology & Advanced Manufacturing],
  table.cell[11/20],
  table.cell[2/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/david-leigh-exploring-the-possibilities-of-nanotechnology")[david-leigh-exploring-the-poss]],
  table.cell[_Integration of Brain Preservation into the Medical System_],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[11/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/dr-ariel-zeleznikow-johnston-the-future-loves-you")[dr-ariel-zeleznikow-johnston-t]],
  table.cell[_Imagination Annotated (book series)_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[11/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[6],
  table.cell[#link("https://www.existentialhope.com/podcasts/ed-finn-how-science-fiction-can-inspire-real-world-innovation")[ed-finn-how-science-fiction-ca]],
  table.cell[_Author Personal Knowledge Graph / Writing Corpus Utility_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[11/20],
  table.cell[2/5],
  table.cell[Engineering],
  table.cell[Build],
  table.cell[5],
  table.cell[#link("https://www.existentialhope.com/podcasts/jim-oshaughnessy-on-investing-in-infinite-human-potential")[jim-oshaughnessy-on-investing-]],
  table.cell[_Artificial General Wisdom_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[10/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[2],
  table.cell[#link("https://www.existentialhope.com/podcasts/liv-boeree-game-theory-moloch-our-hopeful-future")[liv-boeree-game-theory-moloch-]],
  table.cell[_Componentized architectures optimized for inner alignment..._],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[10/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[2],
  table.cell[#link("https://www.existentialhope.com/podcasts/richard-mallah-how-aligned-ai-could-help-us-create-a-flourishing-future")[richard-mallah-how-aligned-ai-]],
  table.cell[_Neighborhood opt-in upzoning with land value capture_],
  table.cell[Decentralized & Democratic Institutions],
  table.cell[11/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/sam-bowman-whats-holding-back-progress-and-how-to-fix-it")[sam-bowman-whats-holding-back-]],
  table.cell[_Kacha's Global Symbiosis Council (GSC)_],
  table.cell[International Governance & Coordination],
  table.cell[10/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/2035-the-era-of-sentient-symbiosis-and-human-ai-flourishment/")[2035-the-era-of-sentient-symbi]],
  table.cell[_Guardian Network_],
  table.cell[International Governance & Coordination],
  table.cell[11/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/edusafe/")[edusafe]],
  table.cell[_Decentralized community-built AI systems_],
  table.cell[Decentralized & Democratic Institutions],
  table.cell[10/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[5],
  table.cell[#link("https://worlds.existentialhope.com/world/new-world-in-the-making/")[new-world-in-the-making]],
  table.cell[_Bio-Responsive AI Interfaces_],
  table.cell[Neurotechnology & Brain-Computer Inte...],
  table.cell[11/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/planet-joy/")[planet-joy]],
  table.cell[_Open-source AI-powered research funding and knowledge pla..._],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[10/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/potentia/")[potentia]],
  table.cell[_Interplanetary Cooperative_],
  table.cell[International Governance & Coordination],
  table.cell[11/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[2],
  table.cell[#link("https://worlds.existentialhope.com/world/resilient-planetary-settlements/")[resilient-planetary-settlement]],
  table.cell[_Civic Loom_],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[11/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[5],
  table.cell[#link("https://worlds.existentialhope.com/world/symphora/")[symphora]],
  table.cell[_AI-powered participatory policy simulation platform_],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[10/20],
  table.cell[3/5],
  table.cell[Social Acceptance],
  table.cell[Convene],
  table.cell[5],
  table.cell[#link("https://worlds.existentialhope.com/world/the-commons-cloud/")[the-commons-cloud]],
  table.cell[_The Flourishing Foundation_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[11/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[5],
  table.cell[],
  table.cell[_The Evals for Evals Institute_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[10/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[3],
  table.cell[],
  table.cell[_The World Convention on Transformative Artificial Intelli..._],
  table.cell[International Governance & Coordination],
  table.cell[11/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[],
  table.cell[_Global Deliberation as a Service (GDaaS)_],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[10/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[],
  table.cell[_World Convention on Transformative Artificial Intelligenc..._],
  table.cell[International Governance & Coordination],
  table.cell[10/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[2],
  table.cell[],
  table.cell[_Tool AI for Tool AI_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[9/20],
  table.cell[3/5],
  table.cell[Engineering],
  table.cell[Build],
  table.cell[4],
  table.cell[],
  table.cell[_NotADoctor.ai medical record serialization and RCT search_],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[10/20],
  table.cell[2/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[6],
  table.cell[#link("https://www.existentialhope.com/podcasts/andrew-critch-what-agi-might-look-like-in-practice")[andrew-critch-what-agi-might-l]],
  table.cell[_AI-mediated conflict resolution tool (retorsion/disgorgem..._],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[10/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/andrew-critch-what-agi-might-look-like-in-practice")[andrew-critch-what-agi-might-l]],
  table.cell[_Aviary_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[10/20],
  table.cell[2/5],
  table.cell[Social Acceptance],
  table.cell[Build],
  table.cell[6],
  table.cell[#link("https://www.existentialhope.com/podcasts/andrew-white-building-an-ai-scientist-to-automate-discovery")[andrew-white-building-an-ai-sc]],
  table.cell[_Windfall Clause_],
  table.cell[Economic Systems & Resource Distribution],
  table.cell[10/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[2],
  table.cell[#link("https://www.existentialhope.com/podcasts/anthony-aguirre-anna-yelizarova-on-worldbuilding")[anthony-aguirre-anna-yelizarov]],
  table.cell[_Project Hieroglyph_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[9/20],
  table.cell[3/5],
  table.cell[Funding],
  table.cell[Fund],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/ed-finn-how-science-fiction-can-inspire-real-world-innovation")[ed-finn-how-science-fiction-ca]],
  table.cell[_Provably Safe AGI via Formal Verification_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[9/20],
  table.cell[3/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/gus-docker-beyond-survival-envisioning-a-technologically-enhanced-utopia")[gus-docker-beyond-survival-env]],
  table.cell[_Closed-loop gene therapy for seizure suppression via acti..._],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[9/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Fund],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/jacques-carolan-the-future-of-brain-health")[jacques-carolan-the-future-of-]],
  table.cell[_AI underwriting / mandatory insurance for AI systems_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[9/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/nathan-labenz-what-are-the-best-case-scenarios-for-ai")[nathan-labenz-what-are-the-bes]],
  table.cell[_Self-Improving System Prompt for Continuous AI Capability..._],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[10/20],
  table.cell[2/5],
  table.cell[Engineering],
  table.cell[Build],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/niklas-lundblad-how-ai-can-accelerate-science-its-own-adoption")[niklas-lundblad-how-ai-can-acc]],
  table.cell[_Multicriteria safety architecture with explicit precedenc..._],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[9/20],
  table.cell[3/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[1],
  table.cell[#link("https://www.existentialhope.com/podcasts/richard-mallah-how-aligned-ai-could-help-us-create-a-flourishing-future")[richard-mallah-how-aligned-ai-]],
  table.cell[_Blockchain-based Universal Self-Actualization Income_],
  table.cell[Economic Systems & Resource Distribution],
  table.cell[10/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/trent-mcconaghy-from-starships-to-tokens-pioneering-futures")[trent-mcconaghy-from-starships]],
  table.cell[_International Council of Life Extension_],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[10/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/a-hope-for-human-immortality/")[a-hope-for-human-immortality]],
  table.cell[_Ecological Balance Council_],
  table.cell[Ecological & Regenerative Systems],
  table.cell[10/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[2],
  table.cell[#link("https://worlds.existentialhope.com/world/green-renaissance/")[green-renaissance]],
  table.cell[_Adaptive Wearable Tech_],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[9/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Build],
  table.cell[7],
  table.cell[#link("https://worlds.existentialhope.com/world/human-centric-technology/")[human-centric-technology]],
  table.cell[_Human-Tech Council_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[10/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/human-centric-technology/")[human-centric-technology]],
  table.cell[_Global Learning Collective_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[9/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[6],
  table.cell[#link("https://worlds.existentialhope.com/world/lumina-the-world-illuminated-by-unleashed-human-brilliance/")[lumina-the-world-illuminated-b]],
  table.cell[_Emotional Coach (Empathetic Neuro-AI)_],
  table.cell[Neurotechnology & Brain-Computer Inte...],
  table.cell[9/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/razmental-emotional-healing-ecosystems/")[razmental-emotional-healing-ec]],
  table.cell[_Regenerative Biospheres_],
  table.cell[Ecological & Regenerative Systems],
  table.cell[9/20],
  table.cell[3/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[5],
  table.cell[#link("https://worlds.existentialhope.com/world/resilient-planetary-settlements/")[resilient-planetary-settlement]],
  table.cell[_AI Alignment Markets_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[10/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[3],
  table.cell[#link("https://worlds.existentialhope.com/world/the-symbiotic-age/")[the-symbiotic-age]],
  table.cell[_Global AI Alignment Commission (GAAC)_],
  table.cell[International Governance & Coordination],
  table.cell[9/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[2],
  table.cell[#link("https://worlds.existentialhope.com/world/the-symbiotic-age/")[the-symbiotic-age]],
  table.cell[_Extracellular vesicle-based blood diagnostics for tissue-..._],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[9/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/amy-proal-rethinking-chronic-disease")[amy-proal-rethinking-chronic-d]],
  table.cell[_Protein-based nanomachines for in vivo tissue repair and ..._],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[8/20],
  table.cell[3/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/david-baker-using-ai-for-science-to-solve-humanitys-biggest-problems")[david-baker-using-ai-for-scien]],
  table.cell[_Biohybrid living DBS electrode (neuron-based implant inte..._],
  table.cell[Neurotechnology & Brain-Computer Inte...],
  table.cell[8/20],
  table.cell[3/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/jacques-carolan-the-future-of-brain-health")[jacques-carolan-the-future-of-]],
  table.cell[_Chemputer / Chemputation programming language_],
  table.cell[Nanotechnology & Advanced Manufacturing],
  table.cell[8/20],
  table.cell[3/5],
  table.cell[Social Acceptance],
  table.cell[Advocate],
  table.cell[7],
  table.cell[#link("https://www.existentialhope.com/podcasts/lee-cronin-catalyzing-progress-through-chemistry")[lee-cronin-catalyzing-progress]],
  table.cell[_Openwater universal diagnostic/therapeutic device_],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[8/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Fund],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/mary-lou-jepsen-a-handheld-device-to-defeat-cancer")[mary-lou-jepsen-a-handheld-dev]],
  table.cell[_AI-driven forking narrative / interactive scenario conten..._],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[8/20],
  table.cell[3/5],
  table.cell[Social Acceptance],
  table.cell[Build],
  table.cell[5],
  table.cell[#link("https://www.existentialhope.com/podcasts/nathan-labenz-what-are-the-best-case-scenarios-for-ai")[nathan-labenz-what-are-the-bes]],
  table.cell[_Agent Contract Declaration Requirement_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[9/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[2],
  table.cell[#link("https://www.existentialhope.com/podcasts/niklas-lundblad-how-ai-can-accelerate-science-its-own-adoption")[niklas-lundblad-how-ai-can-acc]],
  table.cell[_Spectrum from environmental safety to metagenic safety_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[9/20],
  table.cell[2/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[1],
  table.cell[#link("https://www.existentialhope.com/podcasts/richard-mallah-how-aligned-ai-could-help-us-create-a-flourishing-future")[richard-mallah-how-aligned-ai-]],
  table.cell[_Bounded AI Agents_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[9/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[5],
  table.cell[#link("https://www.existentialhope.com/podcasts/worldbuilding-special-3rd-place-floratech")[worldbuilding-special-3rd-plac]],
  table.cell[_BTC Trust Grid_],
  table.cell[Economic Systems & Resource Distribution],
  table.cell[9/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/worldbuilding-course-worldbuilding-toolbox-world-entry-page-world-gallery-x-twitter-instagram-medium-bookmark-sadvipra-ai/")[worldbuilding-course-worldbuil]],
  table.cell[_Global Fungal Biology Research Initiative (Big Tech + Pau..._],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[9/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[3],
  table.cell[#link("https://worlds.existentialhope.com/world/fungi-terra/")[fungi-terra]],
  table.cell[_Biophilic Architecture_],
  table.cell[Ecological & Regenerative Systems],
  table.cell[9/20],
  table.cell[2/5],
  table.cell[Funding],
  table.cell[Fund],
  table.cell[7],
  table.cell[#link("https://worlds.existentialhope.com/world/green-renaissance/")[green-renaissance]],
  table.cell[_Urban Sustainability Network_],
  table.cell[Energy, Environment & Planetary Systems],
  table.cell[9/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[7],
  table.cell[#link("https://worlds.existentialhope.com/world/harmonized-urban-ecosystems/")[harmonized-urban-ecosystems]],
  table.cell[_AI Market Intermediaries_],
  table.cell[Economic Systems & Resource Distribution],
  table.cell[8/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/the-more-beautiful-world-our-hearts-know-is-possible/")[the-more-beautiful-world-our-h]],
  table.cell[_The Indefinite Lifespan_],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[8/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/the-world-of-equal-opportunity-for-sentient-beings-living-the-indefinite-lifespan-immortally/")[the-world-of-equal-opportunity]],
  table.cell[_Memory Looms_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[10/20],
  table.cell[1/5],
  table.cell[Physics],
  table.cell[Research],
  table.cell[1],
  table.cell[#link("https://worlds.existentialhope.com/world/threadtime/")[threadtime]],
  table.cell[_World Cultural Exchange Forum_],
  table.cell[International Governance & Coordination],
  table.cell[9/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[6],
  table.cell[#link("https://worlds.existentialhope.com/world/unity-through-diversity/")[unity-through-diversity]],
  table.cell[_TimeLike / SECHI (Simulation-Enabled Cooperative Human In..._],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[7/20],
  table.cell[4/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[3],
  table.cell[],
  table.cell[_Request for Evaluation (RfE) Protocol_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[9/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[1],
  table.cell[],
  table.cell[_Focused Research Organizations (FROs)_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[7/20],
  table.cell[3/5],
  table.cell[Funding],
  table.cell[Fund],
  table.cell[5],
  table.cell[#link("https://www.existentialhope.com/podcasts/adam-marblestone-solving-sciences-biggest-gaps")[adam-marblestone-solving-scien]],
  table.cell[_Vagus nerve microbiome characterization study_],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[8/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/amy-proal-rethinking-chronic-disease")[amy-proal-rethinking-chronic-d]],
  table.cell[_AI-driven drug repurposing pipeline (AMD/Ripasudil discov..._],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[7/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[5],
  table.cell[#link("https://www.existentialhope.com/podcasts/andrew-white-building-an-ai-scientist-to-automate-discovery")[andrew-white-building-an-ai-sc]],
  table.cell[_Universal Constructor_],
  table.cell[Nanotechnology & Advanced Manufacturing],
  table.cell[6/20],
  table.cell[4/5],
  table.cell[Physics],
  table.cell[Research],
  table.cell[1],
  table.cell[#link("https://www.existentialhope.com/podcasts/david-deutsch-on-beauty-knowledge-and-progress")[david-deutsch-on-beauty-knowle]],
  table.cell[_Bell Labs Systems Engineer Role_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[8/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/eric-gilliam-what-history-can-teach-us-about-doing-better-science")[eric-gilliam-what-history-can-]],
  table.cell[_Meditation-State Detection Model_],
  table.cell[Neurotechnology & Brain-Computer Inte...],
  table.cell[9/20],
  table.cell[1/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/gus-docker-beyond-survival-envisioning-a-technologically-enhanced-utopia")[gus-docker-beyond-survival-env]],
  table.cell[_Vertis Solus space-based solar power array_],
  table.cell[Energy, Environment & Planetary Systems],
  table.cell[7/20],
  table.cell[3/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/pablos-holman-on-creating-technology-that-actually-matters")[pablos-holman-on-creating-tech]],
  table.cell[_Computer-controlled sail cargo ship_],
  table.cell[Energy, Environment & Planetary Systems],
  table.cell[7/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[6],
  table.cell[#link("https://www.existentialhope.com/podcasts/pablos-holman-on-creating-technology-that-actually-matters")[pablos-holman-on-creating-tech]],
  table.cell[_Fire-the-CEO Decision Market_],
  table.cell[Economic Systems & Resource Distribution],
  table.cell[8/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/robin-hanson-on-futurism-his-best-career-advice")[robin-hanson-on-futurism-his-b]],
  table.cell[_Planetary-Scale Intelligence_],
  table.cell[Ecological & Regenerative Systems],
  table.cell[7/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[2],
  table.cell[#link("https://www.existentialhope.com/podcasts/sara-walker-unraveling-lifes-beginnings-with-the-cosmic-perspective")[sara-walker-unraveling-lifes-b]],
  table.cell[_NanoSync – Regenerative Nanotechnology_],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[7/20],
  table.cell[3/5],
  table.cell[Physics],
  table.cell[Research],
  table.cell[2],
  table.cell[#link("https://worlds.existentialhope.com/world/elysium/")[elysium]],
  table.cell[_Institute for Life Extension (ILE)_],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[7/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/elysium/")[elysium]],
  table.cell[_Urban AI systems_],
  table.cell[Energy, Environment & Planetary Systems],
  table.cell[7/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[6],
  table.cell[#link("https://worlds.existentialhope.com/world/harmonized-urban-ecosystems/")[harmonized-urban-ecosystems]],
  table.cell[_AI-Managed Childhood Development Centers_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[7/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/harmony-haven/")[harmony-haven]],
  table.cell[_Predictive AI System for R&D Funding Allocation_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[7/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/innovation-nation/")[innovation-nation]],
  table.cell[_Lifelong AI Guardians_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[8/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/kidtopia/")[kidtopia]],
  table.cell[_Earth UBI_],
  table.cell[Economic Systems & Resource Distribution],
  table.cell[8/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[2],
  table.cell[#link("https://worlds.existentialhope.com/world/protopia-peace-project/")[protopia-peace-project]],
  table.cell[_Jurisdictional Routers_],
  table.cell[International Governance & Coordination],
  table.cell[8/20],
  table.cell[1/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[3],
  table.cell[],
  table.cell[_Pareto-Optimal Negotiation Bots_],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Social Acceptance],
  table.cell[Advocate],
  table.cell[7],
  table.cell[],
  table.cell[_LitQA3 (high-recall literature evaluation benchmark)_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Engineering],
  table.cell[Build],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/andrew-white-building-an-ai-scientist-to-automate-discovery")[andrew-white-building-an-ai-sc]],
  table.cell[_LLM Historical Forecasting Benchmark_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/david-duvenaud-exploring-the-cruxes-and-possibilities-of-post-agi-futures")[david-duvenaud-exploring-the-c]],
  table.cell[_BBN-style Applied R&D Contractor (New BBNs)_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[6/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Fund],
  table.cell[5],
  table.cell[#link("https://www.existentialhope.com/podcasts/eric-gilliam-what-history-can-teach-us-about-doing-better-science")[eric-gilliam-what-history-can-]],
  table.cell[_Closed-loop ultrasound brain-state readout and mood modul..._],
  table.cell[Neurotechnology & Brain-Computer Inte...],
  table.cell[6/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[5],
  table.cell[#link("https://www.existentialhope.com/podcasts/jacques-carolan-the-future-of-brain-health")[jacques-carolan-the-future-of-]],
  table.cell[_Massively scalable intravascular or CSF-routed neural int..._],
  table.cell[Neurotechnology & Brain-Computer Inte...],
  table.cell[6/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[5],
  table.cell[#link("https://www.existentialhope.com/podcasts/jacques-carolan-the-future-of-brain-health")[jacques-carolan-the-future-of-]],
  table.cell[_Continuous AI-Driven Book Marketing Matchmaker_],
  table.cell[Economic Systems & Resource Distribution],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Engineering],
  table.cell[Build],
  table.cell[6],
  table.cell[#link("https://www.existentialhope.com/podcasts/jim-oshaughnessy-on-investing-in-infinite-human-potential")[jim-oshaughnessy-on-investing-]],
  table.cell[_Child Equity Stake Fund (US Birth Endowment)_],
  table.cell[Economic Systems & Resource Distribution],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Social Acceptance],
  table.cell[Advocate],
  table.cell[8],
  table.cell[#link("https://www.existentialhope.com/podcasts/jim-oshaughnessy-on-investing-in-infinite-human-potential")[jim-oshaughnessy-on-investing-]],
  table.cell[_Onerofex (collective AI-mediated dreaming experience)_],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/ken-liu-what-ai-reveals-about-humanity")[ken-liu-what-ai-reveals-about-]],
  table.cell[_Atheoretical Science via Massive Sensor Networks and AI P..._],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[6/20],
  table.cell[3/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/niklas-lundblad-how-ai-can-accelerate-science-its-own-adoption")[niklas-lundblad-how-ai-can-acc]],
  table.cell[_Parallel Federal Science Funding System with Mandatory In..._],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[6/20],
  table.cell[3/5],
  table.cell[Funding],
  table.cell[Advocate],
  table.cell[2],
  table.cell[#link("https://www.existentialhope.com/podcasts/stuart-buck-what-is-good-science")[stuart-buck-what-is-good-scien]],
  table.cell[_Global Childhood Development Authority (GCDA)_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/harmony-haven/")[harmony-haven]],
  table.cell[_The Children's Movement_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[6/20],
  table.cell[3/5],
  table.cell[Funding],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/kidtopia/")[kidtopia]],
  table.cell[_Neural-Adaptive Learning AI_],
  table.cell[Neurotechnology & Brain-Computer Inte...],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/lumina-the-world-illuminated-by-unleashed-human-brilliance/")[lumina-the-world-illuminated-b]],
  table.cell[_Bitcoin-funded renewable energy cooperatives_],
  table.cell[Energy, Environment & Planetary Systems],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[5],
  table.cell[#link("https://worlds.existentialhope.com/world/new-world-in-the-making/")[new-world-in-the-making]],
  table.cell[_Ecosystem-responsive AI management system_],
  table.cell[Ecological & Regenerative Systems],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/potentia/")[potentia]],
  table.cell[_GAI (Global AI Board)_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/sustainable-abundance/")[sustainable-abundance]],
  table.cell[_United Nations Biosphere Geoengineering and AI Governance..._],
  table.cell[International Governance & Coordination],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[2],
  table.cell[#link("https://worlds.existentialhope.com/world/the-world-of-equal-opportunity-for-sentient-beings-living-the-indefinite-lifespan-immortally/")[the-world-of-equal-opportunity]],
  table.cell[_Little AI Robots (emotional decision-support chatbots)_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[6],
  table.cell[#link("https://worlds.existentialhope.com/world/uniqualia/")[uniqualia]],
  table.cell[_Consolidated Intelligence Council_],
  table.cell[International Governance & Coordination],
  table.cell[7/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/unified-peace/")[unified-peace]],
  table.cell[_Neural Harmony Interface_],
  table.cell[Neurotechnology & Brain-Computer Inte...],
  table.cell[6/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/veliona-the-world-of-unfolding-minds/")[veliona-the-world-of-unfolding]],
  table.cell[_Bio-templated microchips via implosion fabrication_],
  table.cell[Nanotechnology & Advanced Manufacturing],
  table.cell[5/20],
  table.cell[3/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/adam-marblestone-solving-sciences-biggest-gaps")[adam-marblestone-solving-scien]],
  table.cell[_Programmable synthetic molecular robots for chemical synt..._],
  table.cell[Nanotechnology & Advanced Manufacturing],
  table.cell[5/20],
  table.cell[3/5],
  table.cell[Physics],
  table.cell[Research],
  table.cell[3],
  table.cell[#link("https://www.existentialhope.com/podcasts/david-leigh-exploring-the-possibilities-of-nanotechnology")[david-leigh-exploring-the-poss]],
  table.cell[_Aldehyde-Stabilized Cryopreservation_],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[6/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/dr-ariel-zeleznikow-johnston-the-future-loves-you")[dr-ariel-zeleznikow-johnston-t]],
  table.cell[_AI-powered blog aggregator with conversational interface_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[7/20],
  table.cell[1/5],
  table.cell[Engineering],
  table.cell[Build],
  table.cell[6],
  table.cell[#link("https://www.existentialhope.com/podcasts/eli-dourado-on-accelerating-progress")[eli-dourado-on-accelerating-pr]],
  table.cell[_EgoLets_],
  table.cell[AI-Mediated Deliberation & Collective...],
  table.cell[5/20],
  table.cell[3/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/ken-liu-what-ai-reveals-about-humanity")[ken-liu-what-ai-reveals-about-]],
  table.cell[_Chemical substrate computation / chemical consciousness_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[5/20],
  table.cell[3/5],
  table.cell[Physics],
  table.cell[Research],
  table.cell[2],
  table.cell[#link("https://www.existentialhope.com/podcasts/lee-cronin-catalyzing-progress-through-chemistry")[lee-cronin-catalyzing-progress]],
  table.cell[_Alexa Gentia (machine-negotiated agent legal structures)_],
  table.cell[AI Safety, Alignment & Governance],
  table.cell[6/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/niklas-lundblad-how-ai-can-accelerate-science-its-own-adoption")[niklas-lundblad-how-ai-can-acc]],
  table.cell[_Origin of Life Evolutionary Engine (chemical space search..._],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[5/20],
  table.cell[3/5],
  table.cell[Physics],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/sara-walker-unraveling-lifes-beginnings-with-the-cosmic-perspective")[sara-walker-unraveling-lifes-b]],
  table.cell[_Assembly Theory_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[6/20],
  table.cell[2/5],
  table.cell[Physics],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/sara-walker-unraveling-lifes-beginnings-with-the-cosmic-perspective")[sara-walker-unraveling-lifes-b]],
  table.cell[_National Science and Technology Foresight Agency (NSTFA)_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[6/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/innovation-nation/")[innovation-nation]],
  table.cell[_Minimum-payload terraforming nanomachine for Mars_],
  table.cell[Nanotechnology & Advanced Manufacturing],
  table.cell[3/20],
  table.cell[4/5],
  table.cell[Physics],
  table.cell[Research],
  table.cell[2],
  table.cell[#link("https://www.existentialhope.com/podcasts/lee-cronin-catalyzing-progress-through-chemistry")[lee-cronin-catalyzing-progress]],
  table.cell[_Microbial Interaction Simulation AI (Anthropic-built)_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[5/20],
  table.cell[2/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/fungi-terra/")[fungi-terra]],
  table.cell[_Institute for Human Perplexity_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[5/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[2],
  table.cell[#link("https://worlds.existentialhope.com/world/uniqualia/")[uniqualia]],
  table.cell[_Gene Drives for Wild Animal Suffering Reduction_],
  table.cell[Ecological & Regenerative Systems],
  table.cell[2/20],
  table.cell[4/5],
  table.cell[Regulation],
  table.cell[Convene],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/david-pearce-a-future-without-suffering")[david-pearce-a-future-without-]],
  table.cell[_Focused Philanthropic Bet Modeled on Warren Weaver / Rock..._],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[3/20],
  table.cell[3/5],
  table.cell[Social Acceptance],
  table.cell[Advocate],
  table.cell[6],
  table.cell[#link("https://www.existentialhope.com/podcasts/eric-gilliam-what-history-can-teach-us-about-doing-better-science")[eric-gilliam-what-history-can-]],
  table.cell[_Jurisdictional Arbitrage Special Economic Zones for BCI R..._],
  table.cell[Neurotechnology & Brain-Computer Inte...],
  table.cell[4/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[5],
  table.cell[#link("https://www.existentialhope.com/podcasts/trent-mcconaghy-from-starships-to-tokens-pioneering-futures")[trent-mcconaghy-from-starships]],
  table.cell[_Affective and Socio-Emotional Atmospheric Reading System_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[4/20],
  table.cell[2/5],
  table.cell[Social Acceptance],
  table.cell[Advocate],
  table.cell[5],
  table.cell[#link("https://worlds.existentialhope.com/world/edusafe/")[edusafe]],
  table.cell[_AI-driven individualized peace education system_],
  table.cell[Education, Development & Human Flouri...],
  table.cell[4/20],
  table.cell[2/5],
  table.cell[Regulation],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/unified-peace/")[unified-peace]],
  table.cell[_Elective Cryonic Suspension at Peak Vitality ('Kyasia')_],
  table.cell[Biotech, Medicine & Life Extension],
  table.cell[4/20],
  table.cell[1/5],
  table.cell[Regulation],
  table.cell[Advocate],
  table.cell[2],
  table.cell[#link("https://www.existentialhope.com/podcasts/david-pearce-a-future-without-suffering")[david-pearce-a-future-without-]],
  table.cell[_Earth AI_],
  table.cell[Economic Systems & Resource Distribution],
  table.cell[3/20],
  table.cell[2/5],
  table.cell[Coordination],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/protopia-peace-project/")[protopia-peace-project]],
  table.cell[_Neural Linguistic Interfaces_],
  table.cell[Neurotechnology & Brain-Computer Inte...],
  table.cell[2/20],
  table.cell[3/5],
  table.cell[Engineering],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://worlds.existentialhope.com/world/unity-through-diversity/")[unity-through-diversity]],
  table.cell[_Phenomenal Binding-Based Sentient AI Architecture_],
  table.cell[Neurotechnology & Brain-Computer Inte...],
  table.cell[1/20],
  table.cell[3/5],
  table.cell[Physics],
  table.cell[Research],
  table.cell[1],
  table.cell[#link("https://www.existentialhope.com/podcasts/david-pearce-a-future-without-suffering")[david-pearce-a-future-without-]],
  table.cell[_Grabby Aliens Three-Parameter Model_],
  table.cell[Scientific Research & Knowledge Infra...],
  table.cell[0/20],
  table.cell[2/5],
  table.cell[Physics],
  table.cell[Research],
  table.cell[4],
  table.cell[#link("https://www.existentialhope.com/podcasts/robin-hanson-on-futurism-his-best-career-advice")[robin-hanson-on-futurism-his-b]],
)


#line(length: 100%, stroke: 0.5pt + luma(180))


== 6. How to Get Involved


=== Fund (7 entities)

Working concepts exist but lack capital to scale.

_Watch list_ (7 entities):
- The Collective of Inner Weavers (Bottleneck: Funding)
- #link("https://hieroglyph.asu.edu/")[Project Hieroglyph] (Bottleneck: Funding)
- Closed-loop gene therapy for seizure suppression via activity-sensing potassium-channel upregulation (Bottleneck: Regulation)
- #link("https://www.openwater.health/")[Openwater] universal diagnostic/therapeutic device (Bottleneck: Regulation)
- #link("https://en.wikipedia.org/wiki/Biophilic_design")[Biophilic Architecture] (Bottleneck: Funding)
- #link("https://www.convergentresearch.org/about-fros")[Focused Research Organizations (FROs)] (Bottleneck: Funding)
- #link("https://en.wikipedia.org/wiki/Raytheon_BBN")[BBN]-style Applied R&D Contractor (New BBNs) (Bottleneck: Coordination)

=== Build (17 entities)

The research is done and the path is clear. What's missing is engineering teams to build it.

_Watch list_ (17 entities):
- Translation Language Models (TLMs) with citizen-owned training databases (Bottleneck: Coordination)
- The #link("https://en.wikipedia.org/wiki/Delphi_method")[Delphi] Collaboration Protocol (Bottleneck: Coordination)
- #link("https://lean-lang.org/")[Lean FRO] (interactive theorem proving infrastructure for mathematics and AI) (Bottleneck: Engineering)
- Large-scale AI-mediated deliberation system (Bottleneck: Engineering)
- #link("https://deepfission.com/")[Deep Fission] borehole nuclear reactor (Bottleneck: Regulation)
- Safety-Netted #link("https://en.wikipedia.org/wiki/Decentralized_autonomous_organization")[DAOs] (Bottleneck: Engineering)
- #link("https://themultiplicity.ai/")[Multiplicity.ai] (Bottleneck: Engineering)
- #link("https://en.wikipedia.org/wiki/Futarchy")[Futarchy] (Bottleneck: Social Acceptance)
- Author Personal Knowledge Graph / Writing Corpus Utility (Bottleneck: Engineering)
- Tool AI for Tool AI (Bottleneck: Engineering)
- _...and 7 more_

=== Research (68 entities)

Promising directions that need more investigation before they're ready for deployment.

_Spotlight:_
- #link("#ai-cryptographic-oracle-with-zero-knowledge-iot-auditing-and-jury-dao")[_AI cryptographic oracle with zero-knowledge IoT auditing and jury-DAO_] — A fraud-resistance layer combining #link("https://en.wikipedia.org/wiki/Zero-knowledge_proof")[zero-knowledge proofs] from IoT sensor data, AI anomaly detection, stake-slashing penalties, and a decentralized human jury for retroactive balance correction. (Bottleneck: Coordination)
- #link("#moral-trade")[_Moral Trade_] — A mechanism by which people or groups with different moral priorities swap concessions so that each gets more of what they care about than unilateral action would yield. Concept originated by #link("https://en.wikipedia.org/wiki/Toby_Ord")[Toby Ord]. (Bottleneck: Coordination)
- #link("#comprehensive-ai-services-drexler")[_Comprehensive AI Services (Drexler)_] — An architecture of many narrow, domain-limited superhuman AIs that interact competitively rather than a single general superintelligence, achieving safety through structural narrowness. Based on #link("https://www.fhi.ox.ac.uk/wp-content/uploads/Reframing_Superintelligence_FHI-TR-2019-1.1-1.pdf")[Eric Drexler's framework]. (Bottleneck: Coordination)
- #link("#wisdom-dao")[_Wisdom DAO_] — A #link("https://en.wikipedia.org/wiki/Decentralized_autonomous_organization")[decentralized autonomous organization] where human citizens and AI systems jointly propose, deliberate, and vote on governance policy using weighted voting and #link("https://en.wikipedia.org/wiki/Blockchain")[blockchain] transparency. (Bottleneck: Regulation)

_Watch list_ (64 entities):
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
- _...and 54 more_

=== Advocate (39 entities)

These need policy changes, regulatory frameworks, or public support to move forward.

_Spotlight:_
- #link("#tokenized-neural-data-sharing-with-selective-disclosure")[_Tokenized neural data sharing with selective disclosure_] — A privacy architecture for #link("https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface")[BCI] systems in which neural data is tokenized so users can selectively disclose specific streams of thought or brain state while retaining others as private. (Bottleneck: Regulation)
- #link("#interbeing-forum")[_Interbeing Forum_] — A rotating bioregional assembly that grants formal representation to ecosystems and future generations through human guardians advised by #link("https://en.wikipedia.org/wiki/Digital_twin")[digital twin] data. (Bottleneck: Regulation)
- #link("#attack-dog-dao-for-climate")[_Attack Dog DAO for Climate_] — A DAO that funds and coordinates environmental litigation on behalf of legally-recognized natural entities, financed through tokenized litigation investment. (Bottleneck: Regulation)
- #link("#accord-of-watersheds")[_Accord of Watersheds_] — An international treaty framework that organizes political cooperation around #link("https://en.wikipedia.org/wiki/Drainage_basin")[watershed] and bioregional boundaries rather than national borders. (Bottleneck: Regulation)
- #link("#watershed-parliaments")[_Watershed Parliaments_] — Bioregional governance bodies organized around watershed boundaries rather than political borders, incorporating ecological feedback into formal decision-making. (Bottleneck: Regulation)
- #link("#loyal-ai-assistance-fiduciary-ai-assistance")[_Loyal AI Assistance (Fiduciary AI Assistance)_] — A personal AI system explicitly designed to be loyal to the individual user's goals rather than to platform or advertiser interests, contrasted with current assistants like Siri or Alexa. Based on #link("https://arxiv.org/abs/2308.02435")[fiduciary AI principles]. (Bottleneck: Regulation)

_Watch list_ (33 entities):
- #link("https://lexdao.org/")[LexDAO] (Bottleneck: Regulation)
- De novo designed universal flu vaccines (#link("https://www.ipd.uw.edu/")[Neil King] / #link("https://www.bakerlab.org/")[Baker Lab] platform) (Bottleneck: Regulation)
- Hybrid Market impact bond ledger (Bottleneck: Regulation)
- Mandatory Open-Source AI Release Policy (Bottleneck: Regulation)
- #link("https://orare.world/")[Orare] - AI-powered Futarchy governance system (Bottleneck: Social Acceptance)
- Global Personhood Token / Trust-of-Personhood Standard (Bottleneck: Regulation)
- Integration of #link("https://www.brainpreservation.org/")[Brain Preservation] into the Medical System (Bottleneck: Regulation)
- Open-source AI-powered research funding and knowledge platform (Bottleneck: Regulation)
- Interplanetary Cooperative (Bottleneck: Regulation)
- The Flourishing Foundation (Bottleneck: Regulation)
- _...and 23 more_

=== Convene (58 entities)

The pieces exist separately — what's missing is coordination between stakeholders.

_Spotlight:_
- #link("#community-governed-ai-mesh-systems")[_Community-Governed AI Mesh Systems_] — Decentralized AI networks trained on locally governed data and stewarded by community trust circles rather than centralized corporate or state actors. (Bottleneck: Coordination)
- #link("#universal-ai-learning-uncommons-ualu")[_Universal AI Learning UnCommons (UALU)_] — A federated governance institution that develops, maintains, and audits AI education tools through multi-stakeholder councils including elders, learners, and ethicists. (Bottleneck: Coordination)
- #link("#bci-operating-system-bci-os")[_BCI Operating System (BCI-OS)_] — An open-source operating system layer for #link("https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface")[brain-computer interfaces] that embeds agency evaluation, AI model compatibility, and privacy standards as core OS-level features. (Bottleneck: Coordination)
- #link("#civic-systems-co-op")[_Civic Systems Co-Op_] — A global open-source consortium that develops and maintains ethical AI tools for municipal and community governance. (Bottleneck: Coordination)
- #link("#interoperable-governance-protocol-stack")[_Interoperable Governance Protocol Stack_] — A shared technical and governance protocol layer that allows citizens to port digital identities, benefits, and credentials across distinct federated city-state systems, and enables AI systems across those jurisdictions to align resource allocation and crisis modeling. (Bottleneck: Regulation)
- #link("#dao-governed-open-innovation-platform-for-tlm-documentation-and-training-data")[_DAO-governed open innovation platform for TLM documentation and training data_] — A DAO-based governance structure that mandates open-source documentation and community-sourced feedback loops for translation model development and adaptation. (Bottleneck: Coordination)
- #link("#digital-twins-for-communities-and-ecosystems")[_Digital Twins for Communities and Ecosystems_] — Real-time #link("https://en.wikipedia.org/wiki/Digital_twin")[digital models] of communities and ecosystems that enable participatory future simulation with locally-owned data. (Bottleneck: Coordination)
- #link("#the-global-deliberation-coordinator")[_The Global Deliberation Coordinator_] — A platform institution designed to coordinate global #link("https://en.wikipedia.org/wiki/Deliberative_democracy")[deliberative processes] and collective decision-making specifically around AI governance. (Bottleneck: Coordination)
- #link("#epistemic-stack")[_Epistemic stack_] — A citation and provenance system for all information—from newspaper articles to social media claims—that lets users trace any assertion back to its raw data sources, with trust scores based on historical accuracy of each link in the chain. (Bottleneck: Coordination)

_Watch list_ (49 entities):
- #link("https://arxiv.org/abs/2308.02435")[AI Fiduciaries] (Bottleneck: Coordination)
- Privacy-Preserving Global Regulatory Markets for AI Verification (Bottleneck: Coordination)
- Continuity Guild (Bottleneck: Coordination)
- BioEcho Mesh (Bottleneck: Coordination)
- The Mnemosyne Assembly (Bottleneck: Coordination)
- Open Cognition Ledger (Bottleneck: Coordination)
- Living Rights Network (Bottleneck: Coordination)
- #link("https://en.wikipedia.org/wiki/OpenProcurement")[Federated Procurement Platforms] (Bottleneck: Coordination)
- contextual autonomy (Bottleneck: Coordination)
- Publishing for Machines (machine-readable scientific publishing framework) (Bottleneck: Social Acceptance)
- _...and 39 more_


#line(length: 100%, stroke: 0.5pt + luma(180))


== 7. Conclusion


The 189 hyper-entities identified in this report represent a curated map of futures that are already shaping the present. They are not predictions — they are coordination attractors, systems around which investment, research, and narrative are already forming even before the first prototype exists. What makes them worth attending to now is precisely that earliness: the decisions made in the next five to ten years about which of these systems to fund, govern, and build will determine whether the technologies of the 2030s and 2040s concentrate power or distribute it, protect human agency or erode it, accelerate beneficial futures or foreclose them.

For funders and policymakers, the key question is not "what is the most powerful technology on the horizon?" Power is not scarce in current technology development — attention and capital are already flowing toward the most transformative systems. The question is: what infrastructure ensures that powerful technologies serve broad human interests rather than narrow ones?

Several patterns in this data are striking. Epistemic infrastructure — systems for verifying truth, enhancing collective reasoning, and making knowledge legible — is chronically underfunded relative to its importance. Governance tools and coordination protocols tend to have the longest time horizons but the highest systemic leverage. Energy and ecological systems consistently score high on d/acc alignment, suggesting that sustainability transitions, if done right, could be among the most broadly beneficial shifts.

The maturity distribution tells its own story. The modal TRL of 3.9 means most entities are between proof-of-concept and early validation. This is not a list of things almost ready to ship — it is a list of things that need patient capital, cross-disciplinary collaboration, and regulatory frameworks designed for experimentation rather than premature standardization.

The window for shaping these systems is open now, and it will not remain open indefinitely. Once infrastructure standards calcify around centralized control, once regulatory frameworks cement incumbent advantages, once public narrative settles on a narrow vision of which futures are possible — the range of available paths narrows dramatically.

What can you do with this information? If you are a funder, the Tier 1 spotlight entities and the action breakdown in this report provide a starting point. Consider whether your portfolio has exposure to infrastructure that works across many possible futures, not just the ones currently receiving the most hype. If you are a policymaker, the entities scoring highest on d/acc alignment represent the systems most worth building regulatory runway for today. If you are a researcher or technologist, the bottleneck analysis throughout this report identifies genuine frontiers: places where the field lacks basic understanding, where governance frameworks don't yet exist, or where the coordination problem is more tractable than the technical one.

This research is designed to be repeatable and extensible. Future iterations should expand the source corpus to include non-English discourse communities, incorporate structured expert elicitation alongside automated scoring, and track entities longitudinally to see which ones move from foundational research toward deployment. The goal is not to produce a single authoritative ranking but to build a shared language for talking about which futures are forming, which deserve more resources, and how the choices we make today constrain or expand the range of tomorrow.

#line(length: 100%, stroke: 0.5pt + luma(180))


== 8. Appendix


=== A. Methodology


This report represents the third iteration of the Foresight Institute's hyper-entity pipeline, designated V3. The pipeline has five stages: extraction, deduplication, web research, scoring, and curation into tiers.

_Source extraction._ Candidate entities were extracted from 109 distinct sources hosted on or linked through Existential Hope. These fell into three categories: transcripts from the Existential Hope podcast series, submissions to the Foresight World Gallery, and essays contributed to the AI Pathways project. Extraction targeted named systems, protocols, institutions, or frameworks described as anticipated or proposed rather than fully operational.

_Deduplication._ Raw extraction produced substantial overlap, with the same concept appearing under variant names across sources. Candidates were deduplicated by concept rather than by label, collapsing near-synonyms into single entries and preserving the most descriptive name. This process reduced the candidate pool to 189 distinct entities.

_Web research._ Each deduplicated entity was researched to establish current development status, identify relevant actors, and assign a Technology Readiness Level on the standard 1–9 scale. The distribution skewed early-stage, with a modal TRL of 4 and a range of 1–8. Most candidates have demonstrated feasibility in laboratory or limited-context conditions but have not yet achieved validated prototypes.

_Scoring._ Each entity was scored on three dimensions. The d/acc score (0–20) assessed alignment with democratic, decentralized, defensive, and differential acceleration principles, with five points available per dimension. The transformative score (0–5) captured how much it could change the way societies coordinate or govern. The actionability score (0–5) assessed whether concrete next steps exist and whether current actors can execute them. Composite scores summed d/acc and transformative dimensions. Scoring was performed by the #link("https://docs.anthropic.com/en/api/getting-started")[Claude API] (#link("https://www.anthropic.com/")[Anthropic]); we reviewed results by hand at the tiering and editorial stages to catch systematic errors and resolve ambiguous cases.

_Tiering._ Entities with composite scores of 14 or above were designated Tier 1 spotlight entities, yielding 19 candidates. The remaining 170 entities form the Tier 2 watch list. Twenty-seven entities appeared in both V3 and the prior V2 analysis, giving us a consistency check that was weighted positively in borderline cases. Primary bottleneck and recommended action type were assigned categorically rather than scored, based on the web research stage assessment of what currently constrains each entity's development.

=== B. Pipeline Prompts


The following prompts were used in the automated stages of the pipeline. All were executed via the Claude API (Anthropic).

_Extraction prompt (podcasts)._
#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[Extract SPECIFIC proposals, systems, architectures, or technologies discussed by the speaker that are: 1. NAMED or CONCRETE enough that someone could write a spec for it 2. NOT YET BUILT at scale (may have prototypes or research) 3. DISCUSSED SERIOUSLY with some mechanism explained (not throwaway mentions)  ANTI-PATTERNS (do NOT extract these): - Generic field descriptions ('AI-enhanced governance') - Vague compound nouns you invented - Already widely deployed technology - Abstract values or principles without implementation mechanisms]


_Extraction prompt (world gallery)._
#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[This is a brief speculative world sketch. Extract 0-2 SPECIFIC technologies, institutions, or systems described that someone could actually build or fund. If nothing is concrete enough to have a mechanism of action, return an empty list. Do NOT extract vague concepts or genre labels.]


_Deduplication prompt._
#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[You are comparing two hyper-entity candidates to determine if they describe the same concept. Classify the relationship as exactly one of: - SAME: These describe the same entity/concept/system (even if named differently). They should be merged. - OVERLAPPING: Related concepts in the same domain, but distinct enough to keep separate. - DISTINCT: Unrelated or only superficially similar.]


_Scoring prompt (excerpt)._
#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[Score this hyper-entity candidate on three dimensions. Use ONLY evidence from the provided description and research data. No evidence = score 0.  A. d/acc Values (0–5 per dimension: Democratic, Decentralized, Defensive, Differential) B. Transformative potential (0–5) C. Actionability: primary bottleneck and recommended action type]


=== C. Scoring Details


Full scoring breakdown for all Tier 1 entities.

=== Community-Governed AI Mesh Systems

_Composite: 21_ | Group: Decentralized & Democratic Institutions | TRL: 4 | v2 consensus: No

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[5/5],
  table.cell[Governance explicitly handled by designated community trust circles (Indigenous and racialized groups) with consent frameworks defining access and use protocols. Decision-making authority distribut...],
  table.cell[d/acc: Decentralized],
  table.cell[5/5],
  table.cell[Mesh architecture explicitly distributes both compute and decision-making authority locally with no single node controlling the system. Federated learning frameworks (Flower, PySyft) enable distrib...],
  table.cell[d/acc: Defensive],
  table.cell[4/5],
  table.cell[System protects community data sovereignty and prevents extraction by centralized actors. Preserves privacy through federated learning (data stays local). Defends against colonization patterns thro...],
  table.cell[d/acc: Differential],
  table.cell[3/5],
  table.cell[Accelerates defensive capabilities (data sovereignty, privacy-preserving training, distributed governance) relative to centralized AI extraction models. However, research data does not substantivel...],
  table.cell[_d/acc Total_],
  table.cell[_17/20_],
  table.cell[Strong d/acc alignment on democratic and decentralized dimensions with clear evidence. Defensive posture evident but not exclusively defensive. Differential advantage claimed but not empirically demonstrated in source material.],
  table.cell[Transformative],
  table.cell[4/5],
  table.cell[If fully implemented and adopted at scale, this would transform multiple fields: (1) AI governance—replacing corporate/state-centric models with community-governed alternatives; (2) Indigenous data so],
  table.cell[Bottleneck],
  table.cell[Coordination],
  table.cell[Research data identifies 'integration complexity: combining three distinct technical and governance layers requires solving interoperability challenges that no current platform addresses' and 'governa],
  table.cell[Action],
  table.cell[Convene],
  table.cell[Given that technical components exist separately (federated learning frameworks mature, Indigenous governance principles established, mesh networks operational) but lack integration, the immediate act],
)


=== Universal AI Learning UnCommons (UALU)

_Composite: 20_ | Group: Education, Development & Human Flourishing | TRL: 3 | v2 consensus: Yes

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[5/5],
  table.cell[UALU explicitly distributes decision-making power through 'governance councils composed of diverse stakeholders—elders, learners, technologists, ethicists' with 'co-creation and oversight' mechanis...],
  table.cell[d/acc: Decentralized],
  table.cell[4/5],
  table.cell[Described as 'decentralised network of community nodes, each contributing to co-creation' with 'federated structure' allowing 'local adaptation while maintaining shared accountability frameworks.' ...],
  table.cell[d/acc: Defensive],
  table.cell[5/5],
  table.cell[UALU's core function is auditing, bias mitigation, and cultural appropriateness oversight—purely protective mechanisms. No offensive capabilities described. Focus on 'justice and care' and preventi...],
  table.cell[d/acc: Differential],
  table.cell[3/5],
  table.cell[UALU accelerates defensive AI governance (auditing, bias detection, ethical oversight) relative to uncontrolled AI deployment. However, research data shows 'most existing initiatives focus on top-d...],
  table.cell[_d/acc Total_],
  table.cell[_17/20_],
  table.cell[],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[UALU transforms the AI education governance field by institutionalizing elder/community council oversight and federated accountability—currently absent at scale. Research confirms 'formal elder/commun],
  table.cell[Bottleneck],
  table.cell[Coordination],
  table.cell[Research data explicitly identifies 'Institutional fragmentation—no existing federated model integrates elder councils, learners, ethicists, and technologists with formal accountability mechanisms' an],
  table.cell[Action],
  table.cell[Convene],
  table.cell[Given TRL 3 status, existing partial analogues (Mozilla, African Union, UNESCO, AIGN), and identified coordination barriers, immediate action should be convening multi-stakeholder working groups to de],
)


=== AI cryptographic oracle with zero-knowledge IoT auditing and jury-DAO

_Composite: 19_ | Group: Decentralized & Democratic Institutions | TRL: 4 | v2 consensus: No

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[4/5],
  table.cell[Jury-DAO component explicitly enables 'randomly selected jury-DAO of token holders can vote to retroactively adjust balances,' distributing fraud adjudication decisions across decentralized human p...],
  table.cell[d/acc: Decentralized],
  table.cell[4/5],
  table.cell[System eliminates single points of failure through: (1) distributed IoT sensor network generating proofs, (2) decentralized AI anomaly detection layer, (3) jury-DAO replacing centralized arbiters, ...],
  table.cell[d/acc: Defensive],
  table.cell[5/5],
  table.cell[Purely defensive architecture: zero-knowledge proofs protect sensor data from spoofing, AI anomaly detection identifies fraudulent claims, quadratic slashing deters cheating, jury-DAO provides huma...],
  table.cell[d/acc: Differential],
  table.cell[3/5],
  table.cell[Moderately differential: ZK-IoT proofs and AI anomaly detection advance defensive fraud detection faster than attackers can generate undetectable false claims. However, differential advantage is no...],
  table.cell[_d/acc Total_],
  table.cell[_16/20_],
  table.cell[],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[Transforms a field (blockchain fraud detection and governance): Combines four previously separate components (ZK-IoT, AI anomaly detection, quadratic slashing, jury-DAO) into integrated fraud-resistan],
  table.cell[Bottleneck],
  table.cell[Coordination],
  table.cell[N/A],
  table.cell[Action],
  table.cell[Research],
  table.cell[N/A],
)


=== Moral Trade

_Composite: 18_ | Group: AI-Mediated Deliberation & Collective Intelligence | TRL: 2 | v2 consensus: Yes

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[5/5],
  table.cell[Moral trade explicitly distributes decision-making power by allowing diverse groups with different moral priorities to negotiate outcomes rather than having any single moral view dominate. Source s...],
  table.cell[d/acc: Decentralized],
  table.cell[4/5],
  table.cell[The mechanism is inherently decentralized—it operates through bilateral/multilateral negotiation between parties rather than centralized authority. However, at civilizational scale, some coordinati...],
  table.cell[d/acc: Defensive],
  table.cell[3/5],
  table.cell[Moral trade is primarily a coordination mechanism rather than inherently defensive or offensive. It enables peaceful resolution of moral disagreements through negotiation rather than competition or...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[No evidence in source material addresses differential acceleration of defensive vs. offensive capabilities. Moral trade is a coordination/negotiation framework that could theoretically be applied t...],
  table.cell[_d/acc Total_],
  table.cell[_14/20_],
  table.cell[],
  table.cell[Transformative],
  table.cell[4/5],
  table.cell[Moral trade has potential to transform multiple fields by enabling civilizational-scale coordination across diverse moral communities. Source describes 'huge opportunities' at civilization scale and n],
  table.cell[Bottleneck],
  table.cell[Coordination],
  table.cell[N/A],
  table.cell[Action],
  table.cell[Research],
  table.cell[N/A],
)


=== BCI Operating System (BCI-OS)

_Composite: 18_ | Group: Neurotechnology & Brain-Computer Interfaces | TRL: 3 | v2 consensus: No

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[4/5],
  table.cell[Open-source governance structure with standards body explicitly designed to maintain human-agency principles. Source states 'open-source governance structure and standards body are created to maint...],
  table.cell[d/acc: Decentralized],
  table.cell[3/5],
  table.cell[OS-level architecture reduces single points of failure by enforcing privacy and agency at the platform layer rather than leaving it to individual applications. Open-source model enables distributed...],
  table.cell[d/acc: Defensive],
  table.cell[5/5],
  table.cell[Purely defensive in posture: embeds privacy protocols, agency evaluation, and consent mechanisms at OS level to protect users from unauthorized neural data access. Source emphasizes 'safeguards hum...],
  table.cell[d/acc: Differential],
  table.cell[3/5],
  table.cell[Moderately differential: privacy and agency protections embedded at OS level could slow malicious actors' ability to exploit BCIs compared to fragmented landscape where each app handles security in...],
  table.cell[_d/acc Total_],
  table.cell[_15/20_],
  table.cell[Strong on democratic governance intent and defensive posture; moderate on decentralization and differential advantage.],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[Transforms a field (neurotechnology/BCI development). BCI-OS would fundamentally restructure how BCIs are developed, deployed, and governed by establishing privacy and agency as architectural requirem],
  table.cell[Bottleneck],
  table.cell[Coordination],
  table.cell[Research data explicitly identifies 'fragmented BCI ecosystem: hardware manufacturers, software developers, and application creators operate independently without standardized interfaces or governance],
  table.cell[Action],
  table.cell[Convene],
  table.cell[TRL 3 status with proof-of-concept work at AE Studio and OpenBCI indicates technical feasibility is not the immediate constraint. Funding is not identified as a barrier. The critical next step is conv],
)


=== Tokenized neural data sharing with selective disclosure

_Composite: 17_ | Group: Neurotechnology & Brain-Computer Interfaces | TRL: 2 | v2 consensus: No

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[4/5],
  table.cell[Tokenized selective disclosure directly distributes decision-making power to individual users over their own neural data. Users can 'grant or revoke access to specific tokens' and choose 'what you ...],
  table.cell[d/acc: Decentralized],
  table.cell[2/5],
  table.cell[The architecture itself is user-centric but relies on regulatory frameworks (HIPAA, state laws) and consent management systems that are inherently centralized or platform-mediated. No evidence of p...],
  table.cell[d/acc: Defensive],
  table.cell[5/5],
  table.cell[This is purely defensive: it protects neural data privacy by limiting exposure, enabling users to withhold sensitive cognitive content, and preventing unauthorized access to specific thought stream...],
  table.cell[d/acc: Differential],
  table.cell[3/5],
  table.cell[The architecture favors defense by enabling granular privacy controls that are difficult for attackers to circumvent without user consent. However, the research data notes 're-identification even f...],
  table.cell[_d/acc Total_],
  table.cell[_14/20_],
  table.cell[Strong on democratic empowerment and defensive posture; moderate on decentralization and differential advantage.],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[This transforms the field of neural data governance and BCI ethics. It moves from binary consent models (share all or nothing) to granular, user-controlled access control, fundamentally changing how n],
  table.cell[Bottleneck],
  table.cell[Regulation],
  table.cell[While regulatory frameworks exist (Montana, Colorado, California, Chile), they treat neural data as sensitive information without implementing granular tokenized mechanisms. Research data explicitly s],
  table.cell[Action],
  table.cell[Advocate],
  table.cell[TRL 2 indicates proof-of-concept stage. No funding barriers are documented. The immediate action is regulatory: advocate for unified federal standards and technical specifications for tokenized neural],
)


=== Civic Systems Co-Op

_Composite: 17_ | Group: AI Safety, Alignment & Governance | TRL: 5 | v2 consensus: No

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[4/5],
  table.cell[Mechanism explicitly states 'distributed across member organizations rather than controlled by a single vendor or government' and 'member cities and communities contribute to and draw from a shared...],
  table.cell[d/acc: Decentralized],
  table.cell[4/5],
  table.cell[Design eliminates single vendor or government control point. Research data confirms 'no unified global open-source consortium exists' currently, but the proposed model distributes maintenance and g...],
  table.cell[d/acc: Defensive],
  table.cell[4/5],
  table.cell[Explicitly framed around 'ethical AI tools' with 'transparent decision logs' and 'ethical standards.' Purpose is governance transparency and accountability, not offensive capability. Open-source mo...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[No evidence in source material that this accelerates defensive AI development faster than offensive. The mechanism focuses on governance transparency and ethical standards for municipal use cases, ...],
  table.cell[_d/acc Total_],
  table.cell[_14/20_],
  table.cell[],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[Transforms the municipal AI governance field by shifting from vendor-controlled (OpenGov serving 2,000+ communities) or loosely federated registries (DPGA with 150+ tools) to a unified cooperative mod],
  table.cell[Bottleneck],
  table.cell[Coordination],
  table.cell[N/A],
  table.cell[Action],
  table.cell[Convene],
  table.cell[N/A],
)


=== Interbeing Forum

_Composite: 17_ | Group: Decentralized & Democratic Institutions | TRL: 3 | v2 consensus: No

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[4/5],
  table.cell[Rotating steward selection from bioregions prevents power entrenchment. Formal representation granted to non-human entities and future generations through designated guardians. Decision-making weig...],
  table.cell[d/acc: Decentralized],
  table.cell[4/5],
  table.cell[Bioregional structure distributes authority across geographic regions rather than centralizing in nation-states. Rotating basis prevents single points of control. Multiple precedents (OACC since 19...],
  table.cell[d/acc: Defensive],
  table.cell[4/5],
  table.cell[Explicitly protective: safeguards ecosystem integrity, represents future generations, audits digital infrastructure for integrity. Designed to constrain rather than expand extractive capacity. Over...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[Digital twin technology could accelerate defensive monitoring and decision-making, but research data shows digital twins are 'in prototype/pilot phase' with 'no integrated system' yet existing. The...],
  table.cell[_d/acc Total_],
  table.cell[_14/20_],
  table.cell[],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[Transforms a field (environmental governance and bioregional decision-making). Combines three existing but separate precedents (legal personhood for ecosystems, future generations representation, citi],
  table.cell[Bottleneck],
  table.cell[Regulation],
  table.cell[N/A],
  table.cell[Action],
  table.cell[Advocate],
  table.cell[N/A],
)


=== Interoperable Governance Protocol Stack

_Composite: 16_ | Group: Decentralized & Democratic Institutions | TRL: 4 | v2 consensus: Yes

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[3/5],
  table.cell[Protocol stack enables citizens to port identities and benefits across systems, increasing individual agency. However, decision-making power remains with jurisdictional authorities who implement th...],
  table.cell[d/acc: Decentralized],
  table.cell[4/5],
  table.cell[Architecture explicitly designed as federated with modular governance components. No single point of control: 'any compliant local system can read and honor records issued by another.' Multiple jur...],
  table.cell[d/acc: Defensive],
  table.cell[4/5],
  table.cell[System is fundamentally protective: enables crisis response, resource sharing, and citizen benefit access without requiring data centralization. Designed to preserve jurisdictional autonomy while e...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[Limited evidence of differential acceleration. The protocol stack itself is defensive (coordination, not weaponization), but research data shows 'federated learning frameworks for privacy-preservin...],
  table.cell[_d/acc Total_],
  table.cell[_13/20_],
  table.cell[],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[Transforms a field (emergency response and cross-jurisdictional governance coordination). Evidence: enables 'relief in hours instead of weeks' and 'seamless resource sharing across local and regional],
  table.cell[Bottleneck],
  table.cell[Regulation],
  table.cell[N/A],
  table.cell[Action],
  table.cell[Convene],
  table.cell[N/A],
)


=== Comprehensive AI Services (Drexler)

_Composite: 16_ | Group: AI Safety, Alignment & Governance | TRL: 2 | v2 consensus: No

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[3/5],
  table.cell[CAIS distributes decision-making across multiple competing specialized systems rather than concentrating it in a single superintelligence. The 'ecology of competing specialized systems' provides ch...],
  table.cell[d/acc: Decentralized],
  table.cell[4/5],
  table.cell[The architecture explicitly eliminates single points of failure by partitioning capabilities into domain-specific services. Source states 'structural narrowness' prevents 'unilateral takeover,' and...],
  table.cell[d/acc: Defensive],
  table.cell[4/5],
  table.cell[CAIS is explicitly framed as a safety architecture: 'safety through narrowness' and 'guardrails we've put in place.' Architectural constraints prevent systems from doing 'end-runs around' safety me...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[CAIS could accelerate defensive capabilities by making uncontrolled generalization structurally difficult. However, research data notes 'foundation models may have undermined some CAIS assumptions'...],
  table.cell[_d/acc Total_],
  table.cell[_13/20_],
  table.cell[],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[CAIS transforms AI safety discourse and the conceptual framing of superintelligence (field-level impact). It offers a fundamentally different architectural paradigm for organizing AI systems. However,],
  table.cell[Bottleneck],
  table.cell[Coordination],
  table.cell[N/A],
  table.cell[Action],
  table.cell[Research],
  table.cell[N/A],
)


=== Attack Dog DAO for Climate

_Composite: 16_ | Group: Ecological & Regenerative Systems | TRL: 3 | v2 consensus: No

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[4/5],
  table.cell[DAO structure inherently distributes governance via token-holder voting. Source describes 'decentralized governance' as core mechanism. However, evidence shows no actual implementation, so democrat...],
  table.cell[d/acc: Decentralized],
  table.cell[3/5],
  table.cell[DAO component reduces single points of failure in capital pooling and decision-making. However, research data identifies critical centralization risks: 'courts have deemed DAOs general partnerships...],
  table.cell[d/acc: Defensive],
  table.cell[4/5],
  table.cell[Mechanism is fundamentally defensive: funding litigation against polluters and harmful actors to protect natural entities. Creates market deterrent against environmental harm rather than enabling n...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[Weak differential advantage. While litigation finance creates defensive incentives, it does not accelerate defensive technology faster than offensive technology. Polluters can equally access litiga...],
  table.cell[_d/acc Total_],
  table.cell[_13/20_],
  table.cell[Strong on democratic distribution and defensive posture; moderate on decentralization due to liability and guardian bottlenecks; weak on differential advantage.],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[Transforms a field (environmental law and climate litigation). Creates new market mechanism linking financial incentives to environmental protection via legal personhood frameworks. Combines three pre],
  table.cell[Bottleneck],
  table.cell[Regulation],
  table.cell[Research data identifies three unresolved regulatory barriers: (1) 'Legal uncertainty around DAO liability...creates structural risk'; (2) 'Environmental personhood frameworks lack standardized liabil],
  table.cell[Action],
  table.cell[Advocate],
  table.cell[Immediate action should target regulatory clarity and legal framework development. Funding or building would encounter insurmountable legal barriers. Research is ongoing (publications cited). Advocacy],
)


=== Wisdom DAO

_Composite: 16_ | Group: Decentralized & Democratic Institutions | TRL: 4 | v2 consensus: No

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[4/5],
  table.cell[Mechanism explicitly distributes decision-making to citizens via personal AI assistants and weighted voting. All citizens can propose and vote on governance policy. Research data shows 40% particip...],
  table.cell[d/acc: Decentralized],
  table.cell[4/5],
  table.cell[Built on blockchain ledger with smart contract enforcement, eliminating centralized bureaucratic gatekeepers. DAO infrastructure (Aragon, MakerDAO precedents) demonstrates technical feasibility of ...],
  table.cell[d/acc: Defensive],
  table.cell[3/5],
  table.cell[Mechanism is primarily defensive: reduces corruption through transparency, prevents centralized power concentration, and uses smart contracts to enforce decisions rather than enable unilateral acti...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[Mechanism accelerates defensive governance infrastructure (transparency, distributed decision-making, corruption reduction). However, research data shows AI agents generate voting recommendations w...],
  table.cell[_d/acc Total_],
  table.cell[_13/20_],
  table.cell[],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[Transforms governance field by shifting from centralized bureaucracy to hybrid human-AI decentralized decision-making. Research demonstrates 97% alignment with historical decisions and 40% participati],
  table.cell[Bottleneck],
  table.cell[Regulation],
  table.cell[N/A],
  table.cell[Action],
  table.cell[Research],
  table.cell[N/A],
)


=== Accord of Watersheds

_Composite: 16_ | Group: International Governance & Coordination | TRL: 6 | v2 consensus: No

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[4/5],
  table.cell[Mechanism explicitly includes 'nations, Indigenous governments, and regional bodies' as signatory parties with multi-stakeholder coordination. IJC and MRC implementations demonstrate 'multi-stakeho...],
  table.cell[d/acc: Decentralized],
  table.cell[3/5],
  table.cell[Distributes authority from national capitals to watershed-based governance bodies, reducing single points of control. However, research data shows 'fragmented form across multiple regional implemen...],
  table.cell[d/acc: Defensive],
  table.cell[4/5],
  table.cell[Framework is explicitly defensive: 'protect rather than attack,' focused on 'conservation and conflict resolution,' 'resource allocation follow hydrological logic,' and 'ecosystem-centered governan...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[No evidence in source material that this framework accelerates defensive technology faster than offensive technology. The mechanism focuses on governance structure and resource coordination, not te...],
  table.cell[_d/acc Total_],
  table.cell[_13/20_],
  table.cell[Strong on democratic inclusion and defensive orientation; moderate on decentralization and weak on differential acceleration.],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[Transforms a field (environmental governance and international law). Shifts organizing principle from national borders to ecological boundaries—a fundamental reframing of how transnational cooperation],
  table.cell[Bottleneck],
  table.cell[Regulation],
  table.cell[TRL 6 indicates operational governance structures exist, but 'a comprehensive international treaty framework...remains at conceptual stage.' Barriers section identifies 'entrenched national sovereignt],
  table.cell[Action],
  table.cell[Advocate],
  table.cell[Given TRL 6 status with existing implementations (IJC, MRC) and pilot projects (Cascadia, Amazon, Asia-Pacific), the immediate need is advocacy to formalize fragmented implementations into unified tre],
)


=== DAO-governed open innovation platform for TLM documentation and training data

_Composite: 16_ | Group: Decentralized & Democratic Institutions | TRL: 3 | v2 consensus: No

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[4/5],
  table.cell[DAO-based governance with smart-contract voting gives communities 'formal decision-making power over how TLM training data is collected, labeled, and updated.' Open innovation platforms enable comm...],
  table.cell[d/acc: Decentralized],
  table.cell[4/5],
  table.cell[DAO structure eliminates single proprietary entity control; 'prevents proprietary capture of the models' through distributed governance. Smart-contract enforcement is inherently decentralized. Howe...],
  table.cell[d/acc: Defensive],
  table.cell[3/5],
  table.cell[The mechanism is primarily defensive: it protects against proprietary capture, prevents bias through community oversight, and enforces transparency via open-source requirements. However, it is not ...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[The entity accelerates defensive capabilities (transparency, distributed control, bias detection) but does not explicitly accelerate defensive tech faster than offensive tech. Research data shows n...],
  table.cell[_d/acc Total_],
  table.cell[_13/20_],
  table.cell[],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[This entity transforms a field (translation model development and AI governance). It shifts the paradigm from proprietary, centralized model development to community-governed, open-source alternatives],
  table.cell[Bottleneck],
  table.cell[Coordination],
  table.cell[N/A],
  table.cell[Action],
  table.cell[Convene],
  table.cell[N/A],
)


=== Watershed Parliaments

_Composite: 16_ | Group: Decentralized & Democratic Institutions | TRL: 4 | v2 consensus: No

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[4/5],
  table.cell[Mechanism explicitly includes 'designated representatives for ecosystem interests alongside human citizens' and 'multi-stakeholder participation' in existing implementations (MDBA, SRBC, ICPRB). Ho...],
  table.cell[d/acc: Decentralized],
  table.cell[3/5],
  table.cell[Watershed-based organization reduces dependence on nation-state political boundaries as single points of control. Research data shows 'fragmented form through river basin organizations' that 'coord...],
  table.cell[d/acc: Defensive],
  table.cell[4/5],
  table.cell[The mechanism is explicitly defensive: 'Proposals must pass multi-generational impact assessments covering all species within the watershed before adoption' and decisions must 'demonstrate positive...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[No evidence in provided materials regarding acceleration of defensive versus offensive technologies. The mechanism focuses on governance structure and decision-making processes rather than technolo...],
  table.cell[_d/acc Total_],
  table.cell[_13/20_],
  table.cell[],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[Watershed Parliaments would transform the field of governance and environmental management by fundamentally reorganizing political jurisdiction around ecological rather than geopolitical boundaries. T],
  table.cell[Bottleneck],
  table.cell[Regulation],
  table.cell[N/A],
  table.cell[Action],
  table.cell[Advocate],
  table.cell[N/A],
)


=== Digital Twins for Communities and Ecosystems

_Composite: 16_ | Group: AI-Mediated Deliberation & Collective Intelligence | TRL: 5 | v2 consensus: Yes

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[4/5],
  table.cell[Mechanism explicitly enables 'participatory future simulation' and 'participatory governance bodies including representatives for non-human entities.' Citizens retain decision-making power through ...],
  table.cell[d/acc: Decentralized],
  table.cell[3/5],
  table.cell[Communities and citizens 'retain ownership of their data' and hold 'digital sovereignty' rather than ceding to centralized platforms. However, sensor networks and models still require coordination ...],
  table.cell[d/acc: Defensive],
  table.cell[4/5],
  table.cell[Mechanism is fundamentally defensive: enables simulation of consequences before implementation, protects community data ownership against centralized platform capture, and supports informed governa...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[No evidence in source material that this accelerates defensive technology faster than offensive technology. Digital twin technology is dual-use (Singapore's system used for 'disaster management' bu...],
  table.cell[_d/acc Total_],
  table.cell[_13/20_],
  table.cell[Strong on democratic and defensive dimensions, moderate on decentralization, weak on differential advantage.],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[Transforms a field (environmental governance and urban planning). Digital twins with genuine participatory governance and community data ownership would fundamentally reshape how communities make deci],
  table.cell[Bottleneck],
  table.cell[Coordination],
  table.cell[Research data identifies multiple barriers but coordination emerges as primary: 'integration at scale remains in prototype/pilot phase,' 'combining community data ownership with real-time sensor netwo],
  table.cell[Action],
  table.cell[Convene],
  table.cell[Given mature component technologies (digital twins operational, data sovereignty frameworks exist) and identified coordination barriers, immediate action should be convening stakeholders across techno],
)


=== Loyal AI Assistance (Fiduciary AI Assistance)

_Composite: 15_ | Group: AI Safety, Alignment & Governance | TRL: 3 | v2 consensus: Yes

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[4/5],
  table.cell[System explicitly designed to 'remain in control' with user maintaining decision-making authority. Contrasts with current assistants that prioritize platform interests over user goals. Fiduciary du...],
  table.cell[d/acc: Decentralized],
  table.cell[2/5],
  table.cell[While individual users gain control over their personal AI system, the research data does not describe distributed architecture or reduced single points of failure. Each user would have their own l...],
  table.cell[d/acc: Defensive],
  table.cell[4/5],
  table.cell[System is explicitly defensive in posture: designed to protect user interests against manipulation, data monetization, and advertiser influence. Mechanism emphasizes 'no selfish or third-party inte...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[While fiduciary AI is defensive in nature, research data provides no evidence that it accelerates defensive capabilities faster than offensive ones. The technology remains conceptual; no comparativ...],
  table.cell[_d/acc Total_],
  table.cell[_12/20_],
  table.cell[Strong on democratic control and defensive posture; weaker on decentralization and differential acceleration.],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[Transforms the field of AI assistance design by reorienting incentive structures from platform/advertiser interests to user interests. Establishes new legal and design frameworks (fiduciary duty) appl],
  table.cell[Bottleneck],
  table.cell[Regulation],
  table.cell[Research data explicitly identifies 'regulatory and legal uncertainty' as primary barrier: 'fiduciary frameworks remain underdeveloped for AI, with no clear enforcement mechanisms or standards for com],
  table.cell[Action],
  table.cell[Advocate],
  table.cell[TRL 3 status indicates research phase is mature (published frameworks, design methodologies, institutional research). Funding exists through research institutions. Primary need is regulatory pathway d],
)


=== The Global Deliberation Coordinator

_Composite: 15_ | Group: AI-Mediated Deliberation & Collective Intelligence | TRL: 4 | v2 consensus: Yes

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[4/5],
  table.cell[Platform explicitly designed to 'convene global stakeholders for deliberative discussions' and coordinate 'collective decision-making across national and organizational boundaries.' UN Global Dialo...],
  table.cell[d/acc: Decentralized],
  table.cell[2/5],
  table.cell[Proposed as a 'platform institution' and 'coordination infrastructure,' which implies centralized convening function. Research shows existing implementations (AI4Deliberation, Global Dialogue) oper...],
  table.cell[d/acc: Defensive],
  table.cell[4/5],
  table.cell[Mechanism focuses on deliberative processes for collective decision-making on AI governance—inherently defensive in posture (governance, coordination, alignment rather than capability acceleration)...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[Deliberation coordination accelerates defensive governance capacity (policy alignment, stakeholder consensus). However, research data provides no evidence this specifically accelerates defensive te...],
  table.cell[_d/acc Total_],
  table.cell[_12/20_],
  table.cell[],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[Transforms the field of AI governance by shifting from fragmented national/regional approaches to coordinated global deliberative infrastructure. Research demonstrates this addresses a critical gap: c],
  table.cell[Bottleneck],
  table.cell[Coordination],
  table.cell[Research explicitly identifies 'representation and coordination gaps: 118 countries (mainly Global South) remain excluded from major AI governance initiatives, and hundreds of incompatible governance],
  table.cell[Action],
  table.cell[Convene],
  table.cell[Given TRL 4 status with multiple pilot projects proven viable, and coordination as primary bottleneck, immediate action should focus on convening stakeholders to design unified coordination architectu],
)


=== Epistemic stack

_Composite: 14_ | Group: Scientific Research & Knowledge Infrastructure | TRL: 4 | v2 consensus: Yes

#table(columns: (auto, auto, auto),
  stroke: 0.5pt + luma(180),
  inset: 6pt,
  table.cell[*Dimension*],
  table.cell[*Score*],
  table.cell[*Evidence*],
  table.cell[d/acc: Democratic],
  table.cell[3/5],
  table.cell[Community Notes demonstrates crowdsourced fact-checking with 133,000+ contributors, distributing verification power. However, only 11% of submitted notes reach 'helpful' status, indicating gatekeep...],
  table.cell[d/acc: Decentralized],
  table.cell[2/5],
  table.cell[C2PA and blockchain-based systems (Numbers Protocol/Capture) add cryptographic and immutability layers, reducing single points of failure for provenance records. However, research data explicitly n...],
  table.cell[d/acc: Defensive],
  table.cell[4/5],
  table.cell[The epistemic stack is fundamentally defensive: it aims to protect users from misinformation by enabling verification and trust assessment rather than generating false claims. The mechanism traces ...],
  table.cell[d/acc: Differential],
  table.cell[2/5],
  table.cell[The system could theoretically accelerate defensive capabilities (verification, trust assessment) relative to offensive ones (disinformation creation). However, research data provides no evidence t...],
  table.cell[_d/acc Total_],
  table.cell[_11/20_],
  table.cell[],
  table.cell[Transformative],
  table.cell[3/5],
  table.cell[The epistemic stack would transform the information verification field by creating a unified, traceable provenance system from raw data through inference to published claims. Research data shows 'no u],
  table.cell[Bottleneck],
  table.cell[Coordination],
  table.cell[N/A],
  table.cell[Action],
  table.cell[Convene],
  table.cell[N/A],
)

