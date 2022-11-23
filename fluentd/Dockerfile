FROM fluent/fluentd:v1.12.0-debian-1.0

USER root
WORKDIR /home/fluent
ENV PATH /home/fluent/.gem/2.3.0/bin/:$PATH

RUN fluent-gem install fluent-plugin-kafka
