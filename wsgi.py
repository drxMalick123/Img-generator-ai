import os
from main import app

if __name__ == "__main__":
    print("Running Flask app...")
    port = int(os.environ.get("PORT", 4000))  # Get port from environment
    app.run(host='0.0.0.0', port=port)
