
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Initalize Cloudinary tags in your Django templates:
# {% load cloudinary %}

# cloudinary.config( 
#                   cloud_name = "dv77rliti", 
#                   api_key = "213853632381728", 
#                   api_secret = "QV24_tQRUyGwSl5UoDt9jd01SYk")

# Cloudinary's APIs allow secure uploading from your servers, directly from your visitors' 
#     browsers or mobile applications, or fetched via remote public URLs.

# how to upload an image to the cloud
    # def upload(file, **options)
    # OR...
    # cloudinary.uploader.upload("my_image.jpg")

# Setup the CLOUDINARY_URL environment variable by copying it from the Management Console:
# Using Windows command prompt/PowerShell
#   > set CLOUDINARY_URL=cloudinary://API-Key:API-Secret@Cloud-name

# In order to delete the uploaded images using Cloudinary's Admin API, run the script:
#     $ python basic.py cleanup
