import pytest
from selenium import webdriver
from pages.product_page import ProductPage
import time
from pages.basket_page import BasketPage


'''
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail(reason="fixing this bug")), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):   # item can add to basket
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()
    #time.sleep(2)
    page.solve_quiz_and_get_code()
    page.correct_name_product()
    page.correct_value_in_basket()
'''  
    
@pytest.mark.xfail(reason="product correct added to basket with message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): # there is no success massage after adding product to basket
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser): # there is no success massage after open product page
     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
     page = ProductPage(browser, link)
     page.open()
     page.should_not_be_success_message()
         
@pytest.mark.xfail(reason="disappearing of alert is not realized yet")
def test_message_disappeared_after_adding_product_to_basket(browser): # success message is disappearing?
     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/" 
     page = ProductPage(browser, link, 0)
     page.open()
     page.should_be_add_product_to_basket()
     time.sleep(4)
     page.should_be_disappeared_success_message_after_adding()
     
def test_guest_should_see_login_link_on_product_page(browser): # login link is on page
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser): # go to login link is ok
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket()
 
@pytest.mark.xfail(reason="basket is empty - OK")   
def test_guest_cant_see_basket_empty_message_after_adding_product(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    page = BasketPage(browser, link)
    page.open()
    #page.should_be_add_product_to_basket()
    page.go_to_basket_page()
    page.should_be_no_empty_basket_message()
    