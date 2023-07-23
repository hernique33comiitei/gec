#!/bin/bash

# Set the full path to the installation directory 
INSTALL_DIR="/usr/gec"

# Clone the repository from GitHub
git clone https://github.com/hernique33comiitei/gec.git "$INSTALL_DIR"

# Create an alias for the gec script 

#bash
# echo "alias gec='python3 ${INSTALL_DIR}/index.py'" >> ~/.bashrc

#zsh
#echo "alias gec='python3 ${INSTALL_DIR}/index.py'" >> ~/.zshrc


source ~/.zshrc && echo "The installation is complete! You can now use the 'gec' command to run the script."

