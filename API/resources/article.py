from flask import Flask, request, jsonify,current_app
from db import db
from models import ArticleModel, MediaModel
from werkzeug.utils import secure_filename
from flask_smorest import Blueprint
import os

blp = Blueprint("Article", "articles", description="Operations sur les articles")

# Configure the media upload directory in the application's configuration
MEDIA_UPLOAD_FOLDER = 'my_uploads'
MEDIA_ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

@blp.route('/add_article', methods=['POST'])
def add_article():
    # Receive article data from the form
    titre = request.form.get('titre')
    contenu = request.form.get('contenu')

    # Create a new article in the database
    new_article = ArticleModel(titre=titre, contenu=contenu)
    db.session.add(new_article)
    db.session.commit()

    # Handle media files
    media_files = request.files.getlist('media_files')
    for media_file in media_files:
        if media_file and allowed_file(media_file.filename, MEDIA_ALLOWED_EXTENSIONS):
            filename = secure_filename(media_file.filename)
            media_file.save(os.path.join(MEDIA_UPLOAD_FOLDER, filename))
            new_media = MediaModel(media_Path=os.path.join(MEDIA_UPLOAD_FOLDER, filename),
                                   article_id=new_article.id)
            db.session.add(new_media)

    db.session.commit()
    return jsonify(message='Article and media added successfully')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in blp.config['MEDIA_ALLOWED_EXTENSIONS']


