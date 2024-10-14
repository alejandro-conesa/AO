FROM python:bullseye
WORKDIR /workspace
RUN pip install numpy
RUN python -m pip install -U matplotlib
