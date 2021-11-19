
FROM python:3
WORKDIR /usr/src/app
ENV path_of_dir "/mnt/shared_from_mydevice"
RUN /bin/echo "Hello $name"
RUN ["/bin/bash", "-c", "echo Hello $name"]
COPY . .
CMD ["assignment.py"]
ENTRYPOINT [ "python3" ]