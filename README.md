# 🧠 Flashcard Quiz App

A Streamlit web app that tests your programming knowledge through multiple-choice flashcard quizzes. Pick a category, choose how many questions you want, and get instant feedback with explanations as you go.

## Project Status

This project is currently under development.

In Progress — core quiz flow is functional (category selection, scoring, explanations, restart), but the app is still being actively developed and refined. Expect changes and possible bugs.

## Current Features

* **Multiple-choice quiz format with shuffled answer options each round.**
* **Category selection — quiz on "All" topics or filter to a specific category from questions.json.**
* **Adjustable question count via a slider (5, 10, 15, 20, or max available).**
* **Instant feedback after each answer — correct/incorrect with the right answer shown.**
* **Explanations displayed after answering, when available for a question.**
* **Live sidebar stats — running score and current question progress.**
* **Progress bar tracking how far through the quiz you are.**
* **End-of-quiz summary with score, percentage, and a performance message (with balloons for high scores 🎈).**
* **Restart option to immediately start a new quiz.**


## Project Structure

```text
Flashcard-Quiz/
│
├── app.py
├── questions.json
├── requirements.txt
├── .gitignore
└── README.MD

```

## Technologies Used

- Python
- Streamlit
- JSON
- Random module
- Git & GitHub

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ShivtejPatil2807/Simple-Guess-Game.git
```

### 2. Open the project folder

```bash
cd  Flashcard-Quiz
```

### 3. Install the required packages 

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

## Question Data
Quiz questions are stored in questions.json they contains:

* **Question**
* **Multiple-choice options**
* **Correct answer**
* **Category**
  
## How It Works

1. Launch the Flashcard Quiz App.
2. Select a programming category.
3. Click Start Quiz.
4. Answer the question.
5. Submit your answer.
6. View your score.

## Live Demo

Coming soon! The application will be deployed using Streamlit Community Cloud.

### 👨‍💻 Author

**Shivtej Patil**

GitHub: [ShivtejPatil2807](https://github.com/ShivtejPatil2807)
