from django.shortcuts import render
from dotenv import load_dotenv
import os
import pyrebase

load_dotenv()

config={
    "apiKey": os.environ.get("API_KEY"),
    "authDomain": os.environ.get("AUTH_DOMAIN"),
    "databaseURL": os.environ.get("DB_URL"),
    "projectId": os.environ.get("PROJECT_ID"),
    "storageBucket": os.environ.get("STORAGE_BUCKET"),
    "messagingSenderId": os.environ.get("MESSAGING_SENDER_ID"),
    "appId": os.environ.get("APP_ID")
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Create your views here.
def LoginPage(req):
    return render(req, 'index.html')

def PostLogin(req):
    email = req.POST.get('user')
    pwd = req.POST.get('pass')

    try:
        user = auth.sign_in_with_email_and_password(email, pwd)
    except:
        message = "Email or Password is incorrect!!!"
        return render(req, "index.html", {"message": message})
    session_id = user['idToken']
    req.session['uid'] = str(session_id)
    return render(req, 'index.html')

def PostLoginGmail(req):
    email = req.POST.get('user')
    pwd = req.POST.get('pass')

    try:
        user = auth.sign_in_with_email_and_password(email, pwd)
    except:
        message = "Email or Password is incorrect!!!"
        return render(req, "index.html", {"message": message})
    session_id = user['idToken']
    req.session['uid'] = str(session_id)
    return render(req, 'index.html')

def Logout(req):
    try:
        del req.session['uid']
    except:
        pass
    return render(req, "index.html")

def Register(req):
    return

def PostRegister(req):
    email = req.POST.get('sign-up-user')
    pwd = req.POST.get('sign-up-pass')
    return