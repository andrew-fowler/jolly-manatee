import traceback
from threading import Thread
from time import sleep
from framework.drivers import saucelabs, firefox
from framework.util.configuration import execution_environment
from framework.util.io import output


def run_saucelabs_test(test):
    driver = None
    session_id = None
    try:
        driver = saucelabs.get()
        session_id = driver.session_id
        output("Running test {}".format(test))

        # Do Test
        test(driver)

        output("Test Passed: {}".format(test))
    except AssertionError as e:
        if session_id is not None:
            output("Test Failed: {0} https://saucelabs.com/beta/tests/{1}/watch".format(e, session_id))

            output(driver.page_source)
    finally:
        if driver is not None:
            driver.quit()


def run_firefox_test(test):
    driver = None
    session_id = None
    try:
        driver = firefox.get()

        # Do Test
        test(driver)

        output("Test Passed: {}".format(test))
    except AssertionError as e:
        output("Test Failed: {0} - {1}".format(test, e))
        traceback.print_exc()
    except Exception as e:
        output("Test Failed: {0} - {1}".format(test, e))
        traceback.print_exc()
    finally:
        if driver is not None:
            driver.quit()


def multithread_tests(tests):
    threadpool = []

    for test in tests:
        if execution_environment() == 'saucelabs':
            threadpool.append(Thread(target=run_saucelabs_test, kwargs={'test': test}))
        elif execution_environment() == 'local':
            threadpool.append(Thread(target=run_firefox_test, kwargs={'test': test}))
    for thread in threadpool:
        thread.start()
    for thread in threadpool:
        thread.join()
#
#
# def multithread(funcs, loops, concurrency, delay=1):
#     """
#     This function is used to multithread function calls.  Each supplied function will be called loops*concurrency times.
#
#     :param funcs: An array of functions to add to the call pool
#     :param loops: The number of times to invoke the functions
#     :param concurrency: The number of threads to spread the invocations across
#     :param delay: The delay (in seconds) between each iteration
#     :return: None
#     """
#     for i in range(0, loops):
#         threadpool = []
#         for i in range(0, int(concurrency / len(funcs))):
#             for func in funcs:
#                 threadpool.append(Thread(target=func))
#         for thread in threadpool:
#             thread.start()
#         for thread in threadpool:
#             thread.join()
#         sleep(delay)
