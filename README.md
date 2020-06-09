# InstagramCrop
A custom python script to automatically add a white square border to all images in a directory. 

Uses the Python Image Library (PIL)

##Usage
Call the script with "python3 insta.py" to uncrop all supported images files in current directory and
store them in a subdirectory 'SQUARES'.

You can also pass images as command line args i.e. "python3 insta.py dog.png cat.jpg" will only uncrop these
two files.

Supported flags for basic border colors:
  -black
  -blue
  -red
  -yellow
  -green
  -grey

###TODO:
-Allow user to specify output directory
-Allow for complex border backgrounds such as a resized-blurred version of the original image
