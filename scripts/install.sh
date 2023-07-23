#!/bin/bash

# Set the full path to the installation directory (changed to /usr/local/bin/)
INSTALL_DIR="/usr/local/bin/"

# Clone the repository from GitHub
git clone https://github.com/hernique33comiitei/gec.git "$INSTALL_DIR"

# Create an alias for the gec script
echo "alias gec='python ${INSTALL_DIR}/gec/index.py'" >> ~/.bashrc

# Load changes from the shell configuration file
source ~/.bashrc

echo "The installation is complete! You can now use the 'gce' command to run the script."
