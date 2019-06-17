from topic import topic
import applicationMap


class user(object):
    def __init__(self):
        self.topics = {}

    def add_topic(self, new_topic):
        self.topics[new_topic] = topic()
        print(self.topics)

    def delete_topic(self, old_topic):
        self.topics.remove(old_topic)

    def check_if_active_topic(self, topic):

        if topic not in applicationMap.m_user.topics:
            print("yay")
            return False

    def print_all(self):
        for topic in self.topics:
            print(topic)
            for key in self.topics.keys():
                for task in self.topics[key].task_list:
                    print(task[0])

    def prioritize(self, topics_dictionary):
            for topic in topics_dictionary:
                print(topic)
                prioritized_tasks= []
                longest_duration = 0
                longest_duration_key = None
                for i in range(0, len(self.topics[topic].task_list)):
                    for task in self.topics[topic].task_list:
                        if longest_duration <= task[1]:
                            prioritized_tasks.insert(0,task[0]) 
                            longest_duration = task[1]
                            #longest_duration_key = task
                            self.topics[topic].task_list.remove(task)
                for task in prioritized_tasks:
                    print(task)
                            


