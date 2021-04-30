#!/bin/bash

sudo apt install python3 -y
sudo apt install python3-pip -y
sudo apt install python3-requests -y
pip3 install colorama
pip3 install optparse-pretty
pip3 install os
sudo chmod +x ops.py
cp -r $(pwd) /usr/bin
ln -s /usr/bin/ops_scanner/ops.py /usr/local/bin/ops
echo '[+]-Setup is completed , you can execute ops from your command line'
