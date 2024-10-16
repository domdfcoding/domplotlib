# stdlib
import json
from operator import itemgetter

for filename in [
		"tests/image_hashes_36.json",
		"tests/image_hashes_37.json",
		"tests/image_hashes_38.json",
		"tests/image_hashes_39.json",
		"tests/image_hashes_313.json",
		"tests/image_hashes.json",
		]:
	with open(filename, encoding="UTF-8") as fp:
		data = list(json.load(fp).items())

	data.sort(key=itemgetter(0))
	with open(filename, 'w', encoding="UTF-8") as fp:
		json.dump(dict(data), fp, indent=2)
		fp.write('\n')
