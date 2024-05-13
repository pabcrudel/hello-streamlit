# Source:
# - https://docs.streamlit.io/deploy/tutorials/docker
# - https://github.com/bigjoedata/streamlit-plus/blob/main/Dockerfile


# ----------------------------------------------------------------------------------------
# Lightweight image that comes with the latest version of Python 3.9
FROM python:3.9-slim AS image

# Set up a non-root user
RUN adduser\
  --disabled-password\
  # `--gecos ''` creates the user without full name, telephone number and other info
  --gecos ''\
  appuser

# Configures Docker to use libraries installed by the user from the command line
ENV PATH=/home/appuser/.local:/home/appuser/.local/bin:/install:$PATH

# Use the non-root user by default
USER appuser
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------
# Stage 1: Builder stage
FROM image AS builder

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --user --no-cache-dir -r requirements.txt

# Copy the source files into the WORKDIR
COPY ./src/ /app
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------
# Stage 2: Application stage
FROM image AS app

# Target directory for the following commands
WORKDIR /app

# Copy the installed packages & source files from the builder stage
COPY --from=builder /home/appuser/.local /home/appuser/.local
COPY --from=builder /app .

# Open the Streamlit’s default port
EXPOSE 8501

# Test if the project is running
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Configure this container as a executable that starts the Streamlit web server
# - Set Toolbar Mode to Viewer to ensure the development toolbar is hidden
ENTRYPOINT streamlit run app.py --client.toolbarMode=viewer
# ----------------------------------------------------------------------------------------
