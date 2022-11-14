from pages.main_page import MainPage
from pages.login_page import LoginPage 
import pytest
from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

def test_guest_can_go_to_login_page(browser):   # login link is presented
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                                                        # открываем страницу
    page.go_to_login_page()                         
    login_page = LoginPage(browser, browser.current_url)      # выполняем метод страницы - переходим на страницу логина
    login_page.should_be_login_page()
    

def test_guest_should_see_login_link(browser):   # link for login/register is here
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_should_see_login_form(browser):      # form for login is here
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    
def test_guest_should_see_register_form(browser):    # form for register is here
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    
def test_guest_should_be_login_url(browser):     # URL contains "login"
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page. should_be_login_url()
    