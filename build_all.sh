#!/bin/bash

# 実行場所
SCRIPT_DIR=$(cd $(dirname $0); pwd)
#cd $SCRIPT_DIR
BUILD_DIR=${SCRIPT_DIR}/app_flask/build_image

# build
# for文を回すなどして自動化しても良いが、例外のディレクトリを作る、
# 順番を決めると行った際に面倒なのでとりあえず手で打ち込む形にする
sh ${BUILD_DIR}/slim_buster/build.sh
sh ${BUILD_DIR}/buster/build.sh
sh ${BUILD_DIR}/centos8/build.sh
sh ${BUILD_DIR}/amazoncorretto8/build.sh
sh ${BUILD_DIR}/openjdk8_slim_buster/build.sh
