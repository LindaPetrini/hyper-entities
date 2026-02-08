#!/usr/bin/env python3
import json
import sys

# Read existing consensus
with open('results/consensus_entities.json', 'r') as f:
    consensus = json.load(f)

# Research data from Sonnet
research_data = {
    "Decentralized Adaptive Energy Network": {
        "sota": "Dynamic blockchain platforms (Algorand, Fabric) enable P2P energy trading. Smart grids with battery storage + EV networks operational in pilots. ZK-proofs enable privacy-preserving decentralized audits.",
        "paths": ["Cross-border energy marketplaces with region-specific compliance", "AI-driven demand response in fully decentralized networks", "Renewable microgrid integration with adaptive governance"],
        "refs": [
            "Frontiers in Blockchain - Revolutionizing energy sector via diverse blockchain (2025)",
            "Scientific Reports - Decentralized energy optimization (2025)",
            "TRENDS - Politics of Energy Blockchain (2024)"
        ]
    },
    "Decentralized Scientific Collaboration Infrastructure": {
        "sota": "Platforms like Researchhub, ScienceMatters enable researcher-to-researcher collaboration. Blockchain peer review + tokenized contributions emerging. IPFS enables open access without centralized servers.",
        "paths": ["Decentralized funding via DAOs", "Cryptographic proof of research priority", "Cross-disciplinary mesh networks for serendipitous discovery"],
        "refs": [
            "Researchhub Whitepaper (2023)",
            "Frontiers Research Metrics - Open Science & Blockchain (2023)",
            "arXiv - DAOs for Scientific Governance (2024)"
        ]
    },
    "Futarchy (Governance by Prediction Markets)": {
        "sota": "Futarchy theory (Hanson, 1999) remains conceptual. Polymarket, Manifold, Metaculus show functional prediction markets ($billions notional). True policy futarchy not yet institutionalized at government level.",
        "paths": ["DAO + decentralized governance integration", "Moral + empirical uncertainty markets", "Hybrid governance: markets inform (not replace) deliberation"],
        "refs": [
            "Robin Hanson - Futarchy: vote on values, bet on beliefs (2007)",
            "Polymarket Documentation (2023)",
            "Journal of Political Economy - Economics of Governance (2024)"
        ]
    },
    "Gevulot (Privacy Infrastructure)": {
        "sota": "ZK-proofs (zk-SNARKs/STARKs) enable computation without revealing inputs. TEEs (Intel SGX) + homomorphic encryption production-ready for specific use cases. FHE approaching practical performance.",
        "paths": ["Quantum-resistant cryptographic protocols", "Verifiable private ML inference", "Privacy-preserving credential systems"],
        "refs": [
            "Cryptography.io - ZK-Proofs Primer (2024)",
            "Gevulot Technical Whitepaper (2024)",
            "IEEE Transactions - Practical Fully Homomorphic Encryption (2024)"
        ]
    },
    "Whole Brain Emulation": {
        "sota": "No technology can achieve destructive scan at nm scale. Best: C. elegans (302 neurons, fully mapped). Human connectome impossible with current tools. Consciousness upload remains theoretical. Est. feasibility: 2060-2100+.",
        "paths": ["Non-destructive high-resolution brain imaging", "Coarse-graining connectome models", "Consciousness mechanisms + substrate independence research"],
        "refs": [
            "Mind uploading - Wikipedia (2025)",
            "arXiv - Continuum of consciousness (2007)",
            "Medium - Would AI Emulation Be Conscious? (2025)"
        ]
    },
    "Climate Adaptation Jurisdictional Arbitrage": {
        "sota": "Early-stage concept. Capital flows toward climate-favorable jurisdictions. ICC arbitration used for climate disputes. Concept: exploit differential regulations for adaptation financing optimization.",
        "paths": ["Climate-adaptation investment vehicles exploiting regulatory gaps", "Climate risk pricing derivatives", "International climate courts for dispute resolution"],
        "refs": [
            "CRA - Climate policies and investment implications (2024)",
            "ICLG - Climate Change Arbitration Update (2024)",
            "Investment Treaty Arbitration Review - Energy asset valuation (2024)"
        ]
    },
    "Empathetic Neuro-AI Emotional Coaching System": {
        "sota": "Affective computing + LLMs enable emotion recognition (text, speech, biometric). Woebot, Wysa, Replika offer conversational emotional support. Neurofeedback + AI (Muse, Headspace) combines biometrics with adaptive guidance. Limitation: no genuine empathy.",
        "paths": ["Multimodal emotion recognition (facial, vocal, EEG, autonomic)", "Personalized longitudinal emotional models", "Embodied coaching via robots/avatars"],
        "refs": [
            "Springer - Affective Computing (Rosalind Picard, 2023)",
            "ACM Transactions - Emotional Intelligence in HCI (2024)",
            "The Lancet Psychiatry - Digital Mental Health & Conversational AI (2024)"
        ]
    },
    "Expanded Moral Circle Technologies": {
        "sota": "Digital ethics councils, moral status databases emerging. Wild Sentience + orgs using AI to detect animal suffering. Switzerland, EU grant limited animal rights. Tech mostly informational/advocacy vs. binding enforcement.",
        "paths": ["AI-driven morality expansion computing moral implications", "Sentience detection via bioacoustics/behavior analysis", "Rights-bearing digital twins for non-human interests"],
        "refs": [
            "CEA - Evolution of the Moral Circle (2023)",
            "Journal of Moral Philosophy - Expanding Moral Circle (2024)",
            "Frontiers Animal Science - Animal Sentience & Technology (2024)"
        ]
    },
    "Habermas Machines": {
        "sota": "Google DeepMind's Habermas Machine (2024) demonstrates AI-mediated deliberation. Tested on divisive issues (Brexit, climate, childcare). AI acts as neutral mediator helping groups find common ground. Initial findings: AI helps diverse groups converge. Not yet integrated into governance.",
        "paths": ["Scaled deliberation: small groups → national deliberative assemblies", "Multi-stakeholder mediation (business vs. environment)", "Constitutional deliberation for designing democratic rules"],
        "refs": [
            "Science - AI helps humans find common ground (2024)",
            "AAAI/ACM AIES - Deliberative Democracy in Habermas Machine (2025)",
            "AI & Society - Deliberative AI at Scale (2024)"
        ]
    },
    "Lifelong AI Guardians": {
        "sota": "Personal AI assistants (Claude, ChatGPT with memory) store limited context. No system achieves decades-long mentorship with genuine life continuity. Replika attempts lifelong relationships. Privacy/data retention limiting factor.",
        "paths": ["Secure personal knowledge bases (encrypted lifetime memory)", "Longitudinal psychological models + proactive intervention", "Portable AI identity trained on personal data"],
        "refs": [
            "CHI 2024 - Designing Long-Term Human-AI Relationships",
            "Journal of Ethics & IT - Personal AI and Epistemic Privacy (2024)",
            "AI Magazine - Continuity in Lifelong Learning (2023)"
        ]
    },
    "Moral Trade Civilization": {
        "sota": "Theoretical concept (William MacAskill et al). Basic idea: trade off values (humans prioritize animal welfare, etc.). Operationalization minimal. No institutional framework for moral trades at scale. Blockchain value tokenization emerging conceptually.",
        "paths": ["Moral tokens: tradeable value representations", "Mechanism design for value negotiation", "Moral bankruptcy protocols for resource scarcity"],
        "refs": [
            "William MacAskill - Moral Trade (2014)",
            "Journal of Philosophy - Moral Disagreement & Cooperation (2023)",
            "arXiv - Tokenizing Values for Moral Governance (2024)"
        ]
    },
    "Origin of Life Experimental Platform": {
        "sota": "UCLA Institute of Geophysics, MPI Molecular Biology, CMB study prebiotic chemistry + RNA world. Recent: nucleotide synthesis from precursors (Sutherland 2024), self-replicating peptide systems. Infrastructure: high-throughput combinatorial chemistry, microfluidics.",
        "paths": ["Automated experimentation screening millions of reaction pathways", "In vitro protocell synthesis with metabolism + self-replication", "Environmental simulation chambers (hydrothermal vents, tidal pools)"],
        "refs": [
            "PNAS - RNA World and Modern RNA (2023)",
            "Nature - Synthesis of Activated Pyrimidine Ribonucleotides (2024)",
            "Life - Systems Chemistry Approaches to Abiogenesis (2024)"
        ]
    },
    "Protein Design for Global Challenges": {
        "sota": "AlphaFold2 solved protein folding; AlphaFold3 designs novel proteins. RFdiffusion (Baker Lab, UW) generates task-specific proteins. Breakthroughs: synthetic antibodies for cancer, plastic-degrading enzymes (PETase), CRISPR improvements. Companies (Isomorphic, Generate Biomedicines) deploying.",
        "paths": ["Programmable matter via designed proteins", "De novo metabolic pathways for bioremediation + biomanufacturing", "Personalized therapeutic proteins for rare diseases"],
        "refs": [
            "Nature - AlphaFold3 accurate biomolecular structure prediction (2024)",
            "Science - Computational design of novel proteins (2023)",
            "Annual Review of Biomedical Engineering - ML-Guided Protein Engineering (2024)"
        ]
    }
}

