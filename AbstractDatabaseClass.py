from abc import ABC, abstractmethod
from sqlalchemy import create_engine


class AbstractDatabaseClass(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def init_db(self):
        engine = create_engine('mysql+pymysql://root:Floppy9side@localhost:3306/PLNT')  # TODO: REMOVE
        connection = engine.connect()