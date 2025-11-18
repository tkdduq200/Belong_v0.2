"""
belong.ml.config

ML 관련 공통 설정 모듈:
- DATA_PATH : 학습/예측에 사용할 CSV 위치
- MODEL_PATH : 학습된 모델(pkl) 위치
- FEATURE 목록 : 숫자형, 지역(구) 원-핫 컬럼 이름
"""

from pathlib import Path

# 이 파일이 위치한 디렉터리 (belong/ml)
ML_ROOT = Path(__file__).resolve().parent

# CSV 데이터 경로 (예: belong/ml/Dataset_ML.csv)
DATA_PATH = ML_ROOT / "Dataset_ML.csv"

# 학습된 모델(pipeline)을 저장/로드할 위치
MODEL_PATH = ML_ROOT / "lonely_death_model.pkl"

# 미래 장기예측 CSV (2026~2075)
FUTURE_PRED_PATH = ML_ROOT / "future_pred_2026_2075_v1_1_linear.csv"

# 타깃 컬럼: 고독사 발생 인원수
TARGET_COL = "값"

# 숫자형 피처 목록
NUMERIC_FEATURES = [
    "연도",
    "노령화지수",
    "1인가구_비율",
    "65세 이상",
    "소비자물가",
    "저소득노인_65~79비율",
    "저소득노인_80이상비율",
    "기초생활수급자비율",
    "lag_1",  # 전년도 고독사 수
]

# 지역(구) 원-핫 컬럼
REGION_FEATURES = [
    "강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구",
    "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구",
    "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중랑구", "중구",
]

# 파생 피처 목록 (참고용)
ADDITIONAL_FEATURES = ["lag_1", "lag_2", "roll_3", "인구x노령화", "노인비x저소득"]

# 최종 학습/예측에 투입할 컬럼
FINAL_FEATURES = NUMERIC_FEATURES + REGION_FEATURES
