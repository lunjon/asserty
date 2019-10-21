test:
	pytest -v tests

dist:
	python3 setup.py sdist bdist_wheel

publish:
	python3 -m twine upload dist/*

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	rm -rf asserty.egg-info build dist
	
.PHONY: clean dist publish test