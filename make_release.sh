#!/usr/bin/env bash

rm -rf --verbose dist  *.egg-info && python setup.py sdist  && twine check dist/* && twine upload dist/*