y0, dy, text = 185,50, "FPS: "+str(framerate)+"\nMIN: "+str(frMIN)+"\nMAX: "+str(frMAX)+"\nAVG: "+str(frAVG)
for i, line in enumerate(text.split('\n')):
    y = y0 + i*dy
    cv2.putText(currStack, line, (50, y ), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA, False)
