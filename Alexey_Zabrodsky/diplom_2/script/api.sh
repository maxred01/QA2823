#!/bin/bash
cd ../
pwd
pytest -s -v tests/test_dollar.py --alluredir=results
