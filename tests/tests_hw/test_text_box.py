from pages.text_box import TextBox

submitted_name = 'tester'
submitted_current_address = 'some address'

def test_text_box(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    text_box_page.name.send_keys(submitted_name)
    text_box_page.current_address.send_keys(submitted_current_address)
    text_box_page.btn_submit.click()
    assert text_box_page.submitted_text.visible()
    assert text_box_page.submitted_text.get_text() == 'Name:' + submitted_name + '\nCurrent Address :' + submitted_current_address