# Underwater Collateral: Flood Risk in Official Land Values, Credit under Relief and Bank Capital — Evidence from Thailand

**One-page summary. Working draft, 2026-11-02 (revised after referee round 5).** Sources are as in `proposal.md`.

## The question

Does physical flood risk reach bank capital, and through which link: valuations, default, recoveries or provisioning? The question is asked of an economy where few homes were insured and regulatory debt relief was the main buffer for household borrowers.

## Why Thailand

- **Household insurance was thin.** An estimated fewer than 1% of dwellings were insured against natural disasters when the 2011 floods caused about THB 1.43 trillion in damage and losses (World Bank 2012).
- **Relief eligibility follows documented rules.** In 2011, lenders could keep the pre-flood classification of affected debtors classified pass or special mention (Bank of Thailand circular 1564/2554). Since 2024, relief is tied to dated disaster declarations, and in 2025 the Bank asked lenders to offer moratoria in Level-4 disaster zones.
- **Official land values for every titled parcel** are reset every four years, and satellites record the 2011 and 2024 floods.

## Three empirical chapters

| | Question | Design | Data |
|---|---|---|---|
| **Underwater valuations** | Do official land values capitalise flood hazard, and how do they adjust after a flood? | Change across valuation rounds around the 2024 floods, flooded against unflooded land at similar height above the valley floor; the 2011 flood edge descriptive only | Public: 37.8 million official parcel values; satellite flood maps |
| **Deferred, not avoided?** | Does relief defer or prevent credit deterioration, and how far do bank appraisals recognise hazard? | Primary: flooded against comparable unflooded borrowers through the 2024–25 relief and after it ends (1,100–2,300 flooded borrowers detect a 2-point rise in delinquency, under assumptions); extension: 2011 difference-in-discontinuities at the arrears threshold | Loan-level data through a University-held agreement. Without access: *A second flood*, Chapter 2's design on the 2025 floods (437 radar-flooded sheets in nine provinces), with data in hand |
| **Breaking point** | What flood severity pushes bank capital below a regulatory threshold? | Reverse stress test with staged ECL over flood scenarios (return period, footprint, timing); breaking severity on reported and economic capital, whose gap is the capital relief hides | Estimates from the first two chapters; public data for an illustrative system-level version |

## Contribution

- **Official valuations.** To my knowledge, the first controlled estimate of how an emerging market's official land values respond to a flood, and whether carry-over of earlier values slows their response (a Hat Yai cross-section already finds flood risk in official valuations; Semarang's official zones rose least where tidal flooding recurs, without controls). After 2011 the Treasury reported no fall in flooded areas.
- **Deferral versus avoided loss.** Relief eligibility rules are used to ask whether low post-flood default reflects resilience, recovery or deferral.
- **A breaking-point frontier.** The flood severity that breaches capital, on reported and economic capital, as a function of how far bank appraisals recognise hazard and what share of losses relief defers.

## Already done (public data only)

- **Data assembled.** Official values, flood maps and provincial credit are downloaded, logged and processed by a reproducible pipeline. 95.8% of parcels (36.2 million) are located on cadastral map sheets.
- **An honest first look.** Within local cells, urban land flooded in 2011 is valued about 48% lower than nearby unflooded land (rural 24%), but flooded sheets are far less built-up; controlling for 2021 land cover removes almost all of the gap, so the cross-section reflects land use, not hazard pricing. It also shows that 250 m flood maps are too coarse for small urban sheets, which is why the 2011 edge design uses rural sheets and the round-to-round design is primary.
- **Treated units for 2024.** Nationwide Sentinel-1 radar maps, built by a fixed rule, show 198 map sheets more than 25% flooded in four provinces, enough, under stated assumptions, to detect a fall of 0.05 log points in official values, about the full assumed hazard discount. In Chiang Rai and Phayao, UNOSAT's multi-sensor map shows 1,214; radar finds few of them, so the radar sample measures prolonged inundation and the UNOSAT sample, co-primary, any flooding.
- **Code ready for loan-level data.** The code for the credit and stress-test chapters has been tested on synthetic data with known parameters.

## About the author

The author holds a Master's in Economics with Distinction. Research governance is set out in the proposal: University-held data agreements, with all approaches to banks made by the University; public pre-registration; a public source log for every policy statement; an adviser outside the supervisory team reviewing the relief chapter's interpretation; and no bank-identifiable results.
