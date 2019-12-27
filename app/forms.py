from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class PostNewsArticle(FlaskForm):
    heading = TextAreaField(u'News heading', validators=[
        DataRequired(), Length(min=1)])
    post = TextAreaField(u'News body', validators=[
        DataRequired(), Length(min=1)])
    submit = SubmitField('Submit News')

class CreateNewHuman(FlaskForm):
    slug = StringField('Slug', validators=[DataRequired()])
    group = StringField('Group', validators=[DataRequired()])
    full_name = StringField('Full name', validators=[DataRequired()])
    full_name_cz = StringField('Full name cz', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    telephone = StringField('Telephone')
    links = StringField('Links')
    ##ids = StringField('IDs')
    orcid = StringField('ORCID')
    researcher_id = StringField('Reasearcher id')
    scopus_id = StringField('SCOPUS id')
    about_text = StringField('Text about the person')
    submit = SubmitField('Create Human')