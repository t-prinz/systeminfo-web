# systeminfo-web
Python application to display basic system information

# Logging into registry.redhat.io will allow you to pull images from registry.access.redhat.com
# but not vice-versa
#
# Specifying the base image without the server will pull the image from registry.access.redhat.com

sudo docker login registry.redhat.io
sudo docker pull registry.access.redhat.com/rhscl/python-36-rhel7

# Look around base container image if desired

sudo docker run -it --rm registry.access.redhat.com/rhscl/python-36-rhel7 /bin/bash

# Build the container image with the application

sudo docker build -t tprinz/systeminfo-web .

# Look inside container image to verify contents
# curl http://localhost:5000 works correctly from inside the container

sudo docker run -it --rm tprinz/systeminfo-web /bin/bash

# Run the container

sudo docker run -d --rm -p 5000:5000 --name systeminfo-web tprinz/systeminfo-web 

# Test the container

curl http://localhost:5000

# Push the image to Quay

sudo docker tag tprinz/systeminfo-web quay.io/tprinz/systeminfo-web
sudo docker push quay.io/tprinz/systeminfo-web

#
# Use the following to make use of the S2I utility
#

sudo s2i build https://github.com/t-prinz/systeminfo-web.git rhscl/python-36-rhel7 tprinz/systeminfo-web-s2i

# Push the image to Quay

sudo docker tag tprinz/systeminfo-web-s2i quay.io/tprinz/systeminfo-web-s2i
sudo docker push quay.io/tprinz/systeminfo-web-s2i

# In OpenShift you can then deploy this container image
