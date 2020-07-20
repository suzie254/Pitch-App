from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,RadioField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit') 

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')  

class PitchForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('1', 'Motivation'),  ('2', 'Promotion'),('3','Product')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create Pitch')  

class UpvoteForm(FlaskForm):
    '''
    Class to create a wtf form for upvoting a pitch
    '''
    submit = SubmitField('Upvote')     