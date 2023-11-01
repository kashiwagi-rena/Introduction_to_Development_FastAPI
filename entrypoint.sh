#!/bin/bash

# DB migretionを実行する
poetry run python -m api.migrae_cloud_db

# uvicornのサーバーを立ち上げる
poetry run uvicorn api.main:app --host 0.0.0.0 --reload