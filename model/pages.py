from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from framework.util import configuration
from model.controls import DayForecasts, CityControl


class WeatherPage(object):
    """
    The main Page object.  Note that since this is a single page application, we don't use a
    BasePage/inheritance hierarchy.
    """
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(configuration.get_target_url())
        return self

    def wait_until_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(*Locators.CITY_INPUT))

    @property
    def city(self):
        return CityControl(self.driver, self.driver.find_element(*Locators.CITY_INPUT))

    @property
    def day_forecasts(self):
        return DayForecasts(self.driver)

    @property
    def error(self):
        return self.driver.find_element(*Locators.ERROR_MESSAGE)


class Locators(object):
    ERROR_MESSAGE = By.XPATH, "//div[@data-test='error']"
    CITY_INPUT = By.XPATH, "//input[@id='city']"
