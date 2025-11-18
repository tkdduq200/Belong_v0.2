"""
belong.ml.feature_builder

- Dataset_ML.csv + 피처 엔지니어링을 수행하여
  학습/예측에 사용 가능한 Feature DataFrame 생성
"""

from typing import Union
from pathlib import Path

import pandas as pd

from .config import DATA_PATH, TARGET_COL
from .data_loader import load_raw_data

PathLike = Union[str, Path]


def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    v0.4 노트북에서 했던 피처 엔지니어링 적용:

    - 구, 연도 기준 정렬
    - lag_1, lag_2 : 전년도 / 재작년 고독사 수
    - roll_3       : 3년 이동평균
    - 인구x노령화   : 총인구 × 노령화지수
    - 노인비x저소득 : 65세 이상 × 저소득노인_80이상비율
    """
    df = df.copy()

    # 정렬
    df = df.sort_values(["구", "연도"])

    # 그룹별 타깃 기준 lag 생성
    df["lag_1"] = df.groupby("구")[TARGET_COL].shift(1)
    df["lag_2"] = df.groupby("구")[TARGET_COL].shift(2)

    # 3년 이동평균
    roll = df.groupby("구")[TARGET_COL].apply(lambda x: x.rolling(3).mean())
    roll = roll.reset_index(level=0, drop=True)
    df["roll_3"] = roll

    # 파생 피처: 인구x노령화
    if "총인구" in df.columns and "노령화지수" in df.columns:
        df["인구x노령화"] = df["총인구"] * df["노령화지수"]

    # 파생 피처: 노인비x저소득
    if "65세 이상" in df.columns and "저소득노인_80이상비율" in df.columns:
        df["노인비x저소득"] = (
            df["65세 이상"] * df["저소득노인_80이상비율"]
        )

    # lag/roll 계산 때문에 앞부분 연도에 NaN이 생김 → 해당 행 제거
    df = df.dropna(subset=["lag_1", "lag_2", "roll_3"]).reset_index(drop=True)

    return df


def build_feature_dataframe(path: PathLike = DATA_PATH) -> pd.DataFrame:
    """
    CSV 로드 + 피처 엔지니어링까지 한 번에 수행하여
    학습/예측에 바로 쓸 수 있는 DataFrame을 반환.
    """
    df = load_raw_data(path)
    df = add_engineered_features(df)
    return df
