# (Args)
# ARG: BASE_IMAGE
# ARG: USER_UID
# ARG: PYTHON_VER


ARG BASE_IMAGE=openjdk:8u242-jre-slim-buster

FROM ${BASE_IMAGE}

# designate using-python
ARG PYTHON_VER=3.7
ENV PYTHON=python${PYTHON_VER}
# python3.8はdebianではまだデフォルトではそのままapt-get出来ない様子

# system update & package install
RUN apt-get clean && \
    apt-get -y update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    ${PYTHON} ${PYTHON}-dev python3-pip python3-setuptools \
    libpcre3 libpcre3-dev \
    zlib1g zlib1g-dev \
    openssl libssl-dev
# todo: 要不要の選別など

# user        
# ref:
# https://zukucode.com/2019/06/docker-user.html
# https://qiita.com/Riliumph/items/3b09e0804d7a04dff85b
# 一般ユーザーアカウントを追加
ENV USER_NAME=app
ARG USER_UID=1000
RUN useradd -m -u ${USER_UID} ${USER_NAME}
# 一般ユーザーにsudo権限を付与
#RUN gpasswd -a ${UID} sudo


# https://medium.com/@rlagowski/create-flask-app-with-uwsgi-nginx-certbot-for-ssl-and-all-this-with-docker-a9f23516618d
#COPY --chown=app:app ./${PIP_REQUIREMENTS} /app/requirments.txt
#COPY --chown=app:app ./app /app
COPY ./requirements.txt /app/requirements.txt
COPY ./app /app
RUN chown -R ${USER_NAME}:${USER_NAME} /app # --chown= では環境変数の代入が効かない

USER ${USER_UID}
WORKDIR /app

# pip
RUN ${PYTHON} -m pip install --user --upgrade pip && \
    ${PYTHON} -m pip install -r requirements.txt --user
ENV PATH $PATH:/home/app/.local/bin

CMD ["uwsgi", "--ini", "uwsgi.ini"]

