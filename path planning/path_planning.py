import sys
import subprocess
import numpy as np
import time
import shutil
import os

#argv[1] denotes the path planning for maze 1 through 3
maze = sys.argv[1]

if len(sys.argv) > 2:
  dir_name_end = "variational_reflectivity"
else:
  dir_name_end = "constant_reflectivity"


#run it separately for now, from thesis/2d
#node_name = rosrun image_view image_saver image:=/image_view_sonar/output _save_all_image:=false _filename_format:=f.jpg
#rosservice = subprocess.run(node_name, shell=True)
#get the rosservice which ends with save /image_saver_no/save
"""
run this before using the code

rosrun image_view image_saver image:=/image_view_sonar/output _save_all_image:=false _filename_format:=f.jpg

"""

image_saver_name = subprocess.run("rosservice list | egrep 'save$'", shell=True, capture_output=True).stdout.decode("utf-8").strip()
print(f"Image saver: {image_saver_name}")

#create the maze directory if it does not exist
dir_name = f"./maze{maze}{dir_name_end}"
if not os.path.isdir(dir_name):
  os.mkdir(dir_name)

def euler_to_quaternions(roll, pitch, yaw):
  cosine_roll = np.cos(roll*0.5)
  sine_roll = np.sin(roll*0.5)

  cosine_yaw = np.sin(yaw*0.5)
  sine_yaw = np.sin(yaw*0.5)

  cosine_pitch = np.cos(pitch*0.5)
  sine_pitch = np.sin(pitch*0.5)

  qx = cosine_yaw*sine_roll*cosine_pitch - sine_yaw*cosine_roll*sine_pitch
  qy = cosine_yaw*cosine_roll*sine_pitch + sine_yaw*sine_roll*cosine_pitch
  qz = sine_yaw*cosine_roll*cosine_pitch - cosine_yaw*sine_roll*sine_pitch
  qw = cosine_yaw*cosine_roll*cosine_pitch + sine_yaw*sine_roll*sine_pitch

  return qx, qz, qy, qw

def get_image(image_no):
  #save image as f.jpg
  subprocess.run("rosservice call " + image_saver_name, shell=True)
  #checks if the file has been created in the root dir
  while True:
    if not os.path.isfile("./f.jpg"):
      continue
    else:
      break
  #rename and move image with it's image name as the planned path number in the path planning file
  shutil.move('./f.jpg', dir_name+f"/{image_no}.jpg")

with open(f"maze{maze}.txt", "r") as f:
    for image_count, line in enumerate(f):
        #delimited with ;
        line_split = line.split(";")
        #position
        pos_x = line_split[0]
        pos_y = line_split[1]
        pos_z = line_split[2]

        #orientation
        quater_x = line_split[3]
        quater_y = line_split[4]
        quater_z = line_split[5]
        quater_w = line_split[6]

        #pose template
        set_pose_template = f"""rostopic pub -1 /gazebo/set_model_state gazebo_msgs/ModelState "model_name: 'blueview_p900'
pose:
  position:
    x: {pos_x}
    y: {pos_y}
    z: {pos_z}
  orientation:
    x: {quater_x}
    y: {quater_y}
    z: {quater_z}
    w: {quater_w}
"
"""
        #Publish the message from a child process
        subprocess.run(set_pose_template, shell=True)
        get_image(image_count)