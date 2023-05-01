import os
import zipfile
from shutil import copytree, rmtree
from jinja2 import Environment, FileSystemLoader
from website import aigenerator


cwd = os.getcwd()
root = os.path.split(os.path.split(cwd)[0])[0] + '\\' \
       + os.path.split(os.path.split(cwd)[0])[1]
templates_dir = os.path.join(root, 'templates')


def list_dirs(root_dir: str) -> list:
    list_of_paths = []
    list_of_dirs = []

    for file in os.listdir(root_dir):
        d = os.path.join(root_dir, file)
        if os.path.isdir(d):
            list_of_paths.append(d)

    for i in list_of_paths:
        splited_subdir = i.split("\\")
        list_of_dirs.append(splited_subdir[7])

    return list_of_dirs


def get_context() -> dict:
    context = {}
    context['LandingPageName'] = "Test"
    context['section1Title'] = "Test"
    return context


def zipdir(path, ziph):
    length = len(path)

    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        folder = root[length:]
        for file in files:
            ziph.write(os.path.join(root, file), os.path.join(folder, file))


def get_list_of_dirs(directory) -> list:  # возвращает список папок без папки "website"
    dirs = list_dirs(directory)
    dirs.remove("website")
    return dirs


def generate(root, templs_dir, site_category):
    template_dir = templs_dir + "\\" + f"{site_category}" + "\\" + "1"
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('index.html')

    copytree(template_dir, root + "\\" + "generated", dirs_exist_ok=True)

    filename = os.path.join(root, 'generated', 'index.html')
    with open(filename, 'w') as fh:
        fh.write(template.render(
            get_context()))

    with zipfile.ZipFile(root + "\\" + 'white_page.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(root + "\\" + "generated", zipf)

    rmtree(root + "\\" + "generated")