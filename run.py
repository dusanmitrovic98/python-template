import os
import subprocess

# Define your virtual environment name
venv_name = "environment"

# Activate the virtual environment
if os.name == "posix":  # Unix/Linux/macOS
    activate_cmd = f"source {venv_name}/bin/activate"
else:  # Windows1
    activate_cmd = f"{venv_name}\\Scripts\\activate"

subprocess.call(activate_cmd, shell=True)

# Install requirements
subprocess.call("pip install -r requirements.txt", shell=True)

# Run your server
server_cmd = "python main.py"  # Replace with the actual command to run your project
subprocess.call(server_cmd, shell=True)
