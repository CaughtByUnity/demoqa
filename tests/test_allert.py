from pages.alerts import Alerts
import time

def test_allert(browser):
    allerts_page = Alerts(browser)
    allerts_page.visit()
    assert not allerts_page.alert()
    allerts_page.btn_call_alert.click()
    time.sleep(2)
    assert allerts_page.alert()

def test_alert_text(browser):
    allerts_page = Alerts(browser)
    allerts_page.visit()
    allerts_page.btn_call_alert.click()
    time.sleep(2)
    assert allerts_page.alert().text == 'You clicked a button'
    allerts_page.alert().accept()
    assert not allerts_page.alert()

def test_confirm(browser):
    allerts_page = Alerts(browser)
    allerts_page.visit()
    allerts_page.btn_call_confirm_alert.click()
    time.sleep(2)
    allerts_page.alert().dismiss()
    assert allerts_page.confirm_result.get_text() == 'You selected Cancel'

def test_prompt(browser):
    allerts_page = Alerts(browser)
    name = 'Dima'
    allerts_page.visit()
    allerts_page.btn_call_prompt_alert.click()
    time.sleep(2)
    allerts_page.alert().send_keys(name)
    allerts_page.alert().accept()
    assert allerts_page.prompt_result.get_text() == f'You entered { name }'