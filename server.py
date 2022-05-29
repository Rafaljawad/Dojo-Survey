from flask import Flask,render_template,redirect,request,session
app=Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

# Have the root route ("/") show a page with the form
@app.route('/')
def show():
    return render_template('index1.html')

# http://localhost:5000 - have this display a nice looking HTML form.  The form should be submitted to '/process'
@app.route('/process',methods=['POST'])
def process_form():
    session['first-name']=request.form['first-name']
    session['last-name']=request.form['last-name']
    session['select-location']=request.form['select-location']
    session['fav-language']=request.form['fav-language']
    session['comment']=request.form['comment']
    session['check']=request.form['check']
    session['status']=request.form['status']
    return redirect('/sucess')

# Have the "/result" route display the information from the form on a new HTML page
@app.route('/sucess')
def show_sucess_index():
    return render_template('index2.html')


#going back to the form page(at route('/'))
@app.route('/back')
def go_back():
    return redirect('/')

if __name__=="__main__": 
    app.run(debug=True)  