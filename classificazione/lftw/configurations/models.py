from typing import List
import torch as th

from cinnamon.configuration import Param
from cinnamon.registry import RegistrationKey, register_class
from pyhighlights.components.models.spp.base import SPPBackbone
from pyhighlights.configurations.fr import GRUFRConfig
from pyhighlights.configurations.mcd import GRUMCDConfig

from pyhighlights.utility.losses import Loss

from pyhighlights.configurations.keys import (
    CLASSIFICATION_LOSS,
    FULL_CLASSIFICATION_LOSS,
    DISCREPANCY_LOSS,
)
from lftw.configurations.keys import (
    LFTW_BACKBONE,
    LFTW_SPARSITY_LOSS,
    LFTW_CONTIGUITY_LOSS,
    CROSS_ENTROPY_ETHNICITY_LOSS,
    FULL_CLASSIFICATION_LOSS_ETHNICITY,
    CROSS_ENTROPY_GENDER_LOSS,
    CROSS_ENTROPY_RELIGION_LOSS,
    CROSS_ENTROPY_SEXOR_LOSS,
    LFTW_ADAM,
)
from lftw.configurations.keys import (
    NAMESPACE,
)

from pyhighlights.configurations.optimizers import AdamConfig

@register_class(
    name="optimizer",
    tags={"adam", "lftw"},
    namespace=NAMESPACE,
    component="torch.optim.Adam",
)
class LFTWAdamConfig(AdamConfig):
    lr: float = Param(2e-4, gt=0.0) 
    weight_decay: float = Param(0.0, ge=0.0)


@register_class(
    name="model",
    tags={"fr", "lftw"},
    namespace=NAMESPACE,
    component="pyhighlights.components.models.spp.fr.FR",
)
class LFTWFRConfig(GRUFRConfig):
    selector_backbones: RegistrationKey[SPPBackbone] = Param(LFTW_BACKBONE)
    
    losses: List[RegistrationKey[Loss]] = Param(
        [CLASSIFICATION_LOSS, 
         LFTW_SPARSITY_LOSS, 
         #LFTW_CONTIGUITY_LOSS
         ]
    )
    optimizer: RegistrationKey[th.optim.Optimizer] = Param(LFTW_ADAM) 

@register_class(
    name="model",
    tags={"lftw", "mcd"},
    namespace=NAMESPACE,
    component="pyhighlights.components.models.spp.mcd.MCD",
)
class LFTWMCDConfig(GRUMCDConfig):
    selector_backbones: RegistrationKey[SPPBackbone] = Param(LFTW_BACKBONE)
    predictor_backbone: RegistrationKey[SPPBackbone] = Param(LFTW_BACKBONE)
    shared_losses: List[RegistrationKey[Loss]] = Param(
        [CLASSIFICATION_LOSS, LFTW_SPARSITY_LOSS]
    )
    predictor_losses: List[RegistrationKey[Loss]] = Param([FULL_CLASSIFICATION_LOSS])
    generator_losses: List[RegistrationKey[Loss]] = Param([DISCREPANCY_LOSS])

@register_class(
    name="model", tags={"fr", "lftw", "ethnicity"}, namespace=NAMESPACE,
    component="pyhighlights.components.models.spp.fr.FR",
)
class LFTWEthnicityFRConfig(LFTWFRConfig):
    losses: List[RegistrationKey[Loss]] = Param(
        [CROSS_ENTROPY_ETHNICITY_LOSS,
         LFTW_SPARSITY_LOSS,
         #LFTW_CONTIGUITY_LOSS
         ]
    )


@register_class(
    name="model", tags={"mcd", "lftw", "ethnicity"}, namespace=NAMESPACE,
    component="pyhighlights.components.models.spp.mcd.MCD",
)
class LFTWEthnicityMCDConfig(LFTWMCDConfig):
    shared_losses: List[RegistrationKey[Loss]] = Param(
        [CROSS_ENTROPY_ETHNICITY_LOSS,
         LFTW_SPARSITY_LOSS,
         #LFTW_CONTIGUITY_LOSS
         ]
    )

    predictor_losses: List[RegistrationKey[Loss]] = Param([FULL_CLASSIFICATION_LOSS_ETHNICITY])


@register_class(
    name="model", tags={"fr", "lftw", "gender"}, namespace=NAMESPACE,
    component="pyhighlights.components.models.spp.fr.FR",
)
class LFTWGenderFRConfig(LFTWFRConfig):
    losses: List[RegistrationKey[Loss]] = Param(
        [CROSS_ENTROPY_GENDER_LOSS,
         LFTW_SPARSITY_LOSS,
         ])


@register_class(
    name="model", tags={"fr", "lftw", "religion"}, namespace=NAMESPACE,
    component="pyhighlights.components.models.spp.fr.FR",
)
class LFTWReligionFRConfig(LFTWFRConfig):
    losses: List[RegistrationKey[Loss]] = Param(
        [CROSS_ENTROPY_RELIGION_LOSS,
         LFTW_SPARSITY_LOSS,
         ])


@register_class(
    name="model", tags={"fr", "lftw", "sexual_orientation"}, namespace=NAMESPACE,
    component="pyhighlights.components.models.spp.fr.FR",
)
class LFTWSexOrFRConfig(LFTWFRConfig):
    losses: List[RegistrationKey[Loss]] = Param(
        [CROSS_ENTROPY_SEXOR_LOSS,
         LFTW_SPARSITY_LOSS,
         ])