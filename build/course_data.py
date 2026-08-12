"""Single source of truth for TGS-2023021099 courseware."""

COURSE_TITLE = "Carbon Footprint Management for Sustainability"
SHORT_TITLE = "Carbon-Footprint-Management-for-Sustainability"
COURSE_CODE = "TGS-2023021099"
TSC_TITLE = "Carbon Footprint Management"
TSC_CODE = "PRE-ENV-4001-1.1"
VERSION = "v7"
VERSION_DATE = "12 August 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "201200696W"
TRAINER = "Dr Alfred Ang"
COURSE_HOURS = "16 training hours over 2 days, plus 2 assessment hours"

LEARNING_OUTCOMES = [
    "LO1 — Analyse carbon emission hotspots using recognised standards, boundaries and reliable activity data.",
    "LO2 — Prioritise carbon-footprint reduction initiatives using projections, feasibility, cost-benefit and decision tools.",
    "LO3 — Develop an implementable carbon-footprint reduction plan with governance, targets, monitoring and continual improvement.",
]

TOPICS = [
    {"code": "1", "title": "Analyse Carbon Emission Hotspots", "subtitle": "Standards, boundaries, data, scopes and hotspot diagnosis", "ks": "K1 · K3 · K7", "a": "A1"},
    {"code": "2", "title": "Prioritise Reduction Initiatives", "subtitle": "Projection, technology, economics and transparent decisions", "ks": "K4 · K5 · K8", "a": "A2"},
    {"code": "3", "title": "Develop the Reduction Plan", "subtitle": "EMS governance, action planning, Singapore requirements and review", "ks": "K2 · K6 · K9", "a": "A3"},
]

KNOWLEDGE = {
    "K1": "Environmental management standards relevant to carbon footprint management, including ISO 14001 and ISO 14064.",
    "K2": "Environmental management system principles and the Plan-Do-Check-Act cycle.",
    "K3": "Methods and tools used to identify and analyse carbon emission hotspots.",
    "K4": "Methods used to project future emissions and model reduction scenarios.",
    "K5": "Feasible technologies and operational measures for carbon footprint reduction.",
    "K6": "Components of an organisational carbon-footprint reduction plan.",
    "K7": "Cost-benefit and investment appraisal tools for carbon-reduction initiatives.",
    "K8": "Tools and techniques used to prioritise carbon-footprint reduction initiatives.",
    "K9": "Tools and techniques used to develop action plans for carbon footprint reduction.",
}

ABILITIES = {
    "A1": "Analyse carbon emission hotspots.",
    "A2": "Prioritise carbon footprint reduction initiatives.",
    "A3": "Develop carbon footprint reduction plans.",
}

DAY_THEMES = {
    1: "Measure What Matters — Boundary, Scopes and Hotspots",
    2: "Move From Insight to Action — Priorities, Plans and Governance",
}

ASSESSMENT = {
    "wa": "Written Assessment (Short-Answer Questions): 9 questions, 1 hour, open book",
    "cs": "Written Assessment (Case Study): 3 questions, 1 hour, open book",
}

RECOMMENDED_COURSES = [
    "WSQ Sustainability Reporting and Assurance",
    "WSQ Environmental, Social and Governance (ESG) Essentials",
    "WSQ Data Analytics for Sustainability",
    "WSQ Business Process Automation with Power Automate",
    "WSQ Business Innovation with Artificial Intelligence",
]

SOURCES = [
    ("GHG Protocol Corporate Standard", "https://ghgprotocol.org/corporate-standard"),
    ("United Nations ActNow — Ten Actions", "https://www.un.org/en/actnow/ten-actions"),
    ("NEA — Singapore Carbon Tax", "https://www.nea.gov.sg/our-services/climate-change-energy-efficiency/climate-change/carbon-tax"),
    ("NEA — Measurement and Reporting Requirements", "https://www.nea.gov.sg/our-services/climate-change-energy-efficiency/climate-change/carbon-tax/measurement-and-reporting-requirements-for-greenhouse-gas-emissions"),
    ("EMA — Singapore Energy Statistics, Chapter 2", "https://www.ema.gov.sg/resources/singapore-energy-statistics/chapter2"),
    ("SAP Sustainability Footprint Management", "https://www.sap.com/sea/products/scm/sustainability-footprint-management.html"),
    ("IMD — Carbon Management", "https://www.imd.org/blog/sustainability/carbon-management/"),
    ("Yurtay (2025), Industry 4.0 and ERP Systems", "https://www.mdpi.com/2076-3417/15/1/480"),
    ("Synesgy — Carbon Footprint Guide", "https://www.synesgy.com/en/esg-guide/carbon-footprint/"),
    ("Green Earth — Carbon Footprints", "https://www.green.earth/carbonfootprints"),
    ("CarbonChain — Reducing Company Footprints", "https://www.carbonchain.com/carbon-accounting/how-can-companies-reduce-carbon-footprint"),
    ("SG Carbon Calculator", "https://github.com/alfredang/sgcarboncalculator"),
]
