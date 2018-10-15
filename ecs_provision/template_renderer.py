import configparser
import json

from jinja2 import Template


class TemplateRenderer:

    def __init__(self, config_file, env):
        self.config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        self.config.read(config_file)
        self.env = env

    def render(self, template_file,  template_type="json"):
        template_str = open(template_file).read()
        template = Template(template_str)
        if template_type=="json":
            variables = json.loads(template.render(**dict(self.config[self.env].items())))
            return variables