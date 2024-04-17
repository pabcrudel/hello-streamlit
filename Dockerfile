# Source: https://docs.streamlit.io/deploy/tutorials/docker

# Lightweight image that comes with the latest version of Python 3.9
FROM python:3.9-slim

# Target directory for the following commands
WORKDIR /app

# Copy the local directory to the WORKDIR
COPY . .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Open the Streamlit’s default port
EXPOSE 8501

# Test if the project is running
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Configure this container as a executable that starts the Streamlit web server
# - Set server address to 0.0.0.0 to run app in production mode in order to
#   remove the development toolbar
ENTRYPOINT\
  streamlit run app.py\
  --server.address=0.0.0.0
