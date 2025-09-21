from pages.tables import Tables
import time
from selenium.webdriver.common.keys import Keys

# def test_tables_rows(browser):
#     page_tables = Tables(browser)
#     page_tables.visit()
#     # Check that submitting empty form does not work by clicking "submit" after clicking "add"
#     page_tables.btn_add.click()
#     page_tables.btn_reg_form_submit.click()
#     assert page_tables.btn_reg_form_submit.visible()
#     page_tables.btn_reg_form_close.click()
#     time.sleep(2)
#     # filling the form and checking that reg form closes and we have a new row in table
#     page_tables.btn_add.click()
#     page_tables.inp_reg_form_first_name.send_keys('tester')
#     page_tables.inp_reg_form_last_name.send_keys('testerovich')
#     page_tables.inp_reg_form_user_email.send_keys('tester@ttt.tt')
#     page_tables.inp_reg_form_age.send_keys('27')
#     page_tables.inp_reg_form_salary.send_keys('5000')
#     page_tables.inp_reg_form_department.send_keys('QA')
#     page_tables.btn_reg_form_submit.click()
#     time.sleep(2)
#     assert not page_tables.btn_reg_form_submit.exist()
#     assert page_tables.new_row_first_name.get_text() == 'tester'
#     # checking 'Edit' button
#     time.sleep(2)
#     page_tables.btn_edit.click()
#     # checking that 'Edit' shows filled reg form
#     assert page_tables.inp_reg_form_first_name.get_dom_attribute('value') == 'Cierra'
#     # change first name and check if row in table update
#     page_tables.inp_reg_form_first_name.clear()
#     page_tables.inp_reg_form_first_name.send_keys('Francesca')
#     page_tables.btn_reg_form_submit.click()
#     assert page_tables.old_row_first_name.get_text() == 'Francesca'
#     # check 'Delete' button (delete row)
#     page_tables.btn_delete_row.click()
#     assert page_tables.old_row_first_name.get_text() == 'Alden'

def test_tables_navigation(browser):
    # Предусловия
    page_tables = Tables(browser)
    page_tables.visit()
    page_tables.rows_select.click()
    page_tables.rows_select.send_keys(Keys.PAGE_UP)
    page_tables.rows_select.send_keys(Keys.ENTER)
    time.sleep(2)
    assert page_tables.rows_visible_5.visible()

    # test case
    # 1 check next and previous buttons are locked
    assert page_tables.btn_previous.get_dom_attribute('disabled')
    assert page_tables.btn_next.get_dom_attribute('disabled')
    # 2 add 3 rows
    for i in range(3):
        page_tables.btn_add.click()
        page_tables.inp_reg_form_first_name.send_keys('tester')
        page_tables.inp_reg_form_last_name.send_keys('testerovich')
        page_tables.inp_reg_form_user_email.send_keys('tester@ttt.tt')
        page_tables.inp_reg_form_age.send_keys('27')
        page_tables.inp_reg_form_salary.send_keys('5000')
        page_tables.inp_reg_form_department.send_keys('QA')
        page_tables.btn_reg_form_submit.click()
        time.sleep(2)
    # check that now we have 2 pages instead of 1
    assert page_tables.total_pages.get_text() == '2'
    page_tables.btn_next.click()
    assert page_tables.current_page.get_dom_attribute('value') == '2'
    page_tables.btn_previous.click()
    assert page_tables.current_page.get_dom_attribute('value') == '1'


