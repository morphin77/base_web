import uvicorn
from base_web.application.app import app


def main():
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000
    )

if __name__ == "__main__":
    main()