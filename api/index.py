from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 193.07,
    "uptime_pct": 97.315,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 124.33,
    "uptime_pct": 97.29,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 168.8,
    "uptime_pct": 98.8,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 203.16,
    "uptime_pct": 99.323,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 134.96,
    "uptime_pct": 99.17,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 123.55,
    "uptime_pct": 98.777,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 146.5,
    "uptime_pct": 97.139,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 202.95,
    "uptime_pct": 98.19,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 124.53,
    "uptime_pct": 98.28,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 196.43,
    "uptime_pct": 98.461,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 147.9,
    "uptime_pct": 98.374,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 179.34,
    "uptime_pct": 98.877,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 111.62,
    "uptime_pct": 97.639,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 151.71,
    "uptime_pct": 97.49,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 169.48,
    "uptime_pct": 98.131,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 218.66,
    "uptime_pct": 99.334,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 183.39,
    "uptime_pct": 98.264,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 169.58,
    "uptime_pct": 98.039,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 163.36,
    "uptime_pct": 97.943,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 220.35,
    "uptime_pct": 99.369,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 190.66,
    "uptime_pct": 98.581,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 143.83,
    "uptime_pct": 98.361,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 104.33,
    "uptime_pct": 99.188,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 188.22,
    "uptime_pct": 97.582,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 222.02,
    "uptime_pct": 97.319,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 205.11,
    "uptime_pct": 97.582,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 160.85,
    "uptime_pct": 97.118,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 116.39,
    "uptime_pct": 99.174,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 185.72,
    "uptime_pct": 98.169,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 169.32,
    "uptime_pct": 97.668,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 217.96,
    "uptime_pct": 97.716,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 196.53,
    "uptime_pct": 97.677,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 146.53,
    "uptime_pct": 98.732,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 220.57,
    "uptime_pct": 98.904,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 143.46,
    "uptime_pct": 97.321,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 168.87,
    "uptime_pct": 97.786,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
