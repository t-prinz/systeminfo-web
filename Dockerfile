FROM registry.access.redhat.com/rhscl/python-36-rhel7

MAINTAINER Trey Prinz "tprinz@redhat.com"

EXPOSE 5000

# Copy the application

COPY . /opt/app-root/src

# Install any needed packages specified in requirements.txt

RUN pip3 install -r requirements.txt

CMD /bin/bash -c 'python3 -u wsgi.py'
#CMD ["python3", "wsgi.py"]
