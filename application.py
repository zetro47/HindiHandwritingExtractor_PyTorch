from flask import Flask, request, jsonify, render_template


    
hindiLetters = ['क', 'ख', 'ग', 'घ',
 'ङ', 'च', 'छ',
 'ज', 'झ', 'ञ',
 'ट', 'ठ', 'ड',
 'ढ', 'ण', 'त',
 'थ', 'द', 'ध', 'न',
 'प', 'फ', 'ब', 'भ',
 'म', 'य', 'र', 'ल',
 'व', 'श', 'ष',
 'स', 'ह', 'character_34_chhya',
 'character_35_tra', 'character_36_gya' ,'0', '1', '2',
 '3', '4', '5','6', '7', '8' ,'9']

app = Flask(__name__)

@app.route('/tell',methods = ['GET'])
def home():
    return "hello"

if __name__ == "__main__":        
    app.run()

