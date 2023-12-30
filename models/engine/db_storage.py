#!/usr/bin/python3
"""
    New engine for database storage for the AirBnB project
                                                            """
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.base_model import Base
import os


class DBStorage:
    """
        Mysql DataBase class for storage
                                        """

    __engine = None
    __session = None

    def __init__(self):
        """
            Instance method to handle initialization
                                                    """
        user = os.environ.get("HBNB_MYSQL_USER", "hbnb_dev_db")
        pssword = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST", "localhost")
        db = os.environ.get("HBNB_MYSQL_DB", "hbnb_dev")

        eng_str = "mysql+mysqldb://{}:{}@{}/{}"
        self.__engine = create_engine(eng_str.format(user,
                                                     pssword,
                                                     host,
                                                     db), pool_pre_ping=True)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if os.environ.get("HBNB_ENV") == "test":
            metadata = MetaData(bind=self.__engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """
            Returns A dictionary of all created objects
                                                        """
        new_dict = {}
        classes_to_query = [User, State, City, Amenity, Place, Review]
        classes = {
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
                }

        if cls:
            if not isinstance(cls, str):
                cls = cls.__name__

            objects = self.__session.query(classes.get(cls)).all()

            for obj in objects:
                key = str(cls) + '.' + str(obj.id)
                new_dict[key] = obj
        else:
            for cls in classes_to_query:
                objects = self.__session.query(classes.get(cls)).all()

                if objects != [(None,)]:
                    for obj in objects:
                        key = str(cls) + '.' + str(obj.id)
                        new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """
            Add the object to the current database session
                                                            """
        self.__session.add(obj)

    def save(self):
        """
            Commit all changes of the current database session
                                                                """
        self.__session.commit()

    def close(self):
        """
            Calls remove() method on the private session attribute
                                                                    """
        self.__session.close()

    def delete(self, obj=None):
        """
            Delete from the current database session obj if not None
                                                                    """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
            Create all tables in the database
                                                """
        """from models.city import City
        from models.state import State
        from models.review import Review
        from models.place import Place
        from models.amenity import Amenity
        from models.user import User """
        from models.base_model import Base

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
        Base.metadata.create_all(self.__engine)
