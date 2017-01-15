from selenium.webdriver.common.by import By

from model.controls.locators import Locators


class HourlyForecast(object):
    """
    HourlyForecast instances represent the individual hourly forecast rows of the weather control.
    """
    driver = None
    container = None

    def __init__(self, driver, container):
        self.driver = driver
        self.container = container

    def click(self):
        self.container.click()

    @property
    def day(self):
        return self.container.find_element(*Locators.HOUR)

    @property
    def weather_icon(self):
        return self.container.find_element(*Locators.WEATHER_ICON)

    @property
    def max_temp(self):
        return self.container.find_element(*Locators.MAX_TEMP)

    @property
    def min_temp(self):
        return self.container.find_element(*Locators.MIN_TEMP)

    @property
    def wind_speed(self):
        return self.container.find_element(*Locators.WIND_SPEED)

    @property
    def wind_direction_icon(self):
        return self.container.find_element(*Locators.WIND_DIRECTION_ICON)

    @property
    def rainfall(self):
        return self.container.find_element(*Locators.RAINFALL)

    @property
    def pressure(self):
        return self.container.find_element(*Locators.PRESSURE)

