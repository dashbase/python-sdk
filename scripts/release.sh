#!/usr/bin/env bash
# This script packages the application and uploads to pypi,
# and automatically make a github release

python setup.py sdist bdist_wheel
twine upload --repository-url ${PYPI_HOST} -u ${PYPI_USERNAME} -p ${PYPI_PASSWORD} dist/*


github-release release --user $CIRCLE_PROJECT_USERNAME \
    --repo $CIRCLE_PROJECT_REPONAME \
    --tag `python setup.py --version`

github-release upload --user $CIRCLE_PROJECT_USERNAME \
    --repo $CIRCLE_PROJECT_REPONAME \
    --tag `python setup.py --version` \
    --name `python setup.py --name`"-"`python setup.py --version`".tar.gz" \
    --file "dist/"`python setup.py --name`"-"`python setup.py --version`".tar.gz"

github-release upload --user $CIRCLE_PROJECT_USERNAME \
    --repo $CIRCLE_PROJECT_REPONAME \
    --tag `python setup.py --version` \
    --name `python setup.py --name`"-"`python setup.py --version`"-py3-none-any.wheel" \
    --file "dist/"`python setup.py --name`"-"`python setup.py --version`"-py3-none-any.wheel"