## The 39 Entities

The following chapters present the 39 consensus entities in nine thematic groups. 15 receive full write-ups; the remaining 24 are in summary format. One pair (Reputational Markets and Prediction Markets as Decision Support Systems) is presented as a single merged entry.

### AI & Human Agency

These entities bet that beneficial AI might come from systems designed for individual people rather than populations. Instead of chatbots serving millions identically, they envision AI with long-term commitments to specific users: filtering information, coaching decisions, or holding legal obligations to act in one person's interest. The underlying logic is that alignment becomes easier when an AI system has a clear principal and a sustained relationship, rather than optimizing for humanity in the abstract.



### Fiduciary AI Assistance
`Foundational Research` | *d/acc: 80% | Tech: N/A*

**Significance.** Today's leading AI assistants are optimized for platform goals, not user welfare. Fiduciary AI inverts this: a digital agent legally and technically bound to a single user's welfare, assisting with career, health, and financial decisions with guaranteed loyalty. Where EgoLets (below) focus on cognitive modeling, fiduciary AI addresses the obligation structure, ensuring an AI system cannot work against its principal. As AI grows more capable, the question of whose interests it serves becomes critical. Individuals with aligned AI advocates could access expert judgment now reserved for the wealthy, rebalancing power away from platforms that profit from attention manipulation.

**Current state.** The concept has intellectual traction: [Metaculus](https://metaculus.com) founder Anthony Aguirre has championed "loyal AI assistance" as a north star. Current implementations remain primitive. The closest approximations are robo-advisors like [Betterment](https://www.betterment.com) and [Wealthfront](https://www.wealthfront.com), which operate under financial fiduciary standards but handle only narrow investment tasks. [Inflection AI](https://inflection.ai)'s Pi attempted user-first design through subscription models but was effectively acquired by Microsoft in 2024 before proving viability. On the technical side, [Hugging Face](https://huggingface.co) supports on-device AI deployment for privacy, and Constitutional AI research explores encoding user values, but no system today mathematically guarantees individual welfare as its optimization target. No jurisdiction has defined fiduciary duty for software. AI safety researchers at [Center for AI Safety](https://www.safe.ai) and [Open Philanthropy](https://www.openphilanthropy.org) have explored related alignment questions under "tool AI" frameworks. The [EU AI Act](https://artificialintelligenceact.eu/) (2024) introduces user-protection requirements, though nothing approaching fiduciary duty. [Character.AI](https://character.ai) and [Replika](https://replika.com) build persistent personal AI relationships but without loyalty guarantees.

**Open questions.** The business model is unsolved: fiduciary AI cannot manipulate users or harvest data, but subscription revenue has not proven sufficient at scale. There are no established methods to encode "long-term user welfare" when users themselves are inconsistent. The paternalism dilemma (should an AI enforce a diet or defer to immediate preferences?) lacks a solution. It remains unclear what it means for software to breach fiduciary duty, or who enforces it. Until someone demonstrates a profitable path to individual-first AI, platforms have every incentive to maintain the status quo.



### EgoLets (Personal AI Assistants)
`Early Demonstrations` | *d/acc: 75% | Tech: 69%*

**Significance.** Today's AI assistants provide the same generic advice to everyone. EgoLets are personalized AI systems that learn how a specific person thinks, decides, and weighs tradeoffs, creating what author Ken Liu calls "little versions of your ego" trained on personal data. Where Fiduciary AI addresses loyalty, EgoLets address fidelity: whether an AI can replicate how a specific person actually reasons. Individuals would gain cognitive partners that mirror their reasoning across professional, creative, and financial domains. This shifts AI from automation tool to personalized augmentation, democratizing bespoke decision support currently available only through expensive human advisors.

**Current state.** Current personal AI assistants like [OpenAI](https://openai.com)'s ChatGPT (with memory features launched 2024), [Anthropic](https://anthropic.com)'s Claude, and Google's Gemini learn user preferences through conversation history. Startups like [Inflection AI](https://inflection.ai), [Replika](https://replika.com), and [Character.AI](https://character.ai) explore personality modeling and emotional rapport. Apple Intelligence (2024) integrates on-device personal context. But none construct cognitive portraits that mirror individual reasoning architectures; they personalize outputs, not decision-making frameworks. The gap between "remembers what you said" and "thinks like you think" remains vast. Technical building blocks are advancing separately: [OpenMined](https://openmined.org) develops privacy-preserving ML for training on personal data without centralized exposure. Microsoft's Copilot and [GitHub Copilot](https://github.com/features/copilot) demonstrate domain-specific assistance that learns individual patterns. Research from the [Allen Institute for AI](https://allenai.org) explores knowledge graph construction. No major organization is explicitly building toward EgoLets as Liu envisioned; the concept exists more as design challenge than funded roadmap.

**Open questions.** There are no established methods to evaluate "cognitive fidelity": how to measure whether an AI's decisions match what a person would actually choose. Human reasoning is contextual, contradictory, and evolving; any static portrait becomes stale. Identity and liability questions are unresolved: who is responsible when an AI acts as a cognitive proxy? Data portability standards do not exist to aggregate decision history across platforms, so the raw material EgoLets need remains siloed across incompatible services.



#### Additional Entities

**Empathetic Neuro-AI Emotional Coaching System**
`Early Demonstrations` | *d/acc: 65% | Tech: 69%*
An AI system providing continuous, personalized emotional support by analyzing neural signals and behavioral patterns to detect and intervene before mental health crises occur. Mental health care demand vastly outstrips supply (average therapy wait times stretch weeks to months), and emotional crises do not follow business hours. This system addresses the mismatch between constant psychological needs and limited therapist availability.

**Lifelong AI Guardians**
`Early Demonstrations` | *d/acc: 65% | Tech: 70%*
Continuous, privacy-preserving monitoring systems that track children's development across fragmented settings (schools, homes, healthcare visits), detecting early warning signs that currently fall through institutional gaps. The aim is to shift child welfare from reactive crisis response to proactive support by building longitudinal profiles that spot developmental deviations before they become serious.
