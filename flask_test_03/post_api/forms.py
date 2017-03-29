from flask_wtf.form import Form
import wtforms


class AddPostForm(Form):
    title = wtforms.StringField('title', [wtforms.validators.length
                                          (min=1, max=200)])
    content = wtforms.StringField('content', [wtforms.validators.length
                                          (min=1, max=200)])