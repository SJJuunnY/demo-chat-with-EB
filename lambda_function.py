# import openai

# openai.api_key = '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'

# def lambda_handler(event, context):
#     if 'm' in event['params']['querystring'] :
#         input_message = event['params']['querystring']['m']
#     else :
#         input_message = "나는 신한투자증권에 입사하려는 개발자야. 클라우드를 공부해야 할 필요가 있을까?"
        
#     message = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo", # 사용 모델
#         messages=[
#           {"role": "system", "content": "너는 클라우드 전문 개발자야. 핵심만 담아서 최대한 짧게 말하는 특징이 있어."},
#           {"role": "user", "content": input_message}
#           ] # 전달 메세지
#     )
#     return message

import openai 

openai.api_key = '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'

def lambda_handler(event, context):
    if 'm' in event['params']['querystring']:
        input_message = event['params']['querystring']['m']
    else:
        input_message = "나는 신한투자증권에 입사하려는 개발자야. 클라우드를 공부해야 할 필요가 있을까?"
    
    message = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # 사용 모델
    messages=[
        {"role": "system", "content": "너는 이모티콘을 엄청 많이 쓰는 사회 초년생 직장인이야. 친근하게 말하려구 반말로 해."},
        {"role": "user", "content": input_message}
        ] # 전달 메세지
    )
    
    return message
