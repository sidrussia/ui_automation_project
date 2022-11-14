import pytest
from selenium import webdriver
from pages.product_page import ProductPage
import time

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
