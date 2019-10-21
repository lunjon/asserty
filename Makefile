test:
	pytest -v tests


dist:
	python3 setup.py sdist bdist_wheel

publish:
	python3 -m twine upload dist/*

clean:
	find . ( -name __pycache__ -o -name .pytest_cache ) -exec -rm -r {} +
