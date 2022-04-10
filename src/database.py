from turtle import distance
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from geocoding import geo

class Database:
  def __init__(self, is_applicant, obj) -> None:
    cred = credentials.Certificate("src/hack-ku-3bc4e-firebase-adminsdk-mxlpu-91994f8fd4.json")
    firebase_admin.initialize_app(cred)
    self._db = firestore.client()
    self._is_applicant = is_applicant
    if self._is_applicant:
      self._applicant = obj
    else:
      self._job_listing = obj
  
  def get_applicant(self):
    min_age = self._job_listing.get_min_age()
    zipcode = self._job_listing.get_zipcode()
    keywords = self._job_listing.get_keywords()
    applicants_list = []

    applicants_ref = self._db.collection(u'Applicants')
    query = applicants_ref.where(u'Keywords', u'array_contains_any', keywords).where(u'Age', u'>=', min_age)
    apps = query.stream() 
    
    for app in apps:
      distance = geo.haversine(geo.extract_lat_long_via_address(app.to_dict()['Zipcode']),geo.extract_lat_long_via_address(zipcode))
      if distance < app.to_dict()['Distance']:
        applicants_list.append(app.to_dict())
    
    return applicants_list

  def get_job_listing(self):
    age = self._applicant.get_age()
    zipcode = self._applicant.get_zipcode()
    dist = self._applicant.get_distance()
    keywords = self._applicant.get_keywords()
    job_listing_list = []

    job_listing_ref = self._db.collection(u'Job_Listings')
    query = job_listing_ref.where(u'Keywords', u'array_contains_any', keywords).where(u'Min_age', u'<=', age)
    jobs = query.stream()

    for job in jobs:
      distance = geo.haversine(geo.extract_lat_long_via_address(zipcode),geo.extract_lat_long_via_address(job.to_dict()['Zipcode']))
      if distance < dist:
        job_listing_list.append(job.to_dict())

    return job_listing_list
    
  def set_applicant(self):
    applicant_ref = self._db.collection(u'Applicant').document(self._applicant.get_phone_number())
    applicant_ref.set({
      u'Phone_number': self._applicant.get_phone_number(),
      u'Name': self._applicant.get_name(),
      u'Age': self._applicant.get_age(),
      u'Zipcode': self._applicant.get_zipcode(),
      u'Distance': self._applicant.get_distance,
      u'Keywords': self._applicant.get_keywords(),
      u'Description': self._applicant.get_description(),
      u'Links': self._applicant.get_links()
    })

  def set_job_listing(self):
    job_listing_ref = self._db.collection(u'Job_Listings').document(self._job_listing.get_phone_number())
    job_listing_ref.set({
      u'Phone_number': self._job_listing.get_phone_number(),
      u'Name': self._job_listing.get_name(),
      u'Min_age': self._job_listing.get_min_age(),
      u'Zipcode': self._job_listing.get_zipcode(),
      u'Keywords': self._job_listing.get_keywords(),
      u'Description': self._job_listing.get_description(),
      u'Links': self._job_listing.get_links()
    })

  def run(self):
    if self._is_applicant:
      job_listings_return = self.get_job_listing()
      return job_listings_return
    else:
      applicants_return = self.get_applicant()
      return applicants_return