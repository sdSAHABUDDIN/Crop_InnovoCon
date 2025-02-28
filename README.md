# Crop Recommendation Website

## 🌱 Overview
The Crop Recommendation Website is a machine learning-powered platform designed to help farmers and agricultural enthusiasts determine the best crops to grow based on environmental and soil conditions. The platform provides recommendations by analyzing various factors such as temperature, humidity, soil type, and other parameters.

## 🚀 Features
- 🌾 **Crop Prediction**: Suggests the best crops based on input parameters.
- 📊 **Machine Learning Model**: Uses trained ML algorithms to analyze environmental data.
- 🖥 **User-Friendly Interface**: Built with **React.js** and styled with **Tailwind CSS**.
- 🔗 **Backend API**: Developed with **PYTHON FLASK**.
- 📦 **Database**: Uses **MongoDB** to store crop and environmental details.

## 🛠 Tech Stack
### **Frontend**
- React.js
- Tailwind CSS
- Axios (for API calls)

### **Backend**
-PYTHON FLASK
-NUMPY
-PANDAS
-FLASK_CORS

### **Database**
- MongoDB (for storing crop and environmental data)

### **Machine Learning**
- Python (for training and deploying ML models)
- Scikit-learn / TensorFlow (for model development)

## 📌 Installation & Setup
### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/crop-recommendation-website.git
cd crop-recommendation-website
```

### **2. Backend Setup**
```bash
cd ~/PY-JSX/Crop-Project/api
requirements.txt
python server.py
```

### **3. Frontend Setup**
```bash
cd frontend
npm install
npm start
```

## 📡 API Endpoints
### **1. User Authentication**
- `POST /api/auth/signup` → Register a new user
- `POST /api/auth/login` → Login and receive a JWT token

### **2. Crop Recommendation**
- `POST /api/recommend` → Sends environment data and receives crop suggestions

## 📷 Screenshots
### Homepage
![Homepage](screenshots/screen1.png)

### Crop Recommendation Result
![Crop Recommendation](screenshots/screen4.png)
![Crop Recommendation](screenshots/screen3.png)


## 🤝 Contributing
Feel free to contribute by submitting issues or pull requests. Let's make this project even better!

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).

