import microblog


class Config(object):

    microblog.app.config['SQLALCHEMY_DATABASE_URI'] = (
        'postgresql://postgres@localhost/blog'
    )
    microblog.app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


class ConfigTesting(object):

    microblog.app.config['SQLALCHEMY_DATABASE_URI'] = (
        'postgresql://postgres@localhost/test'
    )
    microblog.app.config['TESTING'] = True

configs = {
    'default': Config,
    'testing': ConfigTesting,
}
