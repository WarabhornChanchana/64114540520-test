from flask import Flask ,render_template ,request,redirect, url_for

app = Flask(__name__)

courses = [
    {'ID' : 'IR01', 'name': 'IR'},
    {'ID' : 'Com02', 'name': 'Computer'},
    {'ID' : 'DT03', 'name': 'Data'},
]

@app.route('/')
def index():
    return render_template('index.html', courses = courses)

@app.route('/search', method=['GET','POST'])
def search():
    result = None

    if request.method == 'POST':
        course_ID = request.form.get('course_ID')
        result = next((course for course in courses if course['ID'] == course_ID), None)
    return render_template('search.html', result=result)

if __name__=='__main__':
    app.run(debug=True)