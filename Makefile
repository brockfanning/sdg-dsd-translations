install:
	pip install -r requirements.txt --upgrade
	bundle install

import:
	python scripts/import.py

export:
	python scripts/export.py

build: export
	bundle exec jekyll build

serve: export
	bundle exec jekyll serve
