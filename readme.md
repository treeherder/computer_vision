opencv scripts for pick-and-place

includes research materials where relevant

targeted at mac OSX mavericks python2.7

opencv installed with homebrew.... each dependency was installed manually .. in this case, eigen, qt, and  a reinstall of cmake.  in some cases, numpy / scipy will need to be installed as well

to do:
___________________

- [x] find contours
- [x] test with wires
- [x] mask object
- [x] implement template matching
- [ ] find  coordinates of masked + matching object
- [ ] auto-range for thresholding based on expected values
- [ ] integrate the components into a single toolchain


video
--------------------
<dl>
<dt>3dcam</dt>
<dd>supports the kinect through libfreenect, tweaked some fairly straightforward video feed example, powered from a desktop power supply</dd>
<dt>cntr</dt>
<dd>does single largest blob tracking in video, look for the blue dot </dd>
using static images
--------------------
<dt> cell</dt>
<dd>usage: `python cell.py <image.jpg>`</dd>
<dd>the image should be within ~/projects/cv/images and should be already thresholded</dd>
<dd>the bread-and-butter of this project: working on actually identifying the cell on a field</dd>
<dt> wire </dt>
  <dd>usage: `python wire.py <image.jpg>`</dd>
  <dd>this is a clone of cell that works off of wire_thresholding to threshold values for the wire</dd>
<dt> wire_thresholding</dt>
<dd>usage: `python wire_thresholding.py <img.jpg>` </dd>
<dd>a direct clone of thresholding as a placeholder for a more dynamic toolchain</dd>
<dt>thresholding</dt>
<dd>the lynchpin of the rest of the software, performs thresholding operations to reduce noise</dd>
<dd>usage: `python thresholding.py <img.jpg>` </dd>
<dd>runs behind cell, to smooth the transition </dd>
<dd>displays the thresholded image and saves it</dd>
<dt>corner.py</dt>
<dd>foundation functions for edge detection sloppy but reasonably quick</dd>
<dt>good_corner</dt>
<dd>just a demo from the tutorial... pretty accurate but savagely slow.</dd>
<dt>contours</dt>
<dd>an attempt to define the longest continuous rect</dd>
<dt>square and sq2</dt>
<dd>attempts to find black square</dd>
