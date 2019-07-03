import pyscreenshot as imggrab
import time
import pytesseract
import traceback

# x and y coordinates of the part of screen you want to grab and convert to text
start_x = 353
start_y = 469
end_x = 715
end_y = 577

seconds_to_run_capture = 500

print ("sleeping before capture")
time.sleep(2)
print ("staring capture")

# config for tesseract
# '-l eng'  for using the English language
# '--oem 1' for using LSTM OCR Engine
config = ('-l eng --oem 1 --psm 3') 

# run for 500 seconds
for i in range(seconds_to_run_capture):
    try:
        img = imggrab.grab(bbox=(start_x,start_y,end_x,end_y))
        # img.save(str(datetime.datetime.now().time()) + ".png")    # uncomment this to save the image to the working dir
        text = pytesseract.image_to_string(img, config=config)
        print (text)
        # print ("Grabbed image id %d " % i)
        time.sleep(1)                                               # sleep for one seconds before capturing second frame
    except Exception as e:
        print ("Exception - " + str(e))
        traceback.print_exc()
        break

print ("Exiting...")