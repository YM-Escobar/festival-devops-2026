# Festival DevOps Music Fest

## BADGE DE ESTADO

## Descripción

Proyecto desarrollado para la actividad de aprendizaje de Git y GitHub del programa DevOps y Contenedores (Docker). El proyecto simula la gestión de un festival musical utilizando un frontend web y un backend desarrollado con Flask.

## Tecnologías Utilizadas

* HTML5
* CSS3
* Python
* Flask
* Docker
* Docker Compose
* Git
* GitHub

## Estructura del Proyecto

```text
festival-devops/
├── frontend/
│   ├── index.html
│   └── style.css
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Control de Versiones

Para el desarrollo del proyecto se utilizaron las siguientes ramas:

* main
* feature-landing
* feature-backend

Posteriormente las ramas fueron fusionadas mediante merge para integrar todos los cambios en la rama principal.

## Ejecución del Proyecto

1. Clonar el repositorio.
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar:

```bash
docker compose up --build
```

4. Acceder a la aplicación desde el navegador.

## Autor

Yeiner Stainer Moreno Escobar

Actividad de Aprendizaje #6 - Git y GitHub
SENA - DevOps y Contenedores (Docker)