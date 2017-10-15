# Photo-album
Photo Album exercise to practice S3
For more information about this topic don't forget to visit:
- The companion blog article - https://anzpiper.blogspot.com/2017/10/object-storage-for-cloud-foundry-apps.html
- The introduction to Boto S3 repository - https://github.com/cermegno/Boto-S3
# Description
This repo was developed for Pied Piper program 2017.
- Step 1 creates the album with the 3 sample photos in the "photos" directory
- Step 2 prompts the user for the author of the photo and it stores it as object metadata
# IMPORTANT
- This exercise makes use of the Boto library
- step 2 requires input through the console so it is not a good candidate for a "cf push". The "Author" information could be read from a text file with a small modification
## About Python versions
The original version of this repo was developed for Python 2.7. The python3 friendly version has been added in the folder called "_V3"
