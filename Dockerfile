FROM debian:jessie
# MAINTAINER digmore

RUN apt-get update \
        && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
                patch \
                python-pip \
        && rm -fr /var/lib/apt/lists/* \
        && rm -fr /tmp/* \
        && rm -fr /var/tmp/*

COPY instapaperlib.py.diff /tmp/
RUN pip install instapaperlib redis
# For like temporary
RUN patch -p0 < /tmp/instapaperlib.py.diff
COPY app.py /opt/
ENTRYPOINT ["/opt/app.py"]
