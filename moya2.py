import base64

# Ganti dengan API Key Anda
api_key = "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"
encoded_key = base64.b64encode(api_key.encode("utf-8")).decode("utf-8")

print(encoded_key)
