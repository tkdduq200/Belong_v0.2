"""
belong.ml.data_loader

- Dataset_ML.csv 로드
- 미래 예측 CSV 로드 (2026~2075)
"""

from typing import Union
from pathlib import Path

import pandas as pd

from .config import DATA_PATH, FUTURE_PRED_PATH

PathLike = Union[str, Path]


def load_raw_data(path: PathLike = DATA_PATH) -> pd.DataFrame:
    """
    원본 CSV(Dataset_ML.csv)를 읽어서 DataFrame으로 반환.
    """
    path = Path(path)
    df = pd.read_csv(path)

    # 연도는 숫자로 맞춰두는 편이 안전함
    df["연도"] = pd.to_numeric(df["연도"], errors="coerce").astype("Int64")

    return df


def load_future_predictions(path: PathLike = FUTURE_PRED_PATH) -> pd.DataFrame:
    """
    2026~2075년 장기 예측 CSV를 로드하고 최소한의 검증까지 수행.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"미래 예측 CSV 파일을 찾을 수 없습니다: {path}"
        )

    df = pd.read_csv(path)

    required_cols = {"구", "연도", "예측값"}
    if not required_cols.issubset(df.columns):
        raise ValueError(
            f"미래 예측 CSV에 {required_cols} 컬럼이 필요합니다. "
            f"현재 컬럼: {list(df.columns)}"
        )

    df["연도"] = pd.to_numeric(df["연도"], errors="coerce").astype("Int64")

    return df
