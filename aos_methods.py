from selenium import webdriver  # import selenium to the file
import aos_locators as locators
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

s = Service(executable_path='../../chromedriver.exe')
driver = webdriver.Chrome(service=s)


# ----------------------------------------------------------
def setUp():
    print(f'Launch {locators.app} App')
    print('--------------------~*~--------------------')
    # Print test start day and time
    print(f'The test Started at: {datetime.datetime.now()}')
    # Make browser full screen
    driver.maximize_window()
    # Give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # Navigate to Advantage Online Shopping website
    driver.get(locators.aos_url)
    # Check that  URL and the home page title are displayed
    if driver.current_url == locators.aos_url and driver.title == locators.aos_home_page_title:
        print(f'Yey! {locators.app} was launched Successfully!')
        print(f'{locators.app} homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(2)
    else:
        print(f'{locators.app}  did not launch. Check your code for error!')
        print(f'Current URL: {driver.current_url}, Page Title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print('--------------------~*~--------------------')
        print(f'The test Completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


# Create account
def create_user():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, 'create-new-account').click()
    sleep(2)
    # validate we are on 'Create account'
    assert driver.title == locators.aos_add_user_title
    print(f'Account Details...')
    sleep(.50)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
    sleep(.50)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    sleep(.50)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
    sleep(.50)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
    sleep(.50)
    print(f'--- Personal Details...')
    sleep(.50)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.firstname)
    sleep(.50)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.lastname)
    sleep(.50)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
    sleep(.50)
    print(f'--- Address...')
    sleep(.50)
    # select an options 'Canada'
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
    sleep(.50)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    sleep(.50)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    sleep(.50)
    driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
    sleep(.50)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postcode)
    sleep(.50)
    # check 'I agree'
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(.50)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(1)
    print(
        f'New user with \nUsername:\t{locators.username}\nPassword:\t{locators.password} is registered!')


def logout():
    # validate we are on 'Create account'
    assert driver.title == locators.aos_add_user_title
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle > label:nth-of-type(3)').click()
    sleep(2)
    # validate logout successful
    if driver.current_url == locators.aos_url:
        print(f'Logout successful at {datetime.datetime.now()}!')


# login to AOS
def login():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(2)
    print(f'Login Form is displayed: {driver.find_element(By.CLASS_NAME, "login").is_displayed()}')
    driver.find_element(By.NAME, 'username').send_keys(locators.username)
    sleep(2)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    sleep(2)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(2)


# check text if displayed
def check_text():
    # validate we are on homepage
    assert driver.title == locators.aos_home_page_title
    sleep(2)
    print(f'Checking text if displayed..')
    sleep(1.5)

    print(f'Checking text {locators.speakers}..')
    sleep(1)
    if driver.find_element(By.XPATH, "//span[@id='speakersTxt']").is_displayed():
        print(f'Text {locators.speakers} is displayed.')
        sleep(1.5)
    else:
        print(f'Error! Check your code!')
        sleep(1)
        tearDown()
    print(f'Checking text {locators.tablets}..')
    sleep(1)
    if driver.find_element(By.XPATH, "//span[@id='tabletsTxt']").is_displayed():
        print(f'Text {locators.tablets} is displayed.')
        sleep(1.5)
    else:
        print(f'Error! Check your code!')
        sleep(1)
        tearDown()
    print(f'Checking text {locators.laptops}..')
    sleep(1)
    if driver.find_element(By.XPATH, "//span[@id='laptopsTxt']").is_displayed():
        print(f'Text {locators.laptops} is displayed.')
        sleep(1.5)
    else:
        print(f'Error! Check your code!')
        sleep(1)
        tearDown()
    print(f'Checking text {locators.mice}..')
    sleep(1)
    if driver.find_element(By.XPATH, "//span[@id='miceTxt']").is_displayed():
        print(f'Text {locators.mice} is displayed.')
        sleep(1.5)
    else:
        print(f'Error! Check your code!')
        sleep(1)
        tearDown()
    print(f'Checking text {locators.headphones}..')
    sleep(1)
    if driver.find_element(By.XPATH, "//span[@id='headphonesTxt']").is_displayed():
        print(f'Text {locators.headphones} is displayed.')
        sleep(1.5)
    else:
        print(f'Error! Check your code!')
        sleep(1)
        tearDown()


