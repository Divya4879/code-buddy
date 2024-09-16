from flask import Flask, request


app = Flask(__name__)


  
@app.route('/')
def index():
  f = open("template/index.html","r")
  page = f.read()
  f.close()
#   page = page.replace("{weather}",weather_codes[weather_code])
#   page = page.replace("{temp}",temp)
  
  
    
#   page = page.replace("{url}",url)
  return page


app.run(host='0.0.0.0', port=81)