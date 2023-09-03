from flask import Flask, Blueprint
from app.routers.recipes import router as recipes_router


router = Blueprint("api", __name__, url_prefix="/api/v1")


def apply_router(app: Flask) -> Flask:
    router.register_blueprint(recipes_router)
    app.register_blueprint(router)
    return app