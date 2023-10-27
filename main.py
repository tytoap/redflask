from flask import Flask, make_response, jsonify, redirect, render_template, request, url_for
 
 
  
 

app = Flask(__name__)

 
 



 
@app.route("/")
def hello_world():
    
    
   return "Hello"
 
         
  

        


        
 

if __name__ == '__main__':
 
  app.run()
 #app.run('localhost', 8080, debug=True)
