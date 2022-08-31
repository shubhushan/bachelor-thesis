# bachelor-thesis
cd catkin_ws
catkin make
source devel/setup.bash

# launch the simulation for maze1, similar syntax till maze5. multiple targets maze11_raster.launch to maze55_raster.launch
roslaunch nps_uw_multibeam_sonar maze1_raster.launch

cd ..
cd "path planning"

# run image service node to fetch images
rosrun image_view image_saver image:=/image_view_sonar/output _save_all_image:=false _filename_format:=f.jpg

# fetch sonar images
python3 path_planning.py

# grayscale images
cd ../denoising
pip3 install requirements.txt
python3 convert_images_grayscale.py

# denoising images
python3 denoising_python3.py

# numeric extraction
python3 image_analysis.py

# graphic results
python3 results_extraction.py