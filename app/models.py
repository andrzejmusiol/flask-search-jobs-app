import requests
import json
# Funkcja pobierająca dane w JSON i zapisująca je lokalnie
def response(description, location):
	if (description and location):
		response_result = requests.get('https://jobs.github.com/positions.json?search=' + description + '&location=' + location + '')
	elif description:
		response_result = requests.get('https://jobs.github.com/positions.json?search=' + description + '')
	else:
		response_result = requests.get('https://jobs.github.com/positions.json?&location=' + location + '')

	with open('jobs.json', 'w', encoding="utf-8") as file:
		file.write(response_result.text)

	return response_result


print(response('java', 'california'))