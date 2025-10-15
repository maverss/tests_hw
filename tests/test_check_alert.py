from pages.alerts import Alerts
import time


def test_check_timer_alerts(browser):
    alerts = Alerts(browser)
    alerts.visit()

    alerts.btn_timer_alert_button.click()
    
    time.sleep(5)

    assert alerts.alert()