import cv2

#Our Image
img_file = 'car_image.png'
video = cv2.VideoCapture('Pedestrians Compilation.mp4')

#Our pre trained car and pedestrian classifier
car_tracker_file = 'car_dector.xml'
pedestrian_tracker_file = 'haarcascade_fullbody.xml'

#create car classifier
car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

#Runs forever
while True:
    #Read the current frame
    (read_successful, frame) = video.read()

    if read_successful:
        #must convert to grayscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    #detect car
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    
    #Draw rectangles around the cars
    for(x, y, w, h) in cars:
        cv2.rectangle(frame, (x+1, y+2), (x+w, y+h), (225, 0, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 225), 2)


    #Draw rectangles around the pedestrians
    for(x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 225, 225), 2)

    
     # display video
    cv2.imshow('Car and Pedestrian Detector',frame)

    #Dont autoclose (Wait here in the code and listen for a key press)
    cv2.waitKey(1)
    print("Code Complete")

    #Stop execution if press Q
    if key==81 or key=113:
        break


    

# """"
# #create an opencv image
# img = cv2.imread(img_file)


# # convert to grayscale (need for here cascade)
# black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# #create car classifier
# car_tracker = cv2.CascadeClassifier(classifier_file)

# #detect car
# cars = car_tracker.detectMultiScale(black_n_white)

# #Draw rectangles around the cars
# for(x, y, w, h) in cars:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 225), 2)


# #display the image with the faces spotted
# cv2.imshow('Car Detector', img)


# #Dont autoclose (Wait here in the code and listen for a key press)
# cv2.waitKey()


# print("Code Complete")


# """

# #image detection
# """"
# import cv2

# #Our Image
# img_file = 'car_image.png'
# video = cv2.VideoCapture('Pedestrian Compilation.mp4')

# #Our pre trained car classifier
# classifier_file = 'car_dector.xml'

# #Runs forever
# while True:

#     #Read the current frame
#     read_successful, frame = video.read()

# #create an opencv image
# img = cv2.imread(img_file)


# # convert to grayscale (need for here cascade)
# black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# #create car classifier
# car_tracker = cv2.CascadeClassifier(classifier_file)

# #detect car
# cars = car_tracker.detectMultiScale(black_n_white)

# #Draw rectangles around the cars
# for(x, y, w, h) in cars:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 225), 2)


# #display the image with the faces spotted
# cv2.imshow('Car Detector', img)


# #Dont autoclose (Wait here in the code and listen for a key press)
# cv2.waitKey()


# print("Code Complete")
# """
