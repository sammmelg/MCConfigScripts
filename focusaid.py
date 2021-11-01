import os

# When script starts, run multiple commands to put the camera into daytime mode
print("Configuring camera to daytime mode...")
os.system("python -m Utils.CameraControl SetParam Camera Style type2")
os.system("python -m Utils.CameraControl SetParam Camera DayNightColor 1")
os.system("python -m Utils.CameraControl SetParam Camera ElecLevel 30")
os.system("python -m Utils.CameraControl SetParam Camera ExposureParm LeastTime 100")
os.system("python -m Utils.CameraControl SetParam Camera GainParam Gain 30")

# After commands run, ask user if they are done focusing the camera
user_input = input("Are you done focusing the camera (y/n)? ")
while(user_input != "y"):
    user_input = input("Are you done focusing the camera (y/n)? ")

# If yes, the run commands to put camera back to night time mode & end the script
os.system("python -m Utils.CameraControl SetParam Camera Style type1")
os.system("python -m Utils.CameraControl SetParam Camera DayNightColor 2")
os.system("python -m Utils.CameraControl SetParam Camera ElecLevel 100")
os.system("python -m Utils.CameraControl SetParam Camera ExposureParm LeastTime 40000")
os.system("python -m Utils.CameraControl SetParam Camera GainParam Gain 60")
print("The camera has been configured back to nighttime mode.")