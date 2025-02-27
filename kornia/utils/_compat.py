from typing import TYPE_CHECKING, List, Optional, Tuple

import torch
from torch import Tensor

from packaging import version


def torch_version() -> str:
    """Parse the `torch.__version__` variable and removes +cu*/cpu."""
    return torch.__version__.split('+')[0]


# TODO: replace by torch_version_ge``
def torch_version_geq(major, minor) -> bool:
    _version = version.parse(torch_version())
    return _version >= version.parse(f"{major}.{minor}")


def torch_version_lt(major: int, minor: int, patch: int) -> bool:
    _version = version.parse(torch_version())
    return _version < version.parse(f"{major}.{minor}.{patch}")


def torch_version_le(major: int, minor: int, patch: int) -> bool:
    _version = version.parse(torch_version())
    return _version <= version.parse(f"{major}.{minor}.{patch}")


def torch_version_ge(major: int, minor: int, patch: int) -> bool:
    _version = version.parse(torch_version())
    return _version >= version.parse(f"{major}.{minor}.{patch}")


if version.parse(torch_version()) > version.parse("1.7.1"):
    from torch.linalg import qr as linalg_qr
else:
    from torch import qr as linalg_qr  # noqa: F401


if torch_version_ge(1, 10, 0):

    if not TYPE_CHECKING:

        def torch_meshgrid(tensors: List[Tensor], indexing: str):
            return torch.meshgrid(tensors, indexing=indexing)

else:

    if TYPE_CHECKING:

        def torch_meshgrid(tensors: List[Tensor], indexing: Optional[str] = None) -> Tuple[Tensor, ...]:
            return torch.meshgrid(tensors)

    else:

        def torch_meshgrid(tensors: List[Tensor], indexing: str):
            return torch.meshgrid(tensors)


if torch_version_ge(1, 10, 0):
    torch_inference_mode = torch.inference_mode
else:
    torch_inference_mode = torch.no_grad
