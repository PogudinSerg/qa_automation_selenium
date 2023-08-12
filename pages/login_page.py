from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Wrong login url"

    def should_be_login_form(self):
        assert self.browser.is_element_present(*LoginPageLocators.LOGIN_FORM) is True, "Login form didn't appeared"

    def should_be_register_form(self):
        assert self.browser.is_element_present(*LoginPageLocators.REGISTER_FORM) is True, \
            "Register form didn't appeared"
