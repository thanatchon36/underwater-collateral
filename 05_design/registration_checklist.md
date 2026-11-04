# RQ1 registration checklist (for the author, on the day)

**Working draft, 2026-11-03.** Everything here is done by the author from their own OSF account (CP3); nothing is submitted from this workspace. Deadline: before any 2027–30 schedule is published, and by **2 December 2026** at the latest (PAP §9). Allow about two hours. Commands run from the repository root; in Claude Code, type them after `!`.

## 1. Freeze the code (15 min)

0. Mark the documents as the registered versions, before the freeze commit: in `05_design/pre_analysis_plan_rq1_draft.md` replace the title's "working draft (not registered)" with "version registered on OSF Registries", and replace the first paragraph's "Draft of 2026-11-02 for the author to edit and register on OSF Registries" with "Registered on OSF Registries (DOI and timestamp on the registration page)"; do the same for the form's title and first paragraph. The plan already refers to "the commit recorded in the OSF registration", so no hash has to be written into it.
1. Make sure the working tree is clean and everything is pushed: `git status` (nothing to commit) and `git push`.
2. Rebuild and test from raw (about 32 minutes): `.venv/bin/python -I 04_analysis/run_all.py`. It must end with all tests passing. Restore figure PDFs whose only change is the creation date: `git checkout -- 04_analysis/outputs/figures/`.
3. If step 2 changed any table, commit it, and push. Then record the commit: `git rev-parse HEAD`. This is the **registration commit**. Write it into the form in two places: "Code repository" (under *Data identifiers*) and "Code" (under *Statistical models*).
4. Copy the 17 rows of `04_analysis/outputs/tables/registration_hashes.csv` (file, rows, SHA-256 of the decompressed contents) into the form, under the sample-file paragraph of "Codebook". The PAP is registered with these hashes. The sample files themselves stay local (derived from public data, rebuildable by `run_all.py`).

## 2. Build the upload bundle (5 min)

The repository is private, so OSF needs either a public mirror or an upload. The simplest is a zip of the registration commit (code, PAP, form, schemas, hashes; no data):

```
git archive --format=zip -o ../rq1_registration_$(git rev-parse --short HEAD).zip HEAD \
  04_analysis/src 04_analysis/run_all.py requirements.txt \
  05_design/pre_analysis_plan_rq1_draft.md 05_design/osf_registration_form.md \
  03_data/schemas 03_data/README.md 04_analysis/outputs/tables/registration_hashes.csv
```

`git archive` takes files from the commit, not from the working tree, so the zip matches the hash exactly. Checked 2026-11-03: `04_analysis/src` (45 files, about 0.4 MB) holds no credentials or personal data; the only "token" strings are Microsoft Planetary Computer's public anonymous-token URL. If you prefer a public mirror instead, push the same commit to a public repository and give its URL; do not make the working repository public (it holds drafts with your COI notes).

## 3. Fill the placeholders in `osf_registration_form.md`

| Placeholder | Field | What to write |
|---|---|---|
| `[public mirror URL or OSF upload]`, `[hash at registration]`, `[hash]` | Data identifiers; Statistical models | "uploaded to this registration" (or the mirror URL), and the registration commit |
| `[author to confirm the terms on data.go.th]` | Data access | open https://data.go.th/dataset/land-valuation, read the licence shown, and state it |
| `[to be recorded]` | Access date | the only placeholder that stays: the R1 download date is recorded in the deviations log after registration |
| `[Author to state in own words.]` | Prior publication / dissemination | rewrite the draft sentence yourself |
| `[Author to rewrite in own words ...]` | Prior knowledge | rewrite in your own words; say what you have and have not seen (the 2023–26 round only; no R1) |
| `[Author to confirm.]` | Prior knowledge | confirm that you have no role in setting official values and no access to unpublished Treasury data |

Then search the form for any remaining `[` (only `[to be recorded]` may stay) and remove the drafting notes at the top.

## 4. On OSF Registries

1. Start a new registration on OSF Registries and pick the template **"Secondary Data Preregistration"** (version 3, as drafted; menu names not checked here).
2. Paste each section of the form into the field of the same name.
3. Upload: the zip from step 2. Upload the PAP PDF/Markdown separately as well, so reviewers can read it without unzipping.
4. Embargo: choose immediate release or an embargo (check the maximum OSF offers on the day; not verified here). The registration's timestamp, not its visibility, is what proves it predates the 2027–30 round.
5. Submit and **save the registration DOI and the timestamp**.

## 5. After registering

- Add the DOI and the date to the PAP's opening paragraph (replace "working draft (not registered)") and to proposal §7 (one line; the proposal is at 2,400 words, so cut a line elsewhere), and add a ledger row (`06_proposal/claims_ledger.csv`).
- Fill the header of `05_design/deviations_log.md` (DOI, timestamp, commit); from then on, log every change there before reading any affected estimate.
- When the DDPM lists arrive, enter them into `03_data/raw/ddpm_declarations/declarations_2024.csv` (schema `03_data/schemas/ddpm_declarations_2024.md`) and log the receipt in `03_data/README.md`. This is the data the registered code expects, not a change to it.
- When R1 is published: download it (`download_treasury_appraisal.py`, which writes a new dated snapshot folder with SHA-256; pass `--package <id>` if R1 appears as a new data.go.th dataset), note the date in the deviations log, and run the registered commands unchanged (form, *Statistical models*). For each run, copy the sample provinces' files unchanged into one folder and point `--post` at it; the code stops if a province's file is missing or identical to its 2023–26 file, and if more than 10% of a province's sheets find no parcel (then check identifiers and log any harmonisation as a deviation before rerunning). It also stops if more than 99% of matched parcels keep their value or more than 50% move by one common ratio (a unit change or rescaling): check against the Treasury's publication and log any harmonisation as a deviation. With mixed timing (PAP §9) run each subset with `--provinces`, and `--holm` once the R1 family closes; case-(b) provinces later run on R2 with `--round R2`, and `--holm` again after the last of them (separate R2 family).
