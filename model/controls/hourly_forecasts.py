from model.controls.hourly_forecast import HourlyForecast, Locators


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

    def items(self):
        hourly_forecasts = []
        for row in self._rows:
            hourly_forecasts.append(HourlyForecast(self.driver, row))
        return hourly_forecasts

    @property
    def _rows(self):
        rows = self.container.find_elements(*Locators.HOURLY_FORECAST_ROW)
        return rows
