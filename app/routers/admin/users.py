from flask import Blueprint, request, jsonify
from app.models.users import User


router = Blueprint("users", __name__, url_prefix="/users")


@router.route("/")
def users():
    limit = request.args.get("limit", 20)
    users = User.get_list(limit)
    response = {
        "users": users
    }
    return jsonify(response)


@router.route("/<int:user_id>", methods=["GET"])
def user(user_id: int):
    user = User.get_by_id(user_id)
    return jsonify(user)


@router.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    user = User.get_by_id(user_id, to_dict=False)
    if user is not None:
        User.delete(user)
        return "user deleted!", 200
    else:
        return "user does not exist!", 400