Installing Jena/Fuseki Triple Store
"""""""""""""""""""""""""""""""""""

Full documentation for installing the Jena/Fuseki Triple store can be found at:

- https://github.com/stain/jena-docker/tree/master/jena-fuseki

In summary, clone the above repository:

.. code-block:: bash

 git clone https://github.com/stain/jena-docker.git

and run the docker image on port 3030:

.. code-block:: bash

 sudo docker run -p 3030:3030 jena-fuseki


To stop the docker check the status and stop the correct containter id: 

.. code-block:: bash

 sudo docker stats
 sudo docker stop CONTAINER_ID

