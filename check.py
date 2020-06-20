import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def Emotion(id):
    authenticator = IAMAuthenticator('gShpJ1z419dIvo8i4PgG6wbq2IKpo4AoJ0TH-xzQ-hTA')
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        authenticator=authenticator
    )

    tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/a92fa2f2-7e10-491e-bd71-2b8b96f4c32f')
    utterances = [
        {
            "text" : id ,
            "user" : "agent"
        }
    ]

    utterance_analyses = tone_analyzer.tone_chat(utterances).get_result()
    return (json.dumps(utterance_analyses, indent=2))



if __name__ == "__main__":
    print(Emotion("Sorry to hear that."))