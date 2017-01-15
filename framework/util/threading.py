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

        test(driver)

        output("Test Passed: {}".format(test))
    except AssertionError as e:
        if session_id is not None:
            output("Test Failed: {0} {1} https://saucelabs.com/beta/tests/{1}/watch".format(test, e, session_id))
    except Exception as e:
        output("Test Failed: {0} - {1}".format(test, e))
        traceback.print_exc()
    finally:
        if driver is not None:
            driver.quit()


def run_firefox_test(test):
    driver = None

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