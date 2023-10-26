from db import db

class ArticleModel(db.Model):
    __tablename__ = 'Articles'

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(255), unique=True, nullable=False)
    contenu = db.Column(db.Text, nullable=False)

    medias = db.relationship('MediaModel', backref='Articles', lazy=True)

