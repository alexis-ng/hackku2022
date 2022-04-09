import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("database/hack-ku-3bc4e-firebase-adminsdk-mxlpu-91994f8fd4.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'Job_List').document(u'Job_1')
doc_ref.set({
    u'Age': 35,
    u'Location': {
      u'City': u'Lawrence', 
      u'Zip_code': 66044
      },
    u'Description': u'We are looking for a full time electrician'
})

users_ref = db.collection(u'Job_List')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')