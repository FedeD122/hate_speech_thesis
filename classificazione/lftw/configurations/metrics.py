from typing import Sequence

from cinnamon.configuration import Configuration, Param
from cinnamon.registry import register_class, RegistrationKey

from lftw.configurations.keys import (
    NAMESPACE,
    LFTW_POSITIVE,
    LFTW_NEGATIVE
)

from torchmetrics import Metric

from pyhighlights.configurations.metrics import HighlightF1MetricConfig


@register_class(
    name="torchmetric",
    tags={"lftw", "selection_rate_pos"},
    namespace=NAMESPACE,
    component="lftw.components.criteria.ConditionalSelectionRate",
)
class SelectionRatePositiveConfig(Configuration):
    target_label: int = Param(1)


@register_class(
    name="torchmetric",
    tags={"lftw", "selection_rate_neg"},
    namespace=NAMESPACE,
    component="lftw.components.criteria.ConditionalSelectionRate",
)
class SelectionRateNegativeConfig(Configuration):
    target_label: int = Param(0)

@register_class(
    name="metric",
    tags={"lftw", "selection_rate_pos"},
    namespace=NAMESPACE,
    component="pyhighlights.utility.metrics.BoundMetric",
)
class ConditionalSelectionRateMetricConfigPos(HighlightF1MetricConfig):

    name: str = Param("selection_rate_pos")
    metric: RegistrationKey[Metric] = Param(LFTW_POSITIVE)
    inputs: Sequence[str] = Param(["highlight_mask", "mask", "y_true"])

@register_class(
    name="metric",
    tags={"lftw", "selection_rate_neg"},
    namespace=NAMESPACE,
    component="pyhighlights.utility.metrics.BoundMetric",
)
class ConditionalSelectionRateMetricConfigNeg(HighlightF1MetricConfig):

    name: str = Param("selection_rate_neg")
    metric: RegistrationKey[Metric] = Param(LFTW_NEGATIVE)
    inputs: Sequence[str] = Param(["highlight_mask", "mask", "y_true"])