from flask import Flask, render_template, request, redirect
app_lulu = Flask(__name__)

app_lulu.vars=dict()

app_lulu.questions = dict()
app_lulu.questions['Favorite Color?'] = ('Blue', 'Yellow', 'Mauve')
app_lulu.questions['What Time is it?'] = ('Peanut', 'Party', 'Zes uur')
app_lulu.questions['Cupcakes?'] = ('Hell yes!', 'No Way', 'What?')

app_lulu.answers = list()

app_lulu.nquestions = len(app_lulu.questions)

@app_lulu.route('/index_lulu', methods=['GET','POST'])
def index_lulu():
    if request.method == 'GET':
        return render_template('userinfo_lulu.html', num=app_lulu.nquestions)
    elif request.method == 'POST':
        app_lulu.vars['name'] = request.form['name_lulu']
        app_lulu.vars['age'] = request.form['age_lulu']
        return redirect('/main_lulu')
    else:
        return 'request.method was {0}!  Me no likey!'.format(request.method)

@app_lulu.route('/main_lulu')
def main_lulu2():
    if len(app_lulu.questions)==0:
        return render_template('end_lulu.html', answers = app_lulu.answers)
    else:
        return redirect('/next_lulu')

@app_lulu.route('/next_lulu', methods=['GET','POST'])
def next_foo():
    if request.method == 'GET':
        n = app_lulu.nquestions
        q, (a1,a2,a3) = app_lulu.questions.popitem()

        # save the current question
        app_lulu.currentq = q
        return render_template('layout_lulu.html', num=n, question=q, ans1=a1, ans2=a2, ans3=a3)
    elif request.method == 'POST':
        app_lulu.answers.append(request.form['answer_from_layout_lulu'])
        return redirect('/main_lulu')
        

if __name__ == '__main__':
    app_lulu.run(debug=True)

