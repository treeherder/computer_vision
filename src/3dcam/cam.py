#!/usr/bin/env python
from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import cv2  
import numpy as np
global depth, rgb
def main():
  # Get a fresh frame
  (depth,_), (rgb,_) = get_depth(), get_video()
  # Build a two panel color image
  d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
  da = np.hstack((d3,rgb))
  # Simple Downsample
  cv2.imshow('both',np.array(da[::2,::2,::-1]))
        
while True:
  main()
  if cv2.waitKey(5)==27:   #press esc to exit  
    break
    cv2.destroyAllWindows()