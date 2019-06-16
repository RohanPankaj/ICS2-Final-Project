from user import user
from topic import topic

introuction_prompt = "You are using Organize an interactive task manager that will prioritize your tasks in order of greatest to lead importance. Lets Get Started!"
instructions = " Here is a list of things you can type into the terminal. \nadd task - add a new task to your task manager\nadd topic - add a new topic to your task manger \n remove topic - remove a topic from your task manager this will most commpnly be used when you have completed a task \nremove topic - this will remove a topic from your task manger \nprioritize - this will sort all of the taskes in your individual topics and give you a list of what needs to be done and in what order\nprint- prints out all your tasks unsorted with their corresponding topics"


m_user = input("What is your name ")
m_user = user()


new_topic_def = topic()
# ef assign_topic_def():


def task_action_prompt():
    topic = input("What is the name of the topic this task is associated with? ")
    task = input("What is the name of the task? ")

    return topic, task