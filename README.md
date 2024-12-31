Automation Bot: Selenium-Based Quiz Completion

This repository contains a Python script that automates logging in to the ThingQbator NASSCOM Foundation website, handles popups, navigates to an “HTML & CSS” course, clicks “Take Course,” then completes a quiz by selecting answers and submitting. It repeats these actions for each user in a provided list of email–password credentials.
1. Prerequisites

    Python 3.7+ installed.
    GeckoDriver (for Firefox) installed.
        Ensure it’s in your system’s PATH or update the script’s executable_path to point to geckodriver.
    Selenium Python library:

    pip install selenium

2. Usage

    Clone or Download this repository (or just copy the Python script).
    Open the script file (e.g., automation.py).
    Review or Edit:
        CREDENTIALS: The list of dictionaries at the bottom of the script. Each entry has:

{ "email": "example@gmail.com", "password": "12345678" }

ANSWER_KEY: A dictionary at the top of the script that maps quiz questions to correct answers:

    ANSWER_KEY = {
        "Which of the following are examples of block-level elements": "A,B,C",
        "What is the function of the HTML style attribute?": "A",
        ...
    }

    If the quiz question text changes, update keys accordingly or add new ones.

Run the script:

    python automation.py

3. What the Script Does

    Iterates over each user credential in CREDENTIALS.
    Opens Firefox (webdriver.Firefox).
    Navigates to the login page and logs in using the user’s email and password.
    Handles Popups:
        “GET STARTED” popup.
        Interests popup (selects “Robotics” and “IoT,” then clicks “Save”).
    Navigates to the “HTML & CSS” course and clicks “Take Course.”
    Clicks “Take Quiz.”
    Completes the Quiz:
        Finds each question (using the Angular Material stepper).
        Matches question text to an entry in ANSWER_KEY.
        Selects the correct choice(s) (radio or checkbox).
        Clicks “Next” until the last step, then Submits the quiz.
    Closes the browser and proceeds to the next user.

4. Customizing the Script

    Updating Interests:
    Inside the code, you’ll see a list interests = ["Robotics", "IoT"]. Modify as needed for other interests.

    Quiz Logic:
        If your quiz uses checkboxes for multiple answers, ensure the code looks for <mat-checkbox> elements.
        If single-choice, the code uses <mat-radio-button> elements.

    Answer Key:
        Keys: partial text or exact text from the <h6> question tag.
        Values: “A” or “A,B,C” or whichever combination. “A” means first option, “B” means second, and so on.

    Error Handling:
        If an exception occurs for one user (e.g., cannot find a button), the script prints the error, closes that user’s browser, and continues.

5. Troubleshooting

    Element Not Found:
        The site’s HTML structure may change. Verify the XPaths or CSS selectors in the script.
    Quiz Text Mismatch:
        If the question text doesn’t match the key in ANSWER_KEY, it won’t select answers. You may need to add or modify dictionary entries.
    Timeouts:
        If pages or popups load slowly, increase the WebDriverWait timeout or add short time.sleep() calls.

6. License

This script is provided as-is with no warranty. Adjust and use it responsibly according to your needs.
