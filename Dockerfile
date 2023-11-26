FROM python:3.11.4-alpine3.17

LABEL authors="blendi"

WORKDIR /test_work_library/

COPY . .

RUN chmod +x entrypoint.sh

RUN pip install -r requirements.txt

CMD ["sh", "entrypoint.sh"]
