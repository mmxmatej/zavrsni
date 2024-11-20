#!/bin/bash

# Ensure the script exits on errors
set -e

echo "Starting deployment of Server Info Application..."

# Navigate to the application directory
cd "$(dirname "$0")"

# Install dependencies
echo "Installing Python dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Run the application
echo "Starting the server..."
nohup python3 server_info.py &

echo "Server Info Application deployed and running."
