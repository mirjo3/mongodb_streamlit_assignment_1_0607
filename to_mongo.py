from base import Base
from dotenv import load_dotenv
import pymongo
import os

# Class definition
class ToMongo(Base):

    def __init__(self):
        # Initialize the instance of our inherited class:
        super().__init__()
        # Load in the env variables
        load_dotenv()
        self.mongo_url = os.getenv('MONGO_URL')
        # Connect to PyMongo
        self.client = pymongo.MongoClient(self.mongo_url)
        # Create a DataBase
        self.db = self.client.db
        # Connect a collection
        self.performance = self.db.performance
   
    def upload_collection(self):
        self.performance.insert_many(self.df.to_dict('records'))


if __name__ == '__main__':
    c = ToMongo()
    print('Successful connection to client object')
    c.upload_collection()
    print('Successful upload of student performance')
