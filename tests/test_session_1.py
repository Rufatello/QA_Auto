from session.session_1 import Session1


def test_login(browser):
    simple_page = Session1(browser)
    simple_page.open()
    simple_page.login()
    simple_page.password()
    simple_page.button_click()
    simple_page.sales_click()
    simple_page.basket_click()
    assert simple_page.get_cart_item_name() == 'Sauce Labs Backpack'
    assert simple_page.get_cart_items_count() == 1


def test_by(browser):
    simple_page = Session1(browser)
    simple_page.open()
    simple_page.login()
    simple_page.password()
    simple_page.button_click()
    simple_page.sales_click()
    simple_page.basket_click()
    simple_page.checkout().click()
    simple_page.first_name()
    simple_page.last_name()
    simple_page.postal_code()
    simple_page.proceed().click()
    simple_page.finish()
    assert 'Thank you for your order!' == simple_page.compleat()
    simple_page.back()
    simple_page.basket_click()
    assert simple_page.get_cart_items_count() == 0