# check nav menu if displayed
def check_tab_menu():
    if driver.current_url == locators.aos_url:
        # validate we are on homepage
        assert driver.title == locators.aos_home_page_title
        # validate Nav Bar is displayed
        assert driver.find_element(By.XPATH, '//nav').is_displayed()
        sleep(1)
        print(f'Checking Nav Menu..')
        sleep(1.5)
        print(f'Checking {locators.special_offers} link is clickable..')
        sleep(1)
        if driver.find_element(By.XPATH, "//nav/ul/li[7]/a[@role='link']").is_displayed():
            driver.find_element(By.XPATH, "//nav/ul/li[7]/a[@role='link']").click()
            print(f'Link text {locators.special_offers} is clickable!')
            sleep(1.5)
        else:
            print(f'Error! Check your code!')
            sleep(1)
            tearDown()
        print(f'Checking {locators.popular_items} link is clickable..')
        sleep(1)
        if driver.find_element(By.XPATH, "//nav/ul/li[6]/a[@role='link']").is_displayed():
            driver.find_element(By.XPATH, "//nav/ul/li[6]/a[@role='link']").click()
            print(f'Link text {locators.popular_items} is clickable!')
            sleep(1.5)
        else:
            print(f'Error! Check your code!')
            sleep(1)
            tearDown()
        print(f'Checking {locators.contact_us} link is clickable..')
        sleep(1)
        if driver.find_element(By.XPATH, "//nav/ul/li[5]/a[@role='link']").is_displayed():
            driver.find_element(By.XPATH, "//nav/ul/li[5]/a[@role='link']").click()
            print(f'Link text {locators.contact_us} is clickable!')
            sleep(1.5)
        else:
            print(f'Error! Check your code!')
            sleep(1)
            tearDown()
    else:
        print(f'Error! Check your code!')
        sleep(1)
        tearDown()


# check logo if displayed
def check_logo():
    if driver.current_url == locators.aos_url:
        # validate we are on homepage
        assert driver.title == locators.aos_home_page_title
        # validate logo is displayed
        assert driver.find_element(By.CLASS_NAME, 'logo').is_displayed()
        sleep(1)
        print(f'Checking Logo..')
        sleep(1.5)
        if driver.find_element(By.CLASS_NAME, 'logo').is_displayed():
            print(f'Logo is displayed!')
            sleep(1.5)
        else:
            print(f'Error! Check your code!')
            sleep(1)
            tearDown()
    else:
        print(f'Error! Check your code!')
        sleep(1)
        tearDown()


# check contact us
def contact_us():
    if driver.current_url == locators.aos_url:
        # validate we are on homepage
        assert driver.title == locators.aos_home_page_title
        # validate logo is displayed
        assert driver.find_element(By.XPATH, "//*[@id='contact_us']").is_displayed()
        sleep(1)
        print(f'Contact Us is displayed!')
        sleep(1.5)
        if driver.find_element(By.XPATH, "//*[@id='contact_us']").is_displayed():
            print(f'Entering email..')
            sleep(1)
            driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
            sleep(1.5)
            print(f'Entering message..')
            sleep(1)
            driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.messages)
            sleep(1.5)
            print(f'Sending message..')
            sleep(1)
            driver.find_element(By.ID, 'send_btnundefined').click()
            sleep(1.5)
            print(f'Checking confirmation..')
            sleep(1)
            # validate if success
            assert driver.find_element(By.XPATH, '//p[contains(.,"Thank you for contacting Advantage support")]')
            if driver.find_element(By.XPATH, '//p[contains(.,"Thank you for contacting Advantage support")]'):
                print(f'Thank you for contacting Advantage support confirmation is displayed!')
                sleep(1.5)
            else:
                print(f'Error! Check your code!')
                sleep(1)
                tearDown()
            sleep(1.5)
            # validate continue shopping button
            assert driver.find_element(By.XPATH, '//a[contains(.," CONTINUE SHOPPING ")]')
            if driver.find_element(By.XPATH, '//a[contains(.," CONTINUE SHOPPING ")]'):
                print(f'{locators.continue_shopping} button is displayed!')
                sleep(1)
                print(f'{locators.continue_shopping} button is clicked!')
                sleep(1)
                driver.find_element(By.XPATH, f'//a[contains(.,"{locators.continue_shopping}")]').click()
                print(f'Button {locators.continue_shopping} is clickable!')
                sleep(1.5)
            else:
                print(f'Error! Check your code!')
                sleep(1)
                tearDown()
        else:
            print(f'Error! Check your code!')
            sleep(1)
            tearDown()
    else:
        print(f'Error! Check your code!')
        sleep(1)
        tearDown()


# check social media
def check_social_media():
    if driver.current_url == locators.aos_url:
        print(f'Checking Social Media links..')
        sleep(1.5)
        if driver.find_element(By.XPATH, '//*[@id="follow"]').is_displayed():
            # validate logo is displayed
            assert driver.find_element(By.XPATH, '//*[@id="follow"]').is_displayed()
            print(f'Social Media links are displayed!')
            sleep(1.5)
            if driver.find_element(By.XPATH,
                                   "//div[@id='follow']/a[@href=' https://www.facebook.com/MicroFocus/']/img").is_displayed():
                print(f'Facebook is displayed!')
                sleep(1)
                print(f'Clicking Facebook..')
                driver.find_element(By.XPATH,
                                    "//div[@id='follow']/a[@href=' https://www.facebook.com/MicroFocus/']/img").click()
                print(f'Facebook is clickable!')
                sleep(1.5)
            else:
                print(f'Error! Check your code!')
                sleep(1)
                tearDown()
            if driver.find_element(By.XPATH,
                                   "//div[@id='follow']/a[@href='https://twitter.com/MicroFocus']/img").is_displayed():
                print(f'Twitter is displayed!')
                sleep(1)
                print(f'Clicking Twitter..')
                driver.find_element(By.XPATH,
                                    "//div[@id='follow']/a[@href='https://twitter.com/MicroFocus']/img").click()
                print(f'Twitter is clickable!')
                sleep(1.5)
            else:
                print(f'Error! Check your code!')
                sleep(1)
                tearDown()
            if driver.find_element(By.XPATH,
                                   "//div[@id='follow']/a[@href='https://www.linkedin.com/company/1024?trk=tyah&trkInfo=clickedVertical%3Ashowcase%2CclickedEntityId%3A1024%2Cidx%3A2-1-2%2CtarId%3A145431482.327%2Ctas%3Ahewlett%20packard%20enterprise%20software']/img").is_displayed():
                print(f'LinkedIn is displayed!')
                sleep(1)
                print(f'Clicking LinkedIn..')
                driver.find_element(By.XPATH,
                                    "//div[@id='follow']/a[@href='https://www.linkedin.com/company/1024?trk=tyah&trkInfo=clickedVertical%3Ashowcase%2CclickedEntityId%3A1024%2Cidx%3A2-1-2%2CtarId%3A145431482.327%2Ctas%3Ahewlett%20packard%20enterprise%20software']/img").click()
                print(f'LinkedIn is clickable!')
                sleep(1.5)
            else:
                print(f'Error! Check your code!')
                sleep(1)
                tearDown()
        else:
            print(f'Error! Check your code!')
            sleep(1)
            tearDown()
    else:
        print(f'Error! Check your code!')
        sleep(1)
        tearDown()
