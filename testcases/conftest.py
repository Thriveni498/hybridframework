import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup():
    service_obj = Service("C:/Users/Admin/Desktop/chrome driver/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    return driver




