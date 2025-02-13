#!/bin/bash

tox -e py36 -- --mpl-generate-path=tests/baseline_36
tox -e py36 -- --mpl-generate-hash-library=tests/image_hashes_36.json

tox -e py37 -- --mpl-generate-path=tests/baseline_37
tox -e py37 -- --mpl-generate-hash-library=tests/image_hashes_37.json

tox -e py38 -- --mpl-generate-path=tests/baseline
tox -e py38 -- --mpl-generate-hash-library=tests/image_hashes_38.json

tox -e py39 -- --mpl-generate-hash-library=tests/image_hashes_39.json

tox -e py310 -- --mpl-generate-hash-library=tests/image_hashes_313.json

python3 sort_image_hashes.py
