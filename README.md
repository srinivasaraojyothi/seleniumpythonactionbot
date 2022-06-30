# Python Selenium Actionbot wrapper
## Currently supporting functions
### webelement functions  

``` python

    def findElementsBy(self, xpath):
            ...

    def findElementBy(self, xpath):
            ...

    def click(self, xpath):
            ...

    def clear(self, xpath):
            ...   
    
    
    def isClickable(self, xpath, index=None):
            ...
    
    '''
    Simulates typing into the element.

    Args:	
    value - A string for typing, or setting form fields. For setting file inputs, this could be a local file path.
    Use this to send simple key events or to fill out form fields:
    form_textfield = driver.find_element(By.NAME, 'username')
                    form_textfield.send_keys("admin")
    This can also be used to set file inputs.

    file_input = driver.find_element(By.NAME, 'profilePic')
    file_input.send_keys("path/to/profilepic.gif")
    # Generally it's better to wrap the file path in one of the methods
    # in os.path to return the actual path to support cross OS testing.
    # file_input.send_keys(os.path.abspath("path/to/profilepic.gif"))
    '''

    def fillField(self, xpath, text):



    def navigateto(self, urlstring):


    '''
        Gets the given attribute or property of the element.

        This method will first try to return the value of a property with the given name. If a property with that name doesn’t exist, it returns the value of the attribute with the same name. If there’s no attribute with that name, None is returned.

        Values which are considered truthy, that is equals “true” or “false”, are returned as booleans. All other non-None values are returned as strings. For attributes or properties which do not exist, None is returned.

        To obtain the exact value of the attribute or property, use get_dom_attribute() or get_property() methods respectively.

        Args:	
        name - Name of the attribute/property to retrieve.
        Example:

        # Check if the "active" CSS class is applied to an element.
        is_active = "active" in target_element.get_attribute("class")
    '''
    def getAttribute(self, xpath,AttributeName):
     
    
    '''
        Gets the given attribute of the element. Unlike get_attribute(), this method only returns 
        attributes declared in the element’s HTML markup.

        Args:	
        name - Name of the attribute to retrieve.
        Usage:	
        text_length = target_element.get_dom_attribute("class")
    '''
    def getDomAttribute(self, xpath,AttributeName):
            ...



    '''
        Gets the given property of the element.

        Args:	
        name - Name of the property to retrieve.
        Usage:	
        text_length = target_element.get_property("text_length")
    '''
    def getProperty(self, xpath,PropertyName):
            ... 
    '''
        Whether the element is visible to a user.
    '''
    def isElementDisplayed(self, xpath):
            ...
    '''
        Returns whether the element is enabled.
    '''
    def isElementEnabled(self, xpath):
            ... 

    '''
        Returns whether the element is selected.

        Can be used to check if a checkbox or radio button is selected.
    '''
    def isElementSelected(self, xpath):
            ...
    
    '''
        Saves a screenshot of the current element to a PNG image file. Returns
        False if there is any IOError, else returns True. Use full paths in your filename.
    '''
    def currentElementScreenshot(self, xpath,screenShotSavingPath):
            ...
    # action class

    def actionClick(self, xpath):
            ...

    def actionClickandHold(self, xpath=None):
            ...

    def moveToElement(self, xpath):
            ...

    def moveToElementWithOffset(self, xpath, xoffset, yoffset):
            ...

    def moveByOffsett(self, xoffset, yoffset):
            ...

    def actionRelease(self, xpath=None):
            ...

    def keyDown(self, ModifierKey, key, xpath=None):
            ...

    def keyUp(self, ModifierKey, key, xpath=None):
            ...

    def double_click(self, xpath: None):
            ...

    def righttClick(self, xpath=None):
            ...

    def resetActions(self):
            ...

    def sendKeys(self, *keys_to_send):
            ...

    def sendKeysToElement(self, xpath, *keys_to_send):
            ...
        '''
        Gets the full document screenshot of the current window as a base64 encoded string
        which is useful in embedded images in HTML.

        Usage:	
        driver.get_full_page_screenshot_as_base64()
        '''
    def get_screenshot_ofcurrentActive_page_in_base64(self):
            ...

        '''
        Saves a full document screenshot of the current window to a PNG image file. Returns
        False if there is any IOError, else returns True. Use full paths in your filename.
        Args:	
        filename: The full path you wish to save your screenshot to. This should end with a .png extension.
        Usage:	
        driver.get_full_page_screenshot_as_file('/Screenshots/foo.png')
        '''
    def get_screenshot_ofcurrentActive_page_asFile(self,filename:str):
            ...   
        '''get_full_page_screenshot_as_png() → str
        Gets the full document screenshot of the current window as a binary data.

        Usage:	
        driver.get_full_page_screenshot_as_png()
        '''
    def get_screenshot_ofcurrentActive_page_asPNG(self):
            ...

        ''' 
        Saves a screenshot of the current window to a PNG image file. Returns
        False if there is any IOError, else returns True. Use full paths in your filename.
        Args:	
        filename: The full path you wish to save your screenshot to. This should end with a .png extension.
        Usage:	
        driver.save_screenshot('/Screenshots/foo.png')
        '''
    def screenshot_save_full_page_screenshot(self,filename):
            ...

    '''
    returns the embedded text in the image.
    It returns a list of detected text, with each text element containing three types of information. 
    Which are: the text, its bounding box vertices, and the confidence level of the text detection
    '''    
    def get_embeddedText_from_image(self,path:str):
            ...  
    
```
### Drag and Drop

