from model.contact import Contact

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
        wd.find_element_by_name("phone2").send_keys(contact.home_address)
        # fill notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit the form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


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

    '''
     Изменение контакта
    '''
    def change_contact(self, contact):
        wd = self.app.wd
        # выбираем "редактировать"
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
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
        wd.find_element_by_name("phone2").send_keys(contact.home_address)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit the form
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()


    '''
    Проверка на существование контактов
    '''

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))


    def get_contacts_list(self):
        wd = self.app.wd
        # Открываем главную страницу, чтобы wd успел взять список td
        self.app.open_main_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[@name='entry']"):
            cells = element.find_elements_by_tag_name("td")
            id = element.find_element_by_name("selected[]").get_attribute("value")
            firstname = cells[2].text
            lastname = cells[1].text
            contacts.append(Contact(id = id, firstname=firstname, lastname=lastname))
        return contacts
