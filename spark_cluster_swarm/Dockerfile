FROM jupyter/datascience-notebook:latest

USER root

# Install OpenJDK 17 JDK
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID

# Install dependencies
RUN pip install pyspark

# Expose port for JupyterLab
EXPOSE 8888