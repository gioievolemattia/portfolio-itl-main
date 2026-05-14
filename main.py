# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)
# Connettere SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FEEDBACK.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creare il DB
db = SQLAlchemy(app)

# Creare il modello del DB
class Feedback(db.Model):
        
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feedback {self.id}>'

# Esecuzione della pagina dei contenuti
@app.route('/')
def index():
    return render_template('index.html')


# Competenze dinamiche
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    return render_template('index.html', button_python=button_python, button_discord=button_discord)
    

@app.route('/', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        email = request.form['email']
        text = request.form['text']
        
        # Consegna #3. Implementare la registrazione dell'utente.
        feedback = Feedback(email=email, text=text)

        db.session.add(feedback)
        db.session.commit()

        return redirect('/')






if __name__ == "__main__":
    app.run(debug=True) 

