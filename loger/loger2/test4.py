# importation des modules necessaires et declaration de variables global
from flask import Flask,request,render_template,redirect
import time,sqlite3,hashlib
app = Flask(__name__)
local="localhost"
wifi='192.168.43.53'
global log_dir,pass_dir,afih_dir,account,log2

log_dir="/media/root/persistence/code/python_web/loger/data/login.data"
pass_dir="/media/root/persistence/code/python_web/loger/data/password.data"
afih_dir="/media/root/persistence/code/python_web/loger/data/citation.data"

#route home

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

# route experimental

@app.route('/msg',methods=['GET','POST'])
def msg():
    if request.method=='POST':
        return " bienvenu cher(e) {} ".format(request.form['nom'])

    return '<form action="" method="post"><input type="text" name="nom"/><input type="submit" value="envoyer"/></form>' 


#route pour la page de connexion et d'inscription

@app.route('/inscription',methods=['GET','POST'])
def insc():
    if request.method=='POST':
        return " bienvenu "

    return render_template('l&g3.html')


#api de creation de compte utilisateur

@app.route('/confirm1',methods=['GET','POST'])
def confirmm():
    if request.method=='POST':
        login,password,email=request.form['ins-pseudo'],request.form['ins-pass'],request.form['ins-email']
        login=hashlib.sha224((bytes(login,'utf8'))).hexdigest()
        password=hashlib.sha224((bytes(password,'utf8'))).hexdigest()
        DATABASE ="/media/root/persistence/code/python_web/loger/data/auth.db"
        conn=sqlite3.connect(DATABASE)
        cur=conn.cursor()
        cur.execute(" select id from auth ")
        for l in cur:
            id_old=l
        id_old=id_old[0]
        cur.execute(" select login from auth ")
        ps=cur.fetchall()
        pseudo_olds=[]
        for l in ps:
            pseudo_olds.append(l)
            if l[0] ==login :
                cur.close()
                conn.close()
                return " login deja existant"
        
        
        if login=="" or password=="" :
            cur.close()
            conn.close()
            return " login ou password vide "
        else:
            donnee=(id_old+1, login,password,email)
            cur.execute("insert into auth (id ,login ,password ,email) values( ?,?,?,?)",donnee)
            conn.commit()
            cur.close()
            conn.close()
            return " creation reussi"

    else:
        return redirect('/home')


# api de validation d'une connexion client

@app.route('/confirm2',methods=['GET','POST'])
def confirm2():
    booli=False
    if request.method=='POST':
        indexor,indexor2,indexor3,indexor4=0,0,0,0
        login ,password=request.form['con-pseudo'],request.form['con-pass']
        login=hashlib.sha224((bytes(login,'utf8'))).hexdigest()
        password=hashlib.sha224((bytes(password,'utf8'))).hexdigest()
        DATABASE ="/media/root/persistence/code/python_web/loger/data/auth.db"
        conn=sqlite3.connect(DATABASE)
        cur=conn.cursor()
        cur.execute(" select login from auth ")
        ps=cur.fetchall()
        pseudo_olds=[]
        for l in ps:
            pseudo_olds.append(l)
            if l[0] ==login:
                booli=True
                indexor2=indexor
            indexor+=1
        cur.execute(" select id from auth ")
        for l in cur:
            
            if indexor3==indexor2:
                id_old=l
            indexor3+=1
        id_old=id_old[0]
        if booli==False :
            cur.close()
            conn.close()
            return " login incorect"
        elif booli==True:
            cur.execute(" select password from auth ")
            for l in cur:
                if indexor4==indexor2:
                    pass_clef=l
                indexor4+=1
            pass_clef=pass_clef[0]
            if pass_clef != password:
                return " password erronee "
            elif pass_clef == password:
                return " connexion validee id = {} ,login ={} et password = {}".format(id_old,login,pass_clef)
    else:
        return redirect('/home')


#api non finalisser de gestion pages dynamique

@app.route('/perso',methods=['GET','POST'])
def conn_perso():
    if request.method=='POST':
        return " hello"
    else:
        try:
            return redirect('/h_perso')
        except NameError:
            return redirect ('/home')

# lancement en temps que modules

if __name__ =='__main__':
    app.run(host =local,debug=True)
