import os


def get_var(name):
    try:
        return os.environ[name]
    except KeyError:
        assert False, "'{}' environment variable not found.".format(name)


def execution_environment():
    return get_var('EXECUTION_ENVIRONMENT')


def saucelabs_username():
    return get_var('SAUCELABS_USERNAME')


def saucelabs_key():
    return get_var('SAUCELABS_KEY')


def saucelabs_tunnel_name():
    return get_var('SAUCELABS_TUNNEL_NAME')
