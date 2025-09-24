import { useState, useEffect } from 'react';
import axios from 'axios';

function MyBookings() {
  const [bookings, setBookings] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchBookings = async () => {
      // Get the token from localStorage
      const token = localStorage.getItem('token');

      if (!token) {
        setError('You must be logged in to view bookings.');
        return;
      }

      try {
        // IMPORTANT: Send the token in the request headers
        const response = await axios.get('http://127.0.0.1:5000/api/my-bookings', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        setBookings(response.data);
      } catch (err) {
        setError('Failed to fetch bookings.');
      }
    };

    fetchBookings();
  }, []);

  if (error) {
    return <p style={{ color: 'red' }}>{error}</p>;
  }

  return (
    <div>
      <h2>My Bookings</h2>
      <ul>
        {bookings.map(booking => (
          <li key={booking.id}>{booking.package_name}</li>
        ))}
      </ul>
    </div>
  );
}

export default MyBookings;