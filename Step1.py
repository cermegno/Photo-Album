#!/usr/bin/env python2
import os
import boto
from flask import Flask

app = Flask(__name__)

ecs_access_key_id = '11112222333344455@ecstestdrive.emc.com'  
ecs_secret_key = 'VaB5Fh72B7G+7JQqBjEMZ3KErt12IDFxUrPWkpnG'

## Open a session with your ECS
session = boto.connect_s3(ecs_access_key_id, ecs_secret_key, host='object.ecstestdrive.com')  
## Get hold of your bucket
bname = 'photobook'
b = session.get_bucket(bname)
print "ECS connection is: " + str(session)
print "Bucket is: " + str(b)

print "Uploading photos ..."
## Create a list of filenames in "photos" to upload to ECS
for each_photo in os.listdir("photos"):
    print "Uploading " + str(each_photo)
    k = b.new_key(each_photo)
    src = os.path.join("photos", each_photo)
    k.set_contents_from_filename(src)
    k.set_acl('public-read')

## Alterntively walk recursively a dir tree. It creates a string and 2 lists
##
##for (dirpath, dirnames, filenames) in os.walk("photos"):

print "Upload complete!"
print "Starting the photoalbum"

@app.route('/')
def mainmenu():

    begin_page = """
    <html>
    <body>
    <center><h1>My first photo-book in Python</h1>"""

    mid_page = ""
    ## List all the keys in the bucket and grab the images with html code
    for photo in b.list():
        print(photo.key)
        mid_page += """<hr><h2>{}</h2>
        <img src="http://131030155286710005.public.ecstestdrive.com/photobook/{}" width=500><br>""".format(photo.key, photo.key)
    
    end_page = """
    </center>
    </body>
    </html>"""

    return begin_page + mid_page + end_page

if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', '5000')), threaded=True)
