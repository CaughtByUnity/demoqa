from pages.modal_dialogs import DialogsPage
from pages.demoqa import DemoQa

def test_modal_elements(browser):
    dialogs_page = DialogsPage(browser)
    dialogs_page.visit()
    assert dialogs_page.btns_third_menu.check_count_elements(count = 5)

def test_navigation_modal(browser):
    dialogs_page = DialogsPage(browser)
    demoqa_page = DemoQa(browser)
    dialogs_page.visit()
    dialogs_page.refresh()
    dialogs_page.btn_header_icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demoqa_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
