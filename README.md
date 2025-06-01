# Python URL Shortener

A simple yet powerful URL shortener service built with Python and Flask. This service allows users to paste a long URL and get a unique, shorter link. It also includes basic click tracking for the shortened links.

## Features

-   **URL Shortening:** Convert long URLs into concise, easy-to-share short links.
-   **Click Tracking:** Basic tracking of how many times a shortened link has been accessed.
-   **Web Interface:** A simple and clean web page to shorten URLs.
-   **SQLite Database:** Uses SQLite for data storage, making it lightweight and easy to set up.
-   **Test Suite:** Includes unit tests to ensure reliability.
-   **Open for Contributions:** Designed to be extended and improved by the community.

## Technologies Used

-   **Python:** Core programming language.
-   **Flask:** Micro web framework for the web interface and API.
-   **SQLite:** Self-contained, serverless database.
-   **HTML/CSS:** For the frontend user interface.
-   **unittest:** Python's built-in library for testing.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   Python 3.6 or higher
-   pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/RamaAditya49/LinkShrinkr.git
    cd your-repository-name
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    The only external dependency for the core application is Flask.
    ```bash
    pip install Flask
    ```

### Running the Application

1.  **Initialize the database (if not already done by the app):**
    The application is designed to create `urls.db` and the necessary table on first run.

2.  **Run the Flask development server:**
    ```bash
    python app.py
    ```
    The application will be accessible at `http://127.0.0.1:5000/`.

### Running Tests

To run the automated tests:

```bash
python test_app.py
```

## How to Contribute

Contributions are welcome and appreciated! Here's how you can contribute:

1.  **Fork the Project:** Click the 'Fork' button at the top right of this page.
2.  **Create your Feature Branch:**
    ```bash
    git checkout -b feature/AmazingFeature
    ```
3.  **Commit your Changes:** Make your changes and commit them with clear, descriptive messages.
    ```bash
    git commit -m 'Add some AmazingFeature'
    ```
4.  **Push to the Branch:**
    ```bash
    git push origin feature/AmazingFeature
    ```
5.  **Open a Pull Request:** Go to your fork on GitHub and open a pull request to the main repository.

Please make sure to update tests as appropriate and follow the existing code style.

## Future Enhancements (Ideas for Contribution)

-   Custom short URLs.
-   API for programmatic URL shortening.
-   More detailed analytics (e.g., referrers, timestamps of clicks).
-   User accounts to manage links.
-   Rate limiting.
-   Asynchronous task queue for URL processing if external checks are added (e.g., checking if URL is live).
-   Option to set expiration dates for links.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

-   Inspired by various URL shortener services.
-   Built with guidance from the Flask documentation.
```
