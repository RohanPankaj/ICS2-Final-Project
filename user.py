from topic import topic
import applicationMap


class user(object):
    def __init__(self):
        self.topics = {}

    def add_topic(self, new_topic):
        print("yay again")
        new_topic
        self.new_topic_def = topic()
        self.topics[new_topic] = self.new_topic_def
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
                
                for task in self.topics[key]:
                    print(applicationMap.m_user.topics[key])
                    print(task)
                    print(task)
                    print(task[0][0])