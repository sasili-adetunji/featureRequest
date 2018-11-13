from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
from wtforms.widgets import TextArea
from ..models import User, ClientType, ProductAreaType


class FeatureForm(FlaskForm):

    """
    Form for admin to add or edit a request
    """

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description',render_kw={"rows": 10, "cols": 11},  widget=TextArea(), validators=[DataRequired()])
    client= SelectField("Client", choices=ClientType.choices(),)
    client_priority = IntegerField('Client Priority', validators=[DataRequired()])
    target_date = DateField('Target Date', format='%Y-%m-%d')
    product_area = SelectField("Product Area", choices=ProductAreaType.choices())
    submit = SubmitField('Submit')


