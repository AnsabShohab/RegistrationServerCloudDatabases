# Registration Server
This repository contains the python script for the registration server and a couple of other scripts to act as the clients that can connect to it.

1. Clone the repository
2. If the system doesn't have docker, install it from https://docs.docker.com/engine/install/ubuntu/
<!-- 2. Run command `` sudo docker build -t registration-server . ``
3. Run command ``sudo docker run -d -p 52923:52923 registration-server`` to run the server in a container -->
3. Run command `` sudo docker compose up -d``
4. To check the contents of the container, use the command ``sudo docker exec -it <CONTAINER-NAME> /bin/bash``

Developer's Note:

If you encounter an error like this one:

``ERROR: for b644c3ebf8d1_registration-server_server_1  Cannot create container for service server: invalid volume specification: 'd162716c2689ba3838ed872faa3b3befdf0855af01e4270d16fe9616048e12ab:data:rw': invalid mount config for type "volume": invalid mount path: 'data' mount path must be absolute``

A possible solution might be to remove all the previously created images, containers and volumes for this specific application (caution: take care not to remove images and containers created for other applications), for which the following commands can be used 

    ``docker image rm <IMAGE-ID>``    
    ``docker containter rm <CONTAINER-ID>``    
    ``docker volume rm <VOLUME-ID>``

and then build and run the whole application again using the command ``docker-compose up --build -d``

If you want to remove all of the stopped conatiners, volumes not in use and dangling images, the prune command can be used
    ``docker image prune``    
    ``docker containter prune``    
    ``docker volume prune`` 
