
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json, random
def Emotion(emoti_string):
    print("Getting")
    authenticator = IAMAuthenticator('gShpJ1z419dIvo8i4PgG6wbq2IKpo4AoJ0TH-xzQ-hTA')
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        authenticator=authenticator
    )

    tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/a92fa2f2-7e10-491e-bd71-2b8b96f4c32f')
    utterances = [
        {
            "text" : emoti_string ,
            "user" : "agent"
        }
    ]

    utterance_analyses = tone_analyzer.tone_chat(utterances).get_result()
    # print(utterance_analyses)
    # tone_dict =(json.dumps(utterance_analyses, indent=2))
    # json_acceptable_string = tone_dict.replace("'", "\"")
    d = (utterance_analyses)
    print(d )

    # print(d)

    em = d['utterances_tone'][0]['tones'][0]['tone_id']
    print(em)

    if (em == 'excited' or em =='joy'):
        sop = ["Pop Songs" ,"Jazz Songs" , "Rock Love Songs"]
        return random.choice(sop)

    if (em == 'sad' ):
        sopp = ["Soothing Songs" ,"breakup songs" "Blues Songs"]
        return random.choice(sopp)
    if (em =='frustrated'):
        sopp = ["Soothing Songs" , "Blues Songs"  , "Heavy Metal songs"]
        return random.choice(sopp)

    if(em is None):
        soppp = ['Sad Songs', "Jazz Songs" ]
        return random.choice(soppp)


    return "Rock Songs"





if __name__ == '__main__':
    print(Emotion("I am not feeling very good"))
