from pages.progress_bar import ProgressBar
import time

def test_progress_bar(browser):
    bar_page = ProgressBar(browser)
    bar_page.visit()
    time.sleep(2)
    bar_page.btn_start_stop.click()
    while True:
        if bar_page.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            bar_page.btn_start_stop.click()
            break
    time.sleep(2)
    assert bar_page.progress_bar.get_dom_attribute('aria-valuenow') == '51'
