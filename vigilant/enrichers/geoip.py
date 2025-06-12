"""GeoIP mock - offline"""
def enrich_geoip(ip):
    # Mock, in prod call MaxMind
    if ip.startswith("8.8."):
        return {"country":"US","asn":"GOOGLE"}
    return {"country":"unknown","asn":"unknown"}
