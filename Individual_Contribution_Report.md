# EPITA TP2 – Individual Contribution Report

**Student Name:** Sheffy Sabu  
**EPITA Login:** sheffy.sabu@epita.fr  
**Assigned API Group:** Group 5 – Space & Astronomy  
**Project:** NASA Astronomy Picture of the Day (APOD) – Streamlit Frontend  
**Date:** 01/11/2026  

**GitHub Repository:** https://github.com/sheffysabu22/NASA-APOD-Streamlit

---

## 1. Project Overview

The NASA Astronomy Picture of the Day (APOD) project focuses on presenting astronomy-related images and information through a user-friendly application.

My individual contribution focuses on developing a frontend application using Streamlit. The application retrieves astronomy picture information and displays the image along with its relevant details.

The main objective of my work is to create a simple and accessible interface through which users can explore NASA's Astronomy Picture of the Day content.

## 2. Key Features

### 2.1 Streamlit User Interface

I developed the frontend using Streamlit, a Python framework that allows developers to create interactive web applications without requiring extensive frontend programming.

### 2.2 Astronomy Image Display

The application displays the astronomy picture as the main visual element. This allows users to view the selected astronomical image directly through the interface.

### 2.3 Display of Picture Information

The application presents the information associated with the astronomy picture, including:

- **Title:** Identifies the astronomy picture.
- **Date:** Shows the publication date.
- **Explanation:** Provides information about the astronomical subject.

### 2.4 API Integration

The application uses Python's `requests` library to make HTTP requests and retrieve the required astronomy picture information.

### 2.5 Secret Management

I used a `.env` file to store the NASA API key separately from the application code. The `python-dotenv` package loads the environment variable when the application runs.

The `.env` file is excluded from GitHub using `.gitignore` to prevent accidental exposure of the API key.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Developing the frontend interface |
| Requests | Sending HTTP requests |
| python-dotenv | Loading environment variables |
| VS Code | Writing and managing the project code |
| Git | Version control |
| GitHub | Hosting the project repository |

## 4. Repository Structure

The project repository contains the following files:

```text
NASA-APOD-Streamlit/
│
├── app.py
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

**File descriptions:**

- `app.py` – Contains the Streamlit application and frontend implementation.
- `requirements.txt` – Lists the Python packages required to run the application.
- `.gitignore` – Excludes sensitive and unnecessary files, including `.env`, `.venv/`, and Python cache files.
- `README.md` – Provides project documentation.

The `.env` file contains the local NASA API key and is intentionally excluded from the repository.

## 5. Python Environment and Dependency Management

I created an isolated Python virtual environment for the project using Python's built-in `venv` module.

This environment keeps the project's installed packages separate from the global Python installation and other projects.

I installed the required dependencies using the `requirements.txt` file.

The main dependencies are:

- `streamlit` – For creating and running the web application.
- `requests` – For making HTTP requests.
- `python-dotenv` – For loading the API key from the environment file.

### Commands Used

**Create a virtual environment:**

```powershell
python -m venv .venv
```

**Activate the environment:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Install dependencies:**

```powershell
python -m pip install -r requirements.txt
```

**Run the Streamlit application:**

```powershell
python -m streamlit run app.py
```

The application runs locally in a web browser at:

```text
http://localhost:8501
```

## 6. GitHub Collaboration and Version Control

I used Git for version control and GitHub to host my individual project.

I created a separate GitHub repository named `NASA-APOD-Streamlit` and connected it to my local project.

During this process, I performed the following operations:

- Initialised a local Git repository.
- Created and maintained the `.gitignore` file.
- Added the project files to Git.
- Committed the application files.
- Connected the local repository to GitHub using a remote named `origin`.
- Integrated the existing GitHub repository history with my local project.
- Resolved a merge conflict in `.gitignore`.
- Pushed the completed project to the `main` branch.

**Git commands used:**

```powershell
git init
git status
git add .
git commit -m "Add NASA APOD Streamlit application"
git remote add origin https://github.com/sheffysabu22/NASA-APOD-Streamlit.git
git branch -M main
git pull origin main --allow-unrelated-histories --no-edit
git push -u origin main
```

**Individual GitHub Repository:**

https://github.com/sheffysabu22/NASA-APOD-Streamlit

The project was successfully uploaded, and the local branch was configured to track the remote `main` branch.

## 7. Learning Outcomes

Through this individual contribution, I gained practical experience in:

- Understanding the role of a frontend in a Python application.
- Developing a user interface using Streamlit.
- Displaying astronomy images and their associated information.
- Using the Requests library to retrieve information through HTTP requests.
- Managing API keys using environment variables.
- Creating and managing isolated Python virtual environments.
- Installing project dependencies using `requirements.txt`.
- Using Git commands for version control.
- Creating and managing a GitHub repository.
- Resolving a Git merge conflict.
- Understanding the importance of excluding sensitive files from version control.

## 8. Conclusion

My individual contribution to the NASA Space & Astronomy project focuses on developing a Streamlit-based frontend for NASA's Astronomy Picture of the Day application.

I worked on presenting astronomy pictures and their related information through a user-friendly interface. I also gained practical experience in Python environment setup, dependency installation, API key management, and GitHub version control.

By completing and uploading my individual project to GitHub, I improved my understanding of how a Python-based frontend application is developed, tested, and maintained.

## 9. References

- NASA Astronomy Picture of the Day: https://apod.nasa.gov/apod/astropix.html
- NASA API Documentation: https://api.nasa.gov/
- Streamlit Documentation: https://docs.streamlit.io/
- Python Documentation: https://docs.python.org/3/
- Requests Documentation: https://requests.readthedocs.io/
- Python-dotenv Documentation: https://pypi.org/project/python-dotenv/
- Git Documentation: https://git-scm.com/doc
- GitHub Documentation: https://docs.github.com/
- Individual Project Repository: https://github.com/sheffysabu22/NASA-APOD-Streamlit
