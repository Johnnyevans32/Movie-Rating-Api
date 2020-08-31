import os
from flask import Flask, render_template
from flask_restful_swagger_2 import Api
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint

from bento.models import db, ma

from .resources.create_user import CreateUser
from .resources.delete_user import DeleteUser
from .resources.list_user import ListUser
from .resources.retrieve_user import GetUser
from .resources.update_user import UpdateUser

from .resources.list_movie import ListMovie
from .resources.add_movie import AddMovie
from .resources.get_movie import GetMovies
from .resources.retrieve_movie import GetMovie
from .resources.delete_movie import DeleteMovie
from .resources.delete_movies import DeleteMovies
from .resources.update_movie import UpdateMovie

def app_factory():
    """Application factory function, instantiate configure
    and return an application instance"""
    app = Flask(__name__)

    # set swagger ui configuration
    SWAGGER_URL = "/v1/docs"
    API_URL = "/v1/docs.json"
    if os.environ.get("FLASK_ENV") == "development":
        API_URL = "/v1/docs.json"

    # Call factory function to create swaggerui blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL,
            API_URL,
            config={  # Swagger UI config overrides
                'app_name': "Movie Rating Api",
                'validatorUrl': None
            }
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    def page_not_found(e):
        return render_template("error.html", page=API_URL[:-5]), 404
    app.register_error_handler(404, page_not_found)

    # load config for development server
    # if FLASK_ENV is set to development
    # else setup app from environment variables
    if os.environ.get("FLASK_ENV") == "development":
        app.config.from_pyfile("config.py")
    else:
        app.config.from_pyfile("config_pro.py")


    # register extensions
    api = Api(
        app,
        api_version="1.0",
        api_spec_url="/v1/docs",
        title="Movie Rating Api",
        description="A micro-service for managing Movie Rating.",
        consumes=["application/json"],
        produces=["application/json"]
    )

    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)

    # register endpoints
    api.add_resource(CreateUser, '/v1/user/create')
    api.add_resource(DeleteUser, '/v1/user/delete/<string:user_id>')
    api.add_resource(ListUser, '/v1/user/all')
    api.add_resource(GetUser, '/v1/user/<string:user_id>')
    api.add_resource(UpdateUser, '/v1/user/update/<string:user_id>')

    api.add_resource(AddMovie, '/v1/movie/add')
    api.add_resource(ListMovie, '/v1/movie/all')
    api.add_resource(GetMovies, '/v1/movie/<string:user_id>')
    api.add_resource(GetMovie, '/v1/movie/<string:user_id>/<string:title>')
    api.add_resource(DeleteMovie, '/v1/movie/delete/<string:user_id>/<string:title>')
    api.add_resource(DeleteMovies, '/v1/movie/delete/<string:user_id>')
    api.add_resource(UpdateMovie, '/v1/movie/update/<string:user_id>/<string:title>/<string:rating>')

    return app


myapp = app_factory()
