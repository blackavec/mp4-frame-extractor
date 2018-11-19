import argparse

def setup():
  parser = argparse.ArgumentParser(description='export jpeg frame out of mp4 video.')

  parser.add_argument('--video', help='source of video', required=True)
  parser.add_argument('--frame', help='number of frame you wish to export', default=1, required=True)
  parser.add_argument('--out', help='export destination directory')

  return parser.parse_args()