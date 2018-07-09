#!/usr/bin/env bash
#!/usr/bin/env bash
# This script will automatically make a github release after file package generated.

github-release release --user $CIRCLE_PROJECT_USERNAME \
    --repo $CIRCLE_PROJECT_REPONAME \
    --tag `python setup.py --version`

github-release upload --user $CIRCLE_PROJECT_USERNAME \
    --repo $CIRCLE_PROJECT_REPONAME \
    --tag `python setup.py --version` \
    --name `python setup.py --name`"-"`python setup.py --version`".tar.gz" \
    --file "dist/"`python setup.py --name`"-"`python setup.py --version`".tar.gz"