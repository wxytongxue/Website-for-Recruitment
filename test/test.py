from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'hello word!',200
if __name__=='__main__'
    app.run()
