import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# -----------------------------------------------------------------------------
# 1. MASTER ANSWER KEY DICTIONARY
#    Key: (part of) the question text (as it appears in <h6>)
#    Value: "A", "B", "C", "D", or "A,B,C", etc. for multi-select
# -----------------------------------------------------------------------------
ANSWER_KEY = {
    "What is the function of the HTML style attribute?":                "A",
    "What is the correct syntax to write an HTML comment?":             "A",
    "Which of the following are examples of block-level elements":      "A,B,C",
    "Which of the following properties is used to change the font":     "A,B,C",
    "What are the attributes used to change the size of an image?":     "A",
    "Which tag allows you to add a row in a table?":                    "D",
    "How can you make a bulleted list with numbers?":                   "B",
    "In HTML, which attribute is used to create a link that opens":     "D",
    "How can we write comments in CSS?":                                "A",
    "What are the properties of block-level elements?":                 "D",
    "What is the correct syntax for referring an external CSS?":        "B",
    "How can we select an element with a specific ID in CSS?":          "C",
    "Which of the following are valid CSS position property values?":   "D",
    "Which selector do we use to specify the rule for binding some":    "D",
    "What keyword is used to check whether a given property":           "D",
    "Which of the following property changes the style of right":       "D",
    "Which function is used to serialize an object into a JSON":        "A",
    "When the switch statement matches the expression with the given":  "C",
    "What type of CSS is the following code snippet? <h1 style":        "A",
    "Which of the following is the correct way to select all h1":       "A",
    "What will be the output of the following code snippet? var a =":   "D",
    "What will be the output of the following code snippet? a = [1,":   "A",
    "What will be the output of the following code snippet? let a =":   "B",
    "What will be the output for the following code snippet? <p id":    "D",
    "What will be the output of the following code snippet? (function": "C",
    # Add more if your quiz includes additional questions
}

def get_answer_letters(question_text):
    """
    Given the question text from <h6>, return the letters from ANSWER_KEY, 
    e.g. "A", "B", "A,B,C", or None if unknown.
    
    We do partial matching: if a key from ANSWER_KEY is 'in' the question_text,
    we consider it a match.
    """
    question_lower = question_text.lower()
    for key, val in ANSWER_KEY.items():
        if key.lower() in question_lower:
            return val  # e.g. "A,B,C"
    return None

# -----------------------------------------------------------------------------
# 2. CREDENTIALS: Each user’s email & password
# -----------------------------------------------------------------------------
CREDENTIALS = [
    {"email": "jayanthk933@gmail.com",    "password": "12345678"},
    {"email": "sampadun6@gmail.com",      "password": "12345678"},
    {"email": "pandeyduradarshan@gmail.com", "password": "12345678"},
    {"email": "dubeyramaprasad7@gmail.com",  "password": "12345678"},
    {"email": "ashikamondal7457@gmail.com",  "password": "12345678"},
    {"email": "arpitadas3692@gmail.com",     "password": "12345678"},
    {"email": "ramghosh4758@gmail.com",      "password": "12345678"},
    {"email": "dbitan55@gmail.com",          "password": "12345678"},
    {"email": "bagaadi03@gmail.com",         "password": "12345678"},
    {"email": "mithunanerje8539@gmail.com",  "password": "12345678"},
    {"email": "asimb5674@gmail.com",         "password": "12345678"},
    {"email": "arjunghosh5847@gmail.com",    "password": "12345678"},
    {"email": "rajumondal56666675@gmail.com","password": "12345678"},
    {"email": "sagunhebram54@gmail.com",     "password": "12345678"},
    {"email": "snehaghosh5555645@gmail.com", "password": "12345678"},
    {"email": "ranjitpal45667@gmail.com",    "password": "12345678"},
    {"email": "sukhendas5498@gmail.com",     "password": "12345678"},
    {"email": "chowdhuryrick62@gmail.com",   "password": "12345678"},
    {"email": "karunapal723@gmail.com",      "password": "12345678"},
    {"email": "montudas6382@gmail.com",      "password": "12345678"},
    # ... etc. Add more if needed
]

# -----------------------------------------------------------------------------
# 3. MAIN AUTOMATION LOOP
# -----------------------------------------------------------------------------
for creds in CREDENTIALS:
    email = creds["email"]
    password = creds["password"]
    
    print(f"\n=== Starting automation for user: {email} ===")

    # Set up Firefox driver
    service = Service(executable_path='/usr/local/bin/geckodriver')
    driver = webdriver.Firefox(service=service)
    wait = WebDriverWait(driver, 20)

    try:
        # ---------------------------------------------------------------------
        # (A) LOGIN
        # ---------------------------------------------------------------------
        driver.get("https://thingqbator.nasscomfoundation.org/login")

        wait.until(EC.element_to_be_clickable((By.ID, "exampleInputEmail1"))).send_keys(email)
        driver.find_element(By.ID, "exampleInputPassword1").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

        # ---------------------------------------------------------------------
        # (B) HANDLE POPUP #1: "GET STARTED"
        # ---------------------------------------------------------------------
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".mat-mdc-dialog-container")))
        get_started_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'GET STARTED')])[1]"))
        )
        driver.execute_script("arguments[0].click();", get_started_btn)

        # ---------------------------------------------------------------------
        # (C) HANDLE POPUP #2: Interests
        # ---------------------------------------------------------------------
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "app-user-interst-dialog")))
        # Example: pick "Robotics" and "IoT"
        interests = ["Robotics", "IoT"]
        for interest in interests:
            chip_xpath = (
                f"//mat-chip-option//span[contains(@class, 'mdc-evolution-chip__text-label') "
                f"and contains(text(), '{interest}')]/parent::button"
            )
            chip_btn = wait.until(EC.element_to_be_clickable((By.XPATH, chip_xpath)))
            driver.execute_script("arguments[0].click();", chip_btn)
            time.sleep(1)

        save_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//app-user-interst-dialog//button[not(@disabled)][contains(text(), 'Save')]")
            )
        )
        driver.execute_script("arguments[0].click();", save_btn)

        # ---------------------------------------------------------------------
        # (D) NAVIGATE TO "HTML & CSS" COURSE → CLICK "Take Course"
        # ---------------------------------------------------------------------
        time.sleep(2)
        driver.get("https://thingqbator.nasscomfoundation.org/home/mycourses/-html-&-css")

        take_course_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Take Course')]"))
        )
        driver.execute_script("arguments[0].click();", take_course_button)

        # ---------------------------------------------------------------------
        # (E) CLICK “Take Quiz” (if present)
        # ---------------------------------------------------------------------
        # Sometimes it’s a button or link. Adjust the XPath as needed.
        time.sleep(2)
        take_quiz_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Take Quiz')]"))
        )
        driver.execute_script("arguments[0].click();", take_quiz_button)

        # ---------------------------------------------------------------------
        # (F) QUIZ STEP-BY-STEP
        # ---------------------------------------------------------------------
        while True:
            try:
                # 1) Find the *active* step container (where style="visibility: inherit")
                active_panel = wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR,
                         "mat-vertical-stepper .mat-step.ng-star-inserted "
                         ".mat-vertical-stepper-content[style*='visibility: inherit']"
                        )
                    )
                )
            except TimeoutException:
                print("No more visible steps found. Possibly quiz is done.")
                break

            # 2) Extract question text from <h6>
            try:
                h6 = active_panel.find_element(By.TAG_NAME, "h6")
                question_text = h6.text.strip()
            except:
                question_text = ""
            print("Question text found:", question_text)

            # 3) Look up the correct letters from our ANSWER_KEY
            answers_str = get_answer_letters(question_text)
            print("Answers for this question:", answers_str)

            if answers_str:
                letters = [x.strip() for x in answers_str.split(",")]  # e.g. ["A", "B", "C"]
            else:
                letters = []  # No known answer, or unknown question

            # 4) Identify radio buttons vs. checkboxes
            radio_buttons = active_panel.find_elements(By.CSS_SELECTOR, "mat-radio-button")
            checkboxes    = active_panel.find_elements(By.CSS_SELECTOR, "mat-checkbox")

            # 5) For each letter in letters, click the corresponding item
            #    A → index 0, B → index 1, etc.
            for letter in letters:
                index = ord(letter.upper()) - ord("A")  # A=0, B=1, C=2, D=3
                if index < 0: 
                    continue

                # If single-choice
                if radio_buttons:
                    if index < len(radio_buttons):
                        driver.execute_script(
                            "arguments[0].scrollIntoView({block:'center'});",
                            radio_buttons[index]
                        )
                        driver.execute_script("arguments[0].click();", radio_buttons[index])
                        time.sleep(0.5)
                # If multiple-choice
                elif checkboxes:
                    if index < len(checkboxes):
                        driver.execute_script(
                            "arguments[0].scrollIntoView({block:'center'});",
                            checkboxes[index]
                        )
                        driver.execute_script("arguments[0].click();", checkboxes[index])
                        time.sleep(0.5)

            # 6) Look for NEXT or SUBMIT in the active step
            next_button = None
            submit_button = None

            # Attempt to find "Next"
            next_candidates = active_panel.find_elements(
                By.XPATH, 
                ".//button[contains(@class, 'mat-stepper-next') or @matsteppernext]"
                "[contains(., 'Next')]"
            )
            if next_candidates:
                next_button = next_candidates[0]

            # If not found, look for "Submit"
            if not next_button:
                submit_candidates = active_panel.find_elements(
                    By.XPATH,
                    ".//button[contains(., 'Submit') and "
                    "(@type='submit' or contains(@class,'mat-mdc-raised-button'))]"
                )
                if submit_candidates:
                    submit_button = submit_candidates[0]

            # 7) Click Next or Submit
            if next_button:
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", next_button)
                driver.execute_script("arguments[0].click();", next_button)
                time.sleep(1)
            elif submit_button:
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", submit_button)
                driver.execute_script("arguments[0].click();", submit_button)
                print("Quiz submitted!")
                break
            else:
                # No Next or Submit found → probably end of quiz
                print("No Next or Submit found; presumably done.")
                break

        # Give some time to see results
        time.sleep(3)

    except Exception as e:
        print(f"Error with user {email}: {e}")

    finally:
        driver.quit()
        print(f"=== Finished automation for user: {email} ===\n")
