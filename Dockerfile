FROM python:3.10-slim

# Copy local code to the container image.
ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . ./


RUN apt-get update && apt-get install make
RUN make install

# Run the web service on container startup. Here we use the gunicorn
# webserver.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec uvicorn --host 0.0.0.0 run:create_app
