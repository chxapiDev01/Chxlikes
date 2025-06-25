# chx_free_likes 🇮🇳

Simple Python wrapper for Free Fire Indian Like API by **Chx**.

## ⚡ Install

```bash
pip install chx_free_likes
```

## 🚀 Usage

```python
from chx_free_likes import ChxFreeLikes

api = ChxFreeLikes()
result = api.give_likes("8385763215")

print("Response:", result)

if api.is_success(result):
    print("✅ Likes given to", result.get("PlayerNickname"))
else:
    print("❌ Failed or already max likes reached.")
```

> Created with ❤️ by **Chx** for Indian Free Fire community 🇮🇳
