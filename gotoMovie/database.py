import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext


def connect_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = connect_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))


def test_db_data():
    db = connect_db()
    with current_app.open_resource('test/data.sql') as f:
        db.executescript(f.read().decode('utf-8'))


def delete_db_data():
    db = connect_db()
    with current_app.open_resource('test/delete.sql') as f:
        db.executescript(f.read().decode('utf-8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database')


@click.command('test-db')
@with_appcontext
def test_db_command():
    test_db_data()
    click.echo('test the database sql')


@click.command('delete-db')
@with_appcontext
def delete_db_command():
    delete_db_data()
    click.echo('delete the data in database ')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(test_db_command)
    app.cli.add_command(delete_db_command)
