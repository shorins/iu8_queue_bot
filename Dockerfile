FROM python:3.8-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ src/

# Set environment variables
ENV PYTHONPATH=/app/src

# Run the bot
CMD ["python", "src/main.py"]
