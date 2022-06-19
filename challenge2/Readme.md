# Prerequisites

  

  

Create an EC2 Linux instance on AWS

  

SSH into the instance

  

  

# Installation

  

  

Install Python 3 and git on your instance

  

>sudo yum install python3 git

  

Clone this repository

  

>git clone https://github.com/shzshi/kpmg-challenge

  
  

Install pipenv

  

>sudo pip3 install pipenv

  

Go to directory **challenge2**

  

>cd challenge2

  

Install project dependancies

  

>pipenv install

  

  

# Running

  

  

Open the src folder

  

>cd kpmg-challenge/challenge2/

  

Run script you need:

  

>python3 metadata.py

  

  

Examples for the key ami-id or vpc-id