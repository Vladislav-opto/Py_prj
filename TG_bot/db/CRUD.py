from db import db_session
from models import Good

def add_receipt_content(receipt_content: list, receipt_id: int) -> None:
    for good in receipt_content:
        good["receipt_id"] = receipt_id
    db_session.bulk_insert_mappings(Good, receipt_content)
    db_session.commit()


def get_receipt_content(content_id: int) -> str|None:
    if db_session.query(Good.query.filter(Good.id == content_id).exists()).scalar():
        return Good.query.get(content_id)
    else:
        return None    


def delete_receipt_content(content_id: int) -> None:
    content = Good.query.get(content_id)
    db_session.delete(content)
    db_session.commit()
