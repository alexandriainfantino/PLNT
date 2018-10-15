from abc import ABC, abstractmethod
from sqlalchemy import create_engine


class AbstractDatabaseClass(ABC):

    @abstractmethod
    def init_db(self):
        engine = create_engine('mysql://ainfantino:PLNT@localhost/test')