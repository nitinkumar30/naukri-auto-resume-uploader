import configparser
import os


def read_config(file_path):
    config = configparser.ConfigParser(interpolation=None)
    config.read(file_path)
    return config


def get_config_value(file_path, key):
    config = read_config(file_path)
    return config.get('DEFAULT', key)  # Use 'DEFAULT' section by default


def get_loginPage_xpath_value(key):
    return get_config_value('xpaths/login.properties', key)


def get_uploadResume_xpath_value(key):
    return get_config_value('xpaths/uploadResume.properties', key)


def get_property_value(key):
    return get_config_value('config.properties', key)


def load_credentials():
    username = os.getenv("NAUKRIUSERNAME")
    password = os.getenv("NAUKRIPASSWORD")
    if not username or not password:
        raise ValueError("Missing credentials in environment variables.")
    return username, password
