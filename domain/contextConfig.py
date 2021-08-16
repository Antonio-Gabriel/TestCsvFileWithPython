#!python3

from abc import ABC, abstractmethod
from typing import IO
from dbContext import *

class Context(ABC):

    @abstractmethod
    def context_init(mode: str) -> IO:
        csv_file = open(f'{ROOT}/repo/context.csv', mode, encoding= 'UTF8', newline= '')
        return csv_file
