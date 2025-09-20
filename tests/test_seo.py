from pages.demoqa import DemoQa
# from pages.elements_page import WebElement

def test_check_title_demo(browser):
    demoqa_page = DemoQa(browser)
    demoqa_page.visit()
    assert browser.title == 'DEMOQA'