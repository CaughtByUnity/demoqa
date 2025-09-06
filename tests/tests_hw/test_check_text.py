from pages.demoqa import DemoQa

def test_check_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    if demo_qa_page.footer_text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.':
        return True
    else:
        return False

def test_elements_check_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    if demo_qa_page.text_elements.get_text() == 'Please select an item from left to start practice.':
        return True
    else:
        return False