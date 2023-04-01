if __name__ == '__main__':
    from todo import app, db, AuthType

    with app.app_context():
        db.drop_all()
        db.create_all()
        _types = [
            AuthType(name="default"),
            AuthType(name="google"),
            AuthType(name="twitter"),
            AuthType(name="facebook"),
        ]
        db.session.add_all(_types)
        db.session.commit()
