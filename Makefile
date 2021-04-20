install:
	pip install -r requirements.txt --upgrade
	bundle install

import:
	python scripts/import.py

build:
	python scripts/export.py
	bundle exec jekyll serve
