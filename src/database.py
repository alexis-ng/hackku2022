import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from geocoding import geo

class Database:
  def __init__(self, is_applicant, obj) -> None:
    cred = credentials.Certificate("database/hack-ku-3bc4e-firebase-adminsdk-mxlpu-91994f8fd4.json")
    firebase_admin.initialize_app(cred)
    self._db = firestore.client()
    self._is_applicant = is_applicant
    if self._is_applicant:
      self._applicant = obj
    else:
      self._job_listing = obj
  
  def get_applicant(self):
    pass

  def get_job_listing(self):
    pass

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
      pass
    else:
      pass
    
    
    
    

    # doc_ref = db.collection(u'Job_List').document(u'Job_3')
    # doc_ref.set({
    #     u'Age': 33,
    #     u'Location': {
    #       u'City': u'Olathe', 
    #       u'Zip_code': 66061
    #       },
    #     u'Description': u'We are looking for a full time mechanic'
    # })

    # users_ref = db.collection(u'Job_List')
    # docs = users_ref.stream()

    # for doc in docs:
    #     print(f'{doc.id} => {doc.to_dict()}')