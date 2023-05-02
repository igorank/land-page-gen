import requests

CHATGPT_API_IP = "89.252.17.107"
CHATGPT_API_PORT = "8060"


def getSection1Title(text) -> list:
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                             json={
                                 'text': f"Generate 3 website landing page titles (only 5 words in the title) for the following business: What the business does: {text}"})
    if response.status_code != 200:
        raise Exception
    answer = response.text.replace('\n', '').replace('1', '').replace('2', '').replace('3', '')

    try:
        stripped = answer.split('"', 1)[1]
        stripped = stripped.replace('"', '')
        answer_list = stripped.split('.')
    except IndexError:
        answer_list = answer.split('.')

    while "" in answer_list:
        answer_list.remove("")

    return answer_list


def getSection1Description(business_name, text) -> list:
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                             json={
                                 'text': f"Generate 3 website landing page descriptions for the following business: Business Name: {business_name}. What the business does: {text}"})
    if response.status_code != 200:
        raise Exception
    answer = response.text.replace('\n', '').replace('1', '').replace('2', '').replace('3', '')

    try:
        stripped = answer.split('"', 1)[1]
        stripped = stripped.replace('"', '')
        answer_list = stripped.split('.')
    except IndexError:
        answer_list = answer.split('.')

    while "" in answer_list:
        answer_list.remove("")

    return answer_list


def get_services(text) -> list:
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                             json={
                                 'text': f"Generate 3 short and punchy website service titles for a business: What business does: {text}"})
    if response.status_code != 200:
        raise Exception
    answer = response.text.replace('\n', '').replace('1', '').replace('2', '').replace('3', '')

    try:
        stripped = answer.split('"', 1)[1]
        stripped = stripped.replace('"', '')
        answer_list = stripped.split('.')
    except IndexError:
        answer_list = answer.split('.')

    while "" in answer_list:
        answer_list.remove("")

    return answer_list


def get_service_description(title) -> str:
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                             json={
                                 'text': f"Generate a one description for the following service: Servie Title: {title}"})
    if response.status_code != 200:
        raise Exception
    return response.text.replace('"', '')


def get_features(text) -> list:
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                             json={
                                 'text': f"Generate 3 short and punchy website feature titles for a business: What business does: {text}"})
    if response.status_code != 200:
        raise Exception
    answer = response.text.replace('\n', '').replace('1', '').replace('2', '').replace('3', '')

    try:
        stripped = answer.split('"', 1)[1]
        stripped = stripped.replace('"', '')
        answer_list = stripped.split('.')
    except IndexError:
        answer_list = answer.split('.')

    while "" in answer_list:
        answer_list.remove("")

    return answer_list


def get_service_description(title) -> str:
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                             json={
                                 'text': f"Generate a one description for the following feature: Feature Title: {title}"})
    if response.status_code != 200:
        raise Exception
    return response.text.replace('"', '')
