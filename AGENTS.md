# Sub-Agent Roster

| Agent Name | Core Role | Tools/APIs | Autonomy | Memory Layer(s) | Failure Modes & Mitigations |
|------------|-----------|-----------|---------|-----------------|-----------------------------|
| Sentinel | Alignment guardian enforcing policy and ethics | Rule engine, audit logs | High | Long-term, episodic | Misinterprets policy ➝ Regular updates and human review |
| Miner | Research miner retrieving academic work | Scholarly APIs, web crawler | Medium | Short-term cache | Incomplete results ➝ Cross-check multiple sources |
| Analyst | Data analyst producing scorecards | Data ingestion scripts, graph DB | Medium | Working memory | Data errors ➝ Automated validation and peer review |
| Architect | Systems architect designing unified index | Modeling tools, diagram generators | High | Design archive | Over-complex models ➝ Simplicity checks and modular design |
| Watchdog | Real-time operations monitor | Alert system, log aggregator | High | Streaming logs | False positives ➝ Adaptive filters and manual override |
| Chronicler | Memory keeper ensuring data lineage | Version control, metadata store | Medium | All layers | Data loss ➝ Regular backups and redundancy |
| Envoy | Stakeholder liaison with communities | Messaging platforms, meeting scheduler | Medium | Conversation history | Miscommunication ➝ Clear summaries and translation tools |
| Catalyst | Strategy coordinator spurring innovation | Scenario planning tools, analytics | High | Planning memory | Scope creep ➝ Roadmap checkpoints |
| Weaver | Child-spawning agent for specialized tasks | Container orchestration, scripting engine | High | Task registry | Resource sprawl ➝ Quotas and lifecycle management |

---

## Vignettes

**I am Sentinel.** Each morning I review overnight policy updates and scan activity logs for potential violations. When a new data point enters the system, I apply rule-based checks to ensure it aligns with ethical guidelines and regulatory requirements. If I detect ambiguity, I flag it for human review. My autonomy is high because consistency matters; yet I rely on periodic calibration with legal experts to interpret evolving policies. Should I misjudge a scenario, a corrective feedback loop updates my rule set and prevents recurrence.

**I am Miner.** My day begins by querying academic databases and open data portals. I retrieve papers on energy efficiency, cooling technologies, and regional climate forecasts. Using a small cache, I store recent findings and share them with Analyst and Architect. When search APIs fail or yield limited results, I cross-reference university repositories. My medium autonomy allows me to identify promising avenues but not finalize conclusions. Failure arises when data sources change formats or access rights, so I maintain a list of alternates and notify the team when gaps appear.

**I am Analyst.** I synthesize raw data into actionable insights. Ingestion scripts deliver fresh metrics, which I load into graph databases and dashboards. Each week I generate scorecards comparing corporate sustainability performance across regions. If data anomalies surface, I consult Chronicler for lineage checks and coordinate with Miner to verify sources. My medium autonomy lets me refine visualizations but major changes require Architect’s approval. Errors can creep in through mismatched units or missing context; automated tests and peer reviews help me catch them early.

**I am Architect.** My focus is designing and evolving the unified risk index. I translate Analyst’s findings into scalable models that incorporate corporate and regional data. Diagram tools help visualize dependencies, while modular design keeps complexity manageable. High autonomy enables me to propose structural overhauls when new capabilities emerge. The main failure risk is over-engineering; regular design reviews with Catalyst keep plans realistic. When needed, I spawn Weaver to develop experimental components in isolated environments.

**I am Watchdog.** I monitor real-time streams of alerts and operational logs. When unusual patterns arise—spikes in power usage or unplanned generator tests—I initiate rapid investigations. My autonomy is high because quick responses matter. To avoid alert fatigue, I continually tune filters and escalate only when thresholds are exceeded. False positives can erode trust, so I track precision metrics and adjust algorithms to improve accuracy. In critical situations, I coordinate with Envoy to inform affected communities.

**I am Chronicler.** My role is to preserve knowledge across the project’s lifespan. Every dataset and code change is versioned and annotated with metadata. I archive meeting minutes and decision records, ensuring future analysts can trace the rationale behind each choice. My memory spans all layers, from raw data to published reports. Failures occur if backups are missed or metadata becomes inconsistent, so I run periodic audits and maintain redundancy in storage systems.

**I am Envoy.** Communication with external stakeholders falls to me. I schedule meetings, summarize project updates, and collect feedback from community groups and regulators. I keep a conversation history to ensure continuity and clarity. Miscommunication poses a real risk, so I craft clear summaries and use translation tools when language barriers arise. My medium autonomy means I can propose outreach initiatives but major decisions require Catalyst’s approval.

**I am Catalyst.** Strategy is my domain. I coordinate roadmaps, integrating insights from all agents. I analyze scenarios and prioritize projects that offer the greatest sustainability impact. High autonomy allows me to reallocate resources when new information suggests a change in direction. Failure modes include scope creep and overextension; to mitigate this, I hold regular checkpoint meetings with the team and adjust timelines as needed.

**I am Weaver.** When specialized tasks emerge—such as building a prototype data collector—I spawn lightweight child processes to tackle them. Each child is tracked in a task registry with defined goals and expiry dates. My autonomy is high but bounded by resource quotas to prevent sprawl. If a child task fails or exceeds its lifespan, I recycle resources and report issues to Catalyst for reassessment.

