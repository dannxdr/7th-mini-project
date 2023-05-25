import os, json
import openai

from django.shortcuts import render, redirect
from django.http import JsonResponse

openai.api_key = "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"

# chatGPT
def chatgpt_api(prompt):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )
    result = completion.choices[0]['message']['content']
    return result

#chatGPT에게 그림 요청 API
def imageGPT(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    result =response['data'][0]['url']
    return result
    
# Create your views here.
def index(req):
    return render(req, "selfchatgpt/index.html")

def chat(req):
    if req.method == "POST":
        data = json.loads(req.body)
        prompt = data.get("input_text")
        question_type = data.get("question_type")
        
        if question_type == "text":
        
            result = chatgpt_api(prompt)
        
            context = {
                "question": prompt,
                "result": result,
                "is_image": False
            }
            return JsonResponse(context)
        
        else:
            result = imageGPT(prompt)
            context = {
                "question": prompt,
                "result": result,
                "is_image": True
            }
            return JsonResponse(context)
    else:
        return redirect("selfchatgpt:index")