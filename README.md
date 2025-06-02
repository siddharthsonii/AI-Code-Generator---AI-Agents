# AI Agent Code Generator: Your *Coding Ka Jadoo* 🪄

Welcome to the **AI Agent Code Generator**, a Python-powered *jugaadu* tool that creates entire projects faster than your mom makes *aloo paratha* 🥟! Whether you want a React to-do list, a Flask calculator, or a Java Spring Boot app, this AI *dost* uses OpenAI’s magic to generate code files, install dependencies, and launch your app in a browser—all with a few clicks. Think of it as your *coding ka Baahubali*, saving you from *deadline wali tension* ⏰.

This project includes a Flask web interface, so you can generate apps via a browser, perfect for *desi* devs juggling *client calls* and *chai breaks* ☕. Below, you’ll find everything you need to set up, run, and deploy this *shandaar* tool. Let’s get coding, *bhai*! 🚀

## 📜 What’s This All About?

This AI agent takes your project ideas and turns them into reality. You tell it:
- Project name (e.g., “CalculatorApp”)
- Directory (e.g., `C:\Users\acer\Desktop\newfolder`)
- Features (e.g., “Add, subtract, multiply, divide”)
- Tech stack (e.g., “Python with Flask”, “JavaScript with React”, “Java with Spring Boot”)
- Notes (e.g., “Make it *jhakas* with Bootstrap”)
- Type (e.g., “web app”)

It then:
- Generates all necessary files (e.g., `app.py`, `pom.xml`, `App.js`) using OpenAI’s API.
- Saves them to a directory (locally or temporarily on a server).
- Installs dependencies (like `npm install` or `pip install`).
- Runs the app and opens it in a browser (e.g., `http://localhost:5000`).

Built with Python, Flask, and OpenAI, it’s flexible enough to support *any* tech stack, from React to Spring Boot, making you the *Sharma ji ka beta* of coding! 😎

## 🛠️ Prerequisites

Before you dive in, make sure you have these ready, like prepping *masala* for *biryani* 🍛:

- **Python 3.8+**: Check with `python --version`. If not installed, grab it from [python.org](https://www.python.org/downloads/).
- **pip**: Python’s package manager, usually comes with Python. Verify with `pip --version`.
- **Git**: For cloning the repo. Install from [git-scm.com](https://git-scm.com/) and check with `git --version`.
- **OpenAI API Key**: Sign up at [platform.openai.com](https://platform.openai.com/), create a key, and add it to a `.env` file (more on this below).
- **Tech Stack Dependencies**: Depending on the projects you generate:
  - **React**: Node.js and npm (`node --version`, `npm --version`). Install from [nodejs.org](https://nodejs.org/).
  - **Flask**: Python handles this via `requirements.txt`.
  - **Spring Boot**: Java JDK 17+ (`java -version`) and Maven (`mvn --version`). Install JDK from [oracle.com](https://www.oracle.com/java/technologies/downloads/) and Maven from [maven.apache.org](https://maven.apache.org/download.cgi).
  - **Go**: Go compiler (`go version`). Get it from [go.dev](https://go.dev/dl/).

**Pro Tip**: If you hit a *“mvn not found”* error like before, install Maven and add it to your PATH. We’ll guide you below! 🛠️

## 📦 Installation

Follow these steps to set up the AI agent, as easy as ordering *panipuri* from your favorite *thela* 🥟:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ai-code-generator.git
   cd ai-code-generator
   ```

2. **Install Python Dependencies**:
   Create a virtual environment (optional but recommended) and install packages:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   pip install -r requirements.txt
   ```

   The `requirements.txt` includes:
   ```
   python-dotenv==1.0.1
   openai==1.51.0
   flask==3.0.3
   ```

3. **Set Up the `.env` File**:
   Create a `.env` file in the project root and add your OpenAI API key:
   ```bash
   echo OPENAI_API_KEY=your_openai_api_key_here > .env
   ```
   This is like the *VIP pass* to OpenAI’s AI party 🎫. Don’t share it, or your *coding genie* might vanish!

4. **Fix Maven for Spring Boot (If Needed)**:
   If you plan to generate Java Spring Boot projects (like your calculator app), install Maven:
   - Download from [maven.apache.org](https://maven.apache.org/download.cgi) (e.g., `apache-maven-3.9.6-bin.zip`).
   - Extract to `C:\Program Files\Apache\maven`.
   - Add `C:\Program Files\Apache\maven\bin` to your PATH:
     - Right-click “This PC” → Properties → Advanced system settings → Environment Variables.
     - Edit “Path” under System Variables, add the Maven bin path.
   - Verify with:
     ```bash
     mvn --version
     ```
   - Ensure JDK 17+ is installed (`java -version`). Set `JAVA_HOME` to `C:\Program Files\Java\jdk-17` if needed.

## 🚀 Running the App Locally

Time to fire up the AI agent, like starting your *Bajaj Pulsar* 🏍️! The Flask app runs a web interface to generate projects.

1. **Start the Flask Server**:
   ```bash
   python project_generator.py
   ```
   This launches the app on `http://localhost:5000` (or the port specified in your `.env` file, e.g., `PORT=5000`).

2. **Access the Web Interface**:
   Open your browser and go to `http://localhost:5000`. You’ll see a form asking for:
   - Project name (e.g., “CalculatorApp”)
   - Directory (ignored locally, uses your input like `C:\Users\acer\Desktop\newfolder`)
   - Functionalities (e.g., “Add, subtract, multiply, divide”)
   - Tech stack (e.g., “Java with Spring Boot”)
   - Notes (e.g., “Simple UI”)
   - Project type (e.g., “web app”)

3. **Generate a Project**:
   Fill out the form and click “Generate Project”. The AI agent will:
   - Create files in the specified directory (e.g., `C:\Users\acer\Desktop\newfolder`).
   - Run the `install_command` (e.g., `pip install -r requirements.txt` for Flask).
   - Execute the `run_command` (e.g., `python app.py`).
   - Open the app in a new browser tab (e.g., `http://localhost:5000` for Flask, `http://localhost:8080` for Spring Boot).

   **Example**: For a Flask calculator app, you’ll get files like `app.py`, `templates/index.html`, and a running app at `http://localhost:5000`.

4. **Troubleshooting**:
   - **Maven Error**: If you see *“mvn not found”* for Spring Boot, ensure Maven is installed (see Prerequisites).
   - **Port Conflict**: Check if ports (e.g., 5000, 8080) are free with `netstat -a -n -o | find "5000"`. Kill conflicting processes or change ports in the generated app.
   - **API Key Issue**: Verify your `.env` file has the correct `OPENAI_API_KEY`.

## ☁️ Deploying on Render

Want to share your AI agent with your *coding gang*? Deploy it on [Render](https://render.com) like a *cloud ka raja* 👑! Here’s how:

1. **Prepare the Repository**:
   - Push your code to GitHub:
     ```bash
     echo "OPENAI_API_KEY" >> .gitignore
     git add .
     git commit -m "Ready for Render"
     git push origin main
     ```

2. **Set Up Render**:
   - Sign up at [render.com](https://dashboard.render.com/register).
   - Click **New** > **Web Service**, connect your GitHub repo, and select the branch (e.g., `main`).
   - Configure:
     - **Runtime**: Python
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `python project_generator.py`
     - **Environment Variables**: Add `OPENAI_API_KEY=your_key_here` and `PORT=5000`.
   - Choose the **Free** plan for testing (upgrade for production).
   - Deploy! You’ll get a URL like `https://your-ai-agent.onrender.com`.

3. **Generate Projects on Render**:
   - Visit the Render URL and fill out the form.
   - The agent saves files to a temporary server directory (e.g., `/tmp/CalculatorApp`) and tries to run the app.
   - **Note**: Render’s Free plan supports one port, so running generated apps (e.g., Spring Boot on port 8080) may require a separate service or local execution.

4. **Java Spring Boot on Render**:
   - To generate Spring Boot apps, use a Dockerfile to include Maven and JDK:
     ```dockerfile
     FROM maven:3.9.6-eclipse-temurin-17
     WORKDIR /app
     COPY . .
     RUN pip install -r requirements.txt
     EXPOSE 5000
     CMD ["python", "project_generator.py"]
     ```
   - Update Render to use the Dockerfile and add `JAVA_HOME=/opt/java/openjdk`.

## 🌟 Example: Generating a Calculator App

Let’s generate a Java Spring Boot calculator app, like the one you tried in `newfolder4`:

1. **Fill the Form**:
   - Name: `CalculatorApp`
   - Directory: `C:\Users\acer\Desktop\newfolder` (local) or ignored (Render)
   - Functionalities: `Add, subtract, multiply, divide`
   - Stack: `Java with Spring Boot`
   - Notes: `Simple UI`
   - Type: `web app`

2. **Generated Files**:
   - `pom.xml`: Maven dependencies
   - `src/main/java/com/example/CalculatorApplication.java`: Main app
   - `src/main/java/com/example/CalculatorController.java`: Calculator logic
   - `src/main/resources/templates/index.html`: Web form
   - `README.md`: Instructions

3. **Commands**:
   ```bash
   mvn clean install
   mvn spring-boot:run
   ```

4. **Output**:
   - App runs at `http://localhost:8080`, showing a calculator form.
   - Enter two numbers, select an operation, and see the result!

**Fix for Your Issue**: If you see *“mvn not found”*, install Maven (see Prerequisites). Run commands manually in `C:\Users\acer\Desktop\AI Agent\newfolder4`.

## 🐛 Troubleshooting

- **“mvn not found”**: Install Maven and add to PATH. Retry `mvn clean install`.
- **Port Occupied**: Use `netstat -a -n -o | find "8080"` to find and kill processes.
- **API Error**: Check `OPENAI_API_KEY` in `.env`. Ensure you have OpenAI credits.
- **Render Issues**: Free plan servers sleep after inactivity. Upgrade or redeploy.
- **Generated App Fails**: Check the generated `README.md` for specific instructions or share error logs.

## 🙌 Contributing

Want to make this agent even more *jhakas*? Fork the repo, add features (like a zip-download endpoint), and send a pull request. Let’s build the ultimate *coding ka dabba*! 📦

## 📝 License

MIT License—use it, tweak it, share it, but don’t blame us if your *client* asks for a *panipuri-ordering app* next! 😜

---

*Code Hard, Pyaar Softly!* 💖  
*Happy Coding, Desi Devs!* 🐍️