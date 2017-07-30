# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_contact(self):
        wd = self.wd
        self.open_main_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd, Contact(firstname="Firstname", middlename="Middlename", lastname="Lastname",
                             nickname="Nickname", title="Mr", company="Company", address="Address line",
                             phone_home="+74951234567", phone_mobile="+79031234567", phone_work="+74961234567",
                             fax_number="+74961234560", email="test@mail.ru",
                             homepage="http://example.com", birthday_day="21", birthday_month="12",
                             birthday_year="1990", anniversary_day="18", anniversary_month="10",
                             anniversary_year="2010", secondary_address="secondary address",
                             home_address="home address", notes="notes"))
        self.submit(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def submit(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def add_new_contact(self, wd, contact):
        # create new contact
        wd.find_element_by_link_text("add new").click()
        # fill first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # fill middle name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # fill last name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # fill nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # fill title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        # fill company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        # fill address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # fill home phone
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        # fill mobile phone
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        # fill work phone
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.phone_work)
        # fill fax
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_number)
        # fill email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # fill homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # choose birthday
        if not wd.find_element_by_xpath(
                                "//div[@id='content']/form/select[1]//option[" + contact.birthday_day + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + contact.birthday_day + "]").click()
        if not wd.find_element_by_xpath(
                                "//div[@id='content']/form/select[2]//option[" + contact.birthday_month + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + contact.birthday_month + "]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        # choose anniversary
        if not wd.find_element_by_xpath(
                                "//div[@id='content']/form/select[3]//option[" + contact.anniversary_day + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + contact.anniversary_day + "]").click()
        if not wd.find_element_by_xpath(
                                "//div[@id='content']/form/select[4]//option[" + contact.anniversary_month + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + contact.anniversary_month + "]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        # fill secondary address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        # fill home address into the field phone2
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.home_address)
        # fill notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_main_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
