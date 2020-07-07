##imports
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


##class and function to login on Github
class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get ('https://github.com/login')
    def login(username, password):
        username_input = browser.find_element_by_xpath('//*[@id="login_field"]')
        username_input.send_keys(username)
        password_input = browser.find_element_by_xpath('//*[@id="password"]')
        password_input.send_keys(password)
        sing_in_button = browser.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[9]')
        sing_in_button.click()


##class and function to create a new repository on Github
class NewRepository:
    def create_new_repository(project_name, description, privacy):
        browser.get ('https://github.com/new')
        repository_name = browser.find_element_by_xpath ('//*[@id="repository_name"]')
        repository_name.send_keys(project_name)
        description_input = browser.find_element_by_xpath ('//*[@id="repository_description"]')
        description_input.send_keys(description)
        if privacy == 's':
            mark_public = browser.find_element_by_xpath('//*[@id="repository_visibility_public"]')
            mark_public.click()
        else:
            mark_private = browser.find_element_by_xpath ('//*[@id="repository_visibility_private"]')
            mark_private.click()
        
        readme = browser.find_element_by_xpath('//*[@id="repository_auto_init"]')
        readme.click()
        choose_license = browser.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/div[4]/div[2]/div/details/summary/span[2]')
        choose_license.click()
        mit_license = browser.find_element_by_xpath ('/html/body/div[4]/main/div/form/div[4]/div[4]/div[2]/div/details/details-menu/div/div/div/label[4]/div/div')
        mit_license.click()
        create_repository = browser.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button')
        create_repository.click()


##class and function to create a folder on a directory and a .py file
class CreateProject:
    def create_folder_and_file(project_name):
        path = 'C:\\Users\\user\\Desktop\\Python\\'+ project_name
        acess_rights = 0o755
        try:
            os.mkdir(path, acess_rights)
        except OSError:
            print ('Creation of the directory %s failed' %path)
        else:
            print ('Successfully created the directory %s' %path)

        open(path +'\\'+ project_name +'.py','w+')

            
##inputs and function calls
browser = webdriver.Firefox()
sleep (15)
home_page = HomePage(browser)
project_name = input('What are we making today? ')
username = input('Enter your login: ')
password = input('Enter your password: ')
description = input('Whats the description of the repository: ')

valid_privacy = False
while valid_privacy == False:
    privacy = str(input('Is the repository public? ').lower())
    if privacy != 'y' and privacy != 'n':
        print('Just use Y for YES and N for NO')
    else:
        valid_privacy = True

CreateProject.create_folder_and_file(project_name)
HomePage.login (username,password)
sleep(15)
NewRepository.create_new_repository(project_name, description, privacy)

