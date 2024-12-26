import jwt
import requests
import json
from time import time


# Enter your API key and your API secret
API_KEY = 'lzrB2SmbREmINGpJIoiJg'
API_SEC = 'QLG3V4USRPaThprkRheg0ZhsH8GYcN66'

# create a function to generate a token
# using the pyjwt library


def generateToken():

		# Create a payload of the token containing
		# API Key & expiration time
	payload= {
		'iss': API_KEY, 
  		'exp': time() + 5000
	}
	token = jwt.encode(payload, API_SEC, algorithm="HS256")
	return token


# create json data for post requests
meetingdetails = {"topic": "The title of your zoom meeting",
				"type": 2,
				"start_time": "2024-12-22T10: 21: 57",
				"duration": 45,
				"timezone": "Europe/Madrid",
				"agenda": "Test meeting",

				"recurrence": {"type": 1,
								"repeat_interval": 1
								},
				"settings": {"host_video": True,
							"participant_video": True,
							"join_before_host": False,
							"mute_upon_entry": False,
							"watermark": True,
							"audio": "voip",
							"auto_recording": "cloud"
							}
				}

# send a request with headers including
# a token and meeting details


def createMeeting():
    headers = {'authorization': 'Bearer ' + generateToken(), 'content-type': 'application/json'}
    r = requests.post(
        'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails)
    )

    print("\nCreating Zoom meeting...\n")
    print(f"Response Status Code: {r.status_code}")
    print(f"Response Text: {r.text}")

    if r.status_code != 201:
        print("Error creating Zoom meeting. Please check the response.")
        return

    # Proceed only if the response status is successful
    y = r.json()
    join_URL = y.get("join_url")
    meetingPassword = y.get("password")

    if join_URL and meetingPassword:
        print(f"\nHere is your Zoom meeting link: {join_URL}")
        print(f"Meeting Password: {meetingPassword}")
    else:
        print("Unexpected response structure. Missing 'join_url' or 'password'.")



# run the create meeting function
createMeeting()
