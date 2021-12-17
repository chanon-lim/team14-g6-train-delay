from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

IBM_API_KEY = "uz0Zeix0rUT_M7f5TVOADq1t0-fBymh9Zt5TTIxhs59o"
IBM_ENDPOINT = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/96e3285a-e20c-40e4-8562-8fc9a454209d"

def translate(text):
    if ("平常" in text) or (text == "現在、１５分以上の遅延はありません。"):
        return "Service on schedule"

    model_id = 'ja-en'

    # Prepare the Authenticator
    authenticator = IAMAuthenticator(IBM_API_KEY)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(IBM_ENDPOINT)

    # Translate
    translation = language_translator.translate(
        text=text,
        model_id=model_id).get_result()
        
    return json.loads(json.dumps(translation))["translations"][0]["translation"]