#!/usr/bin/env bash
# This script packages the application and uploads to pypi,
# and automatically make a github release

python setup.py sdist bdist_wheel
twine upload --repository ${CIRCLE_BRANCH} dist/*
