from gmms import create_app

# Create an instance of the app using the factory function
app = create_app()

if __name__ == '__main__':
    # Run the application with debugging enabled to facilitate development
    app.run(debug=True)
