# Triangle-Square-Circle-area-detection
Code to identify a basic shapes, calculate their areas and show contours.

Using OpenCV and different filters, based on color segmentation, identifies and gets shaopes on the same color range and identifies which type of polygon the figure is and calculates its area.

Lets the user choose which of the 2 required images will be analyzed. Once the user selects the image, it is duplicated to draw operations over the copy and 
process the algorithm over the original image. After this, the image is converted from BGR to HSV format, given that color segmentation will be operated using HSV values.

Then, the code it’s split into three similar but different parts, where each of the parts will make a 
specific color segmentation operation based into a desired color range (in case of the red color 
recognition, there was required to use the addition of 2 different ranges) to make it´s individual 
shape recognitions later. All the segmentations are using the hsv image previously mentioned and 
each of them creates a mask and a mix of the color mask over the original image. Then, there are 
performed different operations or filters based on the color and aiming to have the best results for 
each color, being the following the filters and operations applied per color:

• Blue segmentation

  o Median blur
  
  o Gray scale
  
  o Binary threshold
  
  o Dilating
  
  o Eroding
  
• Red segmentation

  o Median Blur
  
  o Gray Scale
  
  o Binary threshold
  
• White segmentation

  o Gray scale
  
  o Binary threshold
  
  
Once applied the operations mentioned above, for each color there is applied the function 
cv.findcontours() for, as its name says, find the contours representing the shapes on each color 
segmentation. On red and blue segmentations, the contours are drawn over the copied original 
image at this point. 

Then, in a For loop working for each of the segmentations and under each of the recognized 
shapes, there is defined the epsilon variable to manage the accuracy of the shape recognition, 
working with cv.approxPolyDP() function. After this, there is drawn each of the shape centers 
using cv.moments() function.

Using the number of lines given by the approximation function, using If statements, there is make 
de decision if the image has 3, 4 or more than 4 lines, it will be a triangle, square or a circle 
respectively. Once identified the kind of shape, a counter for each type of color and figure is 
incremented by 1 and there is calculated the area of that specific shape, adding the calculated 
area to the total area for that kind of figures. In white segmentation, contours are drawn just after 
the for cycle and before if shape selector statements.

Now, after finishing all that process, we must have received the variables for the individual shape 
and total areas and the number of figures based on color, requiring only a few addition operations 
between them to get the totals wanted to display.

Now that we have our desired data, it is displayed on the command prompt, along the individual 
color segmentations in addition of shape and centroids, each of them in individual windows.
At last, the program waits for the user to press a key over any of the displayed images to close the 
program and finish the script execution.
