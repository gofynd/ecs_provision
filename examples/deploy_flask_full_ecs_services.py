import os
from ecs_provision import EcsClient

ENVIRONMENT = os.getenv("ENVIRONMENT")
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")
REGION = os.getenv("REGION")

#create ecs client
ecs_client = EcsClient(access_key_id=ACCESS_KEY_ID, secret_access_key=SECRET_ACCESS_KEY, region=REGION, profile=None, config_file="config.ini", environment=ENVIRONMENT)


def deploy_services(task_file, service_file):
    print("registering new task definition...")
    # register new task definition
    new_task_definition = ecs_client.register_task_definition(task_file)
    # return new task_definition arn
    new_task_definition_arn = new_task_definition['taskDefinition']['taskDefinitionArn']
    print("deploying service...")
    try:
        print("creating service...")
        # try to create service
        ecs_client.create_service(service_file)
    except Exception as e:
        print("service creation failed with exception message {}".format(str(e)))
        # import traceback
        # traceback.print_exc()
        print("trying to update service...")
        # if service already exists update service
        ecs_client.update_service(service_file)
    print("deleting old task definition...")
    # delete old task definition
    task_definition_arn_base = ":".join(new_task_definition_arn.split(":")[:-1])
    old_task_definition_arn = "{}:{}".format(task_definition_arn_base, new_task_definition['taskDefinition']["revision"]-1)
    ecs_client.deregister_task_definition(task_definition_arn=old_task_definition_arn)
    print("Done")


if __name__=="__main__":
    task_definition_file_base = "./"
    service_file_base = "./"
    tergeo_files = [("app-task.json.j2", "app-service.json.j2")]

    for f_tuple in tergeo_files:
        print("deploying {}".format(f_tuple))
        task_def_file = "{}{}".format(task_definition_file_base, f_tuple[0])
        service_file = "{}{}".format(service_file_base, f_tuple[1])
        deploy_services(task_def_file, service_file)