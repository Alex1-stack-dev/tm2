from fastapi import FastAPI, Request, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security.api_key import APIKeyHeader
import uvicorn
import ssl
import logging

app = FastAPI()
API_KEY = "YOUR_SECRET_API_KEY"  # Load securely in real scenarios
api_key_header = APIKeyHeader(name="X-API-Key")

# -- Log ALL HTTP Requests --
logging.basicConfig(filename="access.log", level=logging.INFO)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"{request.method} {request.url} {request.client.host}")
    return await call_next(request)

# -- Auth Dependency --
async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")

# -- PII Redaction for meet endpoint --
@app.get("/live_results", dependencies=[Depends(verify_api_key)])
async def live_results():
    # Redact sensitive fields; don't send birthdates etc.
    results = [{
        "athlete": {"name": r["athlete"]["name"], "team": r["athlete"]["team"]},
        # OMIT DOB or sensitive
        "event": r.get("event"),
        "result": r.get("result"),
    } for r in get_results_from_db()]
    return JSONResponse(content=results)

# -- Enable HTTPS (self-signed for local)
if __name__ == "__main__":
    ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_ctx.load_cert_chain("cert.pem", "key.pem")  # Generate self-signed if needed
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_context=ssl_ctx)

# Helper
def get_results_from_db():
    # Replace with actual db queries
    return [{
        "athlete": {"name": "Jane Smith", "team": "Sharks", "dob": "2006-08-12"},
        "event": "50 Free", "result": "28.45"
    }]
