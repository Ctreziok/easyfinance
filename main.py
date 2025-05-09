from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loan', methods=['GET', 'POST'])
def loan(): #for calculating loan monthly payment
    result = None
    if request.method == 'POST':
        amount = float(request.form['amount'])
        rate = float(request.form['rate']) / 100 / 12
        term = int(request.form['term']) * 12
        monthly = (amount * rate) / (1 - (1 + rate)**-term)
        result = round(monthly, 2)
    return render_template('loan.html', result=result)

@app.route('/investment', methods=['GET', 'POST'])
def investment(): #for calculating investment
    result = None
    if request.method == 'POST':
        principal = float(request.form['principal'])
        monthly = float(request.form['monthly'])
        rate = float(request.form['rate']) / 100 / 12
        years = int(request.form['years'])
        months = years * 12
        future_value = principal * (1 + rate)**months + monthly * (((1 + rate)**months - 1) / rate)
        result = round(future_value, 2)
    return render_template('investment.html', result=result)

@app.route('/retirement', methods=['GET', 'POST'])
def retirement(): #for calculating retirement
    result = None
    if request.method == 'POST':
        savings = float(request.form['savings'])
        contribution = float(request.form['contribution'])
        rate = float(request.form['rate']) / 100 / 12
        years = int(request.form['years'])
        months = years * 12
        future_savings = savings * (1 + rate)**months + contribution * (((1 + rate)**months - 1) / rate)
        result = round(future_savings, 2)
    return render_template('retirement.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
