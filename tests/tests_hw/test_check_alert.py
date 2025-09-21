from pages.alerts import Alerts
import time

def test_check_alerts(browser):
    alerts_page = Alerts(browser)
    alerts_page.visit()
    assert alerts_page.btn_timer_alert.exist()
    alerts_page.btn_timer_alert.click()
    time.sleep(5)
    assert alerts_page.alert()