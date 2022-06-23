from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class customwebDriverwait:
    def __init__(self, browser):
        #( "this is correct")
        self.browser = browser

    '''An expectation for checking that an element is present on the DOM of a page and visible. 
    Visibility means that the element is not only displayed but also has a height and width that is greater than 0.
     locator - used to find the element returns the WebElement once it is located and visible'''

    def WaitFor_VisibilityOf_Element_Located(self, xpath):
        return WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    '''An expectation for checking that an element is present on the DOM of a page. 
    This does not necessarily mean that the element is visible. 
    locator - used to find the element returns the WebElement once it is located'''

    def WaitFor_PresenseOf_Element_Located(self, xpath):
        return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

    '''An Expectation for checking an element is visible and enabled such that you can click it.

    element is either a locator (text) or an WebElement'''

    def WaitForElement_tobe_Clickable(self, xpath):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def WaitForAlert_is_present(self):
        return WebDriverWait(self.browser, 10).until(EC.alert_is_present())

    '''An expectation for checking if the given attribute is included in the specified element. 
    locator, attribute'''

    def WaitFor_element_attribute_to_include(self, xpath, value):
        return WebDriverWait(self.browser, 10).until(EC.element_attribute_to_include((By.XPATH, xpath), value))

    '''An expectation to locate an element and check if the selection state specified is in that state. 
    locator is a tuple of (by, path) is_selected is a boolean'''

    def WaitFor_element_located_selection_state_to_be(self, xpath, is_Selected):
        return WebDriverWait(self.browser, 10).until(EC.element_located_selection_state_to_be((By.XPATH, xpath), is_Selected))

    '''An expectation for the element to be located is selected. locator is a tuple of (by, path)'''

    def WaitFor_element_located_to_be_selected(self, xpath):
        return WebDriverWait(self.browser, 10).until(EC.element_located_to_be_selected((By.XPATH, xpath)))

    '''An expectation for checking if the given element is selected. 
    element is WebElement object is_selected is a Boolean.”'''

    def WaitFor_element_selection_state_to_be(self, xpath, is_Selected):
        return WebDriverWait(self.browser, 10).until(EC.element_selection_state_to_be((By.XPATH, xpath), is_Selected))

    '''An expectation for checking the selection is selected. 
    element is WebElement object'''

    def WaitFor_element_to_be_selected(self, xpath):
        if(customwebDriverwait.WaitFor_VisibilityOf_Element_Located(xpath)):
            target = customwebDriverwait.WaitFor_VisibilityOf_Element_Located(
                xpath)
            return WebDriverWait(self.browser, 10).until(EC.element_to_be_selected(target))

    '''An expectation for checking whether the given frame is available to switch to. 
    If the frame is available it switches the given driver to the specified frame.'''

    def WaitFor_frame_to_be_available_and_switch_to_it(self, xpath):
        return WebDriverWait(self.browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, xpath)))
    '''
    yet to cover the following

    selenium.webdriver.support.expected_conditions.invisibility_of_element(element)
    An Expectation for checking that an element is either invisible or not present on the DOM.

    element is either a locator (text) or an WebElement

    selenium.webdriver.support.expected_conditions.invisibility_of_element_located(locator)
    An Expectation for checking that an element is either invisible or not present on the DOM.

    locator used to find the eleme


    '''
    '''An expectation that a new window will be opened and have the number of windows handles increase'''

    def WaitFor_new_window_is_opened(self):
        currentWindowHandles = self.browser.window_handles
        return WebDriverWait(self.browser, 10).until(EC.new_window_is_opened(currentWindowHandles))

    '''An expectation for the number of windows to be a certain value.'''

    def WaitFor_number_of_windows_to_be(self, number):
        # currentWindowHandles=self.browser.window_handles
        return WebDriverWait(self.browser, 10).until(EC.number_of_windows_to_be(number))

    '''An expectation for checking that there is at least one element present on a web page. 
    locator is used to find the element returns the list of WebElements once they are located'''

    def WaitFor_presence_of_all_elements_located(self, xpath):
        # currentWindowHandles=self.browser.window_handles
        return WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    '''Wait until an element is no longer attached to the DOM. element is the element to wait for. 
    returns False if the element is still attached to the DOM, true otherwise.'''

    def WaitFor_staleness_of(self, xpath):
        element = self.browser.find_element_by_id(xpath)
        return WebDriverWait(self.browser, 10).until(EC.staleness_of(element))

    '''An expectation for checking if the given text is present in the specified element. locator, text'''

    def WaitFor_text_to_be_present_in_element(self, xpath, text_):
        return WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, xpath), text_))

    '''An expectation for checking if the given text is present in the element’s attribute. 
    locator, attribute, text'''

    def WaitFor_text_to_be_present_in_element_attribute(self, xpath, attribute, text_):
        return WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element_attribute((By.XPATH, xpath), attribute, text_))

    '''An expectation for checking if the given text is present in the element’s value. locator, text'''

    def WaitFor_text_to_be_present_in_element_value(self, xpath, text_):
        return WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element_value((By.XPATH, xpath), text_))

    '''An expectation for checking that the title contains a case-sensitive substring. 
    title is the fragment of title expected returns True when the title matches, False otherwise'''

    def WaitFor_title_contains(self, text_):
        # page_title=self.browser.title
        return WebDriverWait(self.browser, 10).until(EC.title_contains(text_))

    '''An expectation for checking the title of a page. title is the expected title, 
    which must be an exact match returns True if the title matches, false otherwise.'''

    def WaitFor_title_is(self, text_):
        # page_title=self.browser.title
        return WebDriverWait(self.browser, 10).until(EC.title_is(text_))

    '''An expectation for checking the current url. url is the expected url, 
    which must not be an exact match returns True if the url is different, false otherwise.'''

    def WaitFor_url_changes(self, url):
        # page_title=self.browser.title
        return WebDriverWait(self.browser, 10).until(EC.url_changes(url))

    '''An expectation for checking that the current url contains a case-sensitive substring. 
    url is the fragment of url expected, returns True when the url matches, False otherwise'''

    def WaitFor_url_contains(self, url):
        # page_title=self.browser.title
        return WebDriverWait(self.browser, 10).until(EC.url_contains(url))

    '''An expectation for checking the current url. pattern is the expected pattern, 
    which must be an exact match returns True if the url matches, false otherwise.'''

    def WaitFor_url_matches(self, pattern):
        # page_title=self.browser.title
        return WebDriverWait(self.browser, 10).until(EC.url_matches(pattern))

    '''An expectation for checking the current url. url is the expected url, 
    which must be an exact match returns True if the url matches, false otherwise.'''

    def WaitFor_url_to_be(self, url):
        # page_title=self.browser.title
        return WebDriverWait(self.browser, 10).until(EC.url_to_be(url))

    '''An expectation for checking that an element, known to be present on the DOM of a page, is visible. 
    Visibility means that the element is not only displayed but also has a height and width that is greater than 0. 
    element is the WebElement returns the (same) WebElement once it is visible'''

    def WaitFor_visibility_of(self, xpath):
        element = self.browser.find_element_by_id(xpath)
        return WebDriverWait(self.browser, 10).until(EC.visibility_of(element))

    '''An expectation for checking that all elements are present on the DOM of a page and visible. 
    Visibility means that the elements are not only displayed but also has a height and width that is greater than 0. 
    locator - used to find the elements returns the list of WebElements once they are located and visible'''

    def WaitFor_visibility_of_all_elements_located(self, xpath):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))

    '''An expectation for checking that there is at least one element visible on a web page. 
    locator is used to find the element returns the list of WebElements once they are located'''

    def WaitFor_visibility_of_any_elements_located(self, xpath):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_any_elements_located((By.XPATH, xpath)))
