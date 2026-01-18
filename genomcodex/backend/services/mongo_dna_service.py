from db.mongo import dna_collection

def get_all_dna_from_mongo(limit=10):
    records = list(dna_collection.find({}, {"_id": 0}).limit(limit))
    return records

def search_dna_by_name(name: str):
    return list(
        dna_collection.find(
            {"Name": {"$regex": name, "$options": "i"}},
            {"_id": 0}
        )
    )
