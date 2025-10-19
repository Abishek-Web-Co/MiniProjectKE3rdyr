# Plant Doctor 🩺🌱

Plant Doctor is a simple, modern web application built with Flask that helps users diagnose common houseplant problems. It uses a multi-step "wizard" questionnaire to gather symptoms and provides a diagnosis, solution, and reasoning based on a simple expert system.

![Plant Doctor Questionnaire](httpsAfter-you-upload-a-screenshot-put-its-link-here.png)
![Plant Doctor Diagnosis](After-you-upload-a-screenshot-put-its-link-here-2.png)
*(**Note:** Replace the image links above with screenshots of your actual application!)*

---

## ✨ Features

* **Multi-Step Wizard:** A clean, responsive form that guides the user through questions one at a time.
* **Dynamic Progress Bar:** A visual indicator that shows the user's progress through the questionnaire.
* **Simple Expert System:** The Flask backend contains a set of rules to diagnose problems based on user input.
* **Clear Results:** The app provides a clear diagnosis (e.g., Overwatering, Sunburn), a practical solution, and the reasoning behind its conclusion.
* **Modern UI:** Styled with pure CSS for a clean, plant-themed, and responsive look.

---

## 🛠️ Tech Stack

* **Backend:** [Flask](https://flask.palletsprojects.com/) (Python)
* **Frontend:** HTML5, CSS3, JavaScript
* **Templating:** [Jinja2](https://jinja.palletsprojects.com/)

---

## 🚀 How to Run This Project

Follow these steps to get the application running on your local machine.

### 1. Prerequisites

* Python 3.7+
* `pip` (Python package installer)
* `git` (for cloning)

### 2. Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-project-name.git](https://github.com/your-username/your-project-name.git)
    cd your-project-name
    ```

2.  **Create and activate a virtual environment:**
    * **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    (This project's only dependency is Flask)
    ```bash
    pip install Flask
    ```
    *(**Pro-tip:** For bigger projects, you'd create a `requirements.txt` file by running `pip freeze > requirements.txt` and install with `pip install -r requirements.txt`)*

4.  **Add Diagnosis Images:**
    The `result.html` file tries to load images for each diagnosis. For this to work, create the following folder structure and add your images:
    ```
    /static
        /images
            overwatered.png
            sunburn.png
            underwatered.png
    ```

### 3. Run the Application

With your virtual environment still active, run the Flask app:

```bash
python app.py