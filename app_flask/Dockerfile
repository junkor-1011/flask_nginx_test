ARG BASE_IMAGE=centos:8
#ARG USER=app


FROM ${BASE_IMAGE}

# system update
RUN yum -y update # && yum clean all

# set locale
#RUN yum reinstall -y glibc-common && yum clean all && \
#    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
#ENV LANG=ja_JP.UTF-8 \
#    LANGUAGE=ja_JP:ja \
#    LC_ALL=ja_JP.UTF-8

# package install
RUN yum groupinstall "Development Tools" -y
RUN yum install -y \
        kernel-devel \
        kernel-headers \
        vim \
        python3 python3-devel \
        pcre pcre-devel \
        zlib zlib-devel \
        openssl openssl-devel \
        && yum clean all
# Note: centos系だとyumで簡単にインストール出来るのはpython3.6までの様子

# user        
# ref:
# https://zukucode.com/2019/06/docker-user.html
# https://qiita.com/Riliumph/items/3b09e0804d7a04dff85b
# 一般ユーザーアカウントを追加
ARG USER_UID=1000
RUN useradd -m -u ${USER_UID} app
# 一般ユーザーにsudo権限を付与
#RUN gpasswd -a ${UID} sudo


USER ${USER_UID}

# https://medium.com/@rlagowski/create-flask-app-with-uwsgi-nginx-certbot-for-ssl-and-all-this-with-docker-a9f23516618d
COPY --chown=app:app ./requirements.txt /app/requirments.txt
WORKDIR /app
COPY --chown=app:app ./app /app

# pip
RUN python3 -m pip install --user --upgrade pip && \
    python3 -m pip install --user \
            uwsgi \
            flask \
            flask-httpauth \
            pandas==1.* 
ENV PATH $PATH:/home/app/.local/bin
# todo: requirments.txt


CMD ["uwsgi", "--ini", "uwsgi.ini"]

