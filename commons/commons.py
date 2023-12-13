import requests
import pymongo
from pymongo.collection import Collection
from pymongo.errors import ConnectionFailure

__client: pymongo.MongoClient = None


def fetch_data(url: str):
    print("fetching data...")
    try:
        response = requests.get(url)

        # returns a dict object
        return response.json()

    except Exception as er:
        print(f"Failed to fetch data {er}")
        return {}


def connect_to_mongodb(connection_string: str):
    global __client
    print("Connecting to MongoDB")
    try:
        if __client is None:
            # Connect to MongoDB
            __client = pymongo.MongoClient(connection_string)
            print("Connected to MongoDB")
    except ConnectionFailure as error:
        print(f"Failed to connect to MongoDB: {error}")


def get_client():
    if __client is not None:
        return __client


def connect_to_database(client, database):
    if client is not None:
        try:
            print("Connecting to Database", database)
            db = client[database]
            return db
        except Exception as er:
            print("Database Connection failed", str(er))


def connect_to_collection(database, collection: Collection):
    if database is not None:
        try:
            print("Connecting to Collection", database)
            collection = database[collection]
            return collection
        except Exception as er:
            print("Connecting to Collection failed", str(er))


def insert_data_into_mongodb(collection: Collection, data):
    if collection is not None:
        try:
            print("Inserting data to Collection", collection)

            # Insert data into MongoDB
            collection.insert_many(data)
            return True
        except Exception as er:
            print("Inserting data failed", str(er))

    return False


def close_mongodb_connection():
    global __client
    if __client is not None:
        __client.close()
        print("MongoDB connection closed.")
