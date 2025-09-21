# Bug Tracker - A Flask and SQLAlchemy Application

A simple yet powerful bug tracking application built with Python, Flask, and SQLAlchemy. This project was developed with the assistance of Google's Gemini Code Assist, showcasing the power of AI in modern software development. The application allows users to manage a list of bugs, including creating, editing, and deleting them.

## Features

*   **CRUD Functionality:** Create, Read, Update, and Delete bugs.
*   **Status Updates:** Easily update the status of a bug directly from the main page.
*   **Database Integration:** Uses SQLite to persist bug data.
*   **Clean UI:** A simple and intuitive user interface.
*   **Tested:** Comes with a suite of unit tests to ensure reliability.

## Tech Stack

*   **Backend:** Python, Flask, Flask-SQLAlchemy, SQLAlchemy
*   **Frontend:** HTML, CSS, Jinja2
*   **Database:** SQLite
*   **Testing:** Pytest
*   **Development Tool:** Gemini Code Assist

## Getting Started

### Prerequisites

*   Python 3.10+
*   pip

### Installation

1.  Clone the repository:
    ```sh
    git clone <your-repo-url>
    ```
2.  Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```
3.  Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1.  Run the application:
    ```sh
    python app.py
    ```
2.  Open your browser and navigate to `http://127.0.0.1:5001/`.

### Running the Tests

1.  Run the tests:
    ```sh
    pytest
    ```

## Showcasing Gemini Code Assist

This entire application was programmed through the Gemini CLI, demonstrating a novel and powerful workflow for modern software development. Instead of writing code in a traditional IDE, I used natural language prompts to instruct Gemini to build the application, from the initial setup to the final tests.

Here are some of the ways Gemini Code Assist helped me:

*   **End-to-End Development:** Gemini handled the entire development process, including scaffolding the project, creating the database schema, building the Flask backend, and generating the HTML/CSS frontend.
*   **Interactive Refactoring:** I used Gemini to interactively refactor the application. For example, when I wanted to improve the bug update feature, I described the desired user experience, and Gemini implemented the necessary changes to the frontend and backend.
*   **Automated Testing:** Gemini wrote the complete pytest suite for the application, ensuring the code is reliable and robust.
*   **Intelligent Debugging:** When I encountered errors, I could simply paste the traceback and ask Gemini to fix the bug. Gemini would analyze the error, identify the root cause, and apply the fix.
*   **Proactive Code Improvement:** Gemini not only fixed errors but also identified and addressed warnings in the code, proactively improving the code quality.

This project is a testament to the power of AI-assisted development and my ability to leverage cutting-edge tools to build high-quality software efficiently.

## License

This project is licensed under the MIT License.
