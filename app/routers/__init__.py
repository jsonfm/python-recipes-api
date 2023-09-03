from flask import Flask, Blueprint
from app.routers.auth import router as auth_router
from app.routers.recipes import router as recipes_router
from app.routers.admin import router as admin_router


router = Blueprint("api", __name__, url_prefix="/api/v1")


def apply_router(app: Flask) -> Flask:
    router.register_blueprint(auth_router)
    router.register_blueprint(recipes_router)
    router.register_blueprint(admin_router)
    app.register_blueprint(router)
    return app