"""
The optimizer wrapper for PyTorch Adam.
"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: GLP-v3

from torch.optim import Adam as torch_Adam
from pypots.optim.base import Optimizer
from typing import Iterable, Tuple


class Adam(Optimizer):
    """The optimizer wrapper for PyTorch Adam.

    Parameters
    ----------
    lr : float, default=0.001,
        The learning rate of the optimizer.

    betas : Tuple[float, float], default=(0.9, 0.999),
        Coefficients used for computing running averages of gradient and its square.

    eps : float, default=1e-08,
        Term added to the denominator to improve numerical stability.

    weight_decay : float, default=0,
        Weight decay (L2 penalty).

    amsgrad : bool, default=False,
        Whether to use the AMSGrad variant of this algorithm from the paper :cite:`reddi2018OnTheConvergence`.
    """

    def __init__(
        self,
        lr: float = 0.001,
        betas: Tuple[float, float] = (0.9, 0.999),
        eps: float = 1e-08,
        weight_decay: float = 0,
        amsgrad: bool = False,
    ):
        super().__init__(lr)
        self.betas = betas
        self.eps = eps
        self.weight_decay = weight_decay
        self.amsgrad = amsgrad

    def init_optimizer(self, params: Iterable) -> None:
        """Initialize the torch optimizer wrapped by this class.

        Parameters
        ----------
        params : Iterable,
            An iterable of ``torch.Tensor`` or ``dict``. Specifies what Tensors should be optimized.
        """
        self.torch_optimizer = torch_Adam(
            params=params,
            lr=self.lr,
            betas=self.betas,
            eps=self.eps,
            weight_decay=self.weight_decay,
            amsgrad=self.amsgrad,
        )