from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# Flask Extensions
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """Application Factory - 엔터프라이즈 스타일 조립 방식."""

    # ------------------------------------------------------------------
    # 1) Flask Application 인스턴스 생성
    # ------------------------------------------------------------------
    app = Flask(__name__)
    app.config.from_object(config)

    # ------------------------------------------------------------------
    # 2) DB 및 마이그레이션 초기화
    # ------------------------------------------------------------------
    db.init_app(app)
    migrate.init_app(app, db)

    # 모델 등록 (마이그레이션용)
    from . import models  # noqa: F401

    # ------------------------------------------------------------------
    # 3) 전략 / 레포지토리 / 서비스 조립 (Strategy Pattern)
    # ------------------------------------------------------------------

    # 전략: ML 모델 기반 예측 전략
    from .strategies.ml_predictor import MLPredictor
    predictor = MLPredictor()

    # 레포지토리: LonelyPrediction DB 핸들러
    from .repositories.prediction_repository import SQLPredictionRepository
    prediction_repository = SQLPredictionRepository()

    # 서비스: Predictor + Repository 조립
    from .services.prediction_service import PredictionService
    prediction_service = PredictionService(
        predictor=predictor,
        repository=prediction_repository,
    )

    # Flask app에 서비스 등록 (Service Registry 방식)
    app.prediction_service = prediction_service

    # ------------------------------------------------------------------
    # 4) Blueprint 등록
    # ------------------------------------------------------------------
    from .views import (
        main_views,
        question_views,
        answer_views,
        auth_views,
        predict_views,
    )

    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(predict_views.bp)

    # ------------------------------------------------------------------
    # 5) 디버깅용 템플릿 경로 출력
    # ------------------------------------------------------------------
    import os
    print(">>> TEMPLATE SEARCH PATH:", app.jinja_loader.searchpath)

    return app
