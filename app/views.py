from bs4 import BeautifulSoup
from django.shortcuts import render
import requests


# Create your views here.
def home(request):
    url = 'https://obhavo.uz/'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html', {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0], 'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5], 'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1], 'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7], 'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


def andijon(request):
    url = 'https://obhavo.uz/andijan'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html',
                  {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0],
                   'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5],
                   'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1],
                   'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7],
                   'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


def buxoro(request):
    url = 'https://obhavo.uz/bukhara'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html',
                  {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0],
                   'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5],
                   'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1],
                   'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7],
                   'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


def urganch(request):
    url = 'https://obhavo.uz/urgench'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html',
                  {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0],
                   'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5],
                   'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1],
                   'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7],
                   'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


def xiva(request):
    url = 'https://obhavo.uz/khiva'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html',
                  {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0],
                   'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5],
                   'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1],
                   'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7],
                   'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


def guliston(request):
    url = 'https://obhavo.uz/gulistan'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html',
                  {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0],
                   'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5],
                   'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1],
                   'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7],
                   'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


def namangan(request):
    url = 'https://obhavo.uz/namangan'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html',
                  {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0],
                   'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5],
                   'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1],
                   'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7],
                   'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


def jizzax(request):
    url = 'https://obhavo.uz/jizzakh'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html',
                  {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0],
                   'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5],
                   'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1],
                   'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7],
                   'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


def qarshi(request):
    url = 'https://obhavo.uz/qarshi'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html',
                  {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0],
                   'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5],
                   'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1],
                   'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7],
                   'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


def termiz(request):
    url = 'https://obhavo.uz/termez'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html',
                  {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0],
                   'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5],
                   'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1],
                   'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7],
                   'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


def samarqand(request):
    url = 'https://obhavo.uz/samarkand'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html',
                  {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0],
                   'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5],
                   'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1],
                   'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7],
                   'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


def fargona(request):
    url = 'https://obhavo.uz/ferghana'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html',
                  {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0],
                   'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5],
                   'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1],
                   'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7],
                   'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


def navoiy(request):
    url = 'https://obhavo.uz/navoi'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html',
                  {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0],
                   'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5],
                   'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1],
                   'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7],
                   'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


def nukus(request):
    url = 'https://obhavo.uz/nukus'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_days = soup.find_all('td', class_='weather-row-day')
    weather_dayInfo = [data.text.split() for data in weather_days]
    weather_city = soup.find_all('h2')
    weather_today = soup.find_all('div', class_='current-day')
    weather_temp = soup.find_all('span', class_='forecast-day')
    weather_tavsif = soup.find_all('td', class_='weather-row-desc')
    weather_yogin = soup.find_all('td', class_='weather-row-pop')
    weather_quyosh_chiqishi = soup.find_all('div', class_='col-2')
    weather_malumotlar = soup.find_all('div', class_='col-1')
    weather_citydata = [data.text for data in weather_city]
    weather_temptoday = soup.find_all('div', class_='current-forecast')
    weather_havo = soup.find_all('div', class_='current-forecast-desc')
    weather_todaydata = [data.text for data in weather_today]
    weather_quyosh_chiqishidata = [data.text.split() for data in weather_quyosh_chiqishi]
    weather_malumotlardata = [data.text.split() for data in weather_malumotlar]
    weather_havodata = [data.get_text(strip=True) for data in weather_havo]
    weather_tempdata = [data.get_text(strip=True) for data in weather_temp]
    weather_temptodaydata = [data.get_text(strip=True) for data in weather_temptoday]
    weather_tavsifdata = [data.get_text(strip=True) for data in weather_tavsif]
    weather_yogindata = [data.get_text(strip=True) for data in weather_yogin]
    result = [sublist[0] for sublist in weather_dayInfo]
    return render(request, 'index.html',
                  {'city': weather_citydata[0], 'today': weather_todaydata[0], 'havo': weather_havodata[0],
                   'temptoday': weather_temptodaydata[0], 'chiq': weather_quyosh_chiqishidata[0][5],
                   'bot': weather_quyosh_chiqishidata[0][8], 'namlik': weather_malumotlardata[0][1],
                   'shamol': weather_malumotlardata[0][4], 'bosim': weather_malumotlardata[0][7], 'days': result[0:7],
                   'temp': weather_tempdata[0:7], 'tavsif': weather_tavsifdata[0:7], 'yogin': weather_yogindata[0:7]})


