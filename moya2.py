import base64

# Ganti dengan API Key Anda
api_key = "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"
encoded_key = base64.b64encode(api_key.encode("utf-8")).decode("utf-8")

print(encoded_key)
