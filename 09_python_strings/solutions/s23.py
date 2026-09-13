url = input("Enter a URL: ").strip()
valid_prefix = url.startswith("http://") or url.startswith("https://")
domain = url.split("://", 1)[1] if valid_prefix else ""
valid = valid_prefix and bool(domain) and " " not in url
print("Valid" if valid else "Invalid")
