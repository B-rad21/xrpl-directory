from xrpl.wallet import Wallet
from x402_xrpl.clients.requests import x402_requests

wallet = Wallet.from_seed("shgxY7nsWTb6h2Qg4NRF6XdTbG1uK")
print("Using address:", wallet.classic_address)

session = x402_requests(
    wallet,
    rpc_url="https://s.altnet.rippletest.net:51234/",
    network_filter="xrpl:1",
    scheme_filter="exact",
)

resp = session.get("http://localhost:8000/directory", timeout=180)
print("Status:", resp.status_code)
print("Body:", resp.text)