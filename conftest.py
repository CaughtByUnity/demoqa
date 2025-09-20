import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def browser():
    service = Service('/home/caughtbyunity/PycharmProjects/demoqa/chromedriver')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.set_window_size(1000, 1000)
    driver.quit()