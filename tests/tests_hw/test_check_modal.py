import time

from pages.modal_dialogs import DialogsPage

def test_check_modal(browser):
    dialogs_page = DialogsPage(browser)
    dialogs_page.visit()
    assert dialogs_page.small_modal.exist()
    assert dialogs_page.large_modal.exist()
    dialogs_page.small_modal.click()
    assert dialogs_page.close_small_modal.exist()
    dialogs_page.close_small_modal.click()
    time.sleep(2)
    assert not dialogs_page.close_small_modal.exist()
    dialogs_page.large_modal.click()
    assert dialogs_page.close_large_modal.exist()
    dialogs_page.close_large_modal.click()
    time.sleep(2)
    assert not dialogs_page.close_large_modal.exist()
