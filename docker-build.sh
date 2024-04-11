#!/bin/bash

dockerImage=hello-streamlit

# Build image
docker build -t $dockerImage .

# Run Docker
echo
docker run -p 80:8501 -d $dockerImage

# Final message
echo
echo Done!
