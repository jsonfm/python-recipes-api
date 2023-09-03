from flask import Blueprint


router = Blueprint("recipes", __name__)

@router.route("/recipes")
def recipes():
    return "recipes"


@router.route("/recipe/<int:recipe_id>")
def recipe(recipe_id):
    print("recipe: ", recipe_id)
    return "recipe"


@router.route("/recipe/<int:recipe_id>", methods=["POST"])
def create_recipe():
    return "update recipe"


@router.route("/recipe/<int:recipe_id>", methods=["PUT"])
def update_recipe():
    return "update recipe!"


@router.route("/recipe/<int:recipe_id>", methods=["DELETE"])
def delete_recipe():
    return "delete recipe!"