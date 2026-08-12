#!/usr/bin/env python3
"""Generate one self-contained folder per course activity."""
import csv, os, re, sys

HERE=os.path.dirname(os.path.abspath(__file__))
REPO=os.path.dirname(HERE)
sys.path.insert(0,HERE)
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3

def write(path,text):
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"w",encoding="utf-8",newline="") as f: f.write(text)

for a in DOMAIN1+DOMAIN2+DOMAIN3:
    folder=os.path.join(REPO,"labs",f"activity-{a['id']:02d}-{a['slug']}")
    os.makedirs(os.path.join(folder,"data"),exist_ok=True)
    readme=f"""# Activity {a['id']}: {a['title']}

**Real-use-case lens:** {a['case']}  
**Source lens:** {a['source']}  
**Objective:** {a['objective']}  
**Deliverable:** {a['deliverable']}

## Scenario

{a['scenario']}

## Detailed procedure

"""
    readme += "\n".join(f"{i}. {step}" for i,step in enumerate(a["steps"],1))
    readme += """

## Evidence checklist

- State the boundary, period, unit and source for every material figure.
- Separate calculated result, assumption and management judgement.
- Show formulas and retain intermediate values.
- Label company-linked figures as reported or illustrative.
- Record uncertainty, limitation and data-improvement actions.
- Ensure the final recommendation answers every scenario question.

## Files in this folder

- `SCENARIO.md` — case context and source note
- `QUESTIONS.md` — discussion and submission questions
- `data/activity-data.csv` — activity dataset or assumption register
"""
    scenario=f"""# Scenario — Activity {a['id']}: {a['title']}

## Case context

{a['scenario']}

## Learning purpose

{a['objective']}

## Source and evidence note

This activity uses **{a['source']}** as its professional or real-use-case lens. Unless explicitly stated otherwise, all quantities, costs, emission factors and company circumstances in this activity are **illustrative teaching data**. They must not be presented as reported company performance.

## Required output

{a['deliverable']}
"""
    questions=f"# Questions — Activity {a['id']}: {a['title']}\n\n"
    questions += "\n".join(f"{i}. {q}" for i,q in enumerate(a["questions"],1))
    questions += """

## Submission prompts

1. What did the quantitative evidence show?
2. Which conclusion depends most on an assumption or weak data?
3. What decision do you recommend, to whom, and by when?
4. What evidence would cause you to revise the recommendation?
"""
    write(os.path.join(folder,"README.md"),readme)
    write(os.path.join(folder,"SCENARIO.md"),scenario)
    write(os.path.join(folder,"QUESTIONS.md"),questions)
    write(os.path.join(folder,"data","activity-data.csv"),a["data"])

print("Generated 9 activity folders under labs/")
