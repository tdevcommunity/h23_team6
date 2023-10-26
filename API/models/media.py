from db import db

class MediaModel(db.Model):
    __tablename__ = 'Medias'

    id = db.Column(db.Integer, primary_key=True)
    media_Path = db.Column(db.String(255), unique=True, nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False, default=db.func.now())

    article_id = db.Column(db.Integer, db.ForeignKey('Articles.id'), nullable=False)
