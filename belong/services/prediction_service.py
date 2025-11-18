from typing import List, Tuple, Optional
from datetime import datetime

from belong.models import LonelyPrediction
from belong.repositories.lonely_prediction_repository import (
    LonelyPredictionRepository,
)
from belong.strategies import PredictorStrategy
from belong.ml import build_feature_dataframe, get_future_curve_for_gu


class PredictionService:
    """
    고독사 예측 관련 비즈니스 로직 담당.
    - ML 예측 (현재년)
    - 예측 결과 DB 캐시
    - 미래(2026~2075) 예측 곡선 조회
    """

    def __init__(
        self,
        predictor: PredictorStrategy,
        prediction_repository: LonelyPredictionRepository,
    ):
        self._predictor = predictor
        self._pred_repo = prediction_repository

        # Feature DataFrame을 한 번만 생성해 캐시
        df_features = build_feature_dataframe()
        self._regions = sorted(df_features["구"].unique().tolist())
        self._years = sorted(
            df_features["연도"].dropna().astype(int).unique().tolist()
        )

    # ---------- 선택 값 조회 ----------

    def get_regions(self) -> List[str]:
        return self._regions

    def get_years(self) -> List[int]:
        return self._years

    # ---------- 현재년도 예측 ----------

    def get_or_predict(
        self, gu: str, year: int
    ) -> Tuple[Optional[LonelyPrediction], bool]:
        """
        (gu, year)에 대해
        - 이미 DB에 있으면: (record, True)
        - 없으면 ML 예측 후 저장: (record, False)
        record가 None이면 예측 실패.
        """
        existing = self._pred_repo.get_by_region_year(gu, year)
        if existing:
            return existing, True

        # Strategy를 통해 예측 수행
        y_pred = None
        y_true = None

        if hasattr(self._predictor, "predict_with_detail"):
            result = self._predictor.predict_with_detail(gu, year)  # type: ignore[arg-type]
            y_pred = result.get("y_pred")
            y_true = result.get("y_true")
        else:
            y_pred = self._predictor.predict(gu, year)

        if y_pred is None:
            return None, False

        record = LonelyPrediction(
            gu=gu,
            year=year,
            predicted_value=float(y_pred),
            actual_value=float(y_true) if y_true is not None else None,
            created_at=datetime.now(),
        )

        record = self._pred_repo.save(record)
        return record, False

    # ---------- 미래 예측 ----------

    def get_future_curve(self, gu: str):
        """
        특정 구에 대한 2026~2075년 예측 결과 리스트 반환.
        """
        return get_future_curve_for_gu(gu)
