#!/usr/bin/env python2
import os
import boto
from flask import Flask

app = Flask(__name__)

ecs_access_key_id = '11112222333344455@ecstestdrive.emc.com'  
ecs_secret_key = 'VaB5Fh72B7G+7JQqBjEMZ3KErt12IDFxUrPWkpnG'

session = boto.connect_s3(ecs_access_key_id, ecs_secret_key, host='object.ecstestdrive.com')  

bname = 'photobook'

b = session.get_bucket(bname)
print "ECS connection is: " + str(session)
print "Bucket is: " + str(b)

print "Uploading photos ..."
for each_photo in os.listdir("photos"):
    print "Uploading " + str(each_photo)
    k = b.new_key(each_photo)
    ## Now we need to ask for extra information
    author = raw_input ("Who is the author of this photograph?")
    ## and store it as metadata
    k.set_metadata('author', author)
    src = os.path.join("photos", each_photo)
    k.set_contents_from_filename(src)
    k.set_acl('public-read')

print "Upload complete!"
print "Starting the photoalbum"

@app.route('/')
def mainmenu():

    begin_page = """
    <html>
    <head>
        <style>
        body {background-image: url("static/backgr2.jpg");} 
        </style>
    </head>
    <body>
    <center><h1>My first photo-book in Python</h1>"""
    mid_page = ""
    for photo in b.list():
        #print(photo.key)
        k = b.get_key(photo)
        ##Don't forget to pull the metadata and use it to build the album
        author = k.get_metadata('author')
        mid_page += """<hr><h2>{}</h2><h3><i>by {}</i></h3>
        <img src="http://131030155286710005.public.ecstestdrive.com/photobook/{}"
        width=500><br>""".format(photo.key, author, photo.key)
    end_page = """
    </center>
    </body>
    </html>"""

    return begin_page + mid_page + end_page

if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', '5000')), threaded=True)
