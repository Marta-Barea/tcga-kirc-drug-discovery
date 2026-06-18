from pathlib import Path
from dotenv import load_dotenv
import os
import requests
import json

# Project configuration
PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(PROJECT_ROOT / ".env")

DATA_DIR = PROJECT_ROOT / os.getenv("DATA_DIR", "data")

CLINICAL_DIR = DATA_DIR / "clinical"
CLINICAL_DIR.mkdir(parents=True, exist_ok=True)

# GDC configuration
GDC_API_BASE_URL = os.getenv("GDC_API_BASE_URL", "https://api.gdc.cancer.gov")
GDC_PROJECT_ID = os.getenv("GDC_PROJECT_ID", "TCGA-KIRC")
GDC_CASES_PAGE_SIZE = int(os.getenv("GDC_CASES_PAGE_SIZE", "1000"))
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "60"))
CLINICAL_FILENAME = os.getenv("CLINICAL_FILENAME", "tcga_kirc_clinical.tsv")

CASES_ENDPOINT = f"{GDC_API_BASE_URL}/cases"

# Fields to retrieve
fields = [
    "submitter_id",
    "demographic.gender",
    "demographic.days_to_birth",
    "demographic.vital_status",
    "diagnoses.tumor_grade",
    "diagnoses.ajcc_pathologic_stage",
    "diagnoses.ajcc_pathologic_t",
    "diagnoses.ajcc_pathologic_n",
    "diagnoses.ajcc_pathologic_m",
    "diagnoses.days_to_last_follow_up",
    "diagnoses.days_to_death",
]

# Query parameters
filters = {
    "op": "in",
    "content": {
        "field": "cases.project.project_id",
        "value": [GDC_PROJECT_ID],
    },
}

params = {
    "filters": json.dumps(filters),
    "fields": ",".join(fields),
    "size": str(GDC_CASES_PAGE_SIZE),
    "format": "TSV",
}

# Download clinical data
response = requests.get(
    CASES_ENDPOINT,
    params=params,
    timeout=REQUEST_TIMEOUT,
)

response.raise_for_status()

output_file = CLINICAL_DIR / CLINICAL_FILENAME

with open(output_file, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Clinical data saved to: {output_file}")
