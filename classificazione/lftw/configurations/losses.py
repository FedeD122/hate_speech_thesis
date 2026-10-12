from typing import List

import torch as th
from cinnamon.configuration import Configuration, Param
from cinnamon.registry import RegistrationKey, register_class

from pyhighlights.configurations.losses import (
    SparsityLossConfig,
    SparsityPenaltyConfig,
    ContiguityPenaltyConfig,
    ContiguityLossConfig,
)

from lftw.configurations.keys import (
    LFTW_SPARSITY,
    LFTW_CONTIGUITY,
    CROSS_ENTROPY_ETHNICITY,
    CROSS_ENTROPY_GENDER,
    CROSS_ENTROPY_RELIGION,
    CROSS_ENTROPY_SEXOR
)
from lftw.configurations.keys import (
    NAMESPACE,
)

LOSS_COMPONENT = "pyhighlights.utility.losses.Loss"


@register_class(
    name="criterion",
    tags={"lftw", "sparsity"},
    namespace=NAMESPACE,
    component="pyhighlights.utility.losses.SparsityPenalty",
)
class LFTWSparsityConfig(SparsityPenaltyConfig):
    """The share of a post the paper asks a selector to keep."""

    threshold: float = Param(0.34, ge=0.0, le=1.0) #sexual orientation
    #threshold: float = Param(0.2, ge=0.0, le=1.0) #ethnicity e religion
    #threshold: float = Param(0.25, ge=0.0, le=1.0) #gender

@register_class(
    name="criterion",
    tags={"lftw","contiguity"},
    namespace=NAMESPACE,
    component="pyhighlights.utility.losses.ContiguityPenalty",
)
class LFTWContiguityConfig(ContiguityPenaltyConfig):
    pass

@register_class(
    name="criterion", 
    tags={"cross_entropy", "ethnicity", "lftw"}, 
    namespace=NAMESPACE,
    component="pyhighlights.utility.losses.CrossEntropy",
)
class CrossEntropyEthnicityConfig(Configuration):
    weight: List[float] | None = Param([1.0, 0.68]) 
    #weight: List[float] | None = Param([1.0, 1.0]) 


@register_class(
    name="criterion", 
    tags={"cross_entropy", "gender", "lftw"}, 
    namespace=NAMESPACE,
    component="pyhighlights.utility.losses.CrossEntropy",
)
class CrossEntropyGenderConfig(Configuration):
    weight: List[float] | None = Param([1.0, 2.11])


@register_class(
    name="criterion", 
    tags={"cross_entropy", "religion", "lftw"}, 
    namespace=NAMESPACE,
    component="pyhighlights.utility.losses.CrossEntropy",
)
class CrossEntropyReligionConfig(Configuration):
    weight: List[float] | None = Param([1.0, 4.87])


@register_class(
    name="criterion", 
    tags={"cross_entropy", "sexual_orientation", "lftw"}, 
    namespace=NAMESPACE,
    component="pyhighlights.utility.losses.CrossEntropy",
)
class CrossEntropySexOrConfig(Configuration):
    weight: List[float] | None = Param([1.0, 4.89])

@register_class(
    name="loss",
    tags={"lftw", "sparsity"},
    namespace=NAMESPACE,
    component=LOSS_COMPONENT,
)
class LFTWSparsityLossConfig(SparsityLossConfig):
    loss: RegistrationKey = Param(LFTW_SPARSITY)


@register_class(
    name="loss", 
    tags={"lftw","contiguity"},
    namespace=NAMESPACE,
    component=LOSS_COMPONENT
)
class LFTWContiguityLossConfig(ContiguityLossConfig):
    loss: RegistrationKey = Param(LFTW_CONTIGUITY)
    coefficient: float = Param(1.0, ge=0.0)

@register_class(
    name="loss", 
    tags={"classification", "ethnicity", "lftw"}, 
    namespace=NAMESPACE, 
    component=LOSS_COMPONENT
)
class ClassificationLossEthnicityConfig(Configuration):
    name: str = Param("classification")
    loss: RegistrationKey[th.nn.Module] = Param(CROSS_ENTROPY_ETHNICITY)
    inputs: List[str] = Param(["class_logits", "y_true"])
    coefficient: float = Param(1.0, ge=0.0)
    enabled: bool = Param(True)

@register_class(
    name="loss",
    tags={"classification", "full", "ethnicity", "lftw"},
    namespace=NAMESPACE,
    component=LOSS_COMPONENT,
)
class FullClassificationLossEthnicityConfig(ClassificationLossEthnicityConfig):
    name: str = Param("full_classification")
    inputs: List[str] = Param(["full_class_logits", "y_true"])

@register_class(
    name="loss", 
    tags={"classification", "gender", "lftw"}, 
    namespace=NAMESPACE, 
    component=LOSS_COMPONENT
)
class ClassificationLossGenderConfig(Configuration):
    name: str = Param("classification")
    loss: RegistrationKey[th.nn.Module] = Param(CROSS_ENTROPY_GENDER)
    inputs: List[str] = Param(["class_logits", "y_true"])
    coefficient: float = Param(1.0, ge=0.0)
    enabled: bool = Param(True)

@register_class(
    name="loss", 
    tags={"classification", "religion", "lftw"}, 
    namespace=NAMESPACE, 
    component=LOSS_COMPONENT
)
class ClassificationLossReligionConfig(Configuration):
    name: str = Param("classification")
    loss: RegistrationKey[th.nn.Module] = Param(CROSS_ENTROPY_RELIGION)
    inputs: List[str] = Param(["class_logits", "y_true"])
    coefficient: float = Param(1.0, ge=0.0)
    enabled: bool = Param(True)

@register_class(
    name="loss", 
    tags={"classification", "sexual_orientation", "lftw"}, 
    namespace=NAMESPACE, 
    component=LOSS_COMPONENT
)
class ClassificationLossSexOrConfig(Configuration):
    name: str = Param("classification")
    loss: RegistrationKey[th.nn.Module] = Param(CROSS_ENTROPY_SEXOR)
    inputs: List[str] = Param(["class_logits", "y_true"])
    coefficient: float = Param(1.0, ge=0.0)
    enabled: bool = Param(True)