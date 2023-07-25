#!/bin/bash

# Set the full path to the installation directory
INSTALL_DIR="$HOME/bin/gec"
SHELL_USED=$(basename "$SHELL")

# Remove the alias for the gec script
if [ "$SHELL_USED" = "bash" ]; then
  sed -i '/alias gec/d' ~/.bashrc
  source ~/.bashrc
fi

if [ "$SHELL_USED" = "zsh" ]; then
  sed -i '/alias gec/d' ~/.zshrc
  source ~/.zshrc
fi

# Remove the installation directory
if [ -d "$INSTALL_DIR" ]; then
  rm -rf "$INSTALL_DIR"
fi

echo "The uninstallation is complete. The 'gec' command and its installation directory have been removed."
