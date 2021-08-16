#!python3

from domain import *


if __name__ == "__main__":
    
    csv_file = Csv()
    data = csv_file.select_data()
    # csv_file.insert_data(*[
    #     {            
    #         "name": "Herlander de Castro Bento",
    #         "age": 20,
    #         "phone": 987345232
    #     }
    # ])
