import pymysql.cursors
import mysql.connector
from model.group import Group
from model.contact import Contact



class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
        #self.connection = pymysql.connect(host=host, database=name, user=user, password=password, flag=pymysql.constants)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name.strip(), header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()



    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 from addressbook where deprecated ='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, email=email, email2=email2, email3=email3, phone_home=home, phone_mobile=mobile, phone_work=work, secondary_phone=phone2))
        finally:
            cursor.close()
        return list



    def get_contact_list_for_homepage(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 from addressbook where deprecated ='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2) = row
                contact = Contact(id=str(id), firstname=firstname, lastname=lastname, address=address)

                emails = []
                if email is not None:
                    emails.append(email)
                if email2 is not None:
                    emails.append(email2)
                if email3 is not None:
                    emails.append(email3)
                contact.all_emails_from_home_page = " ".join(emails).strip()

                phones = []
                if home is not None:
                    phones.append(home)
                if mobile is not None:
                    phones.append(mobile)
                if work is not None:
                    phones.append(work)
                if phone2 is not None:
                    phones.append(phone2)
                contact.all_phones_from_home_page = " ".join(phones).strip()
                list.append(contact)
        finally:
            cursor.close()
        return list
