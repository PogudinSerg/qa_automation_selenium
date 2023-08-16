import time
import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function")
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, "GOOgle1234!")
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_button()
        assert page.get_item_name() == page.get_basket_item_name(), "Wrong item name was added into basket"
        assert page.get_item_price() == page.get_basket_price(), "Wrong item price"

    def test_user_cant_see_success_message(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        assert page.no_success_message() is False, "Success message appeared, but shouldn't"


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    assert page.no_success_message() is False, "Success message appeared, but shouldn't"
    print("test")


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    assert page.success_message_is_disappeared() is True, "Success message disappeared"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, link)
    assert page.basket_is_empty() is True, "Basket is not empty"
    assert page.appeared_empty_message() is True, "Empty message didn't appeared in the basket"
