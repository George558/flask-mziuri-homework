from flask import Flask, render_template

app = Flask(__name__)

# List of programming languages
programming_languages = [
    {'name': 'Python', 'description': 'Python is a high-level, interpreted programming language known for its simplicity and readability.', 'link': 'https://www.python.org/'},
    {'name': 'JavaScript', 'description': 'JavaScript is a scripting language primarily used for adding interactivity to web pages.', 'link': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript'},
    {'name': 'Java', 'description': 'Java is a general-purpose, object-oriented programming language designed to have as few implementation dependencies as possible.', 'link': 'https://www.java.com/'},
    {'name': 'C++', 'description': 'C++ is a general-purpose programming language created as an extension of the C programming language.', 'link': 'https://www.cplusplus.com/'},
    {'name': 'Ruby', 'description': 'Ruby is a dynamic, object-oriented programming language designed for simplicity and productivity.', 'link': 'https://www.ruby-lang.org/'},
]

@app.route('/programming-languages')
def show_programming_languages():
    return render_template('programming_languages.html', programming_languages=programming_languages)

if __name__ == '__main__':
    app.run(debug=True)
