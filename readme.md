# QuantAgri Notes Broadcaster

Auto-posts daily commodity updates to your QuantAgri Substack via Cloud Run API.

## Setup
1. Fork/create repo
2. Settings → Secrets → Add `API_KEY` (if your API requires it)
3. Push → Watch Actions tab for runs

## Local Test
```bash
pip install -r requirements.txt
python broadcast.py soy
