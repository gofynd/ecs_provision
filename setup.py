from setuptools import setup

setup(name='ecs_provision',
        version='0.1.2',
        description='Utility to deploy task defintions and services in json form to ECS',
        url='https://githab.com/fynd/ecs_provision',
        author='Neeraj Shukla',
        author_email='neerajshukla1911@gmail.com',
        packages=['ecs_provision'],
        install_requires=['boto3>=1.7.8', 'Jinja2>=2.10']
      )
