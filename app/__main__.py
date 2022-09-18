import uvicorn
import colorama


if __name__ == "__main__":
    colorama.init()
    uvicorn.run("app:app", port=80, log_level="info")
