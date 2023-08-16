from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        return item_name

    def get_basket_item_name(self):
        basket_item_name = self.browser.find_element(*ProductPageLocators.BASKET_ITEM_NAME).text
        return basket_item_name

    def get_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        return item_price

    def get_basket_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        return basket_price
