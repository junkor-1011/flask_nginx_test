# (Args)
# ARG: BASE_IMAGE
# ARG: USER_UID


ARG BASE_IMAGE=centos:8


FROM ${BASE_IMAGE}

# system update
RUN yum -y update # && yum clean all

# package install
RUN yum groupinstall "Development Tools" -y
RUN yum install -y \
        kernel-devel \
        kernel-headers \
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
ENV PATH $PATH:/home/app/.local/bin
RUN python3 -m pip install --user --upgrade pip && \
    python3 -m pip install -r requirements.txt --user

CMD ["uwsgi", "--ini", "uwsgi.ini"]

