from django.apps import AppConfig


class WebappConfig(AppConfig):
    #this cause a dublicate error, hence override default name to path and give it a label
    #this config is forced to be loaded by being added to __init__.py
    name = 'webapp'