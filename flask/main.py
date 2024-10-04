from app import create_app

app = create_app()



if __name__ == '__main__':
   
    
        # Iniciar la aplicación Flask
        app.run(port=5000, debug=True)  # Asegúrate de usar el puerto 5000
    