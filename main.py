#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import datetime
import time
from fonts.ttf import RobotoMedium
import subprocess

i2c = busio.I2C(SCL, SDA)

WIDTH = os.environ.get('WIDTH', 128)
HEIGHT = os.environ.get('HEIGHT', 32)
ROTATE = os.environ.get('ROTATE', False)

def clear():
  display.fill(0)
  display.image(im)

display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

im = Image.new("1", (WIDTH, HEIGHT), 0)
draw = ImageDraw.Draw(im)

def show(text):
  clear()

  for point_size in range(5, 38):
    font = ImageFont.truetype(RobotoMedium, point_size)
    _, _, w, h = font.getbbox(text)
    
    if w > WIDTH - 2 or h > HEIGHT - 2:
      point_size = point_size - 1
      break

    box_width = w
    box_height = h


  draw.rectangle([0, 0, WIDTH, HEIGHT], fill=0)
  draw.text(((WIDTH-box_width)/2, (HEIGHT-box_height)/2), text, align='center', font=ImageFont.truetype(RobotoMedium, point_size), fill=1)
  rotated_image = im.transpose(Image.ROTATE_180) if ROTATE else im
  display.image(rotated_image)
  display.show()

while True:
  cmd = "hostname"
  host = subprocess.check_output(cmd, shell = True )
  show(host)
  cmd = "hostname -I |cut -f 1 -d ' '"
  ip = subprocess.check_output(cmd, shell = True )
  show(ip)
  time.sleep(15)
  cmd = "top -bn1 | grep load | awk '{printf \"CPU: %.2f%%\", $(NF-2)}'"
  cpu = subprocess.check_output(cmd, shell = True )
  show(cpu)
  time.sleep(15)
  cmd = "free | grep Mem | awk '{printf \"Mem: %.2f%%\", $3/$2 * 100}'"
  mem_usage = subprocess.check_output(cmd, shell = True )
  show(mem_usage)
  time.sleep(15)
  cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
  disk = subprocess.check_output(cmd, shell = True )
  show(disk)
  time.sleep(15)
