from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(_name_)

# Ye HTML design hai jo website par dikhega
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Earning Portal - Free Reward</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f7f6; text-align: center; padding: 50px; }
        .container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); display: inline-block; }
        input[type="email"] { padding: 10px; width: 250px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; }
        button { background: #28a745; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 16px; }
        button:hover { background: #218838; }
        .success { color: green; font-weight: bold; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Welcome to Reward Portal</h2>
        <p>Enter your email to claim your daily bonus!</p>
        <form method="POST">
            <input type="email" name="email" placeholder="Enter your email..." required><br>
            <button type="submit">Claim Now</button>
        </form>
        {% if success %}
            <p class="success">Congratulations! Your reward request has been submitted.</p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    success = False
    if request.method == "POST":
        email = request.form.get("email")
        # Yahan aap email ko database ya file mein save kar sakte hain
        print(f"New User Registered: {email}")
        success = True
    return render_template_string(HTML_PAGE, success=success)

if _name_ == "_main_":
    app.run(debug=True)
