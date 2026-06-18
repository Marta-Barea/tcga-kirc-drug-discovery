from pathlib import Path
from dotenv import load_dotenv
import os

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
