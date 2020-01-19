# NeighbourHoodWatch

#### Application for users to join and find the posts about their neighbourhood.
#### By **Margaret254**&trade;

## Description
This is an app that allow users to be updated on what is happenning on their neighborhoods

## Project live site
  This is the live .[ Click for the link](https://maggie254hood.herokuapp.com/)
 
## Features
* User can log in to application and view other peoples posts.
* A user can join neighborhood.
* A user can create their own hood.
* Admin can regulate images uploaded by deleting from the admin dashboard as well as completely close a users account.


## Setup/Installation requirements
1.Clone or download and unzip the repository from github,https://github.com/margaret254/NeighbourHoodWatch.git

2. Activate virtual environment using python3.6 as default handler virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

3. Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt
4. Create the Database
- psql
- CREATE DATABASE hoodwatch;

4. Create .env file and paste paste the following filling where appropriate:

-SECRET_KEY = '<Secret_key>'
-DBNAME = 'instacopy'
-USER = '<Username>'
-PASSWORD = '<password>'
-DEBUG = True
5. Run initial Migration
-python3.6 manage.py makemigrations instagram
-python3.6 manage.py migrate
6. Run the app
-python3.6 manage.py runserver
-Open terminal on localhost:8000



## Technologies Used
* PYTHON 3.6
* DJANGO FRAMEWORK
* BOOTSTRAP
* CSS
* POSTGRES

## Prerequisite
* PYTHON 3.6
* DJANGO FRAMEWORK
* PYTHON VIRTULENV
* POSTGRESS
## Support and contact details
contact me @ maggiemwas91@gmail.com
### License
The project is under[MIT license](/blob/master/LICENSE)
Copyright &copy; 2019.All rigths reserved