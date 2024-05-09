import os
import shutil

# Check current working directory
print(os.getcwd())

# Create 'static/' directory if it doesn't exist
if not os.path.exists('static/'):
    os.makedirs('static/')

# Define the source and destination paths
source_path = "C:/Users/navee/Documents/VSCODE/output.pdf"
destination_path = "static/output.pdf"

# Move the file
try:
    shutil.move(source_path, destination_path)
    print(f"File moved to {destination_path}")
except Exception as e:
    print(f"Error moving file: {e}")
