import uvicorn
from bot import app
from bot import port

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port = int(port))