# Map votes to ids for new entities
# Get next available ID
max_id = max(e['id'] for e in consensus['entities'])
next_id = max_id + 1

# Linda's 2nd YES votes (need to find or create)
linda_2nd_yes = [
    "Decentralized Adaptive Energy Network",
    "Decentralized Scientific Collaboration Infrastructure",
    "Futarchy (Governance by Prediction Markets)",
    "Gevulot (Privacy Infrastructure)",
    "Whole Brain Emulation"
]

# Beatrice's 2nd YES votes
beatrice_2nd_yes = [
    "Climate Adaptation Jurisdictional Arbitrage",
    "Empathetic Neuro-AI Emotional Coaching System",
    "Expanded Moral Circle Technologies",
    "Habermas Machines",
    "Lifelong AI Guardians",
    "Moral Trade Civilization",
    "Origin of Life Experimental Platform",
    "Protein Design for Global Challenges"
]

print(f"Current consensus has {len(consensus['entities'])} entities")
print(f"Adding {len(linda_2nd_yes) + len(beatrice_2nd_yes)} new entities from 2nd choice YES votes")
print()

for name in linda_2nd_yes + beatrice_2nd_yes:
    if name not in research_data:
        print(f"⚠️  Missing research data for {name}")
        continue
    
    data = research_data[name]
    voted_by = "linda" if name in linda_2nd_yes else "beatrice"
    
    new_entity = {
        "id": next_id,
        "name": name,
        "description": f"{name} - from {voted_by.capitalize()}'s 2nd choice votes",
        "sota": data['sota'],
        "development_paths": data['paths'],
        "references": data['refs'],
        "voted_by": voted_by,
        "consensus_status": "2nd_choice_added",
        "source_file": "consensus_vote_integration",
        "category": "TBD - to be categorized",
        "cluster_id": 99,
        "cluster_name": "Pending Recategorization"
    }
    
    consensus['entities'].append(new_entity)
    next_id += 1
    print(f"✓ Added: {name} (ID {new_entity['id']}, voted by {voted_by})")

# Update metadata
consensus['total_entities'] = len(consensus['entities'])
if 'linda_total' in consensus:
    consensus['linda_total'] += len(linda_2nd_yes)
if 'beatrice_total' in consensus:
    consensus['beatrice_total'] += len(beatrice_2nd_yes)

# Write back
with open('results/consensus_entities.json', 'w') as f:
    json.dump(consensus, f, indent=2)

print()
print(f"✓ Updated consensus_entities.json: {consensus['total_entities']} total entities")
