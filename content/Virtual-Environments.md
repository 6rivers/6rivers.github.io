Title: What is the use of Virtual Environments in Python projects?
Date: 2021-10-13 01:20
Category: Python
Summary: Virtual Environment is used to separate out the versions of packages.



### Use of Virtual Environments in Python Projects:

- Virtual Environment is used to separate out the versions of packages for eg., Django or Flask. 
- In general, if we install Packages directly without Virtual Environment then they will be installed on global levels
- If you have multiple Django projects where some older projects need previous versions of Django and when you need a new project with the latest version of Django package and if you install it without virtual env then your older projects would be affected since the older version of Django package will be replaced with newer version after the upgrade. 
- Hence it is best practice to use Virtual Env for each project and have whatever packages are needed for that particular project inside the virtual environment. 
- venv is recommended for creating Virtual Environments from Python 3.5
- Create a folder for the new project then cd to the folder and execute below to create new virtual env

#### Creating Virtual Env:  

cd to your project folder

##### Linux:

`sudo apt install python3-pip` to install pip if not already present. 

Now install a tool for creating isolated virtual python environments or you can use `venv` that comes directly with Python installation

`pip install virtualenv`

`virtualenv env_name`  or
`python3 -m venv env_name` 

this will create a new folder(env_name) in your current directory
  
To activate a virtual environment

`source env_name/bin/activate`

After activation, you would see a change similar to 
`(venv) C:\Users\Name\Folder>` 

`deactivate` -- to deactivate the venv

##### Windows:

`python -m venv env_name` -- to create Virtual Environment

`env_name\scripts\activate` -- to activate

`deactivate` -- to deactivate

##### other info:

Do not store any project scripts inside 'env_name' folder

`pip list` -- to get a list of packages installed in the current venv

`pip freeze` -- to get a list of packages in a format usable to copy for requirements.txt

command to create a requirements.txt file with a list of packages installed in the current project
`pip freeze > requirements.txt` 

To directly install all packages from the requirements.txt use 
`pip install -r requirements.txt`