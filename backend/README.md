# OmniIDE Payment & Internship Backend

Node.js / Express microservice for creating server-side Razorpay orders and verifying payment HMAC signatures.

---

## 🚀 How to Deploy on Railway (Step-by-Step)

1. Log in to [Railway.app](https://railway.app/).
2. Click **+ New Project** → **Deploy from GitHub Repo**.
3. Select this repository (`Omni-landing-page` or your repo).
4. In the Railway Service settings:
   - Go to **Settings** → **Root Directory** → Set it to `/backend`.
5. Go to the **Variables** tab in Railway and add:
   - `RAZORPAY_KEY_ID`: `rzp_live_TKoC4DwlGTAk8b`
   - `RAZORPAY_KEY_SECRET`: *(Your secret key from Razorpay Dashboard)*
   - `PORT`: `8000` (or leave default)
6. Railway will automatically deploy the service and assign you a live URL (e.g. `https://omni-payment-production.up.railway.app`).
7. Copy that Railway URL and add it to your frontend (or link your custom subdomain like `https://api.omniide.com`).

---

## 📡 API Endpoints

- `GET /` — Health check status
- `POST /api/create-order` — Creates a verified ₹2,599 Razorpay order ID
- `POST /api/verify-payment` — Verifies HMAC SHA-256 payment signature
