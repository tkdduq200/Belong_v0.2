from typing import Dict, Any

import numpy as np

from belong.ml.config import FINAL_FEATURES, TARGET_COL
from belong.ml.feature_builder import build_feature_dataframe
from belong.ml.model_loader import load_model
from .predictor_strategy import PredictorStrategy


class MLPredictor(PredictorStrategy):
    """
    ML 모델 기반 예측 전략.
    Feature DataFrame과 모델은 최초 1회 로딩 후 캐시로 재사용.
    """

    def __init__(self):
        self._df_features = build_feature_dataframe()
        self._model = load_model()

    def predict(self, gu: str, year: int) -> float:
        row = self._df_features[
            (self._df_features["구"] == gu) &
            (self._df_features["연도"] == year)
        ]

        if row.empty:
            raise ValueError(
                f"데이터에 존재하지 않는 (구, 연도) 조합입니다: ({gu}, {year})"
            )

        X = row[FINAL_FEATURES]
        y_pred_arr = self._model.predict(X)
        y_pred = float(np.asarray(y_pred_arr)[0])

        return y_pred

    def predict_with_detail(self, gu: str, year: int) -> Dict[str, Any]:
        """
        예측값 + 실제값(y_true)까지 반환하는 확장 버전.
        """
        row = self._df_features[
            (self._df_features["구"] == gu) &
            (self._df_features["연도"] == year)
        ]

        if row.empty:
            raise ValueError(
                f"데이터에 존재하지 않는 (구, 연도) 조합입니다: ({gu}, {year})"
            )

        X = row[FINAL_FEATURES]

        y_true = None
        if TARGET_COL in row.columns:
            y_true = float(row[TARGET_COL].iloc[0])

        y_pred_arr = self._model.predict(X)
        y_pred = float(np.asarray(y_pred_arr)[0])

        return {
            "구": gu,
            "연도": int(year),
            "y_pred": y_pred,
            "y_true": y_true,
        }
