from flask import Flask,render_template

AI=Flask(__name__)

@AI.route('/fun/<name>')
def fun(name):
	return f'<h1>Welcome my Friend {name}</h1>'

@AI.route('/html_page')
def html_page():
	return render_template('html_page.html',name='Murugan',location='Salem')

if __name__=='__main__':
	AI.run(debug=True)
