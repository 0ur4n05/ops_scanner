#!/bin/bash

if [ -f "/etc/arch-release" ]; then
    sudo pacman -Sy python python-pip python-requests
elif [ -f "/etc/fedora-release"]; then
    sudo dnf install python3 python3-pip python3-requests -y
else # for debian based distros
    sudo apt install python3 python3-pip python3-requests -y
fi

pip3 install colorama
pip3 install optparse-pretty
pip3 install os
sudo chmod +x ops.py
cp -r $(pwd) /usr/bin
ln -s /usr/bin/ops_scanner/ops.py /usr/local/bin/ops
echo '[+]-Setup is completed , you can execute ops from your command line'
