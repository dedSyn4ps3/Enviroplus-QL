#!/bin/bash

BOLD='\033[1m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color


echo "🏗️ ${BOLD}Creating and activating virtual environment...${NC}"

# Create a Python virtual environment
python3 -m venv .env

# Activate the virtual environment
source .env/bin/activate

CURRENT_DIR=$(basename "$PWD")

# Set the path to requirements.txt based on the current directory
if [ "$CURRENT_DIR" == "backend" ]; then
    REQUIREMENTS_FILE="requirements.txt"
else
    REQUIREMENTS_FILE="backend/requirements.txt"
fi

# Install Python dependencies
echo "📦 ${BOLD}${CYAN}Installing dependencies...${NC}"
pip install -r "$REQUIREMENTS_FILE"

echo
echo
echo "🎉 ${BOLD}${GREEN}Setup complete!${NC}"