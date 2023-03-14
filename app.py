from flask import Flask, render_template, request, jsonify

from codedwords import *

app = Flask(__name__, template_folder='.')
messages = []
todo = []
type = []
go = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    messages.append(message)
    response = ''
    #runs the program withe the keyword
    if message == '/start':
        response =  'Choose encryption type /ceasar, /play, /poly'
        return jsonify({'response': response})
    elif messages[-2] == '/start':
        response = typesCode(message)
        return jsonify({'response': response})
    
    elif message == '1':      
        if(len(type) != 0 ):
            todo.append('1')
            response =  messages[-2]+' (ENCRYPTION)Enter the key and code ex. code,key'
            return jsonify({'response': response})
    elif message == '2':
        if(len(type) != 0 ):
            todo.append('2')
            response =  messages[-2]+' (DECRYPTION)Enter the key and code ex. code,key'
            return jsonify({'response': response})
    elif len(todo) != 0:
        response = encryptCode(message)
        return jsonify({'response': response})
    #defaults the proram
    else:
        response = basic_response(message+'')
        return jsonify({'response': response})


#Diffirent types 
def typesCode(message):
    if message == '/ceasar':
       type.append('1') 
       response = 'Enter the number (1)Encrypt or (2)Decrypt'  
       return response
    elif message == '/poly':
        response = 'Enter the number (1)Encrypt or (2)Decrypt' 
        type.append('2')
        return response
    elif message == '/play':
        response = 'Enter the number (1)Encrypt or (2)Decrypt' 
        type.append('3')
        return response
    elif message == '/help':
        response = 'Enter the number (1)Encrypt or (2)Decrypt' 
        type.append('4')
        response = 'sayup' 
        return response
    else:
        return 'invalid! exiting...'




def basic_response(message):
    # define your predefined responses here
    todo.clear()
    type.clear()
    messages.clear()
    if message == 'hello':
        return 'Hi there!'
    elif message == 'how are you?':
        return 'I am doing well, thank you!'
    elif message == 'what is your name?':
        return 'My name is FlaskBot. Nice to meet you!'
    else:
        return 'I am sorry, I do not understand what you are saying.'


#todos (encrypt or decryption)
def encryptCode(message):
    words = message.split(',')
    key = words[1]
    code = words[0]
    if(len(words)==2):
        if(todo[-1] == '1'):
        #ENCRYPT
            if(type[-1] == '1'):
                todo.clear()
                type.clear()
                return 'The Ceasar Encrypted code: '+Ceasar(code,int(key))
            elif(type[-1] == '2'):
                todo.clear()
                type.clear()
                return 'The Polyalphabetic Encrypted code: '+Polyalphabetic(code,key,1)
            elif(type[-1] == '3'):
                todo.clear()
                type.clear()
                return 'The Encrypted code:  '
            else:
                todo.clear()
                type.clear()
                return 'invalid! exiting...'

        #DECRYPT   
        elif(todo[-1] == '2'):
            if(type[-1] == '1'):
                todo.clear()
                type.clear()
                return 'The Ceasar Decrypted code: '+Ceasar(code,int(key)* -1)
            elif(type[-1] == '2'):
                todo.clear()
                type.clear()
                return 'The Polyalphabetic Decrypted code: '+Polyalphabetic(code,key,-1)
            elif(type[-1] == '3'):
                todo.clear()
                type.clear()
                return 'The Decrypted code: '
            else:
                todo.clear()
                type.clear()
                return 'invalid! exiting...'
        else:
            todo.clear()
            type.clear()
            return 'invalid! exiting...'
    else:
        todo.clear()
        type.clear()
        return 'invalid! exiting...'

  
  


if __name__ == '__main__':
    app.run(debug=True)
