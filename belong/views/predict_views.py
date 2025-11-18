from flask import Blueprint, render_template, request, flash
from werkzeug.utils import redirect

from ..services import PredictionService
from ..repositories.lonely_prediction_repository import LonelyPredictionRepository
from ..strategies import MLPredictor

bp = Blueprint("predict", __name__, url_prefix="/predict")

_prediction_service = PredictionService(
    predictor=MLPredictor(),
    prediction_repository=LonelyPredictionRepository(),
)


# ==========================================
# 1) 현재년도 예측 (ML 모델)
# ==========================================

@bp.route("/", methods=("GET", "POST"))
def index():
    """
    /predict/ - ML 기반 고독사 예측
    """
    regions = _prediction_service.get_regions()
    years = _prediction_service.get_years()

    prediction = None
    from_cache = False

    if request.method == "POST":
        gu = request.form.get("gu")
        year_raw = request.form.get("year")

        if not gu or not year_raw:
            flash("구와 연도를 모두 선택해 주세요.")
        else:
            try:
                year = int(year_raw)
            except ValueError:
                flash("연도 값이 올바르지 않습니다.")
                return render_template(
                    "predict/form.html",
                    regions=regions,
                    years=years,
                    prediction=None,
                    from_cache=False,
                )

            prediction, from_cache = _prediction_service.get_or_predict(gu, year)

    return render_template(
        "predict/form.html",
        regions=regions,
        years=years,
        prediction=prediction,
        from_cache=from_cache,
    )


# ==========================================
# 2) 미래 예측 (2026~2075 CSV 기반)
# ==========================================

@bp.route("/future", methods=["GET", "POST"])
def future():
    """
    2026~2075년 장기 예측 서비스 전용 뷰
    - 연도 선택 없음
    - 구 선택만 존재
    """
    gu_list = _prediction_service.get_regions()
    selected_gu = gu_list[0] if gu_list else None

    if request.method == "POST":
        selected_gu = request.form.get("gu") or selected_gu

    records = []
    if selected_gu:
        records = _prediction_service.get_future_curve(selected_gu)

    return render_template(
        "predict/future_predict.html",
        gu_list=gu_list,
        selected_gu=selected_gu,
        records=records,
    )
