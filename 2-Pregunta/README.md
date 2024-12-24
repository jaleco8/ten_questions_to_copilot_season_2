🚀 **10 Preguntas a GitHub Copilot: Desarrollo de APIs Sencillas con Flask** 💡

🔍 **Pregunta 2**:  
*"Escribe una API REST básica usando Flask (Python) que tenga un solo endpoint `/saludo`. Este endpoint debe aceptar un parámetro `nombre` por GET y devolver un JSON con el mensaje 'Hola, [nombre]!'."*

[Ver Video](https://youtu.be/4v1z7k34AY8)

📜 **Por qué lo hacemos**:  
El objetivo es evaluar cómo la inteligencia artificial puede ayudarnos a construir aplicaciones web simples utilizando frameworks populares como Flask. Esto es especialmente útil para desarrolladores que buscan optimizar el tiempo y simplificar tareas repetitivas.

💻 **Código Generado por GitHub Copilot**:  
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saludo', methods=['GET'])
def saludo():
    nombre = request.args.get('nombre', 'Amigo')
    return jsonify({"mensaje": f"Hola, {nombre}!"})

if __name__ == '__main__':
    app.run(debug=True)
```

📡 **Prueba la API**:  
Ejecuta la aplicación y realiza una solicitud GET:  
`curl http://127.0.0.1:5000/saludo?nombre=Juan`

📈 **Beneficios**:  
1️⃣ Simplifica el desarrollo de endpoints básicos.  
2️⃣ Reduce errores comunes en la configuración inicial de Flask.  
3️⃣ Te permite enfocarte en la lógica de negocio y dejar que la IA haga el resto.