from extract_keywords import Extractor
from src.stt import Recognize
from get_server_information import TwilioInformation


def main():
    
    # file_name = "annoy.wav" # input("Enter a file_name: ")
    # clean_words = Extractor(file_name=file_name)
    # print(clean_words.extract())

    # rec = Recognize(file_name)
    # print(rec.convert_to_text())
    
    d = {
        "name" : "https://api.twilio.com/2010-04-01/Accounts/AC808010d97a3e913acc49f1d84781e6db/Recordings/RE1351edc9819df3dbf71b7a73853eac7c",
        "age" : "https://api.twilio.com/2010-04-01/Accounts/AC808010d97a3e913acc49f1d84781e6db/Recordings/RE1351edc9819df3dbf71b7a73853eac7c",
        "zipcode" : "https://api.twilio.com/2010-04-01/Accounts/AC808010d97a3e913acc49f1d84781e6db/Recordings/RE1351edc9819df3dbf71b7a73853eac7c",
        "distance" : "https://api.twilio.com/2010-04-01/Accounts/AC808010d97a3e913acc49f1d84781e6db/Recordings/RE1351edc9819df3dbf71b7a73853eac7c",
        "description" : "https://api.twilio.com/2010-04-01/Accounts/AC808010d97a3e913acc49f1d84781e6db/Recordings/RE1351edc9819df3dbf71b7a73853eac7c"

    }
    information = ["123123123", True, d]
    tester = TwilioInformation(information)
    seeker = tester.get_link_info()

    print(seeker.get_name())
    print(seeker.get_age())
    
main()