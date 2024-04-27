import time
import pytest

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture(scope='class')
def _drivers():
    driver = webdriver.Chrome(options=opts)
    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()



#-------------------------------------------------

'''
CONFTEST
•	Fixtures can be shared or re-used in different test methods and across multiple files through a 
        special python file “conftest.py” 
•	The advantage of having the fixture in “conftest.py” is that you don’t have to import the 
        fixture you want to use in each and every test. 
•	The fixture present in “conftest.py” automatically get discovered by pytest. 
•	Both conftest.py and the test module should be in the same package! 
•	If conftest.py is in other package than the test module, then conftest.py module will not be automatically discovered. 
•	Pytest checks if the conftest.py file is present in the current package. 
•	The discovery of fixture functions starts at test classes, then test modules, then conftest.py files.



If we give 
In terminal --> pytest -vs, this command will execute all the test files in that package,
This we call it as batch execution
'''



















