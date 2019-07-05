from flask import render_template, flash, redirect, url_for, session, request
from app import app , db, lm
from flask_login import login_user, logout_user
from app.models.tables import User
from app.models.forms import LoginForms
import functools


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html')
    

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForms()
    if form.validate_on_submit():
     
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("index"))
        else:
            flash("Invalid login. ")    
    
    
    return render_template("login.html",
                            form=form)




@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    form = RegisterForms()
    if request.method == "POST" :
        username = request.form.get("username")
        password = request.form.get("password")
        name = request.form.get("name")
        email = request.form.get("email")

        if username and password and name and email:
            user = User(username,password,name,email)
            db.session.add(user)
            db.session.commit()

    return redirect(url_for("index")) 




@app.route("/lista")
def lista():
    user = User.query.all()
    return render_template("lista.html",user=user)

@app.route("/excluir/<int:id>")   
def excluir(id):
    user = User.query.filter_by(id=id).first()


    db.session.delete(user)
    db.session.commit()

    user = User.query.all()
    return render_template("lista.html", user=user)

@app.route("/alterar/<int:id>", methods=['GET','POST'])
def alterar(id):
    user = User.query.filter_by(id=id).first()

    if request.method == "POST" :
        username = request.form.get("username")
        password = request.form.get("password")
        name = request.form.get("name")
        email = request.form.get("email")

        if username and password and name and email:
            user.username = username
            user.password = password
            user.name = name
            user.email = email

            db.session.commit()

            return redirect(url_for("lista"))
            
        return render_template("alterar.html", user=user)    


#Crud exemplos#
#@app.route("/teste/<info>")
#@app.route("/teste", defaults={"info":None})
#def teste(info):
   
   
   
   # r = User.query.filter_by(username="Arthur").first()
    #print(r.username, r.name)
    #return "Ok"
    
    
    
    
    #i = User("Arthur", "1234", "Alberto Henrique" , "arthur@gmail.com")
    #db.session.add(i)
    #db.session.commit()
    





#@app.route("/test/")
#def test():
 #       return "Oi!" 