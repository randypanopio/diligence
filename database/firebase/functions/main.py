# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

# i dunno wtf this does but it fixes my problem about "OSError: Project was not passed and could not be determined from the environment." lol
import os
os.environ.setdefault("GCLOUD_PROJECT", "ddiligence-project")

# The Cloud Functions for Firebase SDK to create Cloud Functions and set up triggers.
from firebase_functions import firestore_fn, https_fn

# The Firebase Admin SDK to access Cloud Firestore.
from firebase_admin import initialize_app, firestore, credentials
from google.cloud import firestore


from datetime import datetime, timedelta

cred = credentials.Certificate('super_secrets/serviceAccKey.json')

db = firestore.Client()

initialize_app()

# daily function to update db with new data

print("complete!")