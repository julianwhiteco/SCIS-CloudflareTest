import ipwhois
import dns.resolver

domain = input("Enter domain to check: https://")

url_loadup = dns.resolver.resolve(domain, 'A')
url_whois = ipwhois.IPWhois(url_loadup[0].to_text()).lookup_whois()["nets"][0]["description"]

cdn = ["Cloudflare, Inc."]

if url_whois in cdn:
    print('CloudFlare present on', domain)
else:
    print('CloudFlare not present, found', url_whois)

input("Press enter to exit.")
