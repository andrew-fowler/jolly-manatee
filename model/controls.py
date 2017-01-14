from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait


class CityControl(object):
    """
    CityControl encapsulates the City input.  As it doesn't behave as a normal text input we encapsulate it,
    to abstract away complexity from the consumer
    """
    driver = None
    container = None

    def __init__(self, driver, container):
        self.driver = driver
        self.container = container

    def send_keys(self, text):
        """
        Due to the nature of the control, users have to manually delete a displayed entry, enter the new
        value and hit Return.  To avoid significant duplication in the test script, we encapsulate it.
        :param text: The text to enter into the City input.
        :return: None
        """
        self.container.clear()
        self.container.send_keys(text)
        self.container.send_keys(Keys.RETURN)

    @property
    def text(self):
        """
        The City control has no 'text' in the normal sense.  So, we expose it as a text property to preserve
        uniformity.
        :return: The visibly rendered text.
        """
        return self.container.get_attribute("value")


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
        self.container.click()
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


class HourlyForecasts(object):
    """
    HourlyForecasts is the container for the individual HourlyForecast instances.
    """
    driver = None
    container = None

    def __init__(self, driver, container):
        self.driver = driver
        self.container = container

    def count(self):
        return sum(hourly_forecast.is_displayed() for hourly_forecast in self._rows)

    def item(self, index):
        return HourlyForecast(self.driver, self._rows[index])

    @property
    def _rows(self):
        return self.container.find_elements(*Locators.HOURLY_FORECAST_ROW)


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

    def day(self):
        return self.container.find_element(*Locators.HOUR)

    def weather_icon(self):
        return self.container.find_element(*Locators.WEATHER_ICON)

    def max_temp(self):
        return self.container.find_element(*Locators.MAX_TEMP)

    def min_temp(self):
        return self.container.find_element(*Locators.MIN_TEMP)

    def wind_speed(self):
        return self.container.find_element(*Locators.WIND_SPEED)

    def wind_direction_icon(self):
        return self.container.find_element(*Locators.WIND_DIRECTION_ICON)

    def rainfall(self):
        return self.container.find_element(*Locators.RAINFALL)

    def pressure(self):
        return self.container.find_element(*Locators.PRESSURE)


class Locators(object):
    # TODO: Note: To index - (//xpath)[1]

    DAILY_FORECAST_TABLE_CONTAINER = By.XPATH, "//div[@id='root']/div"
    DAILY_FORECAST_ROW_CONTAINER = By.XPATH, "//div[@style='padding-bottom: 20px;']"  # Note: this is a terrible locator, but there are no additional attributes

    HOURLY_FORECAST_TABLE = By.XPATH, "//div[@class='details']"
    HOURLY_FORECAST_ROW = By.XPATH, ".//div[@class='detail']"
    HOUR = By.XPATH, "//span[@class='hour']"

    PRESSURE = By.XPATH, "//span[contains(@data-test,'pressure')]"
    RAINFALL = By.XPATH, "//span[@class='rainfall']"
    WIND_DIRECTION_ICON = By.XPATH, "//span[contains(@data-test, 'direction')]"
    WIND_SPEED = By.XPATH, "//span[@class='speed']"
    MIN_TEMP = By.XPATH, "//span[contains(@data-test,'minimum')]"
    MAX_TEMP = By.XPATH, "//span[@class='max']"
    WEATHER_ICON = By.XPATH, "//*[name()='svg' and contains(@data-test,'description')]"
    DATE = By.XPATH, "//span[contains(@data-test,'date')]"
    DAY = By.XPATH, "//span[contains(@data-test,'day')]"
