#!/bin/bash
# sudo ./filter_list.sh

export FLASK_APP=filter_list.py
export FLASK_ENV=development
flask run
