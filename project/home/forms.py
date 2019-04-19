from datetime import date   #pragma: no cover
from flask_wtf import FlaskForm #pragma: no cover
from wtforms import StringField, TextAreaField, IntegerField, DateField, SelectField, SubmitField   #pragma: no cover
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError   #pragma: no cover


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

    def validate_target_date(form, target_date):
        if target_date.data < date.today():
            raise ValidationError('Date should be greater than today')
