#!/bin/bash

sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
sudo pip3 install virtualenv
virtualenv -p python3 pridexsenv
pridexsenv/bin/pip3 install -r requirements.txt
