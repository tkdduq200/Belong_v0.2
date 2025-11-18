"""
belong.ml 패키지 초기화 모듈

Service / Strategy / View 에서 자주 사용하는 함수/상수를
짧은 경로로 import 할 수 있도록 재노출한다.
"""

from .config import (
    DATA_PATH,
    MODEL_PATH,
    FUTURE_PRED_PATH,
    TARGET_COL,
    NUMERIC_FEATURES,
    REGION_FEATURES,
    ADDITIONAL_FEATURES,
    FINAL_FEATURES,
)
from .feature_builder import build_feature_dataframe
from .future_predictions import (
    get_future_curve_for_gu,
    future_available_years,
)

__all__ = [
    "DATA_PATH",
    "MODEL_PATH",
    "FUTURE_PRED_PATH",
    "TARGET_COL",
    "NUMERIC_FEATURES",
    "REGION_FEATURES",
    "ADDITIONAL_FEATURES",
    "FINAL_FEATURES",
    "build_feature_dataframe",
    "get_future_curve_for_gu",
    "future_available_years",
]
