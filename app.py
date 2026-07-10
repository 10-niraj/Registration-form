from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "abc123"  

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        if not name or not email or not password  or name.strip()== "" or email.strip()=="" or password.strip()=="":
               
            flash("Registration fail, Try Again 😔")
        else:
            flash(f"Registration Start, Welcome {name} 😊") 

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)



