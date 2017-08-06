class Contact:
    def __init__(self, firstname, middlename, lastname, nickname, title, company, address, phone_home,
                        phone_mobile, phone_work, fax_number, email, homepage, birthday_day, birthday_month,
                        birthday_year, anniversary_day, anniversary_month, anniversary_year, secondary_address,
                        home_address, notes):
        """

        :rtype: object
        """
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.fax_number = fax_number
        self.email = email
        self.homepage = homepage
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.secondary_address = secondary_address
        self.home_address = home_address
        self.notes = notes
