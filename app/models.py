import requests
import json
# Funkcja pobierająca dane w JSON i zapisująca je lokalnie
def response(language, location):
	if (language and location):
		response = requests.get('https://jobs.github.com/positions.json?search=' + language + '&location=' + location + '')
	elif language:
		response = requests.get('https://jobs.github.com/positions.json?search=' + language + '')
	else:
		response = requests.get('https://jobs.github.com/positions.json?&location=' + location + '')

	with open('jobs.json', 'w', encoding="utf-8") as file:
		file.write(response.text)