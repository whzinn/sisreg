from flask import Flask, request
import cont
import os
import consulta

app = Flask(__name__)
app.debug=True

@app.route("/<cpf>")
def index(cpf):
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  
    ip = str(ip)
    ip = ip.replace(".","") 
    cont.cont(ip)
    data = consulta.consulta(cpf)
    return (data)
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
