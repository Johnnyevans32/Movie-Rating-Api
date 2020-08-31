from datetime import datetime
import hashlib
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=False, nullable=True)
    password = db.Column(db.String(255), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def encode_password(self):
        self.password = hashlib.sha1(str(self.password).encode('utf-8')).hexdigest().upper()

    def __str__(self):
        return "<Customer: {}; {} at {}>".format(self.name, self.email, self.created_at)

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    movie_tag = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return "Movies <{id}: {title}: {rating}>".format(
            id=self.id, title=self.title, rating=self.rating)

    __repr__ = __str__


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Movie

    movie = ma.Nested('MovieSchema', many=True, only=("name",))


userSchema = UserSchema()
user_schema_many = UserSchema(many=True)

movieSchema = MovieSchema()
movie_schema_many = MovieSchema(many=True)