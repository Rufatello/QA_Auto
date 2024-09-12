class BasePage:
    '''базовый класс для всех страниц'''
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        '''поиск одного элемента по переданным аргументам'''
        return self.browser.find_element(*args)

    def find_elements(self, args):
        '''поиск нескольких элементов по переданным аргументам'''
        return self.browser.find_elements(*args)



