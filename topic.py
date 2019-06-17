#from main import m_user
import user
import applicationMap
#import task
#from task import task


class topic(object):

    def __init__(self):
        self.task_list = []

    #N: add_task
    # D: adds a task to the corrrespoding topic
    # I: topic (string) - the name of the corresponding topic, new_task (string) - the new task || program will promt usr to enter the ammount of time the task is expected to take and any notes they want to enter
    #R: N/A
    def add_task(self, topic, new_task):
        duration = int(input(
            "How long to you estimate in minuets this task taking? (Enter your answer as an integer ie. 1) "))
        notes = input("Enter and notes (if you have not just hit enter) ")
        applicationMap.m_user.topics[topic].task_list.append(
            [new_task, duration, notes])

    #N: delete_task
    # D: deletes a task from its corresponding topic
    # I: topic (string) - the name of the corresponding topic, old_task (string) - the new task
    #R: N/A

    def delete_task(self, topic, old_task):
        for task in self.task_list:
            if old_task == task[0]:
                self.task_list.remove(task)
