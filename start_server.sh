#!/bin/bash

# Define the log file
LOG_FILE="../output.log"

# Run the command and pipe the output to the log file
pipenv run python main.py > "$LOG_FILE" 2>&1
