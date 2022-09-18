import uvicorn
import colorama


if __name__ == "__main__":
    colorama.init()
    uvicorn.run("app:app", port=8080, log_level="info")
