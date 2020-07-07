from selenium import webdriver

browser = webdriver.Firefox()
print(type(browser))
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('bookcover')
    print(elem)
    #print('Znalezionio element {} wraz z nazwą klasy!'.format(elem.tag_name))

except Exception:
    print('Nie udało się znaleźć elementu wraz z podaną nazwą klasy')