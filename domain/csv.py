
from .contextConfig import Context
from uuid import uuid4
from collections import namedtuple

import csv

class Csv:
    
    def __init__(self) -> None:
        self.__context = Context
        self.__header = [ "id", "name", "age", "phone"]


    def insert_data(self, *args):
        cnt_response = self.__context.context_init("w+")
        writer = csv.DictWriter(cnt_response, fieldnames= self.__header)
        writer.writeheader()
        writer.writerows([
            {
                "id": uuid4(),
                "name": args[0]["name"],
                "age": args[0]["age"],
                "phone": args[0]["phone"]
            }
        ])
        cnt_response.close()


    def select_data(self) -> tuple:
        names = []
        user = namedtuple('User', 'id name age phone')

        cnt_response = self.__context.context_init("r")
        reader = csv.reader(cnt_response)           

        for row in reader:
            names.append(row)
        
        cnt_response.close()

        return user(
            id= names[1][0],
            name= names[1][1],
            age= names[1][2],
            phone= names[1][3],
        )        