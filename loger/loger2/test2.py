from flask import Flask,request,render_template,redirect
import time
app = Flask(__name__)
local="localhost"
wifi='192.168.43.53'
global log_dir,pass_dir,afih_dir,account,log2

log_dir="/media/root/persistence/code/python_web/loger/data/login.data"
pass_dir="/media/root/persistence/code/python_web/loger/data/password.data"
afih_dir="/media/root/persistence/code/python_web/loger/data/citation.data"
@app.route('/home',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        if request.form['cit']=="":
            pass
        else:
            rw=open(afih_dir,'a')
            rw.write(' \n'+request.form['cit'])
            rw.close()
    rd=open(afih_dir,'r')
    global li
    li= rd.readlines()
    rd.close()
    return render_template('acc2.html',listo=li)
@app.route('/msg',methods=['GET','POST'])
def msg():
    if request.method=='POST':
        return " bienvenu cher(e) {} ".format(request.form['nom'])

    return '<form action="" method="post"><input type="text" name="nom"/><input type="submit" value="envoyer"/></form>' 

@app.route('/inscription',methods=['GET','POST'])
def insc():
    if request.method=='POST':
        return " bienvenu "

    return render_template('l&g3.html')

@app.route('/confirm',methods=['GET','POST'])
def confirmm():
    if request.method=='POST':
        log,pas1,pas2=request.form['log'],request.form['password'],request.form['password2']
        if pas1!=pas2:
            return render_template('insc.html',err=" les deux mot de passe ne correspondent pas veillez ressayer")
        elif pas1=="" or pas1=="" or log=="" :
            return render_template('insc.html',err=" le formulaire ne peut pas etre vide")
        else:
            fs=open(log_dir,'r')
            lst2=fs.readlines()
            fs.close()
            if log in lst2:
                return render_template('insc.html',err="le login choisi est deja utiliser veilez en choisir un autre ")
            else:
                fr=open(log_dir,'a')
                fr2=open(pass_dir,'a')
                fr.write("\n"+log)
                fr2.write("\n"+pas1)
                fr.close()
                fr2.close()
                return redirect('/connexion')

    else:
        return redirect('/home')

@app.route('/connexion',methods=['GET','POST'])
def conn():
    if request.method=='POST':
        return " hello"
    else:
        return render_template('conn.html',err="")

@app.route('/confirm2',methods=['GET','POST'])
def confirm2():
    if request.method=='POST':
        log2,pas3=request.form['name2'],request.form['password2']
        fs3=open(log_dir,'r')
        lst3=fs3.readlines()
        fs3.close()
        if log2 not in lst3:
            return render_template('conn.html',err="login not found ,retry")
        elif log2 in lst3:
            fs4=open(pass_dir,'r')
            lst4=fs4.readlines()
            fs4.close()
            ind=lst3.index(log2)
            if pas3!=lst4[ind]:
                return render_template('conn.html',err="incorrect password ,retry")
            elif pas3==lst4[ind]:
                account=log2
                return redirect('/perso'),account
    else:
        return redirect('/home')

@app.route('/perso',methods=['GET','POST'])
def conn_perso():
    if request.method=='POST':
        return " hello"
    else:
        try:
            return redirect('/h_perso')
        except NameError:
            return redirect ('/home')


if __name__ =='__main__':
    app.run(host =local,debug=True)
