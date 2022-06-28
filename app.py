from flask import Flask, request, jsonify
import json
import jwt
import os
import requests

# import ipdb
# ipdb.set_trace() to set a breakpoint for debugging
# Use the ! operator before any python statement inside the ipdb console, i.e. !print(response)

app = Flask(__name__)
app.config["DEBUG"] = True

sessionIdJwt = os.environ.get('CUSTOMER_JWT_SECRET')
sessionId = os.environ.get('AVATAR_SESSION_ID')
uneeq_speak_uri_host = 'https://api.us.uneeq.io'
uneeq_speak_uri_path = f'/api/v1/avatar/{sessionId}/speak'

@app.route('/api/v1/speak', methods=['POST'])
def make_digital_human_speak():
    params = json.loads(request.data)
    
    headers = {
      "Content-Type": 'application/json'
    }

    encodedSessionIdJwt = jwt.encode({'sessionId': f'{sessionId}'}, sessionIdJwt, algorithm='HS256')
    
    instructions = {
        "instructions": {
          "displayHtml": {
            "html": f"<h2>#{params['text_to_speak']}</h2>"
          }
        }
    }
    
    body = {
      'answer': params['text_to_speak'],
      'answerAvatar': json.dumps(instructions, separators=(',', ':'), ensure_ascii=False),
      'sessionIdJwt': encodedSessionIdJwt
    }

    response = requests.post(uneeq_speak_uri_host+uneeq_speak_uri_path, data = json.dumps(body), headers = headers)
    
    return response.content


if __name__ == "__main__":
    app.run()
