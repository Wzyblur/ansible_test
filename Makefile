all:
	@echo 'run gunicorn'
	./run.py
	ansible-playbook -i hosts  deploy.yaml

run_flask:
	gunicorn -c gunicorn_conf.py wsgi:flask_app

run_bottle:
	gunicorn -c gunicorn_conf.py wsgi:bottle_app

deploy:
	git push origin
	ansible-playbook -i hosts  deploy.yaml

