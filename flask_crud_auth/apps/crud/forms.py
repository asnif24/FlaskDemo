from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, length


class UserForm(FlaskForm):
    username = StringField(
        "使用者名稱",
        validators=[
            DataRequired(message="必填使用者名稱"),
            length(max=30, message="no more than 30"),
        ],
    )

    email = StringField(
        "電子郵件",
        validators=[DataRequired(message="必填email"), Email(message="請依照email格式")],
    )

    password = PasswordField("密碼", validators=[DataRequired(message="必填密碼")])

    submit = SubmitField("提交表單")
