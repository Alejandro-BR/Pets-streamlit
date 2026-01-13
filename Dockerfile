FROM python:3.14
RUN pip install install -r requirements.txt
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py" ]