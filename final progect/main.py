from flask import Flask, render_template, request
import random

app = Flask(__name__)
facts_list = ["В 2022 году средняя температура в мире была на 1,15 °C выше доиндустриального уровня. Годовая глобальная температура уже восемь лет подряд превышает доиндустриальный уровень минимум на 1°C.", 
            "Главная причина глобального потепления — выбросы парниковых газов при сжигании ископаемого топлива (угля, нефти и газа). В результате в атмосферу попадают углекислый газ, метан, закись азота, фторированные газы", 
            "Увеличение средней температуры на планете влияет на уровень моря. Ледники тают, из-за чего в океан попадает дополнительная вода. Кроме того, океан нагревается вместе с сушей, и объём тёплой воды больше холодной. За последние 100 лет уровень Мирового океана повысился примерно на 20 см.", 
            "Мировой океан нагревается на 60% быстрее, чем предполагали учёные. Он поглощает до 90% тепла, которое отражается от атмосферы, но в последнее время океан стал нагреваться слишком быстро. В результате вскоре он может стать катализатором потепления климата, то есть начать выбрасывать большое количество тепла в атмосферу."]

@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/random_fact",methods=['GET', 'POST'])
def facts():
    random_fact = random.choice(facts_list)
    return render_template('random_fact.html',random_fact=random_fact)

app.run(debug=True)