import os
import json
import webbrowser
import subprocess
import re
import time
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
client = OpenAI()

# System prompt for OpenAI to generate project files for any language
SYSTEM_PROMPT = """
You are an expert AI coding assistant tasked with generating a to-do list project based on user inputs, supporting any programming language and tech stack. The user will provide:
1. Project name
2. Project directory
3. Main functionalities
4. Preferred tech stack (e.g., Python with Flask, JavaScript with React, Java with Spring Boot, Go with Gin)
5. Additional notes (optional)
6. Project type (e.g., web app, CLI)

Based on these inputs, generate a JSON object containing:
- All necessary source code files for a to-do list app in the specified tech stack (e.g., for Python Flask: `app.py`, `templates/index.html`; for React: `src/App.js`, `src/index.js`, `public/index.html`, `src/App.css`, `src/index.css`; for Java Spring Boot: `pom.xml`, Java class files, templates).
- A dependency file (e.g., `requirements.txt` for Python, `package.json` for JavaScript, `pom.xml` for Java, `go.mod` for Go).
- A `README.md` with setup and run instructions.
- A list of commands to install dependencies and run the app (e.g., `pip install -r requirements.txt` and `python app.py` for Flask).

The to-do list should allow users to add tasks, mark them as complete, and delete them. Use appropriate conventions for the specified tech stack (e.g., functional components and hooks for React, REST controllers for Spring Boot). Ensure all files are valid and functional. Dependency files (e.g., `package.json`, `requirements.txt`) must be plain text or valid JSON without markdown code fences (``` or ```) or explanatory text. The app should be launchable with the provided run command, typically opening a web app in a browser.

Output JSON Format:
{
  "files": {
    "<filename>": "string",
    ...
  },
  "install_command": "string",
  "run_command": "string",
  "run_url": "string"
}

Example for Python Flask:
{
  "files": {
    "app.py": "from flask import Flask, render_template, request, redirect, url_for\napp = Flask(__name__)\ntasks = []\n@app.route('/')\ndef index():\n    return render_template('index.html', tasks=tasks)\n...",
    "templates/index.html": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Todo List</title>\n    <style>\n        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }\n...\n</style>\n</head>\n...",
    "requirements.txt": "flask==2.3.2",
    "README.md": "# Todo List\nRun `pip install -r requirements.txt` and `python app.py` to start."
  },
  "install_command": "pip install -r requirements.txt",
  "run_command": "python app.py",
  "run_url": "http://localhost:5000"
}

Example for JavaScript React:
{
  "files": {
    "package.json": "{\"name\": \"todo-app\", \"version\": \"1.0.0\", \"scripts\": {\"start\": \"react-scripts start\", \"build\": \"react-scripts build\"}, \"dependencies\": {\"react\": \"^18.2.0\", \"react-dom\": \"^18.2.0\", \"react-scripts\": \"5.0.1\"}}",
    "src/App.js": "import { useState } from 'react';\nimport './App.css';\nfunction App() {\n  const [tasks, setTasks] = useState([]);\n...\n}\nexport default App;",
    "src/index.js": "import React from 'react';\nimport ReactDOM from 'react-dom/client';\n...",
    "public/index.html": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Todo App</title>\n</head>\n<body>\n    <div id=\"root\"></div>\n</body>\n</html>",
    "src/App.css": ".App { text-align: center; max-width: 600px; margin: 0 auto; padding: 20px; }\n...",
    "src/index.css": "body { margin: 0; font-family: Arial, sans-serif; background-color: #f0f0f0; }",
    "README.md": "# Todo App\nRun `npm install` and `npm start` to start."
  },
  "install_command": "npm install",
  "run_command": "npm start",
  "run_url": "http://localhost:3000"
}
"""

def clean_text_content(content):
    """Remove markdown code fences and other non-text content."""
    content = re.sub(r'```[\w]*\n|```', '', content)
    return content.strip()

def clean_json_content(content):
    """Remove markdown code fences and ensure valid JSON."""
    content = re.sub(r'```json\n|```', '', content)
    content = content.strip()
    try:
        json.loads(content)
        return content
    except json.JSONDecodeError:
        match = re.search(r'\{[\s\S]*\}', content)
        if match:
            return match.group(0)
        raise ValueError("Generated content is not valid JSON")

def ask_questions():
    """Collect project details from the user."""
    questions = [
        ("What is the name of your project?", "name"),
        ("Which directory should the project be created in? (e.g., C:\\Users\\acer\\Desktop\\project)", "directory"),
        ("What are the main functionalities of the project? (e.g., add tasks, delete tasks)", "functionalities"),
        ("Which tech stack would you like to use? (e.g., Python with Flask, JavaScript with React, Java with Spring Boot)", "stack"),
        ("Any additional notes or requirements for the project?", "notes"),
        ("What type of project is this? (e.g., web app, CLI)", "type")
    ]
    answers = {}
    for question, key in questions:
        answer = input(f"> {question} ")
        answers[key] = answer.strip()
    return answers

def generate_project_files(answers):
    """Use OpenAI to generate project files based on user answers."""
    user_prompt = f"""
    Generate project files for a to-do list app with the following details:
    - Project Name: {answers['name']}
    - Directory: {answers['directory']}
    - Functionalities: {answers['functionalities']}
    - Tech Stack: {answers['stack']}
    - Additional Notes: {answers['notes']}
    - Project Type: {answers['type']}
    
    Provide the content for all necessary files based on the specified tech stack (e.g., for Python Flask: `app.py`, `templates/index.html`, `requirements.txt`; for React: `package.json`, `src/App.js`, etc.). Include a dependency file and a `README.md`. Provide `install_command`, `run_command`, and `run_url` for launching the app. Ensure dependency files are clean (e.g., valid JSON for `package.json`, plain text for `requirements.txt`) without markdown or code fences.
    """
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=messages
    )
    
    result = json.loads(response.choices[0].message.content)
    files = result.get("files", {})
    
    # Clean dependency files
    if "package.json" in files:
        files["package.json"] = clean_json_content(files["package.json"])
    if "requirements.txt" in files:
        files["requirements.txt"] = clean_text_content(files["requirements.txt"])
    if "pom.xml" in files:
        files["pom.xml"] = clean_text_content(files["pom.xml"])
    if "go.mod" in files:
        files["go.mod"] = clean_text_content(files["go.mod"])
    
    # Verify required fields
    required_fields = ["files", "install_command", "run_command", "run_url"]
    for field in required_fields:
        if field not in result:
            raise ValueError(f"Missing required field: {field}")
    
    return result

def save_files(answers, files):
    """Save generated files to the specified directory."""
    project_dir = answers['directory']
    os.makedirs(project_dir, exist_ok=True)
    
    # Create subdirectories based on file paths
    for filename in files:
        dir_path = os.path.dirname(os.path.join(project_dir, filename))
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(project_dir, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(files[filename])

def launch_app(project_dir, install_command, run_command, run_url):
    """Install dependencies and launch the app."""
    browser_opened = False
    try:
        print("Installing dependencies...")
        install_result = subprocess.run(
            install_command,
            cwd=project_dir,
            shell=True,
            capture_output=True,
            text=True
        )
        if install_result.returncode != 0:
            print(f"Install failed: {install_result.stderr}")
            print(f"Please run '{install_command}' manually in the project directory.")
            return
        
        print("Starting the app...")
        server_process = subprocess.Popen(
            run_command,
            cwd=project_dir,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait for the server to start
        time.sleep(8)
        
        # Check if the server is running
        if server_process.poll() is not None:
            stdout, stderr = server_process.communicate()
            print(f"Run failed: {stderr}")
            print(f"Please run '{run_command}' manually in the project directory.")
            return
        
        # Open browser only if not already opened
        if not browser_opened:
            print(f"Opening browser at {run_url}...")
            webbrowser.open_new(run_url)
            browser_opened = True
            print("Browser opened successfully.")
        
        # Keep the server running
        try:
            stdout, stderr = server_process.communicate()
            if stderr:
                print(f"Server error: {stderr}")
        except KeyboardInterrupt:
            print("Stopping the server...")
            server_process.terminate()
            server_process.wait()
            
    except Exception as e:
        print(f"Error launching app: {str(e)}")
        print(f"Please try running '{run_command}' manually in the project directory.")

def main():
    print("Welcome to the Project Generator! Answer the following questions:")
    answers = ask_questions()
    
    answers['directory'] = os.path.normpath(answers['directory'])
    
    print("Generating project files...")
    try:
        result = generate_project_files(answers)
        files = result["files"]
        install_command = result["install_command"]
        run_command = result["run_command"]
        run_url = result["run_url"]
    except ValueError as e:
        print(f"Error generating files: {str(e)}")
        return
    
    print(f"Saving files to {answers['directory']}...")
    save_files(answers, files)
    
    launch_app(answers['directory'], install_command, run_command, run_url)
    
    print("\nIf the app didn't launch correctly, try these steps:")
    print(f"1. Open a terminal and navigate to: cd {answers['directory']}")
    print(f"2. Run: {install_command}")
    print(f"3. Run: {run_command}")
    print(f"4. Open your browser to: {run_url}")

if __name__ == "__main__":
    main()