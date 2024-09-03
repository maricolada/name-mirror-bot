FROM python:3.9.6
ENV TOKEN='7498326020:AAEgRWU5b_nlyXU-EanKv4j-fYzVQK602J8'
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]
EXPOSE 80