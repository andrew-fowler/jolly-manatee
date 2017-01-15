from selenium.webdriver.common.keys import Keys


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
