import logging as logger
from firebase_admin import credentials, firestore, initialize_app


cred = credentials.ApplicationDefault()
initialize_app(cred)
db = firestore.client()


def get_document(collection_name: str, doc_id: str) -> dict:
    """Get one document from a specific collection, as a dictionary.
    Doesn't return subcollections contents
    """
    logger.info(f"[Firestore] Fetching {collection_name}/{doc_id}")
    return db.collection(collection_name).document(doc_id).get().to_dict() or {}


def get_collection(collection_name: str) -> list:
    """Get all documents from a collection, as a list of dictionaries."""
    logger.info(f"[Firestore] Fetching {collection_name}")
    return [
        {"id": doc.id, "data": doc.to_dict()}
        for doc in db.collection(collection_name).get()
    ]


def set_document(collection_name: str, doc_id: str, value: dict):
    """Create a document.
    For update mode, fetch the entire document content and modify the desired value before setting the document.
    This methods follows immutability principle, this means that the whole document will be overwritten when updated.
    """
    logger.info(f"[Firestore] Updating {collection_name}/{doc_id}")
    return db.collection(collection_name).document(doc_id).set(value)


def delete_document(collection_name: str, doc_id: str) -> dict:
    """Delete one document from a specific collection."""
    logger.info(f"[Firestore] Removing {collection_name}/{doc_id}")
    return db.collection(collection_name).document(doc_id).delete()
