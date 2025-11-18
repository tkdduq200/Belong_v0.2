"""
belong.ml.model_loader

- 학습된 lonely_death_model.pkl 로딩
- lru_cache를 이용한 1회 로딩 캐싱
"""

from functools import lru_cache

import joblib

from .config import MODEL_PATH


@lru_cache(maxsize=1)
def load_model():
    """
    lonely_death_model.pkl 을 로드해서 반환.
    여러 번 호출해도 실제로는 한 번만 디스크에서 읽는다.
    """
    try:
        model = joblib.load(MODEL_PATH)
    except FileNotFoundError as exc:
        raise RuntimeError(
            f"모델 파일을 찾을 수 없습니다: {MODEL_PATH}\n"
            "먼저 학습 스크립트를 실행해 모델을 생성하세요."
        ) from exc

    return model
