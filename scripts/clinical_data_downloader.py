import requests
import json
from src.config import (
    CLINICAL_DIR,
    CLINICAL_FILENAME,
    CASES_ENDPOINT,
    GDC_PROJECT_ID,
    GDC_CASES_PAGE_SIZE,
    REQUEST_TIMEOUT,
)

# Fields to retrieve
fields = [
    "submitter_id",
    "demographic.gender",
    "demographic.days_to_birth",
    "demographic.vital_status",
    "demographic.days_to_death",
    "diagnoses.laterality",
    "diagnoses.tumor_grade",
    "diagnoses.ajcc_pathologic_stage",
    "diagnoses.ajcc_pathologic_t",
    "diagnoses.ajcc_pathologic_n",
    "diagnoses.ajcc_pathologic_m",
    "diagnoses.days_to_last_follow_up"
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
