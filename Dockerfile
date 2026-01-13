FROM python:3.14
RUN pip install streamlit pandas numpy
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py" ]