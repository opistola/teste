

class Config(object):
    CENAS = "production"

class TestingConfig(Config):
    DEBUG = True
    ENV = "testing"
    


app_config = {
    "production": Config,
    "testing": TestingConfig
}