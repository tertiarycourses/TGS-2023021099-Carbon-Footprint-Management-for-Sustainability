# Courseware QA Report — v7

Course: Carbon Footprint Management for Sustainability  
Course code: TGS-2023021099  
Audit date: 13 August 2026

## Outcome

**PASS — ready for Google Drive publication and LMS/TMS preflight.**

## Verified package

- Trainer deck: 133 slides, 16:9, all-white Tertiary house style, restrained transitions.
- Learner Guide: A4 DOCX and PDF, detailed activity procedures, scenarios and questions.
- Lesson Plan: A4 DOCX and PDF, exact slide mappings, 8 training hours per day plus a separate 2-hour assessment.
- Activities: 9 individual folders under `activities/`, each with README, scenario, questions and CSV data.
- Assessment: 9 open-ended SAQs mapped K1–K9, 1 hour; 3-question case study mapped A1–A3, 1 hour; question papers and answer keys.
- Source register: primary standards/Singapore requirements and all user-supplied sources.

## Alignment checks

| Requirement | Result |
|---|---|
| Course code and title consistent | Pass |
| TSC PRE-ENV-4001-1.1 and A1–A3 mapped | Pass |
| K1–K9 mapped to WA | Pass |
| A1–A3 mapped to case study | Pass |
| Assessment count, type and timings match approved legacy plan | Pass |
| Old v6 competency content retained or expanded | Pass — see `LEGACY-COVERAGE-MAP.md` |
| No detailed step-by-step procedures in PPT | Pass |
| Detailed procedures in activity guides and Learner Guide | Pass |
| Authentic SG Carbon Calculator visual and activity | Pass |
| Company-linked teaching figures labelled illustrative | Pass |
| Current Singapore carbon-tax/MR context source-linked | Pass |
| Non-certification practice exam omitted | Pass — intentional |

## Technical and visual checks

- PPTX, DOCX and generated PDFs open and convert successfully.
- ZIP package integrity check: no corrupt PPTX/DOCX members.
- PPTX geometry check: zero shapes outside slide bounds.
- Full 133-slide contact-sheet review completed.
- Independent fresh-eye review completed; all blocking findings corrected:
  - seven gases are now shown separately;
  - worked-example and chart text enlarged;
  - activity briefs simplified;
  - course-completion/funding title corrected;
  - source slides show readable source names/domains, with full links in the Learner Guide.
- Learner Guide, Lesson Plan and assessment PDFs sampled visually after A4 conversion.
- Static, page-numbered tables of contents injected into the Learner Guide and Lesson Plan.

## Exact artifact binding for this QA run

| Artifact | SHA-256 |
|---|---|
| Trainer deck PPTX | `203c97cf0d931a0c424ae2ff61c375097a661f4333ee39cb5d6fd9254207c020` |
| Trainer/learner slides PDF | `4ccc422d5e5442d8ec87aee9e59f017a2c1d7d5095a1484a30e1c486f1d1f5e9` |
| Learner Guide DOCX | `34c1d91a768f841187735a30313770828e0b9bdd73364687899d018f9649350a` |
| Learner Guide PDF | `d5e521533850f24e203776f718eef9e446ee2103074af3f75ab60112b1f0a9c0` |
| Lesson Plan DOCX | `11ca0ef31c33918387151230e17e3257c874199aafa23462acdd084435f94383` |
| Lesson Plan PDF | `7d9026b3337e57bf8480dd9fe74508b63eb6dfe14b80b0a321a8905f1dc81780` |

Folder-name verification: the canonical local source is `activities/` with 9 activity folders and 36 files; no local `labs/` directory remains.

## Publication boundary

- Upload both assessment question papers and trainer-only answer keys to Google Drive.
- Link only question papers to LMS/TMS assessment fields; never expose answer keys.
- `.env` stores the approved courseware folder and is excluded from GitHub.
- Reference artifacts and unrelated legacy assessments are excluded from GitHub.
