import os
import glob
import hashlib

md5_hash = hashlib.md5()

image_md5_set = set()

unique_entries = 0
duplicates = 0

for file in glob.glob("*.jpg"):
	current_file = open(file, "rb")
	file_content = current_file.read()
	md5_hash.update(file_content)

	hex = md5_hash.hexdigest()
	
	if hex in image_md5_set:
		print("Duplikat!")
		duplicates = duplicates + 1
	else:
		print("Neuer Eintrag: " + file + " - "+hex)
		image_md5_set.add(hex)
		unique_entries = unique_entries + 1

print("Unique Entries: " + str(unique_entries))
print("Duplicates: " + str(duplicates))
