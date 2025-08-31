# Arquitectura Limpia - Python FastAPI

## Requisitos
- Python 3.8+
- pip

## Instalación del entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

## Instalación de dependencias

```bash
pip install fastapi uvicorn[standard] pydantic
```

## Ejecución del servidor

```bash
python main.py
```

El servidor estará disponible en: http://127.0.0.1:8000

Puedes probar los endpoints y la documentación interactiva en: http://127.0.0.1:8000/docs

---

Estructura basada en arquitectura limpia.
