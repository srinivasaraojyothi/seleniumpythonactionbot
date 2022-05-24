from behave import given, when, then
from behave import *
from selenium.webdriver.common.keys import Keys

from homePageObj import homePageObj
@given(u"user on google page")
def step_impl3(context):
    page=homePageObj(context.browser)
    page.searchinGoogle("https://www.google.com/")
    #context.browser.get("https://www.google.com/")
    print("i am on google-----0")
@when(u"he enters string to search")    
def step_impl2(context):
    page=homePageObj(context.browser)
    page.googleSearch()
    #context.browser.find_element_by_name('q')
    print("he enters string to search---1")
@then(u"he shoould be displayed with the result")    
def step_impl1(context):
    page=homePageObj(context.browser)
    #context.browser.click()
    print(context.browser.find_elements_by_xpath("//button"))        
