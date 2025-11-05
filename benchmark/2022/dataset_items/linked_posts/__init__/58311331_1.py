if __name__ == '__main__':
    stream_link = "https://videos3.earthcam.com/fecnetwork/9974.flv/chunklist_w1421640637.m3u8"
    streamer = ThreadedCamera(stream_link)

    while True:
        frame = streamer.grab_frame()
        if frame is not None:
            cv2.imshow("Context", frame)
        cv2.waitKey(1) 
