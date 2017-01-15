from selenium.webdriver.common.by import By

from model.controls.day_forecast import DayForecast


class DayForecasts(object):
    """
    This class represents the highest level container of the weather display.
    """
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def row(self, index):
        return DayForecast(self.driver, self._rows[index])

    def count(self):
        return len(self._rows)

    def item(self, index):
        return DayForecast(self.driver, self._rows[index])

    @property
    def container(self):
        return self.driver.find_element(*Locators.DAILY_FORECAST_TABLE_CONTAINER)

    @property
    def _rows(self):
        return self.container.find_elements(*Locators.DAILY_FORECAST_ROW_CONTAINER)


class Locators(object):

    DAILY_FORECAST_TABLE_CONTAINER = By.XPATH, "//div[@id='root']/div"
    DAILY_FORECAST_ROW_CONTAINER = By.XPATH, "//div[@style='padding-bottom: 20px;']"  # Note: this is a terrible locator, but there are no additional attributes
