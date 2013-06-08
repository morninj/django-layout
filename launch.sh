#!/bin/bash
set -e
LOGFILE=/var/sites/virtualenvs/{{ project_name }}/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# TODO change user
USER=ubuntu
GROUP=ubuntu
cd /var/sites/virtualenvs/{{ project_name }}/src/{{ project_name }}/
source ../../bin/activate
exec ../../bin/gunicorn_django -b 127.0.0.1:8000 -w $NUM_WORKERS --user=$USER --group=$GROUP --log-level=debug --log-file=$LOGFILE 2>>$LOGFILE
