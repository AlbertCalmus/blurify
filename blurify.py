import sys
import imageio
import numpy as np
from PIL import Image, ImageFilter


def generate_video_from_img(img_path):
  img = Image.open(img_path)
  writer = imageio.get_writer('{}.mp4'.format(np.abs(hash(img_path))), format='FFMPEG', mode='I', fps=10)
    
  for i in range(100, -1, -1):
    new_frame = img.filter(ImageFilter.GaussianBlur(i))
    writer.append_data(np.asarray(new_frame))
  writer.close()
  print("  > Video successfully created!")

if __name__ == '__main__':
  generate_video_from_img(sys.argv[-1])
