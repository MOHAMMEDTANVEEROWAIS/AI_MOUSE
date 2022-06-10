from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  # print ('I got clicked on!')
  # return 'Clicked on.'
  return render_template('AI_VIRTUAL_PAINTER.py')

if __name__ == '__main__':
  app.run(debug=True)