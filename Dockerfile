FROM mi_imagen:3.0
WORKDIR /workspace
RUN pip install numpy
RUN python -m pip install -U matplotlib
