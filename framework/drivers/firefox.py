# TODO: Implement local Firefox driver
from selenium import webdriver


def get():
    return webdriver.Firefox(executable_path="./framework/drivers/binaries/geckodriver")