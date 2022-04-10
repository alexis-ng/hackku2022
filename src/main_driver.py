import zmq
import json
from run_serv import info
from twl_sms import send_sms

y = json.loads(message)
x = []
x.append(y.phone_number)
is_app = not("job_loc" in y.keys())
x.append(is_app)
if (is_app):
    dic = {
        "name":y.name
        "age":y.age
        "zipcode":y.location
        "distance":y.will_move
        "description":y.job_qual
    }
else:
    dic = {
            "name":y.name
            "min_age":y.age_of_employee
            "zipcode":y.job_loc
            "description":y.job_descrip
        }
x.append(dic)
list_ = info(x)
if (is_app):
    for items in list_:
        bd = ""
        for (key, value) in dic.items():
            if key=='Name' or key=='Zipcode' or key=="Description" or key=="Phone_number":
                bd += f"{key}: {value}\n"
        send_sms(y.phone_number, bd)
else:
    for items in list_:
        bd = ""
        for (key, value) in dic.items():
            if key=='Name' or key=="Zipcode" or key=="Distance" or key == "Description" or key=="Phone_number":
                bd += f"{key}: {value}\n"
        send_sms(y.phone_number, bd)
#  Send reply back to client


