from flask import Flask, jsonify, render_template

app = Flask(__name__)


JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'New York, NY',
        'salary': '$120,000 - $150,000',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'San Francisco, CA',
        'salary': '$130,000 - $160,000',
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'Austin, TX',
       
    },
    {
        'id': 4,
        'title': 'UX Designer',
        'location': 'Seattle, WA',
        'salary': '$100,000 - $130,000',
    },


]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='TechCorp')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

