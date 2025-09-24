import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import App from './App.jsx';
import Register from './Register.jsx';
import Login from './Login.jsx';
import './index.css';
import MyBookings from './MyBookings.jsx'

// Define your application's routes
const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
  },
  {
    path: '/register',
    element: <Register />,
  },
  {
    path: '/login',
    element: <Login />,
  },

  {
    path: '/my-bookings',
    element: <MyBookings />,
  },

]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);