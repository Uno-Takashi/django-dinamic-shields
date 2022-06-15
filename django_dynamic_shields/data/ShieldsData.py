from typing import Optional

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
from dataclasses import dataclass, asdict
import json


@dataclass
class ShieldsData:
    label: str
    message: str
    color: str = "lightgrey"
    labelColor: str = "grey"
    isError: bool = False
    namedLogo: Optional[str] = None
    logoSvg: Optional[str] = None
    logoColor: Optional[str] = None
    logoWidth: Optional[str] = None
    logoPosition: Optional[str] = None
    style: Literal["flat", "plastic", "flat-square", "for-the-badge", "social"] = "flat"
    cacheSeconds: Optional[int] = None

    @property
    def dict(self):
        data: dict = asdict(self)
        data = {key: value for key, value in data.items() if value is not None}
        return data
