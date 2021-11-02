import os

main()

def main():
    clock_install()
    dw_choice = input("Are you ready to continue to DWService client install? (y/n) ")
    if dw_choice == "n":
        quit()
    while dw_choice != "y":
        dw_choice = input("Are you ready to continue to DWService client install? (y/n) ")
    dw_install()
    quit()


def clock_install():

    # Check that clock is detected
    os.system("sudo i2cdetect -y 1")

    # Ask the user if the clock was detected
    detected = input("Was the clock detected? (y/n) ")

    # If not, then tell the user to check the clock on the pi and exit the script
    if detected == "n":
        print("Please check the clock on the pi and re-run the script.")
        quit()

    # Otherwise, continue asking until user responds "y"
    else:
        while detected != "y":
            detected = input("Was the clock detected? (y/n) ")

    # Download the RTC script
    os.system("wget https://raw.github.com/mgialluca/LOCAMS_Software/main/RaspberryPi_Files/InstallRTC.sh")

    # Change file permissions on the install script
    os.system("chmod +x InstallRTC.sh")

    # Install the script
    os.system("sudo ./InstallRTC.sh")

    # Tell user the clock has been installed and exit the script
    print("The RTC clock has been installed!")


def dw_install():
    os.system("cd /home/pi/Downloads")
    os.system("chmod +x dwagent.sh")
    os.system("sudo ./dwagent.sh")

if __name__ == "__main__":
    main()
