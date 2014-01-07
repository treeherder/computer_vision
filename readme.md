opencv scripts for pick-and-place

includes research materials where relevant

targeted at mac OSX mavericks python2.7

opencv installed with homebrew.... each dependency was installed manually .. in this case, eigen, qt, and  a reinstall of cmake.  in some cases, numpy / scipy will need to be installed as well

video
--------------------
<dl>
<dt>3dcam</dt>
<dd>supports the kinect through libfreenect, tweaked some fairly straightforward video feed example, powered from a desktop power supply</dd>
<dt>cntr</dt>
<dd>does single largest blob tracking in video, look for the blue dot </dd>
using static images
--------------------
<dt>thresholding</dt>
<dd>the lynchpin of the rest of the software, performs thresholding operations to reduce noise</dd>
<dd>usage: `python thresholding.py --image <img xyz.jpg>` </dd>
<dd>displays the thresholded image and saves it</dd>
<dt>corner.py</dt>
<dd>foundation functions for edge detection sloppy but reasonably quick</dd>
<dt>good_corner</dt>
<dd>just a demo from the tutorial... pretty accurate but savagely slow.</dd>
<dt>contours</dt>
<dd>an attempt to define the longest continuous rect</dd>
<dt>square and sq2</dt>
<dd>attempts to find black square</dd>