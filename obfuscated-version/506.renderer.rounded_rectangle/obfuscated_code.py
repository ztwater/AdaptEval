import cv2
import numpy as np

def rounded_rectangle(var_0, var_1, var_2, var_3=1, var_4=255, var_5=1, var_6=cv2.LINE_AA):

    #  corners:
    #  p1 - p2
    #  |     |
    #  p4 - p3

    var_7 = var_1
    var_8 = (var_2[1], var_1[1])
    var_9 = (var_2[1], var_2[0])
    var_10 = (var_1[0], var_2[0])

    var_11 = abs(var_2[0] - var_1[1])

    if var_3 > 1:
        var_3 = 1

    var_12 = int(var_3 * (var_11/2))

    if var_5 < 0:

        #big rect
        var_13 = (int(var_7[0] + var_12), int(var_7[1]))
        var_14 = (int(var_9[0] - var_12), int(var_9[1]))

        var_15 = (var_7[0], var_7[1] + var_12)
        var_16 = (var_10[0] + var_12, var_10[1] - var_12)

        var_17 = (var_8[0] - var_12, var_8[1] + var_12)
        var_18 = (var_9[0], var_9[1] - var_12)

        var_19 = [
        [var_13, var_14], 
        [var_15, var_16], 
        [var_17, var_18]]

        [cv2.rectangle(var_0, rect[0], rect[1], var_4, var_5) for rect in var_19]

    # draw straight lines
    cv2.line(var_0, (var_7[0] + var_12, var_7[1]), (var_8[0] - var_12, var_8[1]), var_4, abs(var_5), var_6)
    cv2.line(var_0, (var_8[0], var_8[1] + var_12), (var_9[0], var_9[1] - var_12), var_4, abs(var_5), var_6)
    cv2.line(var_0, (var_9[0] - var_12, var_10[1]), (var_10[0] + var_12, var_9[1]), var_4, abs(var_5), var_6)
    cv2.line(var_0, (var_10[0], var_10[1] - var_12), (var_7[0], var_7[1] + var_12), var_4, abs(var_5), var_6)

    # draw arcs
    cv2.ellipse(var_0, (var_7[0] + var_12, var_7[1] + var_12), (var_12, var_12), 180.0, 0, 90, var_4 ,var_5, var_6)
    cv2.ellipse(var_0, (var_8[0] - var_12, var_8[1] + var_12), (var_12, var_12), 270.0, 0, 90, var_4 , var_5, var_6)
    cv2.ellipse(var_0, (var_9[0] - var_12, var_9[1] - var_12), (var_12, var_12), 0.0, 0, 90,   var_4 , var_5, var_6)
    cv2.ellipse(var_0, (var_10[0] + var_12, var_10[1] - var_12), (var_12, var_12), 90.0, 0, 90,  var_4 , var_5, var_6)

    return var_0
