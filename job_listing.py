class JobListing:
    def __init__(self, phone_number) -> None:
        self._phone_number = phone_number
        self._name = ""
        self._min_age = 0
        self._location = ""
        self._keywords = []
        self._description = ""
        self._links = []

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number
    def get_phone_number(self):
        return self._phone_number

    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name

    def set_min_age(self, min_age):
        self._min_age = min_age
    def get_min_age(self):
        return self._min_age

    def set_location(self, location):
        self._location = location
    def get_location(self):
        return self._location
    
    def set_keywords(self, keywords):
        self._keywords = keywords
    def get_keywords(self):
        return self._keywords
    
    def set_desciption(self, desc):
        self._description = desc
    def get_description(self):
        return self._description

    def set_links(self, links):
        self._links = links
    def get_links(self):
        return self._links