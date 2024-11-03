#!/bin/bash

BOLD='\033[1m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color


echo "🏗️ ${BOLD}Creating and activating virtual environment...${NC}"

# Create a Python virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install Python dependencies
echo "📦 ${BOLD}${CYAN}Installing dependencies...${NC}"
pip install -r requirements.txt

echo
echo
echo "🎉 ${BOLD}${GREEN}Setup complete!${NC}"