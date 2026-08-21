import streamlit as st
import json
import random


st.set_page_config(
    page_title="Flashcard Quiz",
    page_icon="🧠",
    layout="centered"
)

with open ("questions.json","r") as file:
    questions = json.load(file)

def load_states():
    defaults = {
        "start_quiz" : False ,
        "score": 0 ,
        "current_questions": 0 ,
        "answered": False ,
        "selected_answer": None ,
        "quiz_questions": []
    }
    for key , value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value

load_states()

st.title("🧠 Flashcard Quiz")
st.caption(" Test your programming knowledge..!")
st.divider()

if not st.session_state.start_quiz:

    col1 ,col2 = st.columns([2,1], vertical_alignment="bottom")

    with col1:

        categories = ["All"]
        
        for question in questions:
            if question["Category"] not in categories:
                categories.append(question["Category"])

        category = st.selectbox(
            "Choose a category",
            categories
            )

    with col2:
        if st.button("Start Quiz",type = "primary", use_container_width = True):

            if ["category"] == "All":
                selected_questions = questions
            else:
                selected_questions = [q for q in questions if q["Category"] == category]

                random.shuffle(selected_questions)

                st.session_state.quiz_questions = selected_questions
                st.session_state.start_quiz = True
                st.session_state.current_questions = 0
                st.session_state.score = 0
                st.session_state.answered = False

                st.rerun()
else:
    quiz_questions = st.session_state.quiz_questions
    current = st.session_state.current_questions

    if current >= len(quiz_questions):
        st.success("🎉 Quiz Completed.")

        st.metric("Your Score",f"{st.session_state.score} / {len(st.session_state.quiz_questions)}")
        percentage = (st.session_state.score / len(quiz_questions)) * 100

        st.write(f"### Percentage : {percentage :.1f}%")

        if percentage >= 80:
            st.balloons()
            st.success("Excellent Work !")

        elif percentage >= 50:
            st.info("Good job ! Keep practicing.")

        else:
            st.warning("keep learning ! Try again.")

        if st.button("Restart Quiz"):
            st.session_state.quiz_start = False
            st.session_state.score = 0
            st.session_state.current_questions = 0
            st.session_state.answered = False 
            st.rerun()

    else:
        question = questions[current]

        st.write(f"### Question ,{current +1 } / {len(quiz_questions)}")
        st.progress(
            (current + 1) / len(quiz_questions)
        )

        st.write("##")

        st.subheader(question["question"])
        selected = st.radio(
            "Choose your answer",
            question["options"],
            key = f"question_{current}"
        )

        if not st.session_state.answered:
            if st.button("Submit Answer"):

                st.session_state.selected_answer = selected
                st.session_state.answered = True

                if selected == question["answer"]:
                    st.session_state.score += 1

                st.rerun()