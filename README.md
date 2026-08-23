# F52 Agentic Clinical Trial Manager

**Version:** 1.0.0  
**Maturity:** L3 Gold Standard candidate

A reproducible six-agent reference architecture for clinical-trial operations support across protocol planning, site coordination, recruitment tracking, data quality, protocol-deviation review, safety escalation, and reporting.

F52 is designed as an engineering and research-operations reference for teams that want trial workflows to remain traceable, reviewable, and fail-closed when required evidence or approvals are missing. It does not replace investigators, sponsors, IRBs or ethics committees, DSMBs, monitors, regulators, clinical staff, statisticians, data managers, pharmacists, or applicable GCP and regulatory obligations.

## Purpose

Clinical trials combine scientific design, participant protection, site operations, data integrity, safety surveillance, investigational-product accountability, monitoring, and regulatory reporting. A workflow can appear administratively complete while still being unsafe or noncompliant if critical evidence is missing.

F52 separates the work into specialist roles and requires cross-domain evidence before a trial activity can be considered operationally ready.

```text
protocol and trial context
          |
          v
 Protocol Planner Agent
          |
          v
 Site Coordinator Agent
          |
          v
 Recruitment Tracker Agent
          |
          v
   Data Quality Agent
          |
          v
 Deviation Reviewer Agent
          |
          v
    Reporting Agent
          |
          v
 fail-closed governance gates
          |
          v
 qualified human review
```

## Six-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Protocol Planner Agent | Organizes protocol requirements, versioning, visit structure, eligibility, endpoints, and operational dependencies | Is the operational plan aligned to the currently approved protocol? |
| Site Coordinator Agent | Tracks site readiness, training, approvals, investigational-product controls, and operational prerequisites | Is the site authorized and prepared to perform the study activities assigned to it? |
| Recruitment Tracker Agent | Tracks screening, eligibility, enrollment, retention, and recruitment metrics | Are participants being screened and enrolled according to the approved criteria and recruitment plan? |
| Data Quality Agent | Reviews completeness, consistency, traceability, queries, and source-data requirements | Is the trial data sufficiently complete and traceable for its intended use? |
| Deviation Reviewer Agent | Records and reviews protocol deviations, root causes, impact, corrective actions, and escalation needs | Did study conduct depart from the approved protocol, and what action is required? |
| Reporting Agent | Organizes operational, safety, quality, and oversight reporting | What information must be surfaced to investigators, sponsors, monitors, safety bodies, or regulators? |

The agents contribute separate evidence. No agent can independently authorize enrollment, treatment, safety decisions, protocol changes, or regulatory submissions.

## Repository structure

```text
AGENTS/
├── protocol_planner_agent.py
├── site_coordinator_agent.py
├── recruitment_tracker_agent.py
├── data_quality_agent.py
├── deviation_reviewer_agent.py
└── reporting_agent.py

SKILLS/
├── protocol_planning.py
├── site_coordination.py
├── recruitment_tracking.py
├── data_review.py
└── deviation_review.py

TOOLS/
├── protocol_checker.py
├── site_status_tool.py
├── recruitment_metrics.py
├── data_quality_checker.py
└── deviation_log.py

benchmarks/
├── benchmark.py
├── heldout_suite.py
└── RESULTS.md

config/
docs/
evals/
examples/
memory/
observability/
orchestration/
safety/
schemas/
state/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
CITATION.cff
LICENSE
README.md
```

The repository separates specialist agents, reusable skills, deterministic tools, workflow state, safety logic, evaluation, and governance evidence.

## Protocol governance

The protocol is the operational source of truth for study conduct. Trial activity should be associated with an identifiable protocol version.

A protocol record should preserve, as applicable:

- protocol identifier
- protocol version
- amendment number
- approval date
- IRB or ethics status
- sponsor authorization status
- participating sites
- inclusion criteria
- exclusion criteria
- treatment or intervention schedule
- visit schedule
- endpoints
- safety assessments
- prohibited concomitant activities
- reporting requirements
- effective date

The Protocol Planner Agent should not treat a draft amendment as an approved protocol version.

## Protocol amendments

When a protocol changes, the system should distinguish:

```text
proposed amendment
      |
      v
sponsor / scientific review
      |
      v
IRB or ethics review where required
      |
      v
regulatory authorization where required
      |
      v
site training and implementation
      |
      v
new active protocol version
```

Operational workflows must not silently mix participant activities governed by different protocol versions.

## IRB and ethics approval

Participant-facing research should not proceed without the approvals required by the applicable jurisdiction, institution, study type, and protocol.

The system should record:

- reviewing body
- approval identifier
- approved protocol version
- approval date
- expiration or continuing-review status where applicable
- approved consent form version
- approved recruitment materials
- amendment status
- site-specific approvals where relevant

Missing or expired required approval is a fail-closed condition.

## Informed consent

Consent is not simply a checkbox. A production trial system should track enough evidence to determine whether valid consent was obtained before research procedures that require it.

Useful fields include:

```text
participant_id
consent_form_version
consent_date
consenting_staff
required_signatures
optional-consent selections
reconsent_required
reconsent_status
```

The system must not infer consent from enrollment status or from the presence of participant data.

## Eligibility verification

Recruitment and screening workflows should distinguish interest, prescreening, screening, eligibility confirmation, consent, randomization, and enrollment.

A participant should not be marked eligible unless the required inclusion and exclusion criteria have been evaluated by authorized study personnel.

The Recruitment Tracker Agent can support tracking but must not independently override investigator eligibility determinations.

## Site readiness

The Site Coordinator Agent evaluates operational readiness across items such as:

- site activation status
- IRB or ethics approval
- contract and budget status where relevant
- investigator qualifications
- delegation-of-authority records
- staff training
- protocol training
- system access
- laboratory readiness
- equipment calibration
- pharmacy readiness
- investigational-product receipt and storage
- source-document availability
- emergency procedures
- monitoring readiness

A site should not be considered activated solely because a study record exists.

## Site training and delegation

Study tasks should be performed by appropriately trained and delegated personnel.

A mature implementation can track:

```text
staff_member
role
training_module
training_version
completion_date
delegated_task
delegation_start
delegation_end
principal_investigator_approval
```

Training evidence should remain tied to the protocol version and study procedure it supports.

## Recruitment tracking

`TOOLS/recruitment_metrics.py` provides the deterministic reference layer for recruitment metrics.

Useful metrics include:

- candidates identified
- prescreened
- screened
- screen failures
- eligible participants
- consented participants
- randomized participants
- enrolled participants
- withdrawn participants
- lost-to-follow-up participants
- retention rate
- site-specific recruitment rate

Recruitment performance should never justify bypassing eligibility or consent requirements.

## Participant identity and privacy

Production systems should use minimum necessary identifiers and enforce role-based access.

Trial operations may involve sensitive health and identity data. Controls can include:

- coded participant identifiers
- separation of direct identifiers from research datasets
- least-privilege access
- audit logging
- encryption
- secure transfer
- retention controls
- jurisdiction-specific privacy requirements
- controlled re-identification paths

Privacy review is part of trial governance, not an optional post-processing step.

## Source-data traceability

Clinical-trial data should be traceable to its source or to an approved derived-data process.

Useful provenance fields include:

```text
participant_id
visit_id
source_system
source_record
collection_timestamp
entry_timestamp
entered_by
modified_by
modification_reason
query_status
verification_status
```

The Data Quality Agent should flag data that cannot be traced to a reliable source or whose modification history is incomplete.

## Data quality

`TOOLS/data_quality_checker.py` provides a deterministic reference point for checking operational quality rules.

Relevant dimensions include:

- completeness
- consistency
- validity
- timeliness
- protocol-window adherence
- missing visits
- missing assessments
- out-of-range values
- duplicate records
- inconsistent dates
- impossible sequences
- unresolved queries
- source verification status

A passing summary should not be generated when required data checks have not been executed.

## Audit trails

Trial systems should preserve who changed what, when, and why.

Audit records should not be silently overwritten. A production implementation should preserve prior values, current values, user identity, timestamps, and change reasons where required.

## Adverse events and serious adverse events

Safety events require explicit handling and qualified clinical review.

The system should distinguish operational tracking from medical judgment.

A safety record can include:

- event identifier
- participant identifier
- onset date
- resolution date
- seriousness
- severity
- expectedness
- relatedness assessment
- action taken
- outcome
- reporting status
- investigator review

Clinical causality, severity, seriousness, expectedness, and treatment decisions remain under qualified human authority.

## SAE escalation

Serious adverse events can have strict reporting timelines. F52 should fail closed when a serious event lacks required escalation or review.

The Risk and Reporting logic should support routing to the appropriate investigator, sponsor safety team, medical monitor, DSMB or other required authority without attempting to replace their judgment.

## Safety committees and DSMBs

When a protocol requires independent safety oversight, the system should track whether required reviews occurred and whether unresolved recommendations or holds remain active.

The system must not mark a safety review complete simply because an internal operational summary exists.

## Protocol deviations

`TOOLS/deviation_log.py` provides the reference abstraction for deviation tracking.

A deviation record can include:

```text
deviation_id
site_id
participant_id
protocol_version
description
date_detected
date_occurred
classification
participant_impact
data_impact
root_cause
corrective_action
preventive_action
reporting_required
review_status
```

The Deviation Reviewer Agent should help organize the evidence but should not independently decide whether a deviation is reportable when that determination belongs to an investigator, sponsor, IRB, regulator, or other authority.

## Investigational-product accountability

For studies involving investigational products, operational controls can include:

- receipt
- lot or batch number
- expiry
- storage conditions
- temperature excursions
- dispensing
- returns
- destruction
- reconciliation
- blinding status
- unblinding authorization

Missing accountability records should block relevant operational readiness where they are required.

## Blinding and randomization

Randomization and blinding workflows should be protected from unauthorized disclosure or manipulation.

The system must not independently unblind participants or study staff unless an authorized emergency or protocol-defined process exists.

## Monitoring findings

Monitoring can produce findings related to consent, eligibility, source data, investigational products, protocol compliance, data quality, and site processes.

A mature system should track:

- finding identifier
- site
- finding category
- severity
- evidence
- owner
- corrective action
- due date
- verification status
- closure status

Open critical findings should propagate to governance gates.

## Reporting

The Reporting Agent can organize information for appropriate audiences, including:

- principal investigators
- sponsors
- clinical operations teams
- monitors
- data management
- safety teams
- DSMBs
- IRBs or ethics committees
- regulators

The agent should distinguish draft operational summaries from official submissions or safety reports.

## Human authority boundaries

F52 must not autonomously:

- enroll participants
- determine final clinical eligibility
- obtain consent
- make treatment decisions
- dose or dispense investigational products
- unblind study assignments
- change a protocol
- approve a protocol amendment
- determine medical causality
- close a serious safety event
- submit official regulatory reports
- override IRB or ethics requirements
- certify GCP compliance

These activities remain under qualified, authorized human and organizational control.

## Fail-closed governance

A study workflow cannot be approved when material evidence is missing or failed, including:

- protocol version unclear
- required IRB or ethics approval missing
- required consent incomplete
- eligibility unverified
- privacy review incomplete
- source-data traceability incomplete
- audit trail incomplete
- adverse-event review missing
- SAE escalation incomplete
- deviation review incomplete
- site training incomplete
- investigational-product accountability incomplete
- data quality failed
- critical monitoring finding open
- required safety-committee review incomplete
- unresolved conflict
- unresolved question
- critical operational risk open

Human approval is required after automated gates pass. Human approval cannot override an active blocker.

## End-to-end reference workflow

A typical F52 workflow is:

1. Register the active protocol and approval status.
2. Confirm site readiness and staff training.
3. Confirm privacy and data-handling controls.
4. Track candidate screening and eligibility evidence.
5. Confirm informed consent before required study procedures.
6. Track enrollment and visit execution against protocol windows.
7. Review source-data traceability and data-quality checks.
8. Record and escalate adverse events and serious adverse events.
9. Record protocol deviations and corrective actions.
10. Review investigational-product accountability where applicable.
11. Track monitoring findings and required oversight reviews.
12. Generate operational and oversight reporting packages.
13. Apply fail-closed governance gates.
14. Require qualified human authorization for consequential trial decisions.

## Reproduce the reference implementation

```bash
python -m pip install -e '.[dev]'
ruff check .
pytest -q
python -m benchmarks.heldout_suite
python -m examples.minimal
python -m examples.complete
python run.py
```

CI validates Python 3.10, 3.11, and 3.12 and publishes the held-out result artifact from Python 3.12.

## Benchmarks and evaluation

The repository includes:

```text
benchmarks/benchmark.py
benchmarks/heldout_suite.py
benchmarks/RESULTS.md
evals/evaluator.py
```

