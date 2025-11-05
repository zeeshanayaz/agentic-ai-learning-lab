import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Todo App", page_icon="📝", layout="centered")

st.title("Todo App (FastAPI + Streamlit)")
st.write("Add and view your tasks easily!")

# --- Add Task Form ---
st.subheader("Add a New Task")
with st.form("add_task_form"):
    name = st.text_input("Task Name")
    description = st.text_area("Task Description")
    submitted = st.form_submit_button("Add Task")

    if submitted:
        if name.strip():
            data = {
                "name": name,
                "description": description,
                # completed not included → defaults to False automatically
            }
            response = requests.post(f"{API_URL}/tasks", json=data)
            if response.status_code == 200:
                st.success("Task added successfully!")
            else:
                st.error(f"Failed to add task. ({response.status_code})")
        else:
            st.warning("Please enter a task name.")

# --- View Tasks ---
st.subheader("View Tasks")
if st.button("Refresh List"):
    response = requests.get(f"{API_URL}/tasks")
    if response.status_code == 200:
        tasks = response.json()
        if tasks:
            for idx, task in enumerate(tasks, start=1):
                status = "✅ Completed" if task["completed"] else "❌ Pending"
                st.markdown(f"**{idx}. {task['name']}** — {status}  \n{task.get('description', '')}")
        else:
            st.info("No tasks found yet.")
    else:
        st.error("Failed to fetch tasks.")
