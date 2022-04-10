from get_server_information import TwilioInformation
from database import Database
# get information


def info(list):
    information = list
    server_info = TwilioInformation(information)
    obj = server_info.get_link_info()
    database = Database(server_info.get_applicant_status(), obj)
    x = database.run()
