from selenium import webdriver

def before_scenario(context, scenario):
  #if 'web' in context.tags:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.browser = webdriver.Chrome("D:/Users/sjyothi/Downloads/chromedriver/chromedriver.exe",options=options)
    #webdriver.Remote(
     #       command_executor='http://127.0.0.1:4444/wd/hub',
      #      options=options)
    context.browser.implicitly_wait(10)
 
def after_scenario(context, scenario):
  #if 'web' in context.tags:
    print(context.tags)
    context.browser.quit()