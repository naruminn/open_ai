# ref: https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook
FROM jupyter/datascience-notebook

USER root
RUN apt-get update
RUN apt-get install -y \
 python-numpy \
 python-dev \
 cmake \
 zlib1g-dev \ 
 libjpeg-dev \
 xvfb \ 
 libav-tools \ 
 xorg-dev \
 python-opengl \ 
 libboost-all-dev \ 
 libsdl2-dev \
 swig \
 xvfb \
 graphviz

USER $NB_UID
RUN pip install gym 
RUN pip install gym[all]
RUN pip install box2d
RUN pip install PyOpenGL
RUN pip install JSAnimation
RUN pip install tensorflow keras
RUN pip install graphviz
RUN pip install pydot

CMD ["xvfb-run", "-s", "-screen 0 1400x900x24", "jupyter", "notebook", "--NotebookApp.token=''"]
