Title: Installing Ubuntu on Windows 10
Date: 2022-08-25
Category: Linux
Summary: How to run a Linux environment on windows to run Linux commands
opengraph_image: ubuntu_og.jpg


### Intro: 

- From time to time, we might need to run a Linux environment on windows to run Linux commands, we can do this by creating a virtual machine on the windows system however it would take more resources(CPU, Memory, and storage)
- But there is another option called WSL aka Windows Subsystem for Linux, which would require fewer resources than a full Virtual Machine.
- WSL also allows you to run Linux command-line tools and apps alongside your Windows command-line and you can even access your Windows files from within Linux environment. 

### how to install Linux system on Windows 10 using WSL:

1. Search for "Turn Windows features On or Off" in the windows search

![turn_on_feature]({static}images/turn_windows_features.png)

2. It will open a window as below, scroll down, select 'Windows subsystems for Linux' and click on OK.

![features_window]({static}images/windows_feature_window.png)

3. Once you click OK, it will apply the required changes and requests you to restart your system

![restart]({static}images/windows_feature_restart.png)

4. After the restart, we can install our preferred Linux Distributions using "Microsoft Store" in your system, and search for 'Ubuntu' or 'Linux'.

![ms_store]({static}images/microsoft_store_ubuntu.png)

5. Here, I am trying to install Ubuntu(Linux distribution)

6. Once installed, open the Ubuntu app, it will take a few moments to finish the installation and would launch a Ubuntu Terminal.

7. Inside the terminal, you will be asked to enter your Unix username and password, which is different from your windows credentials, so you can give new credentials here.

8. Finally, we can run Linux commands in the Ubuntu terminal

9. `ls -al`, will list the files and directories in the current directory


### How to navigate through Windows drives, 
- enter the below commands
    1. `ls /mnt/` 
    2. `cd /mnt/c`
    3. `ls -al`, `cd Users/your_desktop_path/`
    
    ![commands]({static}images/ubuntu_terminal.png)


### Simple Linux Commands :
-  `touch notes.txt` -- to create notes.txt text file
- `nano notes.txt`  -- opens the text file using default and simple terminal-based text editor
- `cat notes.txt` --displays text in the file
- `pwd` -- the path of the current working directory (folder)
- `mkdir Music` -- creates a new 'Music' folder 

You can find and learn more about the Linux command line [here](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview) 

Also, you can open the bash terminal in the windows cmd by running, `bash` command-- and run Linux commands.