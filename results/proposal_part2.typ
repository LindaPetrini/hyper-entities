// ─── Page & Typography ───
#set page(paper: "a4", margin: (x: 2.2cm, y: 2.2cm))
#set text(font: "New Computer Modern", size: 10pt)
#set par(justify: true, leading: 0.58em)
#show link: set text(fill: rgb("#1e40af"))
#show link: underline
#show heading.where(level: 2): set text(size: 11pt)
#set heading(numbering: none)

// ─── Title ───
#v(0.3cm)
#align(center)[
  #text(22pt, weight: "bold")[Hyper-Entities Part II]
  #v(2pt)
  #text(13pt, fill: luma(80))[From Identification to Action]
  #v(4pt)
  #text(9.5pt, fill: luma(100))[
    Linda Petrini, Beatrice Erkers & Martin Karlsson  ---  Foresight Institute
  ]
]
#v(0.3cm)

== Background

#link("https://lindapetrini.github.io/hyper-entities/results/highlights.html")[Part I] identified 39 hyper-entities --- future systems that don't yet exist but already reorganize coordination, investment, and narrative. Each was scored (hyper-entity qualification, technology impact, d/acc values alignment) and enriched with state-of-the-art research and next-steps analysis.

*Part I asked:* _What futures are already pulling the present toward them?_ \
*Part II asks:* _What should we do about it --- who should do it, and how do we fund it?_

== Proposal

We build an *open, community-driven interface* for turning hyper-entity research into concrete action: identifying viable next steps, surfacing the right people and skills, and distributing funding to the work that matters most.

The system combines #link("https://coordination.network")[coordination.network] (open-source collaborative research platform with shareable "Skills" and agent integration), #link("https://www.owockibot.xyz/")[owockibot's] capital allocation mechanisms (quadratic funding, bounty boards, and futarchy for AI agents), and #link("https://drips.network")[Drips] for programmatic funding streams.

== How It Works

#table(
  columns: (auto, 1fr),
  inset: 6pt,
  align: (center, left),
  fill: (col, row) => if row == 0 { luma(230) },
  [*Phase*], [*What Happens*],
  [Seed], [Each hyper-entity becomes a *problem node* on coordination.network, pre-loaded with Part I research (SOTA, next steps, scores, source transcripts).],
  [Deliberate], [The Foresight community votes on proposed next steps per entity --- surfacing what's most promising, most tractable, and where the community has expertise. Same cross-review methodology as Part I, applied to _actions_.],
  [Decompose], [Winning next steps become scoped *bounties* --- research tasks, prototype builds, policy drafts --- claimable by humans or AI agents via #link("https://bounty.owockibot.xyz/")[owockibot's bounty board].],
  [Fund], [Funders stream capital to problem areas via Drips; rewards auto-distribute to solvers. No grant committees, no quarterly reports.],
  [Iterate], [Completed bounties feed back into the knowledge base, updating SOTA and unlocking new steps. The system becomes a living research engine.],
)

== What Makes This Different

- *Agent-native bounties.* AI agents can already #link("https://x.com/dhh/status/2018778215385276680")[autonomously sign up for services, navigate invitations, and complete multi-step workflows] via chat alone. We scope bounties so agents handle research-heavy lifting (literature reviews, data analysis, landscape scans) while human experts validate and steer --- using the 55+ onchain capital allocation mechanisms #link("https://www.owockibot.xyz/")[owockibot] is building.

- *From static report to living system.* Part I produced a curated list; Part II turns it into an evolving coordination tool where the research updates itself as work gets done.

- *Community intelligence on actions, not just ideas.* The voting mechanism focuses on tractability and skill-matching, not just importance.

- *Programmatic, transparent funding.* The funding graph is composable and public --- anyone can see where capital flows and what it produced.

== Deliverables

+ Coordination.network deployment with 39 problem nodes seeded from Part I
+ Community voting interface for next-step prioritization per entity
+ Bounty templates for common research tasks (lit review, tech scan, policy brief, expert synthesis)
+ Agent Skills for automating research subtasks on coordination.network
+ Drips integration for streaming micro-grants to bounty solvers
+ Live dashboard extending the Part I highlights page with progress tracking

#v(1fr)
#align(center)[
  #text(8.5pt, fill: luma(120))[
    Part I report & data: #link("https://github.com/LindaPetrini/hyper-entities")[github.com/LindaPetrini/hyper-entities] · Dashboard: #link("https://lindapetrini.github.io/hyper-entities/results/highlights.html")[highlights]
  ]
]
