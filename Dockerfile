FROM python:3
ENV DIR=/usr/src/registration-server
WORKDIR ${DIR}
COPY registration_server.py ${DIR}/registration_server.py
RUN mkdir registration-server-data
CMD ["python","registration_server.py"]
VOLUME ./registration-server-data
