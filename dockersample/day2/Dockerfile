FROM python:3
WORKDIR /usr/src/app
ENV name “Everyone Present”
RUN  /bin/echo “hello $name”
RUN ["/bin/bash", "-c", "echo hello $name"]
COPY  . .
CMD ["World.py"]
ENTRYPOINT ["python3"]
