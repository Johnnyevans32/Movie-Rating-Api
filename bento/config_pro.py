import os


BASEDIR = os.path.abspath(os.path.dirname(__name__))

DEBUG = False
SECRET_KEY = "op'hdehuldu3h3u'e3ueehe;fhewfhjewfhew;fewfew;fewfefew"

if os.environ.get("DATABASE_URL") is not None:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
else:
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
        os.path.join(BASEDIR, "bento.db"))
SQLALCHEMY_TRACK_MODIFICATIONS = False
