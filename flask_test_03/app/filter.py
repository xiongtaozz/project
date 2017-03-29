from app import app


@app.add_template_filter
def allen(s):
    return s[:4]
