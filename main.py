import applicationMap


action = input("What do you want to do? ")
if action == "add task":
    topic = input("What topic is this associated with? ")
    if applicationMap.m_user.check_if_active_topic(topic) == False:
        applicationMap.m_user.add_topic(topic)
    print(applicationMap.m_user.topics[topic])
    applicationMap.m_user.topics[topic].add_task(topic)
elif action == "add topic":
    u_topic = input("What is the name of the new topic")
    applicationMap.m_user.add_topic(u_topic)
    print(applicationMap.m_user.topics)
elif action == "remove task":
    u_task = input("What is the task you want to delete ")
    u_topic = input("what topic does this task fall under? ")
    applicationMap.m_user.topics[u_topic].remove(u_task)
elif action == "remove topic":
    u_topic = input("What is the name of the topic you want to delete")
    applicationMap.m_user.delete_topic(u_topic)
