import os
import zipfile
from random_username.generate import generate_username
from random import choice
from shutil import copytree, rmtree
from jinja2 import Environment, FileSystemLoader
from website import aigenerator
from random_phone import RandomUkPhone


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


def get_context(landing_page_name: str, landing_page_details: str) -> dict:

    context = {}
    context['LandingPageName'] = landing_page_name

    blocks = []
    blocks_titles = aigenerator.get_section_titles(landing_page_details)
    block_descriptions = aigenerator.get_section_descriptions(landing_page_name, landing_page_details)
    for index, block in enumerate(blocks_titles):
        obj = {}
        block_description = block_descriptions[index]
        obj['title'] = block
        obj['description'] = block_description
        blocks.append(obj)

    context['section1Title'] = blocks[0]['title']
    context['section1Description'] = blocks[0]['description']

    services = []
    service_titles = aigenerator.get_services(landing_page_details)
    for service in service_titles:
        obj = {}
        service_description = aigenerator.get_service_description(service)
        obj['title'] = service
        obj['description'] = service_description
        services.append(obj)

    features = []
    features_titles = aigenerator.get_features(landing_page_details)
    for feature in features_titles:
        obj = {}
        feature_description = aigenerator.get_feature_description(landing_page_name, feature)
        obj['title'] = feature
        obj['description'] = feature_description
        features.append(obj)

    context['service1Title'] = services[0]['title']
    context['service1Description'] = services[0]['description']
    context['service2Title'] = services[1]['title']
    context['service2Description'] = services[1]['description']
    context['service3Title'] = services[2]['title']
    context['service3Description'] = services[2]['description']

    context['section2Title'] = blocks[1]['title']
    context['section2Description'] = blocks[1]['description']
    context['section3Title'] = blocks[2]['title']
    context['section3Description'] = blocks[2]['description']

    context['feature1Title'] = features[0]['title']
    context['feature1Description'] = features[0]['description']
    context['feature2Title'] = features[1]['title']
    context['feature2Description'] = features[1]['description']
    context['feature3Title'] = features[2]['title']
    context['feature3Description'] = features[2]['description']

    rukp = RandomUkPhone()
    context['username'] = generate_username()[0]
    context['mobile_phone'] = rukp.random_mobile()
    context['email'] = context['username'] + "@gmail.com"

    return context


def zipdir(path, ziph):
    length = len(path)

    # ziph is zipfile handle
    for root_dir, _, files in os.walk(path):
        folder = root_dir[length:]
        for file in files:
            ziph.write(os.path.join(root_dir, file), os.path.join(folder, file))


def get_list_of_dirs(directory) -> list:  # возвращает список папок без папки "website"
    dirs = list_dirs(directory)
    dirs.remove("website")
    return dirs


def generate(root_dir, templs_dir, site_category, page_data: dict) -> bool:
    template_dir = templs_dir + "\\" + f"{site_category}" + "\\"
    category_dirs = os.listdir(template_dir)
    full_path = template_dir + str(choice(category_dirs))
    print(full_path)    # TEMP
    env = Environment(loader=FileSystemLoader(full_path))
    template = env.get_template('index.html')

    copytree(full_path, root_dir + "\\" + "generated", dirs_exist_ok=True)

    filename = os.path.join(root_dir, 'generated', 'index.html')
    try:
        with open(filename, 'w') as file:
            file.write(template.render(
                get_context(page_data['name'], page_data['details'])))
    except Exception as exception:
        print(exception)    # TEMP
        return False

    with zipfile.ZipFile(root_dir + "\\" + 'white_page.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(root_dir + "\\" + "generated", zipf)

    rmtree(root_dir + "\\" + "generated")
    return True
