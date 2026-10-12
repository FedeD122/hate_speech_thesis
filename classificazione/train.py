from pathlib import Path

import pandas as pd
import torch
import time

import lftw
import pyhighlights
from cinnamon.registry import Registry
from lftw.configurations.keys import (
    LFTW_FR_TASK,
    LFTW_ETHNICITY_FR_TASK,
    LFTW_ETHNICITY_MCD_TASK,
    LFTW_GENDER_FR_TASK,
    LFTW_RELIGION_FR_TASK,
    LFTW_SEXOR_FR_TASK,
)

valid, invalid = Registry.build(
    directory=Path(lftw.__file__).parent,
    external_directories=[Path(pyhighlights.__file__).parent],
)
print("invalid:", invalid)


task = Registry.from_key(
    LFTW_SEXOR_FR_TASK,
    seeds=[42],
    embeddings="classificazione/glove.twitter.27B.25d.txt",
    )

start = time.time()
task.run()
end = time.time()
print(f"Execution time: {end - start:.2f} seconds")

