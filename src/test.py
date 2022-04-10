from ast import keyword
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from geocoding import geo

cred = credentials.Certificate("src/hack-ku-3bc4e-firebase-adminsdk-mxlpu-91994f8fd4.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

job_list_ref = db.collection(u'Job_Listings').document(u'1113450987')
doc = job_list_ref.get()
doc = doc.to_dict()

applicants_list = []

min_age = doc['Min_age']
keywords = doc['Keywords']
zipcode = doc['Zipcode']

print(min_age, keywords, zipcode)

applicants_ref = db.collection(u'Applicants')
query = applicants_ref.where(u'Age', u'>=', min_age).where(u'Keywords', u'array_contains_any', keywords)
print(query)
docs = query.stream()
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')