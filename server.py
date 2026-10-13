import os
from dotenv import load_dotenv
from fastapi import FastAPI
from x402_xrpl.server import require_payment

load_dotenv()

app = FastAPI(title="XRPL x402 Directory")

app.middleware("http")(
    require_payment(
        path="/directory",
        price=os.getenv("XRPL_PRICE_DROPS", "5000"),
        pay_to_address=os.getenv("XRPL_PAY_TO"),
        facilitator_url=os.getenv("XRPL_FACILITATOR_URL", "https://xrpl-facilitator-testnet.t54.ai"),
        network=os.getenv("XRPL_NETWORK", "xrpl:1"),
        asset="XRP",
        description="Curated list of XRPL x402 services",
        extra={"sourceTag": int(os.getenv("XRPL_SOURCE_TAG", "20260601"))},
    )
)

@app.get("/directory")
async def directory():
    return {
        "network": "XRPL",
        "updated": "2026-10-13",
        "note": "Static curated snapshot. Verify endpoints and prices before use. Expand as you discover more.",
        "services": [
            {
                "name": "Heurist Inference Router",
                "endpoint": "https://example-heurist-xrpl.placeholder",
                "approx_price": "sub-cent RLUSD or XRP",
                "category": "AI inference",
                "notes": "High-volume pay-per-call inference on XRPL via x402"
            },
            {
                "name": "Heurist Mesh",
                "endpoint": "https://example-heurist-mesh.placeholder",
                "approx_price": "RLUSD",
                "category": "AI tools / data",
                "notes": "Tool calls for token data, market summaries, DeFi metrics"
            },
            {
                "name": "AskSurf (market intelligence)",
                "endpoint": "https://example-asksurf.placeholder",
                "approx_price": "XRP",
                "category": "finance / research",
                "notes": "Per-request market questions with AI synthesis"
            },
            {
                "name": "ClawBank XRPL Gateway",
                "endpoint": "https://app.clawbank.co/x402",
                "approx_price": "RLUSD or XRP",
                "category": "gateway / catalog",
                "notes": "Exposes broader x402 catalog payable on XRPL"
            }
        ]
    }

@app.get("/health")
async def health():
    return {"status": "ok", "service": "xrpl-x402-directory"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))