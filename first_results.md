# inter-annotator agreement

Calcolato dividendo prima il testo in tokens(parole con o senza punteggiatura, cambia poco);
Poi per ogni token e per ogni categoria classificazione binaria: 1 se è stato annotato con quella categoria; 0 altrimenti.
Questo procedimento per ogni annotazione.

Scelgo una delle annotazioni come gold standard (la mia in questo caso) e calcolo per ogni componente da annotare Precision, Recall e F1 score per le altre annotazioni. 

Alla fine macro-average tra i risultati per ogni componente

**Testi totali considerati:** 100  
**Gold Standard:** Federica.json  
**Predizioni (Annotatori):** 2  

| Label | precision | recall | f1 score |
| :--- | :---: | :---: | :---: |
| Abuse | 0.188 | 0.375 | 0.250 |
| Animosity | 0.241 | 0.277 | 0.257 |
| Dehumanization | 0.632 | 0.428 | 0.496 |
| Derogation | 0.362 | 0.513 | 0.403 |
| Ethnicity | 0.685 | 0.495 | 0.560 |
| Gender | 0.581 | 0.447 | 0.491 |
| Religion | 0.592 | 0.320 | 0.390 |
| Sexual Orientation | 0.703 | 0.500 | 0.456 |
| Support for hateful entities | 0.496 | 0.548 | 0.519 |
| Threatening language | 0.588 | 0.538 | 0.557 |
| **MACRO-AVERAGE** | **0.507** | **0.444** | **0.438** |


## Agreement con i modelli

### Federica

### Llama

| Label | precision | recall | f1 |
| :--- | :---: | :---: | :---: |
| Abuse | 0.006 | 0.750 | 0.013 |
| Animosity | 0.224 | 0.243 | 0.233 |
| Dehumanization | 0.214 | 0.316 | 0.255 |
| Derogation | 0.210 | 0.561 | 0.305 |
| Ethnicity | 0.561 | 0.573 | 0.567 |
| Gender | 0.393 | 0.632 | 0.485 |
| Religion | 0.316 | 0.240 | 0.273 |
| Sexual Orientation | 0.350 | 0.412 | 0.378 |
| Support for hateful entities | 0.605 | 0.125 | 0.207 |
| Threatening language | 0.432 | 0.296 | 0.351 |
| **MACRO-AVERAGE** | **0.331** | **0.415** | **0.307** |

---

### Mistral

| Label | precision | recall | f1 |
| :--- | :---: | :---: | :---: |
| Abuse | 0.004 | 0.750 | 0.009 |
| Animosity | 0.108 | 0.396 | 0.170 |
| Dehumanization | 0.095 | 0.579 | 0.163 |
| Derogation | 0.108 | 0.482 | 0.176 |
| Ethnicity | 0.617 | 0.521 | 0.565 |
| Gender | 0.373 | 0.658 | 0.476 |
| Religion | 0.667 | 0.240 | 0.353 |
| Sexual Orientation | 0.571 | 0.471 | 0.516 |
| Support for hateful entities | 0.443 | 0.245 | 0.316 |
| Threatening language | 0.278 | 0.390 | 0.324 |
| **MACRO-AVERAGE** | **0.326** | **0.473** | **0.307** |

---

### Qwen

| Label | precision | recall | f1 |
| :--- | :---: | :---: | :---: |
| Abuse | 0.000 | 0.000 | 0.000 |
| Animosity | 0.009 | 0.018 | 0.012 |
| Dehumanization | 0.078 | 0.145 | 0.101 |
| Derogation | 0.110 | 0.596 | 0.186 |
| Ethnicity | 0.482 | 0.552 | 0.515 |
| Gender | 0.176 | 0.579 | 0.270 |
| Religion | 0.800 | 0.480 | 0.600 |
| Sexual Orientation | 0.083 | 0.059 | 0.069 |
| Support for hateful entities | 0.526 | 0.293 | 0.377 |
| Threatening language | 0.500 | 0.197 | 0.283 |
| **MACRO-AVERAGE** | **0.276** | **0.292** | **0.241** |


### Katerina

### Llama

| Label | precision | recall | f1 |
| :--- | :---: | :---: | :---: |
| Abuse | 0.004 | 0.250 | 0.008 |
| Animosity | 0.282 | 0.250 | 0.265 |
| Dehumanization | 0.098 | 0.289 | 0.147 |
| Derogation | 0.180 | 0.539 | 0.270 |
| Ethnicity | 0.327 | 0.615 | 0.427 |
| Gender | 0.262 | 0.696 | 0.381 |
| Religion | 0.158 | 0.375 | 0.222 |
| Sexual Orientation | 0.150 | 0.750 | 0.250 |
| Support for hateful entities | 0.442 | 0.091 | 0.151 |
| Threatening language | 0.527 | 0.464 | 0.494 |
| **MACRO-AVERAGE** | **0.243** | **0.432** | **0.261** |

