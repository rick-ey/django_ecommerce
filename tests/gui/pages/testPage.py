# /tests/gui/page/testPage.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from payments.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class LoginTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)
        super(LoginTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(LoginTests, cls).tearDownClass()

    def setUp(self):
        self.valid_test_user = User.create("tester",
                                           "test@valid.com",
                                           "test",
                                           1234)
        self.sign_in_page = SignInPage(self.browser, self.live_server_url)

    def tearDown(self):
        self.valid_test_user.delete()

    def test_login(self):
        self.sign_in_page.go_to()
        self.sign_in_page.do_login("test@valid.com", "test")
        self.assertTrue(
            self.browser.find_element_by_id("user_info").is_displayed())

    def test_failed_login(self):
        self.sign_in_page.go_to()
        self.sign_in_page.do_login("test@test.com", "password")
        self.assertEquals(
            self.sign_in_page.error_msg, "Incorrect email address or password")

    def test_failed_login_invalid_email(self):
        self.sign_in_page.go_to()
        self.sign_in_page.do_login("test@", "password")
        self.assertEquals(
            self.sign_in_page.error_msg, "Email: Enter a valid email address.")


class SeleniumPage(object):
    '''
    Place to allow for any site-wide configuration you may want for your
    GUI testing
    '''
    def __init__(self, driver, base_url=None, wait_time=10):
        self.driver = driver
        self.base_url = base_url
        self.wait_time = wait_time


class SeleniumElement(object):

    def __init__(self, locator):
        self.locator = locator

    def __get__(self, obj, owner):
        driver = obj.driver
        wait_time = obj.wait_time
        return WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located(self.locator))


class SignInPage(SeleniumPage):

    email_textbox = SeleniumElement((By.ID, "id_email"))
    pwd_textbox = SeleniumElement((By.ID, "id_password"))
    sign_in_button = SeleniumElement((By.NAME, "commit"))
    error_msg_elem = SeleniumElement((By.CSS_SELECTOR, ".errors"))
    sign_in_title = SeleniumElement((By.CSS_SELECTOR, ".form-signin-heading"))

    def do_login(self, email, pwd):
        self.email_textbox.send_keys(email)
        self.pwd_textbox.send_keys(pwd)
        self.sign_in_button.submit()

    @property
    def error_msg(self):
        return self.error_msg_elem.text

    @property
    def rel_url(self):
        return '/sign_in'

    def go_to(self):
        self.driver.get('%s%s' % (self.base_url, self.rel_url))
        assert self.sign_in_title.text == "Sign in"
