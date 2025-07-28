FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl gnupg lsb-release && \
    apt-get clean

RUN curl -fsSL https://ollama.com/install.sh | sh

ENV PATH="/root/.ollama/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 7860

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
