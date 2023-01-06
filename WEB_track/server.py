from flask import Flask, render_template
from weather import weather_by_city
from python_org_news import get_python_news

app = Flask(__name__)

@app.route('/') #декоратор = функция запустится тогда, когда пользовтель введет косую черту (главная страница)
def index() -> str:
    title = "Крутой сайт"
    weather = weather_by_city("Moscow,Russia")
    news_list = get_python_news()
    return render_template('index.html', page_title=title, weather=weather, news_list=news_list)

if __name__ == "__main__":
    app.run(debug=True)