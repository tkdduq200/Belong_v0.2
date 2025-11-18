"""
belong.ml.future_predictions

- 2026~2075년 장기 예측 결과를 다루는 헬퍼 함수 모음
"""

from typing import List, Dict, Any

import pandas as pd

from .data_loader import load_future_predictions


def get_future_curve_for_gu(gu: str) -> List[Dict[str, Any]]:
    """
    특정 구(예: '중랑구')에 대한
    2026~2075년 예측 결과를 리스트로 반환.

    반환 예:
    [
        {"구": "중랑구", "연도": 2026, "예측값": 26.5, "예측값_명": 27},
        ...
    ]
    """
    df = load_future_predictions()

    df_gu = df[df["구"] == gu].copy()
    if df_gu.empty:
        return []

    df_gu = df_gu.sort_values("연도")
    df_gu["예측값_명"] = df_gu["예측값"].round().astype(int)

    return df_gu.to_dict(orient="records")


def future_available_years() -> list[int]:
    """
    미래 예측 CSV에 들어 있는 연도 목록을 반환.
    """
    try:
        df = load_future_predictions()
    except FileNotFoundError:
        return []

    years = (
        df["연도"]
        .dropna()
        .astype(int)
        .unique()
        .tolist()
    )
    return sorted(years)
