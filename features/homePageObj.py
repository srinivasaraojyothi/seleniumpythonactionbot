from wrapper import wrapper

class homePageObj:
     
     obj1="//input[@name='q']"
     obj2="//button"

     def __init__(self, browser):
         self.browser=browser
         self.me =wrapper(self.browser) 
     def searchinGoogle(self,url):
        self.me.navigateto(url)
        #self.browser.get(url)    
     def googleSearch(self):
         self.me.findElementsBy(homePageObj.obj2)