from typing import List
from cinnamon.configuration import Configuration, Param

from lftw.configurations.keys import (
    LFTW, 
    LFTW_ETHNICITY,
    LFTW_ETHNICITY_TEST2,
    LFTW_GENDER, 
    LFTW_GENDER_TEST2,
    LFTW_RELIGION, 
    LFTW_RELIGION_TEST2,
    LFTW_SEXOR, 
    LFTW_SEXOR_TEST2,
    NAMESPACE, 
    LFTW_FR, 
    LFTW_MCD,
    LFTW_ETHNICITY_FR,
    LFTW_ETHNICITY_MCD,
    LFTW_GENDER_FR,
    LFTW_RELIGION_FR,
    LFTW_SEXOR_FR,
    LFTW_POSITIVE_METRIC,
    LFTW_NEGATIVE_METRIC

)

from cinnamon.registry import RegistrationKey, register_class
from lightning.pytorch.callbacks import Callback
from pyhighlights.components.models.base import Model
from pyhighlights.utility.metrics import BoundMetric, build_metrics
from pyhighlights.configurations.keys import (
    F1_METRIC,
    HIGHLIGHT_F1_METRIC,
    SELECTION_RATE_METRIC,
    SELECTION_SIZE_METRIC,
    LOSS_EARLY_STOPPING,
    LOSS_CHECKPOINT,
)

HIGHLIGHT_METRICS = [
    HIGHLIGHT_F1_METRIC,
    SELECTION_RATE_METRIC,
    SELECTION_SIZE_METRIC,
    LFTW_POSITIVE_METRIC,
    LFTW_NEGATIVE_METRIC
]

BINARY_METRICS = [F1_METRIC, *HIGHLIGHT_METRICS]


@register_class(
    name="task",
    tags={"lftw", "fr"},
    namespace=NAMESPACE,
    component="pyhighlights.components.tasks.SPPTask",
    run_method="run",
)
class LFTW_FR_TaskConfig(Configuration):
    
    loader: RegistrationKey = Param(LFTW)
    model: RegistrationKey[Model] = Param(LFTW_FR)
   
    embeddings: str | None = Param(None)
    vocabulary_from: str = Param("vectors")
    callbacks: List[RegistrationKey[Callback]] = Param(
        [LOSS_EARLY_STOPPING, LOSS_CHECKPOINT]
    )

    batch_size: int = Param(64, ge=1)
    save_path: str = Param("results/lftw_fr")
    seeds: list = Param([42])
    store_predictions: bool = Param(True)

    val_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    test_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)


    
    trainer_args: dict = Param({
        "accelerator": "cpu", 
        "max_epochs": 100, 
        "log_every_n_steps": 10
    })

@register_class(
    name="task",
    tags={"lftw", "mcd"},
    namespace=NAMESPACE,
    component="pyhighlights.components.tasks.SPPTask",
    run_method="run",
)
class LFTW_MCD_TaskConfig(Configuration):

    loader: RegistrationKey = Param(LFTW)
    model: RegistrationKey[Model] = Param(LFTW_MCD)
    embeddings: str | None = Param(None)
    vocabulary_from: str = Param("vectors")
    callbacks: List[RegistrationKey[Callback]] = Param(
        [LOSS_EARLY_STOPPING, LOSS_CHECKPOINT]
    )
    
    batch_size: int = Param(64, ge=1)
    save_path: str = Param("results/lftw_fr")
    seeds: list = Param([42])
    store_predictions: bool = Param(True)
    
    val_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    test_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
        
    trainer_args: dict = Param({
        "accelerator": "cpu", 
        "max_epochs": 100, 
        "log_every_n_steps": 10
    })



@register_class(
    name="task",
    tags={"lftw", "fr", "ethnicity"},
    namespace=NAMESPACE,
    component="pyhighlights.components.tasks.SPPTask",
    run_method="run",
)
class LFTW_ETHNICITY_FR_TaskConfig(Configuration):
    
    loader: RegistrationKey = Param(LFTW_ETHNICITY)
    model: RegistrationKey[Model] = Param(LFTW_ETHNICITY_FR)
   
    embeddings: str | None = Param(None)
    vocabulary_from: str = Param("vectors")
    callbacks: List[RegistrationKey[Callback]] = Param(
        [LOSS_EARLY_STOPPING, LOSS_CHECKPOINT]
    )

    batch_size: int = Param(64, ge=1)
    save_path: str = Param("results/lftw_fr")
    seeds: list = Param([42])
    store_predictions: bool = Param(True)

    val_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    test_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    
    trainer_args: dict = Param({
        "accelerator": "cpu", 
        "max_epochs": 150,
        "log_every_n_steps": 10,
    })

