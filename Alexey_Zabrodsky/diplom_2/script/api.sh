#!/bin/bash
cd ../
pwd
pytest -s -v tests/test_api.py --alluredir=results
