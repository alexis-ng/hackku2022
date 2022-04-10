from get_server_information import TwilioInformation
from database import Database
# get information


def main():
    information = []
    server_info = TwilioInformation(information)
    obj = server_info.get_link_info()
    database = Database(server_info.get_applicant_status(), obj)
    



if __name__ == "__main__":
    main()