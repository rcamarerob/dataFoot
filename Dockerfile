FROM python:3.8
COPY ./src .
RUN  python setup.py install
CMD [ "python", "cvsloader.py" ]
