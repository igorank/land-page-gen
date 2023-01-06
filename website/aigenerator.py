import requests

CHATGPT_API_IP = "89.252.17.107"
CHATGPT_API_PORT = "8060"

def getSection1Title(text) -> str:
    # response = bot.ask(f"Generate a website landing page title (only 5 words in the title) for the following business:\nWhat the business does: {text}")
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt", json={'text': "Generate a website landing page title"})
    return response.text


def getSection1Description(business_name, text) -> str:
    # response = bot.ask(f"Generate a website landing page description for the following business:\nBusiness Name: f{business_name}\nWhat the business does: {text}")
    response = requests.post(f"http://{CHATGPT_API_IP}:{CHATGPT_API_PORT}/chatgpt", json={'text': "Generate a website landing page description"})
    return response.text
