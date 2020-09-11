from flask import Flask, render_template, request, flash
#from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
#from config import Config
import os

devicedata = {'Voltage1':'12.1','Voltage2':'12.2','RL1':'OFF','RL2':'ON',}

class RelayForm(FlaskForm):
  RL1_field = SelectField("Relay 1: ", choices=[(1, "ON"), (2, "OFF")], default=2)
  RL2_field = SelectField("Relay 2: ", choices=[(1, "ON"), (2, "OFF")], default=2)
  RL3_field = SelectField("Relay 3: ", choices=[(1, "ON"), (2, "OFF")], default=2)
  RL4_field = SelectField("Relay 4: ", choices=[(1, "ON"), (2, "OFF")], default=2)
  submit = SubmitField('Set')

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

#app.config.from_object(Config)

@app.route("/", methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
   global devicedata
   form = RelayForm(RL1_field=1)
   if request.method == 'POST':
       rl1dat = form.RL1_field.data
       print(rl1dat)
       devicedata['Voltage1'] = '13.1'
#       form = RelayForm(RL1_field=2)
#       flash('Relay set {}, to={}'.format(
#            form.RL1_field.data, form.RL2_field.data))
       return render_template('index.html',**devicedata,form=form)

   return render_template('index.html',**devicedata,form=form)



if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug = True)
