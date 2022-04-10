import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Database:
  def __init__(self, is_applicant, obj) -> None:
    cred = credentials.Certificate("database/hack-ku-3bc4e-firebase-adminsdk-mxlpu-91994f8fd4.json")
    firebase_admin.initialize_app(cred)
    self._db = firestore.client()
    self._is_applicant = is_applicant
    if self._is_applicant:
      self._applicants = obj
    else:
      self._job_listing = obj
  
  def get_applicant(self):
    pass

  def get_job_listing(self):
    pass

  def set_applicant(self):
    pass

  def set_job_listing(self):
    pass

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