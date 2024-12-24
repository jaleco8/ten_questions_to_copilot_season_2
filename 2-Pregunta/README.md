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

📌 *Esta es la segunda entrega de "10 Preguntas a GitHub Copilot", donde exploramos cómo la IA puede transformar nuestras prácticas de desarrollo. ¡No te pierdas los siguientes episodios!*

#APIs hashtag#Python hashtag#Flask hashtag#InteligenciaArtificial hashtag#DesarrolloDeSoftware hashtag#GitHubCopilot hashtag#GitHubLATAM

---

🔍 **Soy Jesús León**, apasionado por el liderazgo técnico, la innovación tecnológica y la inteligencia artificial. En mis publicaciones comparto estrategias prácticas para liderar equipos, adoptar tecnologías emergentes y alinear la tecnología con la estrategia empresarial.  

💡 ¿Te interesan temas como #LiderazgoTecnológico, #InteligenciaArtificial o #ProyectosTecnológicos? Sigue mi perfil 👉 @jaleco8 para no perderte contenido valioso sobre IA, desarrollo de software y gestión estratégica.

> Si consideras útil esta información, apóyalo haciendo "★ Star" en el repositorio. ¡Gracias 🙌!