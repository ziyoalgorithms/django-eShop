FROM python:3.9.5

# set environment variables
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/eShop

COPY ./requirements.txt /usr/src/requirements.txt
COPY ./scripts /scripts
COPY . /usr/src/eShop

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /usr/src/requirements.txt --use-pep517 && \
    useradd -ms /bin/bash ziyo && \
    chmod -R +x /scripts

ENV PATH="/py/bin:$PATH"
ENV PYTHONPATH "${PYTHONPATH}:/py/bin:$PATH"

USER ziyo
EXPOSE 8000
CMD [ "run.sh" ]