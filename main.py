import uvicorn
from app.input.controllers.usuario_controller import app

if __name__ == "__main__":
    uvicorn.run("app.input.controllers.usuario_controller:app", host="127.0.0.1", port=8000, reload=True)
