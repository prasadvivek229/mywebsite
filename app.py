from flask import Flask, render_template
import psutil
from datetime import datetime

app = Flask(__name__)

request_count = 0

@app.route("/")
def home():

    global request_count
    request_count += 1

    with open("index.html","r",encoding="utf-8") as f:
        return f.read()


@app.route("/dashboard")
def dashboard():

    cpu = psutil.cpu_percent()

    memory = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    return render_template(

        "dashboard.html",

        cpu=cpu,

        memory=memory,

        disk=disk,

        requests=request_count,

        time=datetime.now()

    )



if __name__=="__main__":

    app.run(debug=True)