import time
from pages.accordian import AccordianPage
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQa
from pages.alerts import Alerts
import pytest

@pytest.mark.parametrize('pages', [AccordianPage, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'