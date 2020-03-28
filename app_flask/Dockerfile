FROM centos:8

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


# https://medium.com/@rlagowski/create-flask-app-with-uwsgi-nginx-certbot-for-ssl-and-all-this-with-docker-a9f23516618d
COPY ./requirements.txt /app/requirments.txt
WORKDIR /app
COPY ./app /app

# pip
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install \
            uwsgi \
            flask \
            flask-httpauth \
            pandas==1.*         
# todo: requirments.txt

CMD ["uwsgi", "--ini", "uwsgi.ini"]

