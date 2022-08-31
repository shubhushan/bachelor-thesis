import sys
import subprocess


#argv[1] denotes the path planning for maze 1 through 3
maze = sys.argv[1]


with open(f"maze{maze}.txt", 'a') as f:
    #gets the pose of blueview sonar
    get_pose = f"rosservice call /gazebo/get_model_state \"model_name: 'blueview_p900'\" | grep -i -A 9 \"pose\""
    output = subprocess.run(get_pose, capture_output=True, shell=True)
    #turn bytes to string, deterministic output
    tmp = output.stdout.decode("utf-8").split("\n")

    """
        2 => x_pos
        3 => y_pos
        4 => z_pos

        6 => x_q
        7 => y_q
        8 => z_q
        9 => w_q
    """
    #pose of the sonar
    x_pos = tmp[2].split(":")[1].strip()
    y_pos = tmp[3].split(":")[1].strip()
    z_pos = tmp[4].split(":")[1].strip()
    #orientation of the sonar
    x_q = tmp[6].split(":")[1].strip()
    y_q = tmp[7].split(":")[1].strip()
    z_q = tmp[8].split(":")[1].strip()
    w_q = tmp[9].split(":")[1].strip()

    print("pose:")
    print(f"{x_pos}, {y_pos}, {z_pos}")
    print("orientation:")
    print(f"{x_q}, {y_q}, {z_q}, {w_q}")

    f.write(f"{x_pos};{y_pos};{z_pos};{x_q};{y_q};{z_q};{w_q}\n")