from pymongo import MongoClient

uri = "your_mongo_chain_connection"

def create_collection_and_insert_documents():
    client = MongoClient(uri)

    db = client['studentsDC']

    collection = db['studentsDC']

    print("Collection 'comidas_colombianas' created successfully!")

    documents = [
        {
            "name": "Arepa",
            "description": "A type of food made of ground maize dough, originating from Colombia.",
            "ingredients": ["maize", "salt", "water"],
            "region": "Various regions in Colombia"
        },
        {
            "name": "Bandeja Paisa",
            "description": "A traditional Colombian dish from the Antioquia region.",
            "ingredients": ["beans", "rice", "pork", "egg", "plantain", "arepa"],
            "region": "Antioquia"
        },
        {
            "name": "Sancocho",
            "description": "A traditional Colombian soup, often made with chicken, beef, or fish.",
            "ingredients": ["meat", "potatoes", "yuca", "corn", "plantain"],
            "region": "Various regions in Colombia"
        },
        {
            "name": "Ajiaco",
            "description": "A traditional Colombian soup made with chicken, potatoes, and herbs.",
            "ingredients": ["chicken", "potatoes", "corn", "guascas", "cream", "capers"],
            "region": "Cundinamarca, Bogotá"
        },
        {
            "name": "Lechona",
            "description": "A traditional dish made with roasted pig stuffed with rice, peas, and spices.",
            "ingredients": ["pork", "rice", "peas", "spices"],
            "region": "Tolima"
        },
    ]

    result = collection.insert_many(documents)
    print(f"{len(result.inserted_ids)} documents inserted into the collection!")

    client.close()

if __name__ == "__main__":
    create_collection_and_insert_documents()
