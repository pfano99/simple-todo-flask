if __name__ == '__main__':
    from todo import app, db

    with app.app_context():
        db.create_all()
