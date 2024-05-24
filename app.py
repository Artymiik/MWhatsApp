# from script import Main
import json
import time
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if (request.method == 'GET'):
    with open('data.json', 'r', encoding='utf-8') as f:
      data = json.load(f)

    return render_template('Index.html', data = data)

  phones = request.form['Phones']
  message = request.form['Message']

  if not phones:
    return redirect("/error")
  
  if not message:
    return redirect("/error")
  
  message = '\n'.join(request.form['Message'].splitlines())

  time.sleep(2)
  # whatsapp_bot = Main.WhatsAppBot(phones, message)

  # if whatsapp_bot == 200:
  #   return redirect("/success")
  # else:
  #   return redirect("/error")

@app.route('/start', methods = ['GET'])
def start():
  with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

  return render_template('Start.html', data = data)

@app.route('/success', methods = ['GET'])
def success():
  with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

  return render_template('ScriptSuccess.html', data = data)

@app.route('/error')
def Error():
  with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

  return render_template('Error.html', data = data);

if __name__ == '__main__':
  app.run(debug=True)