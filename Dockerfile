FROM python:3.7.3
RUN mkdir -p /var/warehouse_service
ADD . /var/warehouse_service
RUN pip install --upgrade pip
RUN pip install -r /var/warehouse_service/requirements.txt
RUN pip install connexion[swagger-ui]
WORKDIR /var/warehouse_service
EXPOSE 8080
CMD cd /var/warehouse_service && python app.py

