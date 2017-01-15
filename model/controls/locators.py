from selenium.webdriver.common.by import By

class Locators(object):

    HOURLY_FORECAST_TABLE = By.XPATH, "//div[@class='details']"
    HOURLY_FORECAST_ROW = By.XPATH, ".//div[@class='detail']"
    HOUR = By.XPATH, "//span[@class='hour']"

    RECORD = By.XPATH, ".//span[@class='cell']"

    PRESSURE = By.XPATH, ".//span[contains(@data-test,'pressure')]"
    RAINFALL = By.XPATH, ".//span[@class='rainfall']"
    WIND_DIRECTION_ICON = By.XPATH, ".//span[contains(@data-test, 'direction')]"
    WIND_SPEED = By.XPATH, ".//span[@class='speed']"
    MIN_TEMP = By.XPATH, ".//span[contains(@data-test,'minimum')]"
    MAX_TEMP = By.XPATH, ".//span[@class='max']"
    WEATHER_ICON = By.XPATH, ".//*[name()='svg' and contains(@data-test,'description')]"
    DATE = By.XPATH, ".//span[contains(@data-test,'date')]"
    DAY = By.XPATH, ".//span[contains(@data-test,'day')]"