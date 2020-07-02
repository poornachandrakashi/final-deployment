from flask import render_template,request
import os
import time

from aakraman_api.packages.test import test 
from aakraman_api.packages.data import get_df

from aakraman_api import app
from aakraman_api.model import User 

#maybe make it into blueprint later

@app.route('/')
def home():
    return render_template("main.html")

@app.route("/akraman-app")
def akraman():
    return render_template("contact.html")

@app.route("/team")
def team():
    return render_template("team1.html")

@app.route("/audio")
def audio():
    return render_template("audio.html")

@app.route("/xray")
def xray():
    return render_template("xray.html")

@app.route("/xraysubmit", methods = ['POST', 'GET'])
def xray_submit():
    image1 = request.files['image']
    ts = time.gmtime()
    uploadtime = time.strftime("%Y%m%d%H%M%S", ts)
    filename = "image" + uploadtime + ".jpg"
    filename = os.path.join('aakraman_api/static/images/test/',filename)
    app.logger.info("File to upload: ")
    app.logger.info(filename)
    image1.save(filename)
    destination_file1 = "result" + uploadtime + ".jpg"
    destination_file = os.path.join("aakraman_api/static/images/result/", destination_file1)
    result = test("aakraman_api/models/covid19.model", filename, destination_file)
    return render_template('xray-submit.html', image = "static/images/result/"+destination_file1, result = result)

@app.route("/check")
def check():
    return render_template("xraysubmit_new.html")

@app.route('/covid')
def covid():
	df = get_df()
	return render_template('covid.html', table = df.to_html(index = False, justify = 'center', classes = ['set-center','table', 'table-striped', 'table-borderless']))
