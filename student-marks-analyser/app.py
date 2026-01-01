from flask import Flask,render_template,request

app = Flask(__name__)
# creating Flask app object; __name__ helps Flask locate this app and its files
 

@app.route("/")
def welcome():
    return "<h1>welcome to home page</h1>"

# maps the root URL (/) to the welcome() function and returns HTML to the browser

@app.route("/index")
def welcome1():
    return "<h1>welcome to index page</h1>"
@app.route("/form",methods=["GET","POST"]) #HTTP METHODS SHOULD BE UPPERCASE
# handles both displaying the form (GET) and processing submitted data (POST)
def cal():
    if request.method=="GET":
        return render_template("form.html")
    else:
        try:
           maths = float(request.form.get('maths'))
           science = float(request.form.get('science'))
           sst = float(request.form.get('sst'))
        # reads and converts form input values from string to float
       
           average_marks=(maths+science+sst)/3
       # calculates the average of the entered marks
           return render_template('form.html',score=average_marks)#score=average_marks maps a Python variable to a template variable; the names don’t have to be the same.
        except ValueError:
            return render_template("erro.html")
      # sends the calculated result back to the template
    """This route displays a form using GET and processes user input using POST, performs backend logic, and returns the result to the same page"""
if __name__=="__main__":
    #ensures the Flask server runs only when the file is executed directly, not when imported.
    app.run(debug=True)