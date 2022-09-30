import pyrebase

config = {
    "apiKey": "AIzaSyCKAsu8jsEfvwpTll9g9a-sC9syZ5UwOkY",
  "authDomain": "chat-1b421.firebaseapp.com",
  "databaseURL": "https://chat-1b421.firebaseio.com",
  "projectId": "chat-1b421",
  "storageBucket": "chat-1b421.appspot.com",
  "messagingSenderId": "18208425351",
  "appId": "1:18208425351:web:819cefb51a9bee258a7f22",
  "measurementId": "G-9ME51QYBZF"
}


firebase = pyrebase.initialize_app(config)

db = firebase.database()

def cont(ip):
    ip = str(ip)
    c=db.child(f"ip/{ip}").get(ip).val()
    if c == None:
        db.child(f"ip/{ip}").set(1)
        return 23
    else:
        c = c+1
        db.child("ip").update({ip:c})
        return 27
    