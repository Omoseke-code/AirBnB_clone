#!/usr/bin/python3
"""initialises when package is used"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
