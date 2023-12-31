import yaml
import os


def load_config():
    # Read the YAML configuration file
    file_path = "config.yaml"
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)

    # Set the OpenAI API key as a system environment variable
    os.environ["OPENAI_API_KEY"] = config["api_key"]
    return config