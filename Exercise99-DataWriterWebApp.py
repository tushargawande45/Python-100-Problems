# write a program that asks the user to submit text through a web app

from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Text Submission</title>
</head>
<body>
    <h2>Submit Your Text</h2>
    <form method="post">
        <textarea name="user_text" rows="4" cols="50"></textarea><br>
        <input type="submit" value="Submit">
    </form>
    {% if submitted_text %}
        <h3>You submitted:</h3>
        <p>{{ submitted_text }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def submit_text():
    submitted_text = None
    if request.method == "POST":
        submitted_text = request.form.get("user_text")
    return render_template_string(HTML_TEMPLATE, submitted_text=submitted_text)

if __name__ == "__main__":
    app.run(debug=True)
