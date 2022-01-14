# 告訴 Docker，我的 base image 要用 python 3 的版本
FROM python:3

# 環境變數 (這行是告訴 python，有 log 就往外吐)
# 可參考 Is PYTHONUNBUFFERED=TRUE a good idea?
# (https://github.com/awslabs/amazon-sagemaker-examples/issues/319)
ENV PYTHONUNBUFFERED 1

# 執行 shell script (這行是建立一個新資料夾 叫做 code)
RUN mkdir /code

# 切換目錄 到 /code 資料夾底下
WORKDIR /code

# 新增本地端的 requirement.txt 到 docker 的 code/ 資料夾底下
ADD requirements.txt /code/

# 執行 shell script
# (這行是根據 requirements.txt
# 來安裝我需要的 python 套件)
RUN pip install -r requirements.txt

# 新增本地端的所有檔案(django專案) 到 docker 的 code/ 資料夾底下
ADD . /code/

# 告訴 docker container 跑起來之後，要執行的指令們
# (這邊是先執行 init.sh 的 shell script
# 並且 執行 django server 在 8000 port
# (0.0.0.0 很重要，不一定能用 127.0.0.1 取代)
# 可參考 What's the difference between 127.0.0.1 and 0.0.0.0?
# (https://superuser.com/questions/949428/
# whats-the-difference-between-127-0-0-1-and-0-0-0-0)
CMD sh init.sh && python3 manage.py runserver 0.0.0.0:8000
