from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_NAME = (By.XPATH, "//h1")
    PRODUCT_NAME_ADD_ALERT = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']") 
    BASKET_VALUE_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]")
    
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SEE_BASKET_PAGE = (By.XPATH, "//a[@class='btn btn-default']")
    
    
class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//*[contains(text(), 'basket is empty')]")