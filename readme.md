Hugo-Flask Integration Guide
1. Set Up
a. Flask Setup

Ensure you have Flask installed. If not, install it using pip install Flask.
Make sure your Flask application, for example app.py, is ready and in the correct directory.
Make sure you have the necessary CSV files in the specified data directory.
b. Hugo Setup

Ensure Hugo is installed and your Hugo site is set up.
Update your Hugo content with the desired template.
2. Flask-CORS
For Flask and Hugo to communicate properly, especially if they're running on different ports (which they likely are), you might need to handle CORS (Cross-Origin Resource Sharing).

Install Flask-CORS: pip install Flask-CORS
Modify your Flask app to use Flask-CORS:
python
Copy code
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
3. Bash Script for Running Both Servers
Create a file named run_servers.sh with the following content:

bash
Copy code
#!/bin/bash

# Running Flask server
echo "Starting Flask server..."
python3 /path/to/your/app.py &

# Running Hugo server
echo "Starting Hugo server..."
hugo server &

wait
Make sure to replace /path/to/your/app.py with the actual path to your Flask application.

To make the script executable, run:

bash
Copy code
chmod +x run_servers.sh
4. Run the Servers
Execute the Bash script:

bash
Copy code
./run_servers.sh
This will run both the Flask and Hugo servers. You can access the Flask server, typically at http://localhost:5002, and the Hugo server at its designated port, often http://localhost:1313.

5. Debugging
If there are issues with the display in Hugo, check the browser console for any errors. Ensure that the paths, especially for fetching data from Flask, are correct.

If CORS issues arise, ensure Flask-CORS is correctly set up.

That should be all to get your Hugo-Flask integration running. 