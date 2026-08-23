const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const Razorpay = require('razorpay');
const crypto = require('crypto');

dotenv.config();

const app = express();
const PORT = process.env.PORT || 8000;

// Enable CORS for all origins or specific frontend
app.use(cors({
    origin: '*',
    methods: ['GET', 'POST', 'OPTIONS'],
    allowedHeaders: ['Content-Type', 'Authorization']
}));

app.use(express.json());

// Initialize Razorpay client
const razorpay = new Razorpay({
    key_id: process.env.RAZORPAY_KEY_ID || '',
    key_secret: process.env.RAZORPAY_KEY_SECRET || ''
});

// Fixed Internship Program Price (₹2,599 in paise)
const INTERNSHIP_PRICE_PAISE = 259900;

// 1. Health check endpoint
app.get('/', (req, res) => {
    res.json({
        service: 'OmniIDE Payment Gateway Backend',
        status: 'online',
        timestamp: new Date().toISOString(),
        razorpay_configured: Boolean(process.env.RAZORPAY_KEY_ID && process.env.RAZORPAY_KEY_SECRET)
    });
});

app.get('/api/health', (req, res) => {
    res.json({ status: 'ok', uptime: process.uptime() });
});

// 2. Create Razorpay Order (Secure server-side order generation)
app.post('/api/create-order', async (req, res) => {
    try {
        const { name, email, phone, role, institution, status } = req.body;

        if (!name || !email || !phone || !role) {
            return res.status(400).json({
                success: false,
                error: 'Missing mandatory registration fields (name, email, phone, role).'
            });
        }

        if (!process.env.RAZORPAY_KEY_ID || !process.env.RAZORPAY_KEY_SECRET) {
            return res.status(500).json({
                success: false,
                error: 'Razorpay API credentials not configured in environment variables.'
            });
        }

        const receiptId = `omni_${Date.now().toString().slice(-8)}_${Math.floor(100 + Math.random() * 900)}`;

        const orderOptions = {
            amount: INTERNSHIP_PRICE_PAISE, // 259900 paise = ₹2,599.00
            currency: 'INR',
            receipt: receiptId,
            notes: {
                program: '3-Month Industry Internship',
                candidate_name: String(name).slice(0, 40),
                candidate_email: String(email).slice(0, 50),
                candidate_phone: String(phone).slice(0, 20),
                selected_track: String(role).slice(0, 40),
                college: String(institution || 'N/A').slice(0, 50),
                year_experience: String(status || 'N/A').slice(0, 30)
            }
        };

        const order = await razorpay.orders.create(orderOptions);

        return res.status(200).json({
            success: true,
            orderId: order.id,
            amount: order.amount,
            currency: order.currency,
            keyId: process.env.RAZORPAY_KEY_ID
        });
    } catch (err) {
        console.error('Error creating Razorpay order:', err);
        return res.status(500).json({
            success: false,
            error: err.message || 'Failed to create Razorpay order'
        });
    }
});

// 3. Verify Payment Signature (Cryptographic HMAC SHA-256 verification)
app.post('/api/verify-payment', (req, res) => {
    try {
        const {
            razorpay_order_id,
            razorpay_payment_id,
            razorpay_signature,
            candidate
        } = req.body;

        if (!razorpay_order_id || !razorpay_payment_id || !razorpay_signature) {
            return res.status(400).json({
                success: false,
                error: 'Missing required Razorpay payment verification fields.'
            });
        }

        const secret = process.env.RAZORPAY_KEY_SECRET;
        if (!secret) {
            return res.status(500).json({
                success: false,
                error: 'Razorpay Key Secret is missing on server.'
            });
        }

        // Generate expected signature
        const expectedSignature = crypto
            .createHmac('sha256', secret)
            .update(`${razorpay_order_id}|${razorpay_payment_id}`)
            .digest('hex');

        const isSignatureValid = expectedSignature === razorpay_signature;

        if (!isSignatureValid) {
            return res.status(400).json({
                success: false,
                error: 'Invalid payment signature. Payment verification failed.'
            });
        }

        const refId = `OMNI-INT-2026-${Math.floor(1000 + Math.random() * 9000)}`;

        console.log(`[PAYMENT VERIFIED] Order: ${razorpay_order_id}, Payment: ${razorpay_payment_id}, Ref: ${refId}`);

        return res.status(200).json({
            success: true,
            verified: true,
            refId: refId,
            paymentId: razorpay_payment_id,
            orderId: razorpay_order_id,
            message: 'Payment verified successfully.'
        });
    } catch (err) {
        console.error('Error verifying payment:', err);
        return res.status(500).json({
            success: false,
            error: err.message || 'Internal server error during payment verification'
        });
    }
});

app.listen(PORT, () => {
    console.log(`OmniIDE Payment Backend running on port ${PORT}`);
});
