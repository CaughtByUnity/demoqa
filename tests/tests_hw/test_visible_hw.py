from pages.accordian import AccordianPage
import time

def test_visible_accordian(browser):
    accordian_page = AccordianPage(browser)
    accordian_page.visit()
    assert accordian_page.section_1_content.visible()
    accordian_page.section_1_heading.click()
    time.sleep(2)
    assert not accordian_page.section_1_content.visible()

def test_visible_accordian_default(browser):
    accordian_page = AccordianPage(browser)
    accordian_page.visit()
    assert not accordian_page.section_2_content_1.visible()
    assert not accordian_page.section_2_content_2.visible()
    assert not accordian_page.section_3_content.visible()

