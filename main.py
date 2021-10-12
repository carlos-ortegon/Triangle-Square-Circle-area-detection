import cv2 as cv
import numpy as np

bluetriangle = 0
bluesquare = 0
bluecircle = 0
redtriangle = 0
redsquare = 0
redcircle = 0
whitetriangle = 0
whitesquare = 0
whitecircle = 0
bt = 0 
abt = 0 
bs = 0 
abss = 0 
bc = 0 
abc = 0  
rt = 0
art = 0 
rs = 0 
ars =0 
rc = 0 
arc = 0 
wt = 0 
awt = 0 
ws = 0 
aws = 0 
wc = 0 
awc = 0

print ""
print "ARTIFICIAL VISION"
print "PROJECT UNIT 1"
print ""

print "Introduce a number to select an image and press enter"
print "1. Small Figure         2. Big Figure"
select = input()
if select == 1:
    img = cv.imread('Small_figure.jpg')
    print "Small Figure selected"
elif select == 2:
    img = cv.imread('Big_Figure.png')
    print "Big Figure selected"


imgc = img
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)


lower_blue = np.array([80,110,60])
upper_blue = np.array([160,255,255])
bluemask = cv.inRange(hsv, lower_blue, upper_blue)
bluemix = cv.bitwise_and(img, img, mask=bluemask)
blueblur = cv.medianBlur(bluemix, 5)
bluegray= cv.cvtColor(blueblur, cv.COLOR_BGR2GRAY)
_, blueth = cv.threshold(bluegray,75,255,cv.THRESH_BINARY)
blueth = cv.dilate(blueth, None, iterations=1)
blueth = cv.erode(blueth, None, iterations=1)
bluecontours, bluehuerarchy = cv.findContours(blueth, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(imgc, bluecontours, -1, (0,255,0), 2)
for cb in bluecontours:
    blueepsilon = 0.047 * cv.arcLength(cb, True)
    blueapprox = cv.approxPolyDP(cb, blueepsilon, True)
    M = cv.moments(cb)
    if M["m00"] > 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv.circle(imgc, (cX, cY), 3, (0, 255, 0), -1)
    if len(blueapprox) == 3:
        bt = bt + 1
        areabt = cv.contourArea(cb)
        abt = abt + areabt
        bluetriangle += 1
    if len(blueapprox) == 4:
        bs = bs + 1
        areabs = cv.contourArea(cb)
        abss = abss + areabs
        bluesquare += 1
    if len(blueapprox) > 4: 
        bc = bc + 1
        areabc = cv.contourArea(cb)
        abc = abc + areabc
        bluecircle += 1


lower_red1 = np.array([0,100,75])
upper_red1 = np.array([10,255,255])
lower_red2 = np.array([175,100,75])
upper_red2 = np.array([180,255,255])
redmask1 = cv.inRange(hsv, lower_red1, upper_red1)
redmask2 = cv.inRange(hsv, lower_red2, upper_red2)
redmask = cv.add(redmask1, redmask2)
redmix = cv.bitwise_and(img, img, mask=redmask)
redblur = cv.medianBlur(redmix, 5)
redgray= cv.cvtColor(redblur, cv.COLOR_BGR2GRAY)
_, redth = cv.threshold(redgray,1,255,cv.THRESH_BINARY)
redcontours, redhierarchy = cv.findContours(redth, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(imgc, redcontours, -1, (0,255,0), 2)
for cr in redcontours:
    redepsilon = 0.04 * cv.arcLength(cr, True)
    redapprox = cv.approxPolyDP(cr, redepsilon, True)
    M = cv.moments(cr)
    if M["m00"] > 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv.circle(imgc, (cX, cY), 3, (0, 255, 0), -1)
    if len(redapprox) == 3:
        rt = rt + 1
        areart = cv.contourArea(cr)
        art = art + areart
        redtriangle += 1
    if len(redapprox) == 4:
        rs = rs + 1
        arears = cv.contourArea(cr)
        ars = ars + arears
        redsquare += 1
    if len(redapprox) > 4: 
        rc = rc + 1
        arearc = cv.contourArea(cr)
        arc = arc + arearc
        redcircle += 1


lower_white = np.array([0,0,200])
upper_white = np.array([250,100,255])
whitemask = cv.inRange(hsv, lower_white, upper_white)
whitemix = cv.bitwise_and(img, img, mask=whitemask)
whitegray= cv.cvtColor(whitemix, cv.COLOR_BGR2GRAY)
_, whiteth = cv.threshold(whitegray,216,230,cv.THRESH_BINARY)
whitecontours, whitehierarchy = cv.findContours(whiteth, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for cw in whitecontours:
    whiteepsilon = 0.04 * cv.arcLength(cw, True)
    whiteapprox = cv.approxPolyDP(cw, whiteepsilon, True)
    cv.drawContours(imgc, [whiteapprox], -1, (0,255,0), 2)
    M = cv.moments(cw)
    if M["m00"] > 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv.circle(imgc, (cX, cY), 3, (0, 255, 0), -1)
    if len(whiteapprox) == 3:
        wt = wt + 1
        areawt = cv.contourArea(cw)
        awt = awt + areawt
        whitetriangle += 1
    if len(whiteapprox) == 4:
        ws = ws + 1
        areaws = cv.contourArea(cw)
        aws = aws + areaws
        whitesquare += 1
    if len(whiteapprox) > 4: 
        wc = wc + 1
        areawc = cv.contourArea(cw)
        awc = awc + areawc
        whitecircle += 1


areatriangles = awt + art + abt
areasquares = aws + ars + abss
areacircles = awc + arc + abc 
areatotal = areatriangles + areacircles + areasquares

totalfigures = bluetriangle + bluesquare + bluecircle + redtriangle + redsquare + redcircle + whitetriangle + whitesquare + whitecircle
totaltriangles = bluetriangle + redtriangle
totalsquares = bluesquare + redsquare
totalcircles = bluecircle + redcircle

print ""
print "TRIANGLES"
print "Blue: ",bluetriangle
print "Red: ",redtriangle
print "White: ",whitetriangle
print "Area:", areatriangles
print ""
print "SQUARES"
print "Blue: ", bluesquare
print "Red: ", redsquare
print "White: ", whitesquare
print "Area: ", areasquares
print ""
print "CIRCLES"
print "Blue: ", bluecircle
print "Red: ", redcircle
print "White: ",whitetriangle
print "Area: ", areacircles
print ""
print "TOTALS"
print "Figures: ", totalfigures
print "Area: ", areatotal

if select == 1:
    cv.imwrite("Results/Small/Blue Segmentation.png", bluemix)
    cv.imwrite("Results/Small/Red Segmentation.png", redmix)
    cv.imwrite("Results/Small/White Segmentation.png", whitemix)
    cv.imwrite("Results/Small/Contours and Centroids.png", imgc)
if select == 2:
    cv.imwrite("Results/Big/Blue Segmentation.png", bluemix)
    cv.imwrite("Results/Big/Red Segmentation.png", redmix)
    cv.imwrite("Results/Big/White Segmentation.png", whitemix)
    cv.imwrite("Results/Big/Contours and Centroids.png", imgc)
cv.imshow("Blue Segmentation", bluemix)
cv.imshow("Red Segmentation", redmix)
cv.imshow("White Segmentation", whitemix)
cv.imshow("Contours and Centroids", imgc)

cv.waitKey(0)
cv.destroyAllWindows()

#Made with pain, suffering, frustration, and a lot of coffee