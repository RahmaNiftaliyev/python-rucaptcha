import asyncio

from python_rucaptcha.text_captcha import TextCaptcha

# Rucaptcha API Key from your account
RUCAPTCHA_KEY = "ad911111111111ca81755768608fa758570"

# Balance control

text_captcha = TextCaptcha(rucaptcha_key=RUCAPTCHA_KEY, language=1)
result = text_captcha.captcha_handler(textcaptcha="Какой сегодня день недели?")

print(result)

# ASYNC


async def run():
    # Balance control

    text_captcha = TextCaptcha(rucaptcha_key=RUCAPTCHA_KEY, language=1)
    result = await text_captcha.aio_captcha_handler(textcaptcha="Какой сегодня день недели?")

    print(result)


asyncio.run(run())
