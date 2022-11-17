from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_add_product_to_basket(self):
    	add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
    	add_button.click()
    	
    def correct_name_product(self):
    	assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADD_ALERT).text, "Poduct name is incorrect"
    	    
    def correct_value_in_basket(self):
    	assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*ProductPageLocators.BASKET_VALUE_MESSAGE).text, "Basket value is incorrect"
    	
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
       
    def should_be_disappeared_success_message_after_adding(self):
    	 assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is not disappeared, but should be"