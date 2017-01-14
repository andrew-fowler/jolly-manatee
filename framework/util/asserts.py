def assert_equal(expected, actual, message=""):
    if expected != actual:
        message = "Equality failure.  Expected: '{0}' Actual: '{1}'".format(expected, actual)
        raise AssertionError(message)