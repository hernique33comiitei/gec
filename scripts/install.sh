#!/bin/bash

# Set the full path to the installation directory 
INSTALL_DIR="$HOME/bin/gec"
SHELL_USED=$(basename "$SHELL")

# Clone the repository from GitHub
git clone https://github.com/hernique33comiitei/gec.git "$INSTALL_DIR"

# Create an alias for the gec script 

if [ "$SHELL_USED" = "bash" ]; then
  echo "alias gec='python3 ${INSTALL_DIR}/index.py'" >> ~/.bashrc
  source ~/.bashrc
fi

if [ "$SHELL_USED" = "zsh" ]; then
  echo "alias gec='python3 ${INSTALL_DIR}/index.py'" >> ~/.zshrc
  source ~/.zshrc
fi

echo "$SHELL_USED"


echo "The installation is complete! You can now use the 'gec' command to run the script."

