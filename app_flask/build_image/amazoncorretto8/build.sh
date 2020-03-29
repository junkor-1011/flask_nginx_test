#!/bin/bash

# 実行スクリプトのpath取得
# https://qiita.com/koara-local/items/2d67c0964188bba39e29
SCRIPT_DIR=$(cd $(dirname $0); pwd)

# symbolicの実体を辿ってimageをbuild
# ref: https://blog.kkty.jp/entry/2019/06/16/214951
tar -czh . | docker build \
        -t app_flask_test_amazoncorretto8 \
        --build-arg BASE_IMAGE=amazoncorretto:8 \
        --build-arg USER_UID=1000 \
        - 
