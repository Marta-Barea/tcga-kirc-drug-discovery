import numpy as np
from pathlib import Path
import pandas as pd
from src.config import (
    PROJECT_ROOT,
    CLINICAL_DIR,
    CLINICAL_FILENAME
)


def prepare_clinical_data():
    clinical_data_path = PROJECT_ROOT / CLINICAL_DIR / CLINICAL_FILENAME
    clinical_data = pd.read_csv(clinical_data_path, sep="\t")

    # Keep identifiers as first columns
    id_columns = ['id', 'submitter_id']
    other_columns = [
        col for col in clinical_data.columns if col not in id_columns]
    clinical_data = clinical_data[id_columns + other_columns]

    # Keep only the first diagnosis record
    columns_to_drop = [
        col for col in clinical_data.columns
        if col.startswith("diagnoses.")
        and not col.startswith("diagnoses.0.")
    ]

    clinical_data = clinical_data.drop(columns=columns_to_drop)

    clinical_data = clinical_data.rename(
        columns=lambda x: x.rsplit(".", 1)[-1]
    )

    # TCGA stores age as negative days from birth
    clinical_data['age_at_diagnosis'] = - \
        clinical_data['days_to_birth'] / 365.25

    # Convert time variables from days to years
    clinical_data['years_to_last_follow_up'] = clinical_data['days_to_last_follow_up'] / 365.25
    clinical_data['years_to_death'] = clinical_data['days_to_death'] / 365.25

    clinical_data = clinical_data.drop(
        columns=[
            'days_to_birth',
            'days_to_last_follow_up',
            'days_to_death'
        ]
    )

    # Create survival variables
    clinical_data['event'] = (
        clinical_data['vital_status'] == 'Dead'
    ).astype(int)

    clinical_data['survival_time'] = np.where(
        clinical_data['event'] == 1,
        clinical_data['years_to_death'],
        clinical_data['years_to_last_follow_up']
    )

    # Handle missing values
    clinical_data = clinical_data.dropna(subset=["survival_time"])

    clinical_data = clinical_data.dropna(subset=["ajcc_pathologic_stage"])

    clinical_data['ajcc_pathologic_m'] = clinical_data['ajcc_pathologic_m'].fillna(
        'MX')
    clinical_data['ajcc_pathologic_n'] = clinical_data['ajcc_pathologic_n'].fillna(
        'NX')
    clinical_data['ajcc_pathologic_t'] = clinical_data['ajcc_pathologic_t'].fillna(
        'TX')
    clinical_data['tumor_grade'] = clinical_data['tumor_grade'].fillna(
        'GX')

    clinical_data['laterality'] = clinical_data['laterality'].fillna(
        clinical_data['laterality'].mode()[0])

    clinical_data['age_at_diagnosis'] = clinical_data['age_at_diagnosis'].fillna(
        clinical_data['age_at_diagnosis'].median())

    return clinical_data


if __name__ == "__main__":
    prepare_clinical_data()
