# Defraudo - AI-Powered Fraud Detection System

## 📌 Overview

Defraudo is an AI-powered fraud detection system designed to analyze digital transactions in real-time and detect fraudulent activities. The system leverages **machine learning** for fraud detection, **Node.js** for backend processing, and **React Native** for the frontend.

## 🚀 Features

- **Real-time Fraud Detection** using AI models.
- **Razorpay Payment Integration** for seamless transactions.
- **Location-based Transaction Verification.**
- **Device ID Tracking** for user identification.
- **Secure Payment Verification** using Razorpay Signature Validation.

## 🛠️ Tech Stack

- **Frontend:** React Native
- **Backend:** Node.js, Express.js
- **Database:** MongoDB
- **Payment Gateway:** Razorpay
- **Machine Learning:** Python (For AI Model)

## 📂 Project Structure

```
Defraudo/
│── client/          # React Native Frontend
│── server/          # Node.js Backend
│── ml-model/        # Fraud Detection AI Model
│── README.md        # Project Documentation
│── .env             # Environment Variables
│── package.json     # Dependencies
```

## 📌 Installation & Setup

### 🔹 Prerequisites

- **Node.js** (v16+ recommended)
- **MongoDB** (Installed & Running)
- **Razorpay Account**

### 🔹 Backend Setup

```bash
git clone https://github.com/your-username/defraudo.git
cd defraudo/server
npm install
```

### 🔹 Configure Environment Variables

Create a `.env` file inside the `server/` directory and add:

```env
PORT=7000
MONGO_URI=your_mongodb_connection_string
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret
```

### 🔹 Start the Server

```bash
npm start
```

### 🔹 Frontend Setup

```bash
cd ../client
npm install
npm start
```

## 📌 API Endpoints

### 🔹 **Create Razorpay Order**

**Endpoint:** `POST /api/razorpay/order`

```json
{
  "amount": 5000
}
```

### 🔹 **Verify Payment**

**Endpoint:** `POST /api/razorpay/verify`

```json
{
  "razorpay_order_id": "order_xyz",
  "razorpay_payment_id": "pay_xyz",
  "razorpay_signature": "generated_signature"
}
```

## 📌 Contributors

- **My self** - Manan Monani
- **Team Member 1** - Nevil Dhinoja
- **Team Member 2** - Krishil Agrawal
- **Team Member 3** - Parthiv Panchal
- **Team Member 4** - Astha Makwana
- **Team Member 5** - Yashvi Bhadani

## 📌 License

This project is **MIT Licensed**. Feel free to use and modify it. 😊

---

Made with ❤️ by the **Defraudo Team** 🚀

Represented This at Indus University as Team Defraudo.
