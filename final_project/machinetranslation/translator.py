import os
import json
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
#language_translator.set_disable_ssl_verification(True)



def english_to_french(english_text):

    if english_text == None or len(english_text) == 0:
        return ""
    translation_response = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()

    json_response = json.loads(json.dumps(translation_response))
    french_text = json_response["translations"][0]["translation"]

    return french_text

def french_to_english(french_text):
    if french_text == None or len(french_text) == 0:
        return ""
        
    translation_response = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()

    json_response = json.loads(json.dumps(translation_response))
    english_text = json_response["translations"][0]["translation"]

    return english_text

