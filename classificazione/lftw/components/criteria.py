import torch as th

from pyhighlights.utility.metrics import SelectionRate

class ConditionalSparsityPenalty(th.nn.Module):
    """Sparsity penalty applied only when y_true == 1"""
    def __init__(self, threshold_pos: float = 0.15, threshold_neg: float = 0.15):
        super().__init__()
        self.threshold_pos = threshold_pos
        self.threshold_neg = threshold_neg

    def forward(self, selection, mask, y_true):
        pos = (y_true.view(-1) == 1).to(selection.dtype).unsqueeze(-1)
        neg = 1.0 - pos

        denom_pos = (mask * pos).sum().clamp_min(1.0)
        denom_neg = (mask * neg).sum().clamp_min(1.0)

        rate_pos = (selection * pos).sum() / denom_pos
        rate_neg = (selection * neg).sum() / denom_neg

        loss_pos = (rate_pos - self.threshold_pos).abs()
        loss_neg = (rate_neg - self.threshold_neg).abs() 
        return loss_pos + loss_neg

class ConditionalSelectionRate(SelectionRate):
    """Selection rate calcolata solo sulle righe con y_true == target_label"""

    def __init__(self, target_label: int = 1, **kwargs):
        super().__init__(**kwargs)
        self.target_label = target_label

    def update(self, preds: th.Tensor, target: th.Tensor, y_true: th.Tensor) -> None:
        label_mask = y_true.view(-1) == self.target_label
        if not label_mask.any():
            return
        super().update(preds[label_mask], target[label_mask])

