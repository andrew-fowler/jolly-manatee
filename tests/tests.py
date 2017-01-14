from framework.util.asserts import assert_equal
from model.pages import WeatherPage


def test_page_is_accessible(driver):
    WeatherPage(driver).load()
    assert_equal(expected="5 Weather Forecast", actual=driver.title)


def test_default_city_is_glasgow(driver):
    page = WeatherPage(driver).load()
    assert_equal(expected="Glasgow", actual=page.city.text)


def test_by_default_5_rows_are_displayed(driver):
    page = WeatherPage(driver).load()
    assert_equal(expected=5, actual=page.day_forecasts.count())


def test_entering_city_displays_five_days_forecast(driver):
    # Given I load the weather page
    # When I enter a city name
    # Then 5 days are displayed

    page = WeatherPage(driver).load()
    page.city.send_keys("Edinburgh")

    # TODO: May need to wait for page to stabilise here
    assert_equal(expected=5, actual=page.day_forecasts.count())


def test_selecting_day_displays_three_hours_of_forecast(driver):
    # Given I load the weather page
    # When I select the first day
    # Then hourly forecasts are displayed

    page = WeatherPage(driver).load()

    page.day_forecasts.item(0).click()

    assert page.day_forecasts.item(0).hourly_forecasts.count() > 0


def test_deselecting_day_hides_hourly_forecast(driver):
    # Given I load the weather page
    # And I select the first day
    # And I select the first day
    # Then the hourly forecast disappears
    page = WeatherPage(driver).load()

    daily_forecast = page.day_forecasts.item(1)

    daily_forecast.click()
    daily_forecast.click()

    daily_forecast.wait_until_hourlies_hidden()

    assert_equal(expected=0, actual=daily_forecast.hourly_forecasts.count(),
                 message="Unexpectedly found hourly forecasts.")


def test_day_attributes_are_displayed_by_default(driver):
    # Given I load the weather page
    # Then each daily forecast should display condition
    # And each daily forecast should display wind speed and direction
    # And each daily forecast should display aggregate rainfall
    # And each daily forecast should display minimum and maximum temperatures

    page = WeatherPage(driver).load()

    daily_forecast = page.day_forecasts.item(1)

    assert daily_forecast.weather_icon.is_displayed(), "Weather icon not displayed"
    assert daily_forecast.wind_speed.is_displayed(), "Wind speed not displayed"
    assert daily_forecast.wind_direction_icon.is_displayed(), "Wind direction not displayed"
    assert daily_forecast.rainfall.is_displayed(), "Rainfall not displayed"
    assert daily_forecast.min_temp.is_displayed(), "Min Temp not displayed"
    assert daily_forecast.max_temp.is_displayed(), "Max Temp not displayed"


def test_specifying_unknown_city_displays_standard_error(driver):
    # Given I load the weather page
    # When I specify an unknown city value
    # Then the standard error message is displayed
    page = WeatherPage(driver).load()
    page.city.send_keys("Unknown")
    assert page.error.is_displayed(), "Error not displayed as expected"