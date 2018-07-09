#!/usr/bin/env bash

# build package and upload to private pypi index
cat <<EOF >> ~/.pypirc
[distutils]
index-servers =
    master
    develop

[master]
repository: ${PYPI_HOST}
username: ${PYPI_USERNAME}
password: ${PYPI_PASSWORD}

[develop]
repository: ${DEVELOP_PYPI_HOST}
username: ${DEVELOP_PYPI_USERNAME}
password: ${DEVELOP_PYPI_PASSWORD}
EOF
