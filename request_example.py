import requests
# URL, до якого ви хочете виконати HTTP-запит
url = "будь-який іншийhttps://www.example.com"  # або  URL
# Виконання GET-запиту до вказаного URL
response = requests.get(url)
# Виведення вмісту відповіді на екран
print(response.text)
