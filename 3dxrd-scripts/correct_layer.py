import numpy as n
import os

layers = range(1)
images = 720
start_image = 1628
#images = 120
#start_image = 2228
threshold_i2 = 25
threshold_p = 25

for l in layers:
    stem = "austenite_1_" 
    imagedir = "../NF_data" 
    savedir = "../cor2_NF_data" 
    try:
        os.system("mkdir %s" %savedir)
    except:
        pass
    #calculate min

    background = "%s/minimum.edf" %(imagedir)
    #apply connectivity search on scaled
    counter = 1
    for i in range(0,images):
        input = "%s/%s%0.5d.tif" %(imagedir,stem,i+start_image)
        output = "%s/%s%0.5d.tif" %(savedir,stem,i+start_image)
        print input, output, "star2 ",i+1,counter,images
        command = "python correct_one.py -i %s -b %s -o %s -t %i -p %i" %(input,background,output,threshold_i2,threshold_p)
        try:
            os.system(command)
        except:
            continue
        counter = counter + 1


