import requests

# URL сервера
url = "http://localhost:8081/subject"

# Данные, которые нужно добавить
data = {
    "name": "Subject2",
    "mark": "4"
}

# Выполнение POST-запроса
response = requests.post(url, data=data)

# Вывод результата
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")