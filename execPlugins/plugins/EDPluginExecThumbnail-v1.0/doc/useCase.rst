This EDNA execution plugin generates thumbnails,

This means that it takes an image from a detector (Frelon, MarCCD, ...) wich is read 
as a 2D array or integer or floats using the Fabio library and then converted into an
image using the Python Imaging Library.

The output format is usually JPEG or PNG, by default in black & white. we call this thumbnails
as they are most of the time smaller than the original image (2k x 2k) and due to the output format 
which is 8bit unsigned integer, a lot of imformation is lost. Neverthless such transformation is 
needed for  easy / online visualization of the results.   

There are some usefull options not set by default like:
-gamma to enhance the lighter part of the image. gamma=0.3 is most of the time a good starting point.  
-colorize to get a nice colorized image with a color scale going from black-blue-red-yellow-white. 
   
I strongly advise you to run the test suite with

  $EDNA_HOME/kernel/bin/edna-test-launcher.py --test EDTestSuitePluginExecThumbnailv10 

as it contains some routines to install all the needed libraries like Fabio, PIL, Numpy and Scipy within EDNA. 