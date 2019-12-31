#! /bin/bash

PYTHON_VENV_NAME=FaceDetect
PYTHON_VERSION=3.7.6

pyenv virtualenvs | grep $PYTHON_VENV_NAME > /dev/null
found=$?

if [ $found -ne 0 ]; then
    pyenv virtualenv $PYTHON_VERSION $PYTHON_VENV_NAME
fi

pyenv activate $PYTHON_VENV_NAME

pip install -U numpy scipy matplotlib opencv-python
