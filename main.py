from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/amstrong/<int:n>')

def amstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10

    if (sum == copy_n):
        print(f"{copy_n} is an amstrong number")
        result ={
            "Number": copy_n,
            "Amstrong": True,
            "Server IP": "122.234.213.53"
        }
    else:
        print(f"{copy_n} is not an amstrong number")
        result = {
            "Number": copy_n,
            "Amstrong": False,
            "Server IP": "122.234.213.53"
        }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
