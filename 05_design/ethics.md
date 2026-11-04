# Ethics and research governance

**Working draft, 2026-11-02 (Phase 4).** This file sets out the main ethical issues and how each would be handled in a university ethics review.

## 1. Independence of the research

**Issue.** The research evaluates whether collateral values, provisioning and capital reflect flood risk, which in effect assesses outcomes of the regulatory framework, and it needs data that banks and the supervisor hold.

**Handling.**
- **Data.** Only public data, and data obtained through formal access agreements, are used.
- **Policy facts.** Every policy statement is sourced from a public document; see `02_policy_context/policy_timeline.md`.
- **Pre-specification.** Hypotheses and specifications for RQ1 are written down and registered publicly before estimation. This guards against results being shaped, or seen to be shaped, by what the data show.

## 2. Personal data (Thailand's PDPA and UK GDPR)

**Tier 1 public data.**
- **Treasury appraisal values.** These are parcel-level, but identified only by map sheet and parcel number, with no owner information. *Interpretation:* they are not personal data on their own. Parcel numbers are never linked to land-title or owner records, which the project does not hold.
- **Satellite rasters and aggregate statistics.** No personal data.

**Tier 2 restricted data** (loan-level credit data, RQ2, if access is granted).
- *Legal basis.* A data-sharing agreement with the data controller (a bank or credit bureau) under PDPA, with the controller de-identifying the data before transfer. Access is through a secure environment held by the controller, or by the host university under its data-protection policy.
- *Minimisation.* Only the variables needed: loan characteristics, payment status, stage, collateral location coarsened to the minimum resolution the design needs, and collateral value. No names, ID numbers or exact addresses.
- *Disclosure control.* Outputs are aggregated, with cell-count thresholds and output checking before release.
- *Pipeline development.* All code is developed on synthetic data (`03_data/synthetic/`) matching the Tier 2 schema, so code can be shared and reviewed without access to real records.

## 3. Harm and misuse of results

**Issue.** Fine-grained maps of flood-related collateral overvaluation could, if published at parcel or village level, affect land values or credit access for specific communities.

**Handling.** Results are published at aggregation levels that support the policy conclusion (district or map-sheet bands), and not as a parcel-level "risk list". Distributional findings are framed as evidence for policy design, such as relief targeting and insurance, not as grounds for withdrawing credit.

## 4. Third-party data terms

All Tier 1 sources are logged in `03_data/README.md` with their licence:
- The Global Flood Database is CC BY-NC 4.0, which allows non-commercial academic use, with attribution.
- Treasury data are under the DGA Open Government Licence.
- Sources whose terms forbid reuse, such as the REIC price indices, are excluded.

## 5. Human participants

None are planned. If the project adds interviews with bank risk staff, for example on staging practice under relief, these would need separate ethics approval and informed consent.

## Author notes

- A reader's likely question is how research that assesses a regulatory framework stays independent of the institutions it studies. The answer combines public data, formal access routes and pre-specification. Show these points in the proposal's data section, not only here.
