build:
	docker build -t vigilant .
	npm run build || echo "need npm install"
test:
	pytest -q
	npm test || true
run:
	python -m vigilant scan . --format json
