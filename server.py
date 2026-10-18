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
        facilitator_url=os.getenv("XRPL_FACILITATOR_URL", "https://xrpl-facilitator-mainnet.t54.ai"),
        network=os.getenv("XRPL_NETWORK", "xrpl:0"),
        asset="XRP",
        description="Curated list of XRPL x402 services",
        extra={"sourceTag": int(os.getenv("XRPL_SOURCE_TAG", "20260601"))},
    )
)

@app.get("/directory")
async def directory():
    return {
        "network": "XRPL",
        "updated": "2026-10-18",
        "note": "Curated mix of ClawBank XRPL proxies and direct Heurist Mesh tools. Pay the listed amount to receive the full list.",
        "services": [
            {
                "name": "ClawBank Exa Search",
                "endpoint": "https://app.clawbank.co/x402/proxy/exa-search",
                "approx_price": "sub-cent RLUSD or XRP",
                "category": "web search",
                "notes": "Neural web search via ClawBank XRPL gateway"
            },
            {
                "name": "ClawBank Tavily Search",
                "endpoint": "https://app.clawbank.co/x402/proxy/tavily-search",
                "approx_price": "sub-cent RLUSD or XRP",
                "category": "web search",
                "notes": "AI-oriented web search via ClawBank XRPL gateway"
            },
            {
                "name": "ClawBank Token Price",
                "endpoint": "https://app.clawbank.co/x402/proxy/token-price",
                "approx_price": "sub-cent RLUSD or XRP",
                "category": "market data",
                "notes": "Token price lookup via ClawBank XRPL gateway"
            },
            {
                "name": "Heurist Project Search",
                "endpoint": "https://mesh.heurist.xyz/x402/xrpl/agents/AIXBTProjectInfoAgent/search_projects",
                "approx_price": "RLUSD",
                "category": "crypto research",
                "notes": "Direct Heurist Mesh tool — search crypto projects"
            },
            {
                "name": "Heurist Market Summary",
                "endpoint": "https://mesh.heurist.xyz/x402/xrpl/agents/AIXBTProjectInfoAgent/get_market_summary",
                "approx_price": "RLUSD",
                "category": "market data",
                "notes": "Direct Heurist Mesh tool — recent market summary"
            }
        ]
    }

@app.get("/health")
async def health():
    return {"status": "ok", "service": "xrpl-x402-directory"}

if __name__ == "__main__":