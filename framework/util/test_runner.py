from framework.util.parsing import get_tests_from_module
from framework.util.threading import multithread_tests
from tests import tests


def run_tests():
    multithread_tests(get_tests_from_module(tests))

