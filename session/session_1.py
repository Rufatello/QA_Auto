from selenium.webdriver.common.by import By

from session.base_page import BasePage

# локаторы
login = (By.ID, 'user-name')
password = (By.ID, 'password')
button = (By.ID, 'login-button')
sales = (By.ID, 'add-to-cart-sauce-labs-backpack')
basket = (By.CLASS_NAME, 'shopping_cart_link')
cart_item_name = (By.CLASS_NAME, 'inventory_item_name')
checkout = (By.ID, 'checkout')
first_name = (By.ID, 'first-name')
last_name = (By.ID, 'last-name')
postal_code = (By.ID, 'postal-code')
proceed = (By.ID, 'continue')
finish = (By.ID, 'finish')
compleat = (By.CLASS_NAME, 'complete-header')
back = (By.ID, 'back-to-products')
cart_items = (By.CLASS_NAME, 'cart_item')


class Session1(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        '''метод открытия ссылки'''
        self.browser.get('https://www.saucedemo.com')

    def login(self):
        '''метод для ввода логина'''
        login_field = self.find(login)
        login_field.send_keys('standard_user')

    def password(self):
        '''метод для ввода пароля'''
        password_field = self.find(password)
        password_field.send_keys('secret_sauce')

    def button_click(self):
        '''метод для нажатия кнопки: "Loпin"'''
        return self.find(button).click()

    def sales_click(self):
        '''метод для нажатия кнопки: "add to cart"'''
        return self.find(sales).click()

    def basket_click(self):
        '''метод для нажатия кнопки карзины'''
        return self.find(basket).click()

    def get_cart_item_name(self):
        '''метод возвращает названия элемента корзины'''
        return self.find(cart_item_name).text

    def checkout(self):
        '''метод для нажатия кнопки: "checkout"'''
        return self.find(checkout)

    def first_name(self):
        '''метод для ввода имени'''
        name_field = self.find(first_name)
        name_field.send_keys('123')

    def last_name(self):
        '''метод для ввода фамилии'''
        last_name_field = self.find(last_name)
        last_name_field.send_keys('123')

    def postal_code(self):
        '''метод для воода карты'''
        postal_code_field = self.find(postal_code)
        postal_code_field.send_keys('123')

    def proceed(self):
        '''метод для нажатия кнопки: "compleat"'''
        return self.find(proceed)

    def finish(self):
        '''метод для нажатия кнопки: "finish"'''
        return self.find(finish).click()

    def compleat(self):
        '''метод возвращает текст на экране об успешной покупке'''
        return self.find(compleat).text

    def back(self):
        '''метод для нажатия кнопки: "back"'''
        return self.find(back).click()

    def get_cart_items_count(self):
        '''метод считает количество элементов в корзине'''
        return len(self.browser.find_elements(*cart_items))
