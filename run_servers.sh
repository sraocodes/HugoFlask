#!/bin/bash

# Start Flask server
cd backend && . venv/bin/activate && python app.py &

# Start Hugo server
hugo server &
