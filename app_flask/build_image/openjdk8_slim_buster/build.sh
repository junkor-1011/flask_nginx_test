#!/bin/bash

# 実行スクリプトのpath取得
# https://qiita.com/koara-local/items/2d67c0964188bba39e29
SCRIPT_DIR=$(cd $(dirname $0); pwd)
cd $SCRIPT_DIR

# symbolicの実体を辿ってimageをbuild
# ref: https://blog.kkty.jp/entry/2019/06/16/214951
tar -czh . | docker build \
        -t app_flask_test_openjdk8_slim_buster \
        --build-arg BASE_IMAGE=openjdk:8u242-jre-slim-buster \
        --build-arg USER_UID=1000 \
        --build-arg PYTHON_VER=3.7 \
        - 
