ECS-Provision
=============

ECS-Provision is ecs service deployment utility for humans.

Installation
-------

.. code:: shell

    pip install ecs_provision

Example
-------

We will run one flask application example in ecs. Below is deployment code. Make sure docker is install on your machine.

.. code:: shell

    export ENVIRONMENT=pre_production
    export APP_CONFIG=pre_production
    export REGION=us-east-2
    export branch_name=master
    export image_tag=production
    export image_base_uri=replace-this-with-image-base-uri
    export app_image=flask-full
    DOCKER_LOGIN=`aws ecr get-login --no-include-email --region us-east-2`
    sudo ${DOCKER_LOGIN}
    git clone https://github.com/gofynd/flask-full.git
    cd flask-full
    git checkout $branch_name
    git pull origin $branch_name
    docker-compose build
    if [ $? -ne "0" ]; then
        exit 1
    else
        sudo docker tag $app_image:latest $image_base_uri/$app_image:$image_tag
        sudo docker push $image_base_uri/$app_image:$image_tag
        cd examples
        python deploy_flask_full_ecs_services.py
    fi

