// src/api/index.js
import axios from 'axios';

require('dotenv').config();

// Create an Axios instance with common configuration
const axiosInstance = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL, // Base URL for all API calls
  timeout: 10000, // Timeout after 10 seconds
  headers: {
    'Content-Type': 'application/json', // Set common content type
  },
});

// Request interceptor (if needed)
axiosInstance.interceptors.request.use(
  (config) => {
    // Modify request config if needed, for example, adding an authorization token
    // config.headers.Authorization = `Bearer ${token}`;
    return config;
  },
  (error) => {
    // Handle request error
    return Promise.reject(error);
  }
);

// Response interceptor (if needed)
axiosInstance.interceptors.response.use(
  (response) => {
    // Modify response data if needed
    return response;
  },
  (error) => {
    // Handle response error
    // Optionally, you can handle specific status codes here
    if (error.response && error.response.status === 401) {
      // Handle unauthorized errors
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
