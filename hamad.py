from flask import Flask,render_template

import datetime
from datetime import datetime
hamad  = Flask(__name__)
 

@hamad.route("/<int:x>/")
def tolba(x): 
    x=x-1
    p=["modric","CR7","messi","zlatan"]#فكرنى ليه بنعمل  p=p
    return render_template("tolba.html",pagename="tolba.html",x=p[x],p=p)

@hamad.route("/kiro")
def kiro(): 
    return render_template("kiro.html",pagenme="kiro.html")

 
@hamad.route("/")
def karem(): 
    
    return render_template("karem.html",pagenme="karem.html")

@hamad.route("/<string:f>/")
def balo(f): 
    return render_template(f"{f}.html",pagenme=f"{f}.html")
@hamad.route("/")#ملاحظة عند تغير مكتن هذه الفانكشن يتغير ترتيب الصفحات اللى ستفتح اولا وعند ازالتها تمام هذا لا يؤثر بتاتا 
def base(): 
   
    return render_template("base.html",pagename="base.html",n=n)






if __name__ =="__main__":
    hamad.run(debug=True)
