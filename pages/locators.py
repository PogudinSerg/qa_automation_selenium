from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FORM = (By.ID, "id_registration-email")
    PASSWORD_FORM = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD_FORM = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-lg")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main H1")
    BASKET_ITEM_NAME = (By.CSS_SELECTOR, "#messages .alert:first-child strong")
    FIRST_INNER_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:first-child")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")


class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    FIRST_INNER_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:first-child")
