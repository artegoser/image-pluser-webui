from PIL import Image, ImageFilter
import ffmpeg
import os


def images_to_video(directory, fps):
    glob_path = os.path.join(directory, "*.png")
    video_path = os.path.join(directory, "video.mp4")

    ffmpeg.input(glob_path, pattern_type="glob",
                 framerate=fps).output(video_path).run()
