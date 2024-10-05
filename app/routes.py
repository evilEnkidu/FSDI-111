from flask import Flask
app = Flask(__name__)
@app.get("/aboutme")
def get_home():
        me = {
                "first_name":"Emiliano",
                "last_name":"Magana",
                "hobbies":"REDACTED",
                "is_online": True
        }
        return me
