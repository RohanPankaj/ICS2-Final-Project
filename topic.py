#from main import m_user
import user
import applicationMap
#import task
from task import task


class topic(object):
    def __init__(self):
        self.task_list = []
        self.duration = None
        self.notes = None
        ask_def = [self.task_list, self.duration, self.notes]

    def add_task(self, topic, new_task):
        #new_task = input("What is the name of the new task")
        applicationMap.m_user.topics[topic] = applicationMap.m_user.new_topic_def.task_list
        new_task = task()
        applicationMap.m_user.topics[topic].append(new_task)
        new_task.duration = input(
            "How long to you estimate in minuets this task taking? ")
        new_task.notes = input("Do you have any notes for this task")

    def delete_task(self, topic, new_task):
        applicationMap.m_user.topics[topic].remove(new_task)
