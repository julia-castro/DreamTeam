class Config(object):
  print('config object')
  #put any configurations here that are common across all environments

class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
  DEBUG = False


app_config = {
  'development': DevelopmentConfig,
  'production': ProductionConfig
}