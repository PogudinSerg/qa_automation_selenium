from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def item_name_equal_basket_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        basket_item_name = self.browser.find_element(*ProductPageLocators.BASKET_ITEM_NAME).text
        assert item_name == basket_item_name, "Wrong item name was added into basket"

    def item_price_equal_basket_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert item_price == basket_price, "Wrong item price"

    def no_success_message_appeared(self):
        result = self.is_element_present(*ProductPageLocators.FIRST_INNER_MESSAGE)
        assert result is True, "Success message appeared, but shouldn't"

    def success_message_is_disappeared(self):
        result = self.is_disappeared(*ProductPageLocators.FIRST_INNER_MESSAGE)
        assert result is False, "Success message disappeared"
