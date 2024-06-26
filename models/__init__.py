#!/usr/bin/python3
"""Object storage instantiation

    * If environment variable `HBNB_TYPE_STORAGE` is set to `db`,
    instantiates a database storage engine (DBStorage).
    * Otherwise, instantiates a file storage engine (FileStorage).
"""

from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
