import logging

from flask import Flask, request, make_response, render_template

from kanji_grade_alignment_tool import furigana_html, basic_text

application = Flask(__name__, template_folder='templates', static_url_path='', static_folder='static', )
application.config["EXPLAIN_TEMPLATE_LOADING"] = True

@application.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        message = "Hello, World"
        return render_template('index.html', message=message)
    else:
        grade = request.form.get("grade")
        text = request.form.get("document")
        logging.info("Received request {}".format(text))

        if request.form.get("output_type") == "furigana":
            ret = furigana_html(text, int(grade))
        else:
            ret = basic_text(text, int(grade))

        ret = "<br />".join(ret.split("\n"))
        return render_template('index.html', message=ret, grade=grade, text=text, output_type=request.form.get("output_type"))


# run the application
if __name__ == "__main__":
    application.run(debug=True)
