import os


BASEDIR = os.path.abspath(os.path.dirname(__name__))

DEBUG = True
SECRET_KEY = "op'hdehuldu3h3u'e3ue"
SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
    os.path.join(BASEDIR, "bento.db"))
SQLALCHEMY_TRACK_MODIFICATIONS = False
