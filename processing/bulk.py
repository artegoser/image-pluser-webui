from PIL import Image, ImageFilter
import ffmpeg
import os
from processing.utils import generate_name, get_date_text


def images_to_video(directory, fps, img_ext, img_name_format, video_name, video_ext, video_dir):
    images_pattern = os.path.join(directory, f"{img_name_format}.{img_ext}")

    if video_dir:
        video_path = os.path.join(video_dir, f"{video_name}.{video_ext}")
    else:
        video_path = generate_name(
            extension=video_ext, name=video_name, subfolder="videos")

    ffmpeg.input(images_pattern,
                 framerate=fps).output(video_path, pix_fmt='yuv420p').global_args("-y").run()


def video_to_images(video_path, img_ext):

    images_pattern = generate_name(
        extension=img_ext, name=f"%d", subfolder=os.path.join("images", get_date_text()))

    ffmpeg.input(video_path).output(images_pattern).run()
