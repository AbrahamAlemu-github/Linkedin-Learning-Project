import openai
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, static_url_path="/static")


class LLMModel:
    def __init__(self):
        self.api_key = "[insert key]"  # Replace with your actual OpenAI API key

    def evaluate(self, code, instructions):
        openai.api_key = self.api_key

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {
                        "role": "user",
                        "content": f"Evaluate the following code based on these instructions:\n\nInstructions: {instructions}\n\nCode:\n{code}\n\nProvide a score out of 100 and give a brief explanation. Do not give the correct answer.",
                    },
                ],
                max_tokens=300,
                temperature=0.5,
            )
            feedback = response.choices[0].message["content"].strip()
            score = self.extract_score(feedback)
            return {"feedback": feedback, "score": score}
        except Exception as e:
            return {"feedback": f"Error evaluating code: {str(e)}", "score": 0}

    def extract_score(self, feedback):
        score_line = [line for line in feedback.split("\n") if "Score:" in line]
        if score_line:
            score = score_line[0].split(":")[1].strip().split("/")[0]
            return int(score)
        return 0


model = LLMModel()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/myprofile")
def myprofile():
    return render_template("myprofile.html")


@app.route("/page1")
def page1():
    return render_template("page1.html")


@app.route("/part1")
def part1():
    return render_template("part1.html")


@app.route("/part2")
def part2():
    return render_template("part2.html")


@app.route("/basic-java-course")
def basic_java_course():
    return render_template("basic-java-course.html")


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username == "rroslansky@linkedin.com" and password == "helloworld":
        return jsonify({"redirect": url_for("page1")})
    else:
        return jsonify({"error": "Invalid username or password"}), 401


@app.route("/evaluate", methods=["POST"])
def evaluate_code():
    data = request.get_json()
    code = data["code"]
    instructions = data["instructions"]
    result = model.evaluate(code, instructions)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
