FROM python:3.8.0-buster

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the code
COPY /bot .
COPY config.json .

# Run the bot
CMD ["python", "main.py"]
