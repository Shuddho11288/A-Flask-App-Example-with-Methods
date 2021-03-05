from flask import Flask, request
import math,cmath
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"
@app.route('/funnysite', methods=['GET','POST'])
def lollollol():
    if request.method == 'POST':
        return "Apnar submissionti vul hoyeche ajonno apnake www.pagol.com e 10000$ taka jorimana dite hbe.\nDhonnobad."
    return"""
				  <form method="post">
                  <label for="name" class="leading-7 text-sm text-gray-600">নাম</label>
                  <input type="text" id="name" name="name" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
                </div>
              </div>
              <div class="p-2 w-1/2">
                <div class="relative">
                  <label for="email" class="leading-7 text-sm text-gray-600">ই-মেইল</label>
                  <input type="email" id="email" name="email" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
                </div>
              </div>
              <div class="p-2 w-full">
                <div class="relative">
                  <label for="message" class="leading-7 text-sm text-gray-600">মেসেজ</label>
                  <textarea id="message" name="message" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"></textarea>
                </div>
              </div>
              <div class="p-2 w-full">
                <button class="flex mx-auto text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg" type="submit">মেসেজ পাঠান</button>
              </div>
				  </form>
"""

@app.route('/wishdoc')
def lollol():
    return """<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<style>
	body{
		background-color: aqua;
	}
	footer{
		background-color: aliceblue;
		padding: 50px;
	}
	div{
		background-color: lightblue;
	}
	p{
		color: black;
		background-color: white;
	}

</style>
<body>
<div class="container">
</em></a>
<div>
  <h2><strong><u>PAGE: WISH DOCUMANTATION</u></strong></h2>
</div>
<a href="http://shuddho.pythonanywhere.com/wish/Shuddho"><em>
<div><em>Wish from Tasawar Ahmed Shuddho!</em></div>
<iframe width="700" height="500" src="http://shuddho.pythonanywhere.com/wish/Shuddho"></iframe>
</em></a>
<div>
  <p>Here you can see a link below at the frame's end. That is the link for creating your wish! Custom wish will be available soon!</p>
  <p>LINK = <a href="http://shuddho.pythonanywhere.com/wish/Shuddho" rel="nofollow noopener" role="link" tabindex="0" target="_blank">http://shuddho.pythonanywhere.com/wishform</a></p>
  <p>And the whole thing is free also!</p>
</div>
<iframe src="http://shuddho.pythonanywhere.com/wishform" width="700" height="500"></iframe>
<div>
  <p>Here you just fill up the form! And click on submit. You get a link in a moment! Just copy it and share with your friends! :)  </p>
  <p>And yes if you need any help from us send an email at<em><strong> tasawarshuddho@gmail.com</strong></em> !</p>
</div>
<footer>
Thanks For Your Support!
</footer>
</div>

</body>"""

@app.route('/home')
def hello2():
    return hello()
@app.route('/wish/<username>')
def wisher(username):
    return f"<style>.co"+"{background-image: linear-gradient(to right, lightgreen , lightyellow);padding: 50px;color: white;}</style>"+f"<h3 class=\"co\">{username} is wishing you a happy life!</h3>\n<img src=\"https://hotemoji.com/images/dl/f/happy-emoji-by-google.png\"><a href=\"http://Shuddho.pythonanywhere.com/wishform\">Click here to make your one!</a>"
@app.route('/calculator', methods= ['GET','POST'])
def calculatorpage():
    if request.method == 'POST':
        var =request.form['scr']
        try:
            var = str(var).replace("x","*")
            var = str(var).replace("^","**")
            var = str(var).replace("%","/100")
            result = eval(str(var), {"math":math,"cmath":cmath})
            result = str(result).replace("j","i")


        except Exception as e:
            return f"{e}"
        html = f"""
        {var} = {result}
        """
        return html
    else:
        print(request.method)
        html = """
        <form  method="post">
    <input class="form-group" type="text" name="scr" placeholder="Enter your math expression">
    <input type="submit">
    </form>
    """
        return html


@app.route('/wishform', methods=['GET','POST'])
def handle_data():
    global projectpath
    projectpath = ""
    if request.method == 'POST':
        projectpath = request.form['projectFilepath']
        return f"<style>.co"+"{background-image: linear-gradient(to right, blue , green);padding: 50px;color: white;}</style>"+f"<div class=\"co\">LINK= http://Shuddho.pythonanywhere.com/wish/{projectpath}</div><h3>Share it with others!</h3>"
    return f"""<style>
    form"""+"{"+f"""
        background-image: linear-gradient(to right, lightblue , lightgreen);
        padding: 50px;
    """+"}"+f"""
</style>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<div class="container">
<h2>Enter your name and click submit to generate your link!</h2>
<form  method="post">
    <input class="form-group" type="text" name="projectFilepath" value={projectpath}>
    <input type="submit">
</form>
</div>"""



if __name__ == '__main__':
    app.run()

