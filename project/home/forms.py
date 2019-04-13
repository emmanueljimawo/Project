from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class FeatureRequestForm(FlaskForm):
    title = StringField(
        'Title', validators=[DataRequired(), Length(min=2, max=40)])
    description = TextAreaField(
        'Description', validators=[DataRequired()])
    client = SelectField('Client', choices=[('Client A', 'Client A'), (
        'Client B', 'Client B'), ('Client C', 'Client C')])
    client_priority = IntegerField(
        'Client Priority', validators=[NumberRange(min=1), DataRequired()])
    target_date = DateField('Target Date', validators=[DataRequired()])
    product_area = SelectField('Product Area', choices=[('Policies', 'Policies'), (
        'Billing', 'Billing'), ('Claims', 'Claims'), ('Reports', 'Reports')])
    submit = SubmitField('Add')
