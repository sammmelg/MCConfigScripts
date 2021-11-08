import os


def main():
    # Run clock install function
    clock_install()

    # Ask the user if they are ready to install dwagent
    dw_choice = input("Are you ready to continue to DWService client install? (y/n) ")

    # Make sure the user's choice is valid
    choice_check(dw_choice)

    # Install dwagent
    dw_install()

    # Ask user if they are ready to generate ssh keys
    ssh_choice = input("Are you ready to generate ssh keys? (y/n) ")

    # Make sure the user's choice is valid
    choice_check(ssh_choice)

    # Generate ssh keys
    ssh_gen()

    quit()


def choice_check(choice):
    if choice == "n":
        quit()
    while choice != "y":
        choice = input("Please try again (y/n) ")


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
    # Go to the downloads folder
    os.chdir("/home/pi/Downloads")

    # Pull the dwagent.sh file from github
    os.system("wget https://github.com/sammmelg/locamsfiles/raw/main/dwagent.sh")

    # Make dwagent installable
    os.system("chmod +x dwagent.sh")

    # Install dwagent
    os.system("sudo ./dwagent.sh")


def ssh_gen():
    # Change directory to ssh folder
    os.chdir("/home/pi/.ssh")

    # Run key gen line
    os.system("sudo ssh-keygen -t rsa -b 4096 -o -a 100")


if __name__ == "__main__":
    main()
