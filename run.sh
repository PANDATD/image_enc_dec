#!/usr/bin/env bash

echo "Checking Updates"
sudo apt-get update -y
echo "checking upgrades"
sudo apt-get upgrade -y
echo"removing unwated packages"
sudo apt autoremove -y
echo "Installing pip"
sudo apt-get install python3-pip -y
echo "Installing TKINTER"
sudo apt-get install python3-tk
echo "Installing required packages"
pip3 install -r requirement.txt
