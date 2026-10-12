from cinnamon.registry import RegistrationKey

NAMESPACE = "lftw"

def key(name: str, *tags: str) -> RegistrationKey:
    return RegistrationKey(name=name, tags=set(tags), namespace=NAMESPACE)

EARLY_STOPPING = key("callback", "early_stopping")
CHECKPOINT = key("callback", "checkpoint")

LFTW = key("dataset", "lftw")
LFTW_TEST2 = key("dataset", "lftw", "test2")
LFTW_ETHNICITY = key("dataset", "lftw", "ethnicity")
LFTW_ETHNICITY_TEST2 = key("dataset", "lftw", "ethnicity", "test2")
LFTW_GENDER = key("dataset", "lftw", "gender")
LFTW_GENDER_TEST2 = key("dataset", "lftw", "gender", "test2")
LFTW_RELIGION = key("dataset", "lftw", "religion")
LFTW_RELIGION_TEST2 = key("dataset", "lftw", "religion", "test2")
LFTW_SEXOR = key("dataset", "lftw", "sexual_orientation")
LFTW_SEXOR_TEST2 = key("dataset", "lftw", "sexual_orientation", "test2")

LFTW_FR_TASK = key("task", "lftw", "fr")
LFTW_MCD_TASK = key("task", "lftw", "mcd")
LFTW_ETHNICITY_FR_TASK = key("task", "lftw", "fr", "ethnicity")
LFTW_ETHNICITY_FR_TASK_TEST2 = key("task", "lftw", "fr", "ethnicity", "test2")
LFTW_GENDER_FR_TASK = key("task", "lftw", "fr", "gender")
LFTW_GENDER_FR_TASK_TEST2 = key("task", "lftw", "fr", "gender", "test2")
LFTW_RELIGION_FR_TASK = key("task", "lftw", "fr", "religion")
LFTW_RELIGION_FR_TASK_TEST2 = key("task", "lftw", "fr", "religion", "test2")
LFTW_SEXOR_FR_TASK = key("task", "lftw", "fr", "sexual_orientation")
LFTW_SEXOR_FR_TASK_TEST2 = key("task", "lftw", "fr", "sexual_orientation", "test2")
LFTW_ETHNICITY_MCD_TASK = key("task", "lftw", "mcd", "ethnicity")

LFTW_ADAM = key("optimizer", "lftw", "adam")
LFTW_BACKBONE = key("backbone", "lftw")
LFTW_FR = key("model", "fr", "lftw")
LFTW_MCD = key("model", "mcd", "lftw")
LFTW_ETHNICITY_FR = key("model", "fr", "lftw", "ethnicity")
LFTW_ETHNICITY_MCD = key("model", "mcd", "lftw", "ethnicity")
LFTW_GENDER_FR = key("model", "fr", "lftw", "gender")
LFTW_RELIGION_FR = key("model", "fr", "lftw", "religion")
LFTW_SEXOR_FR = key("model", "fr", "lftw", "sexual_orientation")

LFTW_SPARSITY = key("criterion", "sparsity", "lftw")
LFTW_CONTIGUITY = key("criterion", "contiguity", "lftw")
CROSS_ENTROPY_ETHNICITY = key("criterion", "cross_entropy", "ethnicity", "lftw")
CROSS_ENTROPY_GENDER = key("criterion", "cross_entropy", "gender", "lftw")
CROSS_ENTROPY_RELIGION = key("criterion", "cross_entropy", "religion", "lftw")
CROSS_ENTROPY_SEXOR = key("criterion", "cross_entropy", "sexual_orientation", "lftw")

LFTW_SPARSITY_LOSS = key("loss", "sparsity", "lftw")
LFTW_CONTIGUITY_LOSS = key("loss", "contiguity", "lftw")
CROSS_ENTROPY_ETHNICITY_LOSS = key("loss", "classification", "ethnicity", "lftw")
FULL_CLASSIFICATION_LOSS_ETHNICITY = key("loss", "classification", "full", "ethnicity", "lftw")
CROSS_ENTROPY_GENDER_LOSS = key("loss", "classification", "gender", "lftw")
CROSS_ENTROPY_RELIGION_LOSS = key("loss", "classification", "religion", "lftw")
CROSS_ENTROPY_SEXOR_LOSS = key("loss", "classification", "sexual_orientation", "lftw")