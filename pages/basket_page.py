from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def appeared_empty_message(self):
        result = self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE)
        assert result is True, "Empty message didn't appeared in the basket"

    def basket_is_empty(self):
        result = self.is_not_element_present(*BasketPageLocators.FIRST_INNER_MESSAGE)
        assert result is True, "Basket is not empty"