@register_class(
    name="task",
    tags={"lftw", "fr", "ethnicity", "test2"},
    namespace=NAMESPACE,
    component="pyhighlights.components.tasks.SPPTask",
    run_method="run",
)
class LFTW_ETHNICITY_TEST2_FR_TaskConfig(Configuration):

    loader: RegistrationKey = Param(LFTW_ETHNICITY_TEST2)
    model: RegistrationKey[Model] = Param(LFTW_ETHNICITY_FR)

    embeddings: str | None = Param(None)
    vocabulary_from: str = Param("vectors")
    callbacks: List[RegistrationKey[Callback]] = Param(
        [LOSS_EARLY_STOPPING, LOSS_CHECKPOINT]
    )

    batch_size: int = Param(64, ge=1)
    save_path: str = Param("results/lftw_fr_ethnicity_test2")
    seeds: list = Param([42])
    store_predictions: bool = Param(True)

    val_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    test_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)

    trainer_args: dict = Param({
        "accelerator": "cpu",
        "max_epochs": 100,
        "log_every_n_steps": 10,
    })

@register_class(
    name="task",
    tags={"lftw", "mcd", "ethnicity"},
    namespace=NAMESPACE,
    component="pyhighlights.components.tasks.SPPTask",
    run_method="run",
)
class LFTW_ETHNICITY_MCD_TaskConfig(Configuration): 
    loader: RegistrationKey = Param(LFTW_ETHNICITY)
    model: RegistrationKey[Model] = Param(LFTW_ETHNICITY_MCD)
   
    embeddings: str | None = Param(None)
    vocabulary_from: str = Param("vectors")
    callbacks: List[RegistrationKey[Callback]] = Param(
        [LOSS_EARLY_STOPPING, LOSS_CHECKPOINT]
    )

    batch_size: int = Param(64, ge=1)
    save_path: str = Param("results/lftw_mcd")
    seeds: list = Param([42])
    store_predictions: bool = Param(True)

    val_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    test_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    
    trainer_args: dict = Param({
        "accelerator": "cpu", 
        "max_epochs": 100,
        "log_every_n_steps": 10,
    })

@register_class(
    name="task",
    tags={"lftw", "fr", "gender"},
    namespace=NAMESPACE,
    component="pyhighlights.components.tasks.SPPTask",
    run_method="run",
)
class LFTW_GENDER_FR_TaskConfig(Configuration):
    
    loader: RegistrationKey = Param(LFTW_GENDER)
    model: RegistrationKey[Model] = Param(LFTW_GENDER_FR)
   
    embeddings: str | None = Param(None)
    vocabulary_from: str = Param("vectors")
    callbacks: List[RegistrationKey[Callback]] = Param(
        [LOSS_EARLY_STOPPING, LOSS_CHECKPOINT]
    )

    batch_size: int = Param(64, ge=1)
    save_path: str = Param("results/lftw_fr_gender")
    seeds: list = Param([42])
    store_predictions: bool = Param(True)

    val_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    test_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    
    trainer_args: dict = Param({
        "accelerator": "cpu", 
        "max_epochs": 150, 
        "log_every_n_steps": 10
    })

@register_class(
    name="task",
    tags={"lftw", "fr", "gender", "test2"},
    namespace=NAMESPACE,
    component="pyhighlights.components.tasks.SPPTask",
    run_method="run",
)
class LFTW_GENDER_TEST2_FR_TaskConfig(Configuration):

    loader: RegistrationKey = Param(LFTW_GENDER_TEST2)
    model: RegistrationKey[Model] = Param(LFTW_GENDER_FR)

    embeddings: str | None = Param(None)
    vocabulary_from: str = Param("vectors")
    callbacks: List[RegistrationKey[Callback]] = Param(
        [LOSS_EARLY_STOPPING, LOSS_CHECKPOINT]
    )

    batch_size: int = Param(64, ge=1)
    save_path: str = Param("results/lftw_fr_gender_test2")
    seeds: list = Param([42])
    store_predictions: bool = Param(True)

    val_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    test_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)

    trainer_args: dict = Param({
        "accelerator": "cpu",
        "max_epochs": 100,
        "log_every_n_steps": 10,
    })

