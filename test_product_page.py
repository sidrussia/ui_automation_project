import pytest
from selenium import webdriver
from pages.product_page import ProductPage
#import time

def test_guest_can_add_product_to_basket(browser):   # item can add to basket
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()
    page.solve_quiz_and_get_code()
    #time.sleep(1)
    page.correct_name_product()
    page.correct_value_in_basket()