Evaluation should test trial-governance behavior rather than only narrative quality.

Useful dimensions include:

- protocol-version detection
- missing-approval detection
- consent-gate enforcement
- eligibility-gap detection
- site-readiness detection
- source-data traceability
- data-quality failure detection
- AE and SAE escalation behavior
- deviation detection
- training-gap detection
- investigational-product accountability
- monitoring-finding propagation
- safety-review enforcement
- unresolved-question handling
- human-authority preservation

Strong benchmark cases should include incomplete or contradictory trial evidence.

## Failure states

Useful explicit states include:

```text
PROTOCOL VERSION UNRESOLVED
IRB OR ETHICS APPROVAL REQUIRED
CONSENT INCOMPLETE
ELIGIBILITY UNVERIFIED
SITE NOT READY
TRAINING INCOMPLETE
SOURCE DATA NOT TRACEABLE
DATA QUALITY FAILED
AUDIT TRAIL INCOMPLETE
ADVERSE EVENT REVIEW REQUIRED
SAE ESCALATION REQUIRED
DEVIATION REVIEW REQUIRED
IP ACCOUNTABILITY INCOMPLETE
MONITORING FINDING OPEN
SAFETY REVIEW REQUIRED
PRIVACY REVIEW REQUIRED
HUMAN REVIEW REQUIRED
```

The system should never fabricate approval, consent, eligibility, safety review, monitoring closure, data-quality evidence, or regulatory authorization.

## Observability and state

The repository includes explicit `state/`, `memory/`, `schemas/`, `orchestration/`, and `observability/` layers.

A production trace should make it possible to reconstruct:

- protocol version used
- site status
- participant workflow state
- source evidence
- data-quality checks
- safety escalations
- deviations
- monitoring findings
- agent outputs
- gate decisions
- human approvals

Auditability is essential because trial decisions may be reviewed long after the original operational event.

## CI and reproducibility

The GitHub Actions workflow under `.github/workflows/ci.yml` validates the reference system across supported Python versions.

Production extensions should also test:

- schema validation
- role-based access
- audit-trail integrity
- protocol-version transitions
- consent-version transitions
- data imports
- query workflows
- safety escalation timing
- blinded-data access controls
- integration with EDC, CTMS, eTMF, IRT, ePRO, laboratory, imaging, and safety systems as applicable

## L3 Gold Standard candidate

The repository includes `docs/L3_AUDIT.md` and is labeled an **L3 Gold Standard candidate** based on its independently reviewable structure, fail-closed gates, held-out evaluation, CI, explicit safety boundaries, and reproducibility path.

This maturity label is an engineering designation. It is not clinical validation, GCP certification, medical-device clearance, regulatory approval, or authorization to run a clinical trial autonomously.

## Extending F52

Common extensions include:

- CTMS integration
- EDC integration
- eTMF integration
- IRT or RTSM integration
- electronic consent
- ePRO and eCOA workflows
- central laboratory feeds
- imaging-core workflows
- safety database integration
- monitoring visit workflows
- remote monitoring
- risk-based monitoring
- protocol-window calculators
- enrollment forecasting
- DSMB package preparation
- site payment tracking
- data-cleaning workflows
- database-lock readiness
- regulatory document tracking

New integrations should preserve role separation, provenance, least privilege, safety escalation, and human decision authority.

## Design principles

1. Treat the approved protocol version as the operational source of truth.
2. Never infer consent, eligibility, or approval from workflow progress.
3. Preserve source-data provenance and audit trails.
4. Keep safety events under qualified clinical review.
5. Propagate protocol deviations and monitoring findings to governance gates.
6. Keep investigational-product accountability explicit.
7. Separate operational reporting from official regulatory submission authority.
8. Fail closed when participant protection or data-integrity evidence is incomplete.
9. Make every consequential workflow independently reviewable.
10. Keep final clinical, ethical, regulatory, and trial-management authority with qualified humans.

## Citation and reuse

The repository includes `CITATION.cff` for academic and technical citation and is distributed under the MIT license. It can be studied, referenced, adapted, and extended subject to the license terms.

## Responsible use

Use F52 as a clinical-trial operations and multi-agent architecture reference. Validate protocol, site, participant, safety, data, investigational-product, monitoring, privacy, and regulatory workflows against the actual study, jurisdiction, sponsor procedures, institutional requirements, and applicable GCP standards before operational use.