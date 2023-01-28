from pathlib import Path

basedir = Path(__file__).parent.parent


class BaseConfig:
    SECTRET_KEY = "23jnidhfGIH7huyihg7HUYGUY6gyhUTUG"
    WTF_CSRF_SECRET_KEY = "aIJIS72NHUuihd8jkH79HI78UHBN8"


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFUCATIONS = False
    SQLALCHEMY_ECHO = True


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFUCATIONS = False
    WTF_CSRF_ENABLED = False


config = {"testing": TestingConfig, "local": LocalConfig}
