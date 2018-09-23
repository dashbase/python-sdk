# Dashbase python-sdk
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fdashbase%2Fpython-sdk.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fdashbase%2Fpython-sdk?ref=badge_shield)



## DEV

```
pip install dashbase_sdk

# test pypi
pip install --index-url https://test.pypi.org/simple/ dashbase_sdk
```


### Build package

```
pipenv install --dev
pipenv shell

python3 setup.py sdist bdist_wheel

```

### Upload

```
twine upload  dist/*

# test pypi
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

```

## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fdashbase%2Fpython-sdk.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fdashbase%2Fpython-sdk?ref=badge_large)