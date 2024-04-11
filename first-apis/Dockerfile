FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
# CMD ["python", "app.py"]
CMD ["flask", "run", "--host", "0.0.0.0"]