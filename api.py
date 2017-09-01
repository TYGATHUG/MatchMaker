import json
import requests

def get_personality(input_string):
	input_string = 'asdad'
	response = requests.post("https://gateway.watsonplatform.net/personality-insights/api/v3/profile?version=2016-10-20&consumption_preferences=true&raw_scores=true",
	         auth=("99ed4dec-a5c2-4684-8211-ea736ac6312d", "7b0qu4CHWQbG"),
	         headers = {"content-type": "text/plain"},
	         data = input_string
	         )

	jsonProfile = json.loads(response.text)
	print input_string
	
	return jsonProfile