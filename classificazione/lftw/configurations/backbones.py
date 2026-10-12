from cinnamon.configuration import Param
from cinnamon.registry import register_class
from pyhighlights.configurations.backbones import GRUBackboneConfig

from lftw.configurations.keys import (
    NAMESPACE,
)

GRU_BACKBONE_COMPONENT = (
    "pyhighlights.components.models.spp.implementations.GRUBackbone"
)


@register_class(
    name="backbone",
    tags={"lftw"},
    namespace=NAMESPACE,
    component=GRU_BACKBONE_COMPONENT,
)
class LFTWBackboneConfig(GRUBackboneConfig):
    """The baselines' encoder, embedding from the GloVe table the task reads."""

    vocab_size: int = Param(2, ge=1)
    embedding_dim: int = Param(25, ge=1)
    hidden_size: int = Param(16, ge=1)
    freeze_embeddings: bool = Param(True)
    dropout_rate: float = Param(0.0, ge=0.0, lt=1.0)