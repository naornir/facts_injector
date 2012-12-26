import time
import datetime
import uuid
import random
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps



class EventGenerator:
    def __init__(self):
        self.users = ["gil","omer","oran","guy","tom","jerry","yossi","roi"]
        self.device_models = ["iPhone5","Iphone","GalaxyS2","GalaxyS3","Android"]
        
    def random_user_event(self, name):
        new_user = {
                    "_id" : "user_" + name,
                    "application" : "testproduct",
                    "user" :  name,
                    "device": self.get_random_device(),
                    "fact" : "user",
                    "gender": "male",
                    "age": random.randint(15,45),
                    "time" : datetime.datetime.now()
                    }

        return new_user

    def get_random_name(self):
        return self.users[ random.randint(1, len(self.users) - 1) ] 
    def get_random_device(self):
        return self.device_models[ random.randint(1, len(self.device_models) - 1) ] 



    def inject(self, number_of_events):
        self.get_db().find.drop()
        for each_name in self.users:
            new_event = self.random_user_event(each_name)
            self.get_db().data.insert(new_event)

    def get_db(self):
        return MongoClient()['bi']






if __name__ == "__main__":
    generator =  EventGenerator()
    generator.inject(500)
