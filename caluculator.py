from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Button Calculator</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                height: 100vh;
            }}
            .container {{
                background: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                text-align: center;
                width: 300px;
                margin-bottom: 20px;
            }}
            h1 {{
                margin-bottom: 20px;
                color: #007bff;
            }}
            .screen {{
                width: 100%;
                height: 50px;
                margin-bottom: 20px;
                font-size: 20px;
                text-align: right;
                padding: 5px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f9f9f9;
                box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
            }}
            .buttons {{
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 10px;
            }}
            button {{
                background-color: #007bff;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
            }}
            button:hover {{
                background-color: #0056b3;
            }}
            button.operator {{
                background-color: #ffc107;
            }}
            button.operator:hover {{
                background-color: #e0a800;
            }}
            button.clear {{
                background-color: #dc3545;
            }}
            button.clear:hover {{
                background-color: #bd2130;
            }}
            footer {{
                font-size: 14px;
                color: #66;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Calculator</h1>
            <form method="post">
                <input type="text" name="screen" class="screen" value="{screen_value}" readonly>
                <div class="buttons">
                    <button type="submit" name="button" value="7">7</button>
                    <button type="submit" name="button" value="8">8</button>
                    <button type="submit" name="button" value="9">9</button>
                    <button type="submit" name="button" value="/">÷</button>

                    <button type="submit" name="button" value="4">4</button>
                    <button type="submit" name="button" value="5">5</button>
                    <button type="submit" name="button" value="6">6</button>
                    <button type="submit" name="button" value="*">×</button>

                    <button type="submit" name="button" value="1">1</button>
                    <button type="submit" name="button" value="2">2</button>
                    <button type="submit" name="button" value="3">3</button>
                    <button type="submit" name="button" value="-">-</button>

                    <button type="submit" name="button" value="0">0</button>
                    <button type="submit" name="button" value=".">.</button>
                    <button type="submit" name="button" value="=">=</button>
                    <button type="submit" name="button" value="+">+</button>

                    <button type="submit" name="button" value="C" class="clear">C</button>
                </div>
            </form>
        </div>
        <footer>
            Developed by S naveen kumar odinschool, Yelloti
        </footer>
    </body>
    </html>
    """

    # Default screen value
    screen_value = ""

    # Process button clicks
    if request.method == "POST":
        button = request.form.get("button")
        screen_value = request.form.get("screen", "")

        if button == "C":  # Clear screen
            screen_value = ""
        elif button == "=":  # Evaluate the expression
            try:
                screen_value = str(eval(screen_value))
            except Exception:
                screen_value = "Error"
        else:  # Append button value to screen
            screen_value += button

    return html_code.format(screen_value=screen_value)


if __name__ == "__main__":
    app.run(debug=True)
