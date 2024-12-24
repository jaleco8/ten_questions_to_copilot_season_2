# API Flask

Este proyecto es una API simple creada con Flask que devuelve un saludo.

## Requisitos

- Python 3.x
- Flask

## Instalación

1. Clona este repositorio:
    ```sh
    git clone git@github.com:jaleco8/ten_questions_to_copilot_season_2.git
    cd 2-Pregunta
    ```

2. Crea un entorno virtual (opcional pero recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install Flask
    ```

## Ejecución

Para ejecutar el script [api_flask.py](http://_vscodecontentref_/0), usa el siguiente comando:
  ```sh
  python 2-Pregunta/api_flask.py
  ```

La API estará disponible en http://127.0.0.1:5000/saludo.

## Uso

Para obtener un saludo, realiza una solicitud GET a la ruta /saludo con un parámetro opcional nombre. Ejemplo:

  ```curl http://127.0.0.1:5000/saludo?nombre=Juan```

La respuesta será un JSON con el mensaje de saludo.

  ```
  {
      "mensaje": "Hola Juan!"
  }
  ```
