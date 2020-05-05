from flask import Flask, render_template
import data

app = Flask(__name__)
title = data.title
subtitle = data.subtitle
description = data.description
departures = data.departures
tours = data.tours


@app.route('/')
def render_main():
   return render_template('index.html', tours = tours, title = title, subtitle = subtitle, description = description, departures = departures)


@app.route('/departures/<current_departure>')
def render_departures(current_departure):
   # Создаем переменные, которые будем передавать в шаблон
   filtered_tours = {}
   count_tours = 0
   min_price = 0
   max_price = 0
   min_nights = 0
   max_nights = 0

   # Фильтруем туры по выбранному направлению
   for key,value in tours.items():
      if value["departure"] == current_departure:
         filtered_tours[key] = value
         # Наполняем переменные
         count_tours = count_tours + 1
         if min_price >= value["price"] or min_price == 0:
            min_price = value["price"]
         if max_price <= value["price"] or max_price == 0:
            max_price = value["price"]
         if min_nights >= value["nights"] or min_nights == 0:
            min_nights = value["nights"]
         if max_nights <= value["nights"] or max_nights == 0:
            max_nights = value["nights"]
   # Рендерим
   return render_template('departure.html', tours = tours, filtered_tours = filtered_tours, title = title, departures = departures, current_departure = current_departure, count_tours = count_tours, min_price = min_price, max_price = max_price, min_nights = min_nights, max_nights = max_nights)


@app.route('/tours/<int:id>/')
def render_tours(id):
   return render_template('tour.html', tours = tours[id], title = title, subtitle = subtitle, description = description, departures = departures)

app.run()