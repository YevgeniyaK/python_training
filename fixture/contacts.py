from model.contact import Contact
from model.group import Group
import re

class ContactsHelper:
    def __init__(self, app):
        self.app = app

    '''
      Форма добавления контакта
    '''

    def add_new_contact(self, contact):
        wd = self.app.wd
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
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        # fill homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # choose birthday
        if not wd.find_element_by_xpath(
                                "//div[@id='content']/form/select[1]//option[" + contact.birthday_day + "]").is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[1]//option[" + contact.birthday_day + "]").click()
        if not wd.find_element_by_xpath(
                                "//div[@id='content']/form/select[2]//option[" + contact.birthday_month + "]").is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[2]//option[" + contact.birthday_month + "]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        # choose anniversary
        if not wd.find_element_by_xpath(
                                "//div[@id='content']/form/select[3]//option[" + contact.anniversary_day + "]").is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[3]//option[" + contact.anniversary_day + "]").click()
        if not wd.find_element_by_xpath(
                                "//div[@id='content']/form/select[4]//option[" + contact.anniversary_month + "]").is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[4]//option[" + contact.anniversary_month + "]").click()
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
        wd.find_element_by_name("phone2").send_keys(contact.secondary_phone)
        # fill notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit the form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contacts_cache = None

    '''
     Удаление первого контакта
    '''

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit the deletion
        wd.find_element_by_xpath("//form[@name='MainForm']/div[@class='left']/input[@value='Delete']").click()
        # нажимаем ok во всплывающем окне
        alert = wd.switch_to_alert()
        alert.accept()
        self.contacts_cache = None

    '''
    Удаление рандомного контакта
    '''

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit the deletion
        wd.find_element_by_xpath("//form[@name='MainForm']/div[@class='left']/input[@value='Delete']").click()
        # нажимаем ok во всплывающем окне
        alert = wd.switch_to_alert()
        alert.accept()
        self.contacts_cache = None

    '''
     Изменение контакта
    '''

    def change_contact(self, index, contact):
        wd = self.app.wd
        # выбираем "редактировать"
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%d]/td[8]/a/img" % (index + 2)).click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.phone_work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_number)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if not wd.find_element_by_xpath(
                                "//div[@id='content']/form/select[1]//option[" + contact.birthday_day + "]").is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[1]//option[" + contact.birthday_day + "]").click()
        if not wd.find_element_by_xpath(
                                "//div[@id='content']/form/select[2]//option[" + contact.birthday_month + "]").is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[2]//option[" + contact.birthday_month + "]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        if not wd.find_element_by_xpath(
                                "//div[@id='content']/form/select[3]//option[" + contact.anniversary_day + "]").is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[3]//option[" + contact.anniversary_day + "]").click()
        if not wd.find_element_by_xpath(
                                "//div[@id='content']/form/select[4]//option[" + contact.anniversary_month + "]").is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[4]//option[" + contact.anniversary_month + "]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_phone)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit the form
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contacts_cache = None

    contacts_cache = None

    '''
    Проверка на существование контактов
    '''

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        # Открываем главную страницу, чтобы wd успел взять список td
        self.app.open_main_page()
        if self.contacts_cache is None:
            wd = self.app.wd
            self.contacts_cache = []
            for element in wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[@name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                #Если в конце или начале текста есть пробелы, они будут удалены
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contacts_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                                   all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contacts_cache)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_main_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_main_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email=email, email2=email2, email3=email3,
                       phone_home=phone_home, phone_mobile=phone_mobile, phone_work=phone_work, secondary_phone=secondary_phone)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        phone_home = re.search("H: (.*)", text).group(1)
        phone_mobile = re.search("M: (.*)", text).group(1)
        phone_work = re.search("W: (.*)", text).group(1)
        return Contact(phone_home=phone_home, phone_mobile=phone_mobile, phone_work=phone_work)


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_id(id)
        wd.find_element_by_xpath("//form[@name='MainForm']/div[@class='left']/input[@value='Delete']").click()
        alert = wd.switch_to_alert()
        alert.accept()
        self.contacts_cache = None


    def select_contact_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def change_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.app.open_contact_edit_page(id)
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.phone_work)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_phone)
        # submit the form
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contacts_cache = None


    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.app.open_main_page()
        self.select_contact_id(contact.id)
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='"+group.id+"']").click()
        wd.find_element_by_xpath("//div[@class='right']/input[@name='add']").click()


    def get_contacts_list_from_groups_page(self, group_id):
        # Открываем страницу контактов в группе
        wd = self.app.wd
        wd.get(self.app.base_url + "?group=" + group_id)
        contacts_list = []

        # в группе без названия нет кнопки удаления контакта
        if len(wd.find_elements_by_xpath("//input[@name='remove']")) == 0:
            return contacts_list

        for element in wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[@name='entry']"):
            cells = element.find_elements_by_tag_name("td")
            id = element.find_element_by_name("selected[]").get_attribute("value")
            #Если в конце или начале текста есть пробелы, они будут удалены
            firstname = cells[2].text
            lastname = cells[1].text
            address = cells[3].text
            all_emails = cells[4].text
            all_phones = cells[5].text
            contacts_list.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                               all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return contacts_list


    def delete_contact_from_group_by_id(self, id):
        wd = self.app.wd
        self.select_contact_id(id)
        wd.find_element_by_xpath("//input[@name='remove']").click()

