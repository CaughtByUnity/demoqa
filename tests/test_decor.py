import pytest
from pages.demoqa import DemoQa
from pages.radio_button import Radio

@pytest.mark.smoke
def test_decor(browser):
    decor_page = DemoQa(browser)
    decor_page.visit()
    assert decor_page.header_5.check_count_elements(6)
    for element in decor_page.header_5.find_elements():
        assert element.text != ''

@pytest.mark.regress
def test_decor_radio(browser):
    radio_page = Radio(browser)
    radio_page.visit()
    radio_page.btn_yes.click_force()
    assert radio_page.text.get_text() == 'You have selected Yes'
    radio_page.btn_impressive.click_force()
    assert radio_page.text.get_text() == 'You have selected Impressive'
    assert 'disabled' in radio_page.btn_no.get_dom_attribute('class')