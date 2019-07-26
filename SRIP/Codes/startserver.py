from flask import Flask, render_template, request, flash
import sqlite3
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
def lab():
    return render_template("lab.html")

@app.route("/save", methods=['GET', 'POST'])
def save():
    conn = sqlite3.connect('log_history.db')
    data = request.form
    #form = SaveLog.save_to_db(data)

    #if form.validate_on_submit():
     #   flash(f'Account created')
     #   return render_template("lab.html")

    #print(data['code'])
    #print(data['language'])
    #print(data['codeId'])

    conn.execute("INSERT INTO log_history_table (time, code, language, problemid) VALUES (?,?,?,?)",(str(datetime.datetime.now()),data['code'],data['language'],data['codeId']))
    conn.commit()
    cursor = conn.cursor()
    cursor.execute("select * from log_history_table order by problemid;")
    rows=cursor.fetchall()

    #for row in rows:
    #    for i in row:
    #        print(i)
    conn.close()
    
    return render_template("Previous_submissions.html",rows=rows)


if __name__ == '__main__':
    app.run(debug=True)