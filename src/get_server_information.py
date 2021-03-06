# from unicodedata import name
# from numpy import extract
import requests
from src.stt import Recognize
from job_seeker import Job_Seeker
from extract_keywords import Extractor
from job_listing import JobListing

def get_info(url, file_name):
    doc = requests.get(url, stream=True)
    with open(file_name, 'wb') as f:
        f.write(doc.content)
    sr = Recognize(file_name)
    return sr.convert_to_text()

def extract_description(desc):
    extractor = Extractor(desc)
    return extractor.extract()

class TwilioInformation:
    def __init__(self, information) -> None:
        self._phone_number = information[0]
        self._is_applicant = information[1]
        self._links = information[2]

 
    def get_applicant_status(self):
        return self._is_applicant


    def get_link_info(self):
        if self._is_applicant:
            # create a new applicant
            seeker = Job_Seeker(phone_number=self._phone_number)
            
            name = get_info(self._links["name"], "name")
            age = int(get_info(self._links["age"], "age"))
            zipcode = int(get_info(self._links["zipcode"], "zipcode"))
            distance = get_info(self._links["distance"], "distance")
            try:
                distance = int(distance)
            except:
                distance = None
            description = get_info(self._links["description"], "description")
            keywords = extract_description(description)

            seeker.set_name(name)
            seeker.set_age(age)
            seeker.set_zipcode(zipcode)
            seeker.set_distance(distance)
            seeker.set_description(description)
            seeker.set_keywords(keywords)
            seeker.set_links = self._links
            
            return seeker
        
        else:
            # create a new job
            job = JobListing(phone_number=self._phone_number)
            
            name = get_info(self._links["name"], "name")
            min_age = int(get_info(self._links["min_age"], "min_age"))
            zipcode = int(get_info(self._links["zipcode"], "zipcode"))
            description = get_info(self._links["description"], "description")
            keywords = extract_description(description)

            job.set_name(name)
            job.set_min_age(min_age)
            job.set_zipcode(zipcode)
            job.set_description(description)
            job.set_keywords(keywords)
            job.set_links(self._links)

            return job


