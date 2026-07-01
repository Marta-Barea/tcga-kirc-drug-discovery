<div align="center">

# Standard Oncological Clinical Variables

*Definitions and categorical encodings based on the AJCC/TNM classification system and standard pathological reporting.*

</div>

| **Variable** | **Description** | **Encoded Values** |
|--------------|-----------------|--------------------|
| `ajcc_pathologic_m` | **Distant metastasis status (AJCC TNM)** | `M0`: No distant metastasis.<br>`M1`: Distant metastasis present.<br>`MX`: Distant metastasis cannot be assessed. |
| `ajcc_pathologic_n` | **Regional lymph node involvement (AJCC TNM)** | `N0`: No regional lymph node metastasis.<br>`N1`: Metastasis in regional lymph node(s).<br>`N2`: More extensive regional lymph node involvement.<br>`N3`: Advanced regional lymph node involvement.<br>`NX`: Regional lymph nodes cannot be assessed. |
| `ajcc_pathologic_stage` | **Overall pathological stage (AJCC)** | `Stage I`: Localized disease.<br>`Stage IA–IB`: Early localized disease.<br>`Stage II`: Larger or locally advanced tumor without distant metastasis.<br>`Stage IIA–IIB`: Stage II substages.<br>`Stage III`: Regional spread (e.g., lymph nodes or local extension).<br>`Stage IIIA–IIIC`: Stage III substages.<br>`Stage IV`: Distant metastatic disease.<br>`Stage IVA–IVB`: Stage IV substages.<br>`Unknown`: Stage not available. |
| `ajcc_pathologic_t` | **Primary tumor size and extent (AJCC TNM)** | `T0`: No evidence of primary tumor.<br>`T1`: Tumor confined to the kidney, ≤7 cm.<br>`T1a`: ≤4 cm.<br>`T1b`: >4–7 cm.<br>`T2`: Tumor >7 cm, confined to the kidney.<br>`T2a`: >7–10 cm.<br>`T2b`: >10 cm.<br>`T3`: Tumor extends into major veins or perinephric tissues, not beyond Gerota's fascia.<br>`T4`: Tumor invades beyond Gerota's fascia, including the ipsilateral adrenal gland.<br>`TX`: Primary tumor cannot be assessed. |
| `laterality` | **Primary tumor location** | `Left`: Left kidney.<br>`Right`: Right kidney.<br>`Bilateral`: Both kidneys.<br>`Midline`: Tumor located at the midline.<br>`Not Reported`: Information unavailable. |
| `tumor_grade` | **Histological tumor grade** | `G1`: Well differentiated (low grade).<br>`G2`: Moderately differentiated.<br>`G3`: Poorly differentiated (high grade).<br>`G4`: Undifferentiated/anaplastic (highest grade).<br>`GX`: Grade cannot be assessed. |