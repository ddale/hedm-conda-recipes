from optparse import OptionParser
import fabio
import numpy as n
from ImageD11.connectedpixels import *
from scipy import ndimage
import os


if __name__=='__main__':


  def get_options():
    parser = OptionParser()
    parser.add_option("-i", "--input", action="store",
                      dest="input", type="string",
                      help="name of image to correct")
    parser.add_option("-b", "--background", action="store",
                      dest="background", type="string",
                      help="name of background image")
    parser.add_option("-o", "--output", action="store",
                      dest="output", type="string",
                      help="name of corrected image")
    parser.add_option("-t", "--threshold", action="store",
                      dest="threshold", type="int",
                      default = 40,
                      help="intensity threshold")
    parser.add_option("-p", "--pixels", action="store",
                      dest="pixels", type="int",
                      default = 40,
                      help="number of pixels for signal")
 
    options , args = parser.parse_args()

    do_exit = False

    if options.input == None:
      print "\nNo input file name supplied [-i input]\n"
      do_exit = True
    if options.background == None:
      print "\nNo background file name supplied [-b background]\n"
      do_exit = True
    if options.output == None:
      print "\nNo output file name supplied [-o output]\n"
      do_exit = True
    if do_exit:
        parser.print_help()
        sys.exit()
    return options


  def correct_image(input,output,threshold,pixels,background):
      im = fabio.open(input)
      min = fabio.open(background)
      im.data = im.data - min.data
      # array to hold peak labels
      labels = n.zeros( im.data.shape, n.int )
      # determine which pixels in which peaks, how many peaks
      npeaks = connectedpixels( im.data, labels, threshold, 0 )
      # determine properties of each peak
      props = blobproperties( im.data, labels, npeaks, 0 )
      # number of pixels in peaks
      # labels go from 1->n with 0 being not in a peak...
      # ... so add an empty peak at zero to get match up
      npx = n.array([0,]+list( props[:, s_1]), n.int)
      npximage = n.take( npx, labels.ravel() )
      npximage.shape = labels.shape
      # You can now choose 1 when there is >10 px
      im1 = n.where( npximage>pixels, 10, 0)
      # ... or the original data
      im2 = n.where( npximage>pixels, im.data, 0)
      #smoothing
      for j in range(3):
          im1= ndimage.gaussian_filter(im1,1)
      # finally to save
      im.data = n.array(im1,dtype=n.uint16)
      im.write(output)

  options = get_options()
  correct_image(options.input,options.output,options.threshold,options.pixels,options.background)

