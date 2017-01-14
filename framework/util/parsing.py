import inspect


def get_tests_from_module(class_to_inspect):
    tests = []
    for method in inspect.getmembers(class_to_inspect, predicate=inspect.isfunction):
        if str(method[0]).startswith("test_"):
            tests.append(method[1])

    return tests
