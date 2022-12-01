from src.extensions.database import db


class AbstractDB:
    def __init__(self, table):
        self.table = table

    def get_by_id(self, object_id):
        query = db.session.query(self.table).get(object_id)
        return query

    def delete_by_id(self, object_id):
        pass

    def register_object(self, object):
        db.session.add(object)
        db.session.commit()
        db.session.refresh(object)
