FROM python:3.9 AS build-stage
# Install dependencies
COPY  DoCheckerBack/requirements.txt .
RUN pip install --user -r requirements.txt
# PRODUCTION STAGE
FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /DoChecker/DoCheckerBack
COPY .. .
COPY --from=build-stage /root/.local/ /usr/local/
CMD ["/bin/bash"]