@register_class(
    name="task",
    tags={"lftw", "fr", "religion"},
    namespace=NAMESPACE,
    component="pyhighlights.components.tasks.SPPTask",
    run_method="run",
)
class LFTW_RELIGION_FR_TaskConfig(Configuration):
    
    loader: RegistrationKey = Param(LFTW_RELIGION)
    model: RegistrationKey[Model] = Param(LFTW_RELIGION_FR)
   
    embeddings: str | None = Param(None)
    vocabulary_from: str = Param("vectors")
    callbacks: List[RegistrationKey[Callback]] = Param(
        [LOSS_EARLY_STOPPING, LOSS_CHECKPOINT]
    )

    batch_size: int = Param(64, ge=1)
    save_path: str = Param("results/lftw_fr_religion")
    seeds: list = Param([42])
    store_predictions: bool = Param(True)

    val_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    test_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    
    trainer_args: dict = Param({
        "accelerator": "cpu", 
        "max_epochs": 100, 
        "log_every_n_steps": 10
    })

@register_class(
    name="task",
    tags={"lftw", "fr", "religion", "test2"},
    namespace=NAMESPACE,
    component="pyhighlights.components.tasks.SPPTask",
    run_method="run",
)
class LFTW_RELIGION_TEST2_FR_TaskConfig(Configuration):

    loader: RegistrationKey = Param(LFTW_RELIGION_TEST2)
    model: RegistrationKey[Model] = Param(LFTW_RELIGION_FR)

    embeddings: str | None = Param(None)
    vocabulary_from: str = Param("vectors")
    callbacks: List[RegistrationKey[Callback]] = Param(
        [LOSS_EARLY_STOPPING, LOSS_CHECKPOINT]
    )

    batch_size: int = Param(64, ge=1)
    save_path: str = Param("results/lftw_fr_religion_test2")
    seeds: list = Param([42])
    store_predictions: bool = Param(True)

    val_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    test_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)

    trainer_args: dict = Param({
        "accelerator": "cpu",
        "max_epochs": 100,
        "log_every_n_steps": 10,
    })

@register_class(
    name="task",
    tags={"lftw", "fr", "sexual_orientation"},
    namespace=NAMESPACE,
    component="pyhighlights.components.tasks.SPPTask",
    run_method="run",
)
class LFTW_SEXOR_FR_TaskConfig(Configuration):
    
    loader: RegistrationKey = Param(LFTW_SEXOR)
    model: RegistrationKey[Model] = Param(LFTW_SEXOR_FR)
   
    embeddings: str | None = Param(None)
    vocabulary_from: str = Param("vectors")
    callbacks: List[RegistrationKey[Callback]] = Param(
        [LOSS_EARLY_STOPPING, LOSS_CHECKPOINT]
    )

    batch_size: int = Param(64, ge=1)
    save_path: str = Param("results/lftw_fr_sexor")
    seeds: list = Param([42])
    store_predictions: bool = Param(True)

    val_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    test_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    
    trainer_args: dict = Param({
        "accelerator": "cpu", 
        "max_epochs": 100, 
        "log_every_n_steps": 10
    })

@register_class(
    name="task",
    tags={"lftw", "fr", "sexual_orientation", "test2"},
    namespace=NAMESPACE,
    component="pyhighlights.components.tasks.SPPTask",
    run_method="run",
)
class LFTW_SEXOR_TEST2_FR_TaskConfig(Configuration):

    loader: RegistrationKey = Param(LFTW_SEXOR_TEST2)
    model: RegistrationKey[Model] = Param(LFTW_SEXOR_FR)

    embeddings: str | None = Param(None)
    vocabulary_from: str = Param("vectors")
    callbacks: List[RegistrationKey[Callback]] = Param(
        [LOSS_EARLY_STOPPING, LOSS_CHECKPOINT]
    )

    batch_size: int = Param(64, ge=1)
    save_path: str = Param("results/lftw_fr_sexor_test2")
    seeds: list = Param([42])
    store_predictions: bool = Param(True)

    val_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)
    test_metrics: List[RegistrationKey[BoundMetric]] = Param(BINARY_METRICS)

    trainer_args: dict = Param({
        "accelerator": "cpu",
        "max_epochs": 100,
        "log_every_n_steps": 10,
    })
        "accelerator": "cpu",
        "max_epochs": 100,
        "log_every_n_steps": 10,
    })
