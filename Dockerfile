# Source: https://docs.streamlit.io/deploy/tutorials/docker

# Lightweight image that comes with the latest version of Python 3.9
FROM python:3.9-slim

# Target directory for the following commands
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && rm requirements.txt

# Copy the source files into the WORKDIR
COPY ./src/ .

# Open the Streamlit’s default port
EXPOSE 8501

# Test if the project is running
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Configure this container as a executable that starts the Streamlit web server
# - Set Toolbar Mode to Viewer to ensure the development toolbar is hidden
ENTRYPOINT streamlit run app.py --client.toolbarMode=viewer
