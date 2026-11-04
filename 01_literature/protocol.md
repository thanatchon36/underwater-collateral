# Literature search protocol: R3 "Underwater Collateral"

**Working draft, 2026-11-02.** Topic chosen at CP1; framing in `CLAUDE.md`.

## Strands

| ID | Strand | Question the strand answers for the proposal |
|---|---|---|
| S1 | Disasters, floods and bank credit | What happens to credit supply, demand, default and bank balance sheets after floods and other disasters? |
| S2 | Physical climate risk in property and collateral values | Is flood or climate hazard capitalised into property prices and lenders' collateral valuations, and how fast? |
| S3 | Climate risk in credit-risk models, IFRS 9 ECL and stress testing | How do supervisors and banks translate physical hazard into PD, LGD, ECL, capital and (reverse) stress tests, and what is the evidence on whether provisions reflect it? |
| S4 | Satellite and remote-sensing measurement of floods in economics | What can flood maps (MODIS, Sentinel-1 SAR, the Global Flood Database) measure, at what resolution, with what error, and how have economists used them for identification? |
| S5 | Emerging markets: the insurance gap, debt relief and forbearance after disasters, and Thailand's 2011 floods | How do relief, forbearance and thin insurance change the default response, and what is known about the 2011 Thai floods' economic and financial effects? |

## Sources

General web search (sparingly); OpenAlex, Crossref and Semantic Scholar APIs; NBER, SSRN (via OpenAlex/Crossref where blocked), RePEc/IDEAS, CEPR; BIS, IMF, NGFS, FSB, ECB, Federal Reserve, Bank of England, Banco de España and other central bank staff papers; PIER and BOT; top journals (AER, QJE, JPE, Econometrica, REStud, JF, RFS, JFE, JFQA, RoF, JME, the AEJs, JFI, JBF, JUE, Real Estate Economics, J. Environmental Economics and Management, Nature/Nature Climate Change for measurement).

## Inclusion criteria

- Directly informs one of the strand questions; empirical or methodological contribution, or an official supervisory framework document.
- Peer-reviewed, or a working paper in a recognised series (NBER, CEPR, central bank, IMF, BIS, university departments, SSRN with an identifiable author affiliation).
- Priority to 2015–2026, with older seminal work included where it is the standard citation.
- Retracted papers are excluded as evidence. Ouazad & Kahn (RFS 2022) is retracted; mention it only as a retraction.

## Snowballing

Seed papers (from `01_literature/strands/S0_scoping.bib`): Albertazzi, Djekic & Ponte Marques (2026); Garbarino & Guin (2021); Cortés & Strahan (2017); Bernstein, Gustafson & Lewis (2019); Chitchumnong et al. (2025); Tellman et al. (2021); Kocornik-Mina et al. (2020). Snowball backwards (references) and forwards (citations) via OpenAlex or Semantic Scholar.

## Recording

Each strand produces the following files:

- `01_literature/strands/S<n>_notes.md`: synthesis plus a per-paper note.
- `01_literature/strands/S<n>.bib`: BibTeX with `url` and `note = {verified YYYY-MM-DD via <source>}`.
- `01_literature/strands/S<n>_matrix.csv`: the lit_matrix columns.

These are merged into `01_literature/references.bib` and `01_literature/lit_matrix.csv`.

Read depth is recorded honestly: `abstract`, `intro` or `full`. For the 10–15 closest papers overall, aim for `intro` or `full`, using open working-paper or author versions.
