import cv2

#Our Image
img_file = 'car_image.png'

#Our pre trained car classifier
classifier_file = 'car_dector.xml'


#create an opencv image
img = cv2.imread(img_file)


# convert to grayscale (need for here cascade)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#create car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

#detect car
cars = car_tracker.detectMultiScale(black_n_white)

print(cars)

#display the image with the faces spotted
cv2.imshow('Car Detector', black_n_white)


#Dont autoclose (Wait here in the code and listen for a key press)
cv2.waitKey()


print("Code Complete")