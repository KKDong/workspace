# -*- coding: utf-8 -*-
# all the imports

from flask import request, redirect, url_for,\
	render_template
from apps import app
from database import Database

dataStorage = Database()

@app.route('/', methods=['GET', 'POST'])
def show_entries():
	entries = dataStorage.out()
	return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
	storage={}

	storage['num'] = dataStorage.num
	storage['count'] = 0
	storage['title'] = request.form['title']
	storage['contents'] = request.form['contents']

	dataStorage.put(storage)
	dataStorage.num += 1

	return redirect(url_for('show_entries'))

@app.route('/del/<idx>', methods=['GET'])
def del_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			dataStorage.database.remove(data)
			break

	return redirect(url_for('show_entries'))