import requests

CHATGPT_API_IP = "89.252.17.107"
CHATGPT_API_PORT = "8060"


def getSection1Title(text) -> str:
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                             json={
                                 'text': f"Generate a one website landing page title (only 5 words in the title) for the following business: What the business does: {text}"})
    return response.text.replace('"', '')


def getSection1Description(business_name, text) -> str:
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                             json={
                                 'text': f"Generate a one website landing page description for the following business: Business Name: {business_name}. What the business does: {text}"})
    return response.text.replace('"', '')


def get_services(text) -> list:
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                             json={
                                 'text': f"Generate 3 short and punchy website service titles for a business: What business does: {text}"})
    answer = response.text.replace('\n', '').replace('1', '').replace('2', '').replace('3', '')
    stripped = answer.split('.', 1)[1]
    # stripped = stripped.replace(' ', '')
    print(stripped)
    answer_list = stripped.split('.')
    print(answer_list)
    return answer_list


def get_service_description(title) -> str:
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                             json={
                                 'text': f"Generate a one description for the following service: Servie Title: {title}"})
    return response.text.replace('"', '')


def get_features(text) -> list:
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                             json={
                                 'text': f"Generate 3 short and punchy website feature titles for a business: What business does: {text}"})
    answer = response.text.replace('\n', '').replace('1', '').replace('2', '').replace('3', '')
    stripped = answer.split('.', 1)[1]
    # stripped = stripped.replace(' ', '')
    answer_list = stripped.split('.')
    return answer_list


def get_service_description(title) -> str:
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                             json={
                                 'text': f"Generate a one description for the following feature: Feature Title: {title}"})
    return response.text.replace('"', '')
