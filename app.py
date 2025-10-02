from flask import Flask, render_template, request, redirect, url_for

# 1. Initialize the Flask application
app = Flask(__name__)

# 2. Define the main route (Home Page)
@app.route('/')
def index():
    """Renders the main portfolio page."""
    # The render_template function automatically looks inside the 'templates' folder
    return render_template('index.html', title='My Portfolio', name='Your Name')

# 3. Define the Contact Form route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get the data submitted from the form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # TODO: Implement logic here to send the email or store the message.
        # For now, we'll just print it.
        print(f"New Contact Submission - Name: {name}, Email: {email}, Message: {message}")

        # Redirect the user to prevent form resubmission and show a "thank you"
        # The url_for function looks up the URL for the 'index' function.
        return redirect(url_for('index'))
    
    # If the request method is GET, just show the contact form (or the home page with the form on it)
    return render_template('index.html', title='Contact Me')


# 4. Run the application
if __name__ == '__main__':
    # Setting debug=True is helpful during development as it reloads the server on code changes
    app.run(debug=True)