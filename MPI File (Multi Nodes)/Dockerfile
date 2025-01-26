FROM ubuntu:20.04

# Set non-interactive mode for apt to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    mpich \
    python3-mpi4py \
    python3-numpy && \
    apt-get clean

# Copy your MPI Python script to the Docker container
COPY CST435-MPI-Code.py /app/

# Set the working directory
WORKDIR /app

# Set the entry point to run the MPI Python script
ENTRYPOINT ["mpirun", "python3", "CST435-MPI-Code.py"]
