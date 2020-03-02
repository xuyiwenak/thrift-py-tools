FROM pypy:2
WORKDIR /home/project
COPY ./ /home/project
RUN pip install thrift -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pypy test.py