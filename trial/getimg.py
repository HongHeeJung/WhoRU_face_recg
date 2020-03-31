# -*- coding: UTF-8 -*-
try:
    from google.cloud import storage
except ImportError:
    raise ImportError('Failed to import the Cloud Storage library for Python. Make sure '
                      'to install the "google-cloud-storage" module.')
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import datetime
import urllib.request

db_url = 'https://whoru-ed991.firebaseio.com/'
sr_buck = 'whoru-ed991.appspot.com'
cred = credentials.Certificate("./whoru-ed991-firebase-adminsdk-o6sq7-2aa9f68fea.json")
db_app = firebase_admin.initialize_app(cred, {'databaseURL': db_url})
sr_app = firebase_admin.initialize_app(cred, {'storageBucket': sr_buck,}, name='storage')
# ref = db.reference('/whoru-ed991')
ref = db.reference()


def find_user():
    rd = ref.child('10주 1300/Request Detection/').get()
    if rd == 1:
        username = ref.child('10주 1300/username/').get()
        print(username)


bucket = storage.bucket(app=sr_app)
# 핸드폰에서 firebase에 저장할 때 비교 사진 저장 이름이 중요
blob = bucket.blob("WhoRU_target/jacob.jpg")
img_url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
# print(img_url)
find_user()
# firebase에서 폴더에 저장할 때 비교 사진 이름 중요 -> face recognition
urllib.request.urlretrieve(img_url, './knn_examples/train/{}.jpg'.format(username))
print("save")

