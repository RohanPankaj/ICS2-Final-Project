#from main import m_user
import user
import applicationMap
#import task
#from task import task


class topic(object):

    def __init__(self):
        self.task_list = []

    def add_task(self, topic, new_task):
        
        duration = int(input(
            "How long to you estimate in minuets this task taking? (Enter your answer as an integer ie. 1)"))
        notes = input("Do you have any notes for this task")
        applicationMap.m_user.topics[topic].task_list.append([new_task,duration, notes])

    def delete_task(self, topic, new_task):
        applicationMap.m_user.topics[topic].remove(new_task)

    def update_list(self):
        self.task_list
