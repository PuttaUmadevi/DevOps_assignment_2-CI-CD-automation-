from flask import Flask, render_template

# Initialize the Flask application
# The name of the module is passed to Flask
app = Flask(__name__)

# --- Routes ---

# The root route (http://127.0.0.1:5000/)
@app.route("/")
def index():
    """
    Renders the main ticketing interface.
    Flask automatically looks for 'index.html' inside the 'templates' folder.
    """
    # Note: Because index.html is self-contained (HTML/CSS/JS in one file),
    # we avoid any issues with static file path lookups.
    return render_template("index.html")

# --- Application Startup ---

# This block is essential for local development when running 'python app.py'
if __name__ == "__main__":
    # Runs the application on the local development server.
    # We use debug=True for easier development, allowing code changes to reload automatically.
    app.run(host="0.0.0.0", port=5000, debug=True)
