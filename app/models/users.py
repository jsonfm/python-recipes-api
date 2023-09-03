from app import db
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255))
    is_active = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, default=db.func.now(), onupdate=db.func.now())

    # serialize options
    serialize_rules = ("-password", "-username")

    @classmethod
    def get_by_id(cls, user_id, to_dict: bool = True):
        result = cls.query.filter_by(id=user_id).first()
        if result is not None and to_dict:
            return result.to_dict()
        return result

    @classmethod
    def get_list(cls, limit: int = 20, offset: int = 0, to_dict: bool = True):
        result = cls.query.limit(limit).offset(offset).all()
        if result is not None and to_dict:
            return [user.to_dict() for user in result]
        return result

    @classmethod
    def get_by_email(cls, email: str, to_dict: bool = True):
        result = cls.query.filter_by(email=email).first()
        if result is not None and to_dict:
            return result.to_dict()
        return result 

    @classmethod
    def delete(cls, user):
        db.session.delete(user)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()
