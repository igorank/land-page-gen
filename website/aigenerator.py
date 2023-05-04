import requests

CHATGPT_API_IP = "89.252.17.107"
CHATGPT_API_PORT = "8060"


def getSection1Title(text) -> list:
    for _ in range(3):
        response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                                 json={
                                     'text': f"Generate 3 website landing page titles (only 5 words in the title) for the following business: What the business does: {text}"})
        if response.text != "Unable to fetch the response, Please try again.":
            print(response.text)  # TEMP
            stripped_trash = response.text.split('1', 1)[1]
            stripped_trash = stripped_trash.split('\n\n', 1)[0]
            answer = stripped_trash.replace('\n', '').replace('1', '').replace('2', '').replace('3', '') + '.'
            fixed_answer = answer[1:]
            try:
                stripped = fixed_answer.split('"', 1)[1]
                stripped = stripped.replace('"', '')
                answer_list = stripped.split('.')
            except IndexError:
                answer_list = fixed_answer.split('.')

            while "" in answer_list:
                answer_list.remove("")

            print(answer_list)  # TEMP
            return answer_list
        if response.status_code != 200:
            raise Exception("Unable to connect to ChatGPT server")
    raise Exception("Unable to fetch the response, Please try again")


def getSection1Description(business_name, text) -> list:
    for _ in range(3):
        response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                                 json={
                                     'text': f"Generate 3 website landing page descriptions for the following business: Business Name: {business_name}. What the business does: {text}"})
        if response.text != "Unable to fetch the response, Please try again.":
            print(response.text)
            stripped_trash = response.text.split('1', 1)[1]
            first = stripped_trash.split('\n2', 1)[0]
            second = stripped_trash.split('\n2', 1)[1].split('\n3', 1)[0]
            third = stripped_trash.split('\n2', 1)[1].split('\n3', 1)[1].split('\n', 1)[0]
            list_of_resp = [first, second, third]

            answer_list = []
            for i in list_of_resp:
                fixed_str = i.replace('\n', '').replace('"', '')
                new_str = fixed_str[2:]
                answer_list.append(new_str)

            while "" in answer_list:
                answer_list.remove("")

            print(answer_list)  # TEMP
            return answer_list
        if response.status_code != 200:
            raise Exception("Unable to connect to ChatGPT server")
    raise Exception("Unable to fetch the response, Please try again")


def get_services(text) -> list:
    for _ in range(3):
        response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                                 json={
                                     'text': f"Generate 3 short and punchy website service titles for a business: What business does: {text}"})
        if response.text != "Unable to fetch the response, Please try again.":
            print(response.text)
            stripped_trash = response.text.split('1', 1)[1]
            stripped_trash = stripped_trash.split('\n\n', 1)[0]
            answer = stripped_trash.replace('\n', '').replace('1', '').replace('2', '').replace('3', '') + '.'
            fixed_answer = answer[1:]
            try:
                stripped = fixed_answer.split('"', 1)[1]
                stripped = stripped.replace('"', '')
                answer_list = stripped.split('.')
            except IndexError:
                answer_list = fixed_answer.split('.')

            while "" in answer_list:
                answer_list.remove("")

            print(answer_list)  # TEMP
            return answer_list
        if response.status_code != 200:
            raise Exception("Unable to connect to ChatGPT server")
    raise Exception("Unable to fetch the response, Please try again")


def get_features(text) -> list:
    for _ in range(3):
        response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                                 json={
                                     'text': f"Generate 3 short and punchy website feature titles for a business: What business does: {text}"})
        if response.text != "Unable to fetch the response, Please try again.":
            print(response.text)
            stripped_trash = response.text.split('1', 1)[1]
            stripped_trash = stripped_trash.split('\n\n', 1)[0]
            answer = stripped_trash.replace('\n', '').replace('1', '').replace('2', '').replace('3', '') + '.'
            fixed_answer = answer[1:]
            try:
                stripped = fixed_answer.split('"', 1)[1]
                stripped = stripped.replace('"', '')
                answer_list = stripped.split('.')
            except IndexError:
                answer_list = fixed_answer.split('.')

            while "" in answer_list:
                answer_list.remove("")

            print(answer_list)  # TEMP
            return answer_list
        if response.status_code != 200:
            raise Exception("Unable to connect to ChatGPT server")
    raise Exception("Unable to fetch the response, Please try again")


def get_service_description(title) -> str:
    for _ in range(3):
        response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                                 json={
                                     'text': f"Generate a one description for the following service: Servie Title: {title}"})
        if response.text != "Unable to fetch the response, Please try again.":
            try:
                answer = response.text.split(':', 1)[1]
            except IndexError:
                return response.text.replace('"', '')
            else:
                return answer.replace('"', '')
        if response.status_code != 200:
            raise Exception("Unable to connect to ChatGPT server")
    raise Exception("Unable to fetch the response, Please try again")


def get_feature_description(title) -> str:
    for _ in range(3):
        response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt",
                                 json={
                                     'text': f"Generate a one description for the following feature: Feature Title: {title}"})
        if response.text != "Unable to fetch the response, Please try again.":
            return response.text.replace('"', '')
        if response.status_code != 200:
            raise Exception("Unable to connect to ChatGPT server")
    raise Exception("Unable to fetch the response, Please try again")
