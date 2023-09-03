from flask import Blueprint
from app.routers.admin.users import router as users_router


router = Blueprint("admin", __name__, url_prefix="/admin")
router.register_blueprint(users_router)