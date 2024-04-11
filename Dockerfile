# Source: https://docs.streamlit.io/deploy/tutorials/docker

# Lightweight image that comes with the latest version of Python 3.9
FROM python:3.9-slim

# Target directory for the following commands
WORKDIR /app

# Copy the local directory to the WORKDIR
COPY . .

# Install dependecies
RUN pip3 install -r requirements.txt

# Open the Streamlit’s default port
EXPOSE 8501

# Test if the project is runing
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Configure this container as a executable that starts the Streamlit web server
ENTRYPOINT streamlit run app.py
