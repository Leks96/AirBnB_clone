#!/usr/bin/env python3
"""
module file storage serializer
and deserializer JSON types
"""

import json
from models.base_model import BaseModel
from models.user import user

class FileStorage:
	"""
	class for file storage
	"""

	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""
		return dict rep of all obj
		"""
		return self.__objects

	def new(self, object):
		"""sets in objects the obj with the
		key <object class name>.id

		Args:
			object: object to write
		"""
		self.__objects[object.__class__.__name__ + '.' + str(object)] = object

	def save(self):
		"""
		serializes object to the json file
		"""
		with open(self.__file_path, 'w+') as f:
			json.dump({key: val.to_dict() for key, val in self.__objects.items()
					}, f)

	def reload(self):
		"""
		deserialize the json file to_objects, if
		it exist otherwise nothing
		"""
		try:
			with open(self.__file_path, 'r') as f:
				dict = json.loads(f.read())
				for val in dict.values():
					classes = val["__class__"]
					self.new(eval(classes)(**val))
		except Exception:
			pass
