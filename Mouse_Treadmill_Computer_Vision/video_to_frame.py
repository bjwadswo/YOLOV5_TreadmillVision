import cv2 
import argparse
import os

ROOT = os.getcwd() # store working directory for a default
def parse_opt(known=False): # function to parse arguments that can be called in a single line of if name main statement
    parser = argparse.ArgumentParser() # instantiate instance of parser
    # define argument parser for main function
    parser.add_argument('--load', default=ROOT,help='path within working directory containing videos to be loaded')
        # expects a folder with a list of videos. Function will iterate through all videos
    parser.add_argument('--save', default=ROOT,help='path within working directory to save frames')
    return parser.parse_known_args()[0] if known else parser.parse_args()


def main(load,save):
    for root, dirs, files in os.walk(load):
        video_list = files # get list of all videos in the video directory
    for i, video in enumerate(video_list):
        if str(video)[0] != ".":
            vidObj = cv2.VideoCapture(os.path.join(load,video)) # collects video object in cv2 framework
            count = 0 # count the frame number
            success = 1 # track when reached the end of the video
            while success:
                success, img = vidObj.read() # this will step by step read each frame of the video
                # don't want to save every frame. There was ~30k frames in the smallest 15min video
                # Guess that there is a total of 200-250k frames in the five selected training videos
                # want ~250-500 training images, try saving every 1000th frame
                if count % 1000 == 0: # execute code every 1000th frame
                    cv2.imwrite(f"{save}vid{i}frame{count}.jpg", img) # save within the frames folder, record video number and frame number
                count += 1 # count next frame


if __name__ == '__main__':
    opt = parse_opt() # parse_opt() gives a dictionary of parsed arguments
    print(opt)
    main(opt.load,opt.save)