---

### Mistral

| Label | precision | recall | f1 |
| :--- | :---: | :---: | :---: |
| Abuse | 0.003 | 0.250 | 0.006 |
| Animosity | 0.137 | 0.408 | 0.205 |
| Dehumanization | 0.045 | 0.553 | 0.084 |
| Derogation | 0.110 | 0.549 | 0.183 |
| Ethnicity | 0.395 | 0.615 | 0.481 |
| Gender | 0.254 | 0.739 | 0.378 |
| Religion | 0.333 | 0.375 | 0.353 |
| Sexual Orientation | 0.286 | 1.000 | 0.444 |
| Support for hateful entities | 0.400 | 0.220 | 0.284 |
| Threatening language | 0.241 | 0.434 | 0.310 |
| **MACRO-AVERAGE** | **0.220** | **0.514** | **0.273** |

---

### Qwen

| Label | precision | recall | f1 |
| :--- | :---: | :---: | :---: |
| Abuse | 0.000 | 0.000 | 0.000 |
| Animosity | 0.107 | 0.180 | 0.134 |
| Dehumanization | 0.028 | 0.105 | 0.045 |
| Derogation | 0.118 | 0.716 | 0.203 |
| Ethnicity | 0.318 | 0.673 | 0.432 |
| Gender | 0.104 | 0.565 | 0.176 |
| Religion | 0.267 | 0.500 | 0.348 |
| Sexual Orientation | 0.000 | 0.000 | 0.000 |
| Support for hateful entities | 0.638 | 0.354 | 0.455 |
| Threatening language | 0.881 | 0.446 | 0.592 |
| **MACRO-AVERAGE** | **0.246** | **0.354** | **0.238** |

### Arianna

### Llama

| Label | precision | recall | f1 |
| :--- | :---: | :---: | :---: |
| Abuse | 0.131 | 0.439 | 0.202 |
| Animosity | 0.133 | 0.139 | 0.136 |
| Dehumanization | 0.152 | 0.224 | 0.181 |
| Derogation | 0.252 | 0.296 | 0.273 |
| Ethnicity | 0.357 | 0.347 | 0.352 |
| Gender | 0.311 | 0.396 | 0.349 |
| Religion | 0.263 | 0.217 | 0.238 |
| Sexual Orientation | 0.350 | 0.219 | 0.269 |
| Support for hateful entities | 0.093 | 0.015 | 0.026 |
| Threatening language | 0.548 | 0.343 | 0.422 |
| **MACRO-AVERAGE** | **0.259** | **0.263** | **0.245** |

---

### Mistral

| Label | precision | recall | f1 |
| :--- | :---: | :---: | :---: |
| Abuse | 0.131 | 0.655 | 0.218 |
| Animosity | 0.138 | 0.487 | 0.215 |
| Dehumanization | 0.060 | 0.368 | 0.104 |
| Derogation | 0.210 | 0.412 | 0.278 |
| Ethnicity | 0.420 | 0.337 | 0.374 |
| Gender | 0.254 | 0.354 | 0.296 |
| Religion | 0.444 | 0.174 | 0.250 |
| Sexual Orientation | 0.429 | 0.188 | 0.261 |
| Support for hateful entities | 0.200 | 0.087 | 0.121 |
| Threatening language | 0.304 | 0.391 | 0.342 |
| **MACRO-AVERAGE** | **0.259** | **0.345** | **0.246** |

---

### Qwen

| Label | precision | recall | f1 |
| :--- | :---: | :---: | :---: |
| Abuse | 0.000 | 0.000 | 0.000 |
| Animosity | 0.041 | 0.083 | 0.055 |
| Dehumanization | 0.113 | 0.211 | 0.147 |
| Derogation | 0.165 | 0.392 | 0.232 |
| Ethnicity | 0.345 | 0.376 | 0.360 |
| Gender | 0.304 | 0.792 | 0.439 |
| Religion | 0.333 | 0.217 | 0.263 |
| Sexual Orientation | 0.083 | 0.031 | 0.045 |
| Support for hateful entities | 0.388 | 0.170 | 0.236 |
| Threatening language | 0.607 | 0.219 | 0.322 |
| **MACRO-AVERAGE** | **0.238** | **0.249** | **0.210** |
