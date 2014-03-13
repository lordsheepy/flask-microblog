

class Config(object):

    SQLALCHEMY_DATABASE_URI = 'postgresql://bloguser:bloguser@localhost/blog'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class ConfigTesting(object):

    SQLALCHEMY_DATABASE_URI = 'postgresql://bloguser:bloguser@localhost/test'
    TESTING = True


class TravisTesting(object):

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost/test'
    TESTING = True


configs = {
    'default': Config,
    'testing': ConfigTesting,
    'travis': TravisTesting,
}
