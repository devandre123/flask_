FROM python:3
WORKDIR /usr/src/app
COPY Requirements.txt .
RUN pip install --no-cache-dir -r Requirements.txt
COPY . .
CMD ["python", "app.py"]
