from sanic import Sanic
from sanic.response import json
from app.config import Config

Config.load_config()

app = Sanic(Config.get("APP_NAME"))

# Accessing environment variables
@app.get("/")
async def home(request):
    debug_mode = Config.get("DEBUG")
    return json({"message": "Hello, Sanic!", "debug": debug_mode})

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(Config.get("PORT", 8000)),
        debug=Config.get("DEBUG", "False").lower() == "true"
    )