```python

def dragAndDrop(self, sourcexpath, destinationxpath):
            ...

    def dragAndDropByOffset(self, sourcexpath, xoffset, yoffset):
            ...
```
### window and frame functions
```python
    def switchToWindowUsingName(self, windowName):
            ...  

    def switchtoWindowUsingHandle(self, windowNumber):
            ...  
    # frame switch, It’s possible to access subframes by separating the path with a dot,
    # and you can specify the frame by its index too. That is: driver.switch_to_frame("frameName.0.child")
    # would go to the frame named “child” of the first subframe of the frame called “frameName”. All frames are evaluated as if from *top*.

    def swithToFrame(self, xpath):
            ...  
        
    # Once we are done with working on frames, we will have to come back to the parent
    # frame which can be done using:

    def swithToParentFrame(self):
            ...  

```
### Dropdown
```python

    def selectDropDownByValue(self, xpath, valueToSelect):
            ...  

    def selectDropDownByIndex(self, xpath, indexToSelect):
        elementPresense=super().WaitFor_PresenseOf_Element_Located(xpath)
        #elementVisibility=super().WaitFor_VisibilityOf_Element_Located(xpath)
        if(elementPresense):
            #if(elementVisibility):
                select = Select(self.browser.find_element(By.XPATH, xpath))
                select.select_by_index(indexToSelect)

    def selectDropDownByVisibleText(self, xpath, textToSelect):
            ...  

    def deselectAllOptionsInDropDown(self, xpath):
            ...  

    def getDefaultSelectedDropDownOptions(self, xpath):
            ...  

    def getAllOptionInDropDown(self, xpath):
            ...  

    def deselectByIndex(self, xpath, index):
            ...  

    def deselectByValue(self, xpath, value):
            ...  

    def deselectByVisibleText(self, xpath, text):
            ...  

    def getFirstSelecteOption(self, xpath):
            ...  
```
### Alerts
```python
    #alerts
    # Use this class to interact with alert prompts. 
    # It contains methods for dismissing, accepting, inputting, and getting text from alert prompts.   
    def acceptAlert(self):
            ... 
    def dismissAlert(self):
            ... 
    def getAlertText(self):
            ... 
    def sendKeystoAlert(self,keysToSend):
            ... 
```