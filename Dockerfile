# Utiliser une image Python officielle
FROM python:3.9-slim

# Installer les dépendances
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copier le code source dans le conteneur
COPY . /app
WORKDIR /app

# Lancer l'application (par exemple Streamlit ou API Flask)
CMD ["streamlit", "run", "app/ui/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
