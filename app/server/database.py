import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.wishlist

wishes_collection = database.get_collection("wishes_collection")

# helpers


def wishes_helper(Item) -> dict:
    return {
        "id": str(Item["id"]),
        "fullname": Item["name"],
        "description": Item["description"],
        "image": Item["image"],
        "link": Item["link"],
        "have": Item["have"],
    }
