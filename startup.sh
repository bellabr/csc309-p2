#!/bin/bash
check_virtualenv() {
    if ! command -v virtualenv &> /dev/null; then
        echo "virtualenv is not installed. Installing..."
        python3 -m pip install --user virtualenv
        echo "virtualenv installation complete."
    fi
}
python3 -m venv venv
    source "./venv/bin/activate"
    pip install -U pip

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow

python3 ./meetq/manage.py migrate