from chatgpt import ChatGPT

bot = ChatGPT()


def getSection1Title(text) -> str:
    response = bot.ask(f"Generate a website landing page title"
                       f" (only 5 words in the title) for the following business:\nWhat the business does: {text}")
    return response


def getSection1Description(business_name, text) -> str:
    response = bot.ask(f"Generate a website landing page description"
                       f" for the following business:\nBusiness Name: f{business_name}"
                       f"\nWhat the business does: {text}")
                       # f"Content length should be: between 140 to 160 words)")
    return response
