import base64

# Ganti dengan API Key Anda
api_key = "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"
encoded_key = base64.b64encode(api_key.encode("utf-8")).decode("utf-8")

print(encoded_key)
