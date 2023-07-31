FROM python

WORKDIR /app

COPY exercicio1.py .
COPY credentials.ini .
COPY files_csv/movies.csv ./files_csv/
COPY files_csv/series.csv ./files_csv/

RUN pip install boto3

CMD ["python", "exercicio1.py"]