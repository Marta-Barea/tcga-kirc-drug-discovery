from pathlib import Path
import pandas as pd
from src.config import (
    PROJECT_ROOT,
    CLINICAL_DIR,
    CLINICAL_FILENAME
)

# Load clinical data
clinical_data_path = PROJECT_ROOT / CLINICAL_DIR / CLINICAL_FILENAME
clinical_data = pd.read_csv(clinical_data_path, sep="\t")

# Drop diagnosis columns with an index greater than 0 (keep diagnoses.0.*)
columns_to_drop = [
    col for col in clinical_data.columns
    if col.startswith("diagnoses.")
    and not col.startswith("diagnoses.0.")
]

# Drop the identified columns
clinical_data = clinical_data.drop(columns=columns_to_drop)

print(clinical_data.columns)

# Rename columns
clinical_data = clinical_data.rename(
    columns=lambda x: x.rsplit(".", 1)[-1]
)
