import base64

# Ganti dengan API Key Anda
api_key = "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"
encoded_key = base64.b64encode(api_key.encode("utf-8")).decode("utf-8")

print(encoded_key)
