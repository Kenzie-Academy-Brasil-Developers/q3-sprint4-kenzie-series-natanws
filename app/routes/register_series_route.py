from flask import Blueprint

from app.controllers import series_controller

bp = Blueprint("series", __name__, url_prefix="/series")

bp.post('')(series_controller.create)
bp.get('')(series_controller.series)
bp.get('/<int:serie_id>')(series_controller.select_by_id)