from pages.tables import Tables

def test_sort(browser):
    page_tables = Tables(browser)
    page_tables.visit()
    page_tables.sort_by_first_name.click()
    assert page_tables.sort_by_first_name.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_tables.sort_by_last_name.click()
    assert page_tables.sort_by_last_name.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_tables.sort_by_age.click()
    assert page_tables.sort_by_age.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_tables.sort_by_email.click()
    assert page_tables.sort_by_email.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_tables.sort_by_salary.click()
    assert page_tables.sort_by_salary.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_tables.sort_by_department.click()
    assert page_tables.sort_by_department.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
