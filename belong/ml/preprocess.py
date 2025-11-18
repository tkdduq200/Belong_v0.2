"""
belong.ml.preprocess

기존 노트북에서 사용하던 인터페이스를 유지하기 위한 래퍼 모듈.
실제 구현은 feature_builder.py 에 있다.
"""

from typing import Union
from pathlib import Path

import pandas as pd

from .feature_builder import (
    add_engineered_features,
    build_feature_dataframe,
)
from .data_loader import load_raw_data

PathLike = Union[str, Path]

__all__ = [
    "load_raw_data",
    "add_engineered_features",
    "build_feature_dataframe",
]
