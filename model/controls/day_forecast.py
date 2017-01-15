from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from framework.util.io import output
from model.controls.hourly_forecast import Locators
from model.controls.hourly_forecasts import HourlyForecasts


class DayForecast(object):
    """
    DayForecast instances represent the individual daily rows of the weather control.
    """
    container = None
    driver = None

    def __init__(self, driver, container):
        self.driver = driver
        self.container = container

    def click(self):
        self.container.find_element(*Locators.RECORD).click()
        self.wait_until_stable()

    def wait_until_stable(self, timeout=2):
        """
        Used to block until the relevant day forecast row is visibly stable.  This is useful, as clicking a
        day forecast will cause the hourly forecasts to expand or collapse causing inconsistent behaviour.
        :param timeout: An optional timeout in seconds to wait until the control is stable.
        :return: None
        """
        WebDriverWait(self.driver, timeout)\
            .until(lambda s: self.is_stable())

    def is_stable(self):
        """
        Uses
        :return: Whether or not the control is currently visibly stable.
        """
        first_check = self.container.rect
        sleep(0.5)
        return first_check == self.container.rect

    def wait_until_hourlies_hidden(self, timeout=5):
        WebDriverWait(self.driver, timeout)\
            .until(lambda s: self.hourly_forecasts.count()==0)

    def get_sum_of_hourly_rainfall(self):
        sum = 0
        for hourly_forecast in self.hourly_forecasts.items():
            sum += int(hourly_forecast.rainfall.text.replace('mm', ''))
        return sum

    @property
    def hourly_forecasts(self):
        return HourlyForecasts(self.driver, self.container.find_element(*Locators.HOURLY_FORECAST_TABLE))

    @property
    def day(self):
        return self.container.find_element(*Locators.DAY)

    @property
    def date(self):
        return self.container.find_element(*Locators.DATE)

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
