# Agentic Clinical Trial Manager

**System:** F52  
**Version:** 1.0.0  
**Maturity:** L3 Gold Standard candidate

A six-agent reference architecture for clinical trial operations support. The system coordinates protocol planning, site coordination, recruitment tracking, data quality, protocol-deviation review, and reporting while keeping consequential trial decisions under qualified human authority.

## Fail-closed governance

Trial operations cannot be approved when protocol versioning, IRB/ethics approval, informed consent, eligibility verification, privacy review, source-data traceability, audit trails, adverse-event review, serious-adverse-event escalation, deviation review, site training, investigational-product accountability, data quality, monitoring findings, safety-committee review, conflicts, unresolved questions, or material open risks are incomplete.

Human approval is required after automated gates pass and cannot override an active blocker.

## Reproduce

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

## Scope boundary

This repository is an engineering reference for research-operations decision support. It does not replace investigators, sponsors, IRBs/ethics committees, DSMBs, monitors, regulators, site staff, or applicable GCP and regulatory obligations. L3 is an engineering maturity designation, not clinical validation or regulatory authorization.
