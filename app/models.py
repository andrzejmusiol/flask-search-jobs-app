import requests
import json
# Funkcja pobierająca dane w JSON i zapisująca je lokalnie
def response(description, location):
	if (description and location):
		response = requests.get('https://jobs.github.com/positions.json?search=' + description + '&location=' + location + '')
	elif description:
		response = requests.get('https://jobs.github.com/positions.json?search=' + description + '')
	else:
		response = requests.get('https://jobs.github.com/positions.json?&location=' + location + '')

	with open('jobs.json', 'w', encoding="utf-8") as file:
		file.write(response.text)