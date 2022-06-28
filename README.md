# UneeQ Unsolicited Responses in Python

This application packages up a Flask app and a virtual environment that you can use in order to deploy a small service that interfaces with the UneeQ API in order to make a digital human speak.

## Instructions

- git clone this repo
- cd to directory
- `source venv/unsolicited_env/bin/activate` This will use Python 3.7.2, we assume it's installed on your system
- `pip install -r requirements.txt` Assumes pip is an alias python3 -m pip command
- You should adapt the code to process YOUR Customer JWT Secret and active Avatar Session ID.  These values are set in the project as environment variables, but this is not a long-term solution.  The Customer JWT Secret can remain an environment variable, but the Avatar Session ID will change with each new session, so you should handle this value dynamically
- Assuming you use the environment variable approach, start a digital human session from the Creator UI in a browser
- Open the JS Console of your browser and locate the Avatar Session ID value, copy that
- Back in your project directory, `export AVATAR_SESSION_ID=$VALUE_YOU_JUST_COPIED CUSTOMER_JWT_SECRET=$YOU_CUSTOMER_JWT_SECRET`
- `python app.py`

Now you can send a POST request to your service running on your localhost and the digital human running in your browser should speak.

cURL:

```
curl --location --request POST 'localhost:5000/api/v1/speak' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text_to_speak": "I really like listening to Rage Against the Machine"
}'
```