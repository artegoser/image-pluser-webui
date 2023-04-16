import os
import datetime


def generate_name(
    name=False, subfolder="stacked", extension="png", format="%Y-%m-%d_%H-%M-%S"
):
    os.makedirs(os.path.join(".", "output", subfolder), exist_ok=True)

    if name is False or name == "":
        name = get_date_text(format)

    return os.path.join(".", "output", subfolder, f"{name}.{extension}")


def generate_name_with_file_name(name, subfolder):
    os.makedirs(os.path.join(".", "output", subfolder), exist_ok=True)

    return os.path.join(".", "output", subfolder, name)


def get_date_text(format="%Y-%m-%d_%H-%M-%S"):
    return datetime.datetime.now().strftime(format)
