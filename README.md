EPITA TP2 – NASA Astronomy Picture of the Day (APOD)

Streamlit Frontend Application

Student Name: Sheffy Sabu  
EPITA Login: sheffy.sabu@epita.fr  
Assigned API Group: Group 5 – Space & Astronomy  
Project: NASA Astronomy Picture of the Day (APOD) – Streamlit Frontend  
Date: 01/11/2026  

GitHub Repository: [NASA-APOD-Streamlit](https://github.com/sheffysabu22/NASA-APOD-Streamlit)

---

 1. Project Overview

The NASA Astronomy Picture of the Day (APOD) project focuses on presenting astronomy-related images and information through a user-friendly application.

My individual contribution focuses on developing the frontend using Streamlit, a Python framework for creating interactive web applications.

The application retrieves astronomy picture information and presents the image along with its associated details.

The main objective is to provide a simple and accessible interface through which users can explore astronomy content.

 2. Key Features

 2.1 Streamlit User Interface

I developed the frontend using Streamlit. It provides a simple interface for displaying astronomy content without requiring users to interact directly with API responses or terminal output.

 2.2 Astronomy Image Display

The application displays the astronomy picture as its main visual element, allowing users to view the selected image directly through the interface.

 2.3 Display of Picture Information

The application presents information associated with the astronomy picture, including:

- Title: Identifies the astronomy picture.
- Date: Shows the publication date.
- Explanation: Provides information about the astronomical subject.
- Image: Displays the astronomy picture.

 2.4 API Integration

The application uses Python's `requests` library to send HTTP requests and retrieve astronomy picture information from the configured data source.

 2.5 Secret Management

I used a `.env` file to store the NASA API key separately from the application code.

The `python-dotenv` package loads environment variables when the application runs.

The `.env` file is excluded from GitHub using `.gitignore` to prevent accidental exposure of the API key.

 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Frontend and user interface |
| Requests | Sending HTTP requests |
| python-dotenv | Loading environment variables |
| uv | Python project and dependency management |
| VS Code | Code editing and project development |
| Git | Version control |
| GitHub | Repository hosting and collaboration |
| NASA APOD | Astronomy picture content |

 4. Repository Structure

The project repository contains the following files:

```text
NASA-APOD-Streamlit/
│
├── app.py
├── pyproject.toml
├── uv.lock
├── requirements.txt
├── .gitignore
└── README.md
```

 File Descriptions

- app.py: Contains the Streamlit application and frontend implementation.
- pyproject.toml: Defines project information, Python requirements and dependencies.
- uv.lock: Records the resolved dependency versions to support reproducible installations.
- requirements.txt: Lists the Python packages required by the application.
- .gitignore: Excludes sensitive and unnecessary files, including `.env`, `.venv/` and Python cache files.
- README.md: Provides project documentation and setup instructions.

The `.env` file contains the local API key and is intentionally excluded from the repository.

 5. Python Environment and Dependency Management

I used `uv` to initialise and manage the Python project environment.

The project uses an isolated virtual environment to keep its dependencies separate from the global Python installation and other projects.

I added the required dependencies using `uv add` and synchronised the environment using `uv sync`.

 Main Dependencies

- streamlit: Used to create and run the frontend application.
- requests: Used to send HTTP requests.
- python-dotenv: Used to load environment variables from the `.env` file.

 Commands Used

Initialise the Python project:

```powershell
uv init --bare
```

Add project dependencies:

```powershell
uv add streamlit requests python-dotenv
```

Synchronise the project environment:

```powershell
uv sync
```

Display the dependency tree:

```powershell
uv tree
```

Run the Streamlit application:**

```powershell
uv run streamlit run app.py
```

The application runs locally in a web browser at:

```text
http://localhost:8501
```

 Running the Project from GitHub

After cloning the repository, use the following commands:

```powershell
git clone https://github.com/sheffysabu22/NASA-APOD-Streamlit.git
cd NASA-APOD-Streamlit
uv sync
uv run streamlit run app.py
```

A valid local `.env` file containing the required API key must be configured before running the application.

Example environment variable format:

```text
NASA_API_KEY=your_nasa_api_key
```

Replace the example value with your own API key. Never upload the actual `.env` file to GitHub.

 6. GitHub Collaboration and Version Control

I used Git for version control and GitHub to host my individual project.

I created a separate GitHub repository named `NASA-APOD-Streamlit` and connected it to my local project.

During development, I performed the following operations:

- Initialised a local Git repository.
- Created and maintained the `.gitignore` file.
- Added and committed project files.
- Connected the local repository to GitHub using a remote named `origin`.
- Managed changes using the `main` branch.
- Integrated the existing GitHub repository history with my local project.
- Resolved Git merge conflicts.
- Committed application and project configuration files.
- Used Git pull and push operations to synchronise local and remote changes.

 Git Commands

```powershell
git init
git status
git add .
git commit -m "Add NASA APOD Streamlit application"
git remote add origin https://github.com/sheffysabu22/NASA-APOD-Streamlit.git
git branch -M main
git pull origin main
git push -u origin main
```

Individual GitHub Repository:

[https://github.com/sheffysabu22/NASA-APOD-Streamlit](https://github.com/sheffysabu22/NASA-APOD-Streamlit)

 7. Learning Outcomes

Through this individual contribution, I gained practical experience in:

- Understanding the role of a frontend in a Python application.
- Developing a user interface using Streamlit.
- Displaying astronomy images and their associated information.
- Using the Requests library to retrieve information through HTTP requests.
- Managing API keys using environment variables.
- Creating and managing Python project environments using `uv`.
- Managing dependencies through `pyproject.toml` and `uv.lock`.
- Understanding dependency trees using `uv tree`.
- Using Git commands for version control.
- Creating and managing a GitHub repository.
- Resolving Git merge conflicts.
- Understanding the importance of excluding sensitive files from version control.

 8. Conclusion

My individual contribution to the NASA Space & Astronomy project focuses on developing a Streamlit-based frontend for NASA Astronomy Picture of the Day content.

I worked on presenting astronomy pictures and their related information through a user-friendly interface. I also gained practical experience in Python environment setup, dependency management using `uv`, API key management and GitHub version control.

By completing and maintaining my individual project on GitHub, I improved my understanding of how a Python-based frontend application is developed, tested and maintained.

 9. References

1. NASA Astronomy Picture of the Day: https://apod.nasa.gov/apod/astropix.html
2. NASA API Documentation: https://api.nasa.gov/
3. Streamlit Documentation: https://docs.streamlit.io/
4. Python Documentation: https://docs.python.org/3/
5. Requests Documentation: https://requests.readthedocs.io/
6. Python-dotenv Documentation: https://pypi.org/project/python-dotenv/
7. uv Documentation: https://docs.astral.sh/uv/
8. Git Documentation: https://git-scm.com/doc
9. GitHub Documentation: https://docs.github.com/
10. Individual Project Repository: https://github.com/sheffysabu22/NASA-APOD-Streamlit
