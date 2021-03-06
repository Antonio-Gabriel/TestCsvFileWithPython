# Test Csv File With Python

Teste de leitura de um arquivo **CSV** para implementação no projecto EmployeeRegister,
basicamente esse protótipo faz apenas a leiruta e inserção em uma única linha os dados para o arquivo csv.


Depois será adicionado como módulo no projecto `Employee`

Exemplo de implementação da leitura

```python
class Context(ABC):

    @abstractmethod
    def context_init(mode: str) -> IO:
        csv_file = open(f'{ROOT}/repo/context.csv', mode, encoding= 'UTF8', newline= '')
        return csv_file
```


```python
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
```

```python
csv_file.insert_data(*[
    {            
        "name": "Herlander de Castro  Bento",
        "age": 20,
        "phone": 987345232
    }
])
```


Apresentação do retorno dentro do arquivo **csv**

```csv
id,name,age,phone
769331be-927a-4580-bdcb-2f72ddb80c86,Herlander de Castro Bento,20,987345232

```