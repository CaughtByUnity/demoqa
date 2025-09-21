from pages.base_page import BasePage
from components.components import WebElement

class Alerts(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)
        self.btn_call_alert = WebElement(driver, '#alertButton')
        self.btn_call_confirm_alert = WebElement(driver, '#confirmButton')
        self.confirm_result = WebElement(driver, '#confirmResult')
        self.btn_call_prompt_alert = WebElement(driver, '#promptButton')
        self.prompt_result = WebElement(driver, '#promptResult')
        self.btn_timer_alert = WebElement(driver, '#timerAlertButton')