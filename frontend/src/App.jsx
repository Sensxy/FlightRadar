import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [packages, setPackages] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    // The backend is running on port 5000
    // We must use the full URL here
    axios.get('http://127.0.0.1:5000/api/packages')
      .then(response => {
        setPackages(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the data!", error);
        setError('Failed to load packages. Is the backend server running?');
      });
  }, []); // The empty array means this effect runs once on component mount

  return (
    <>
      <h1>FlightRadar Packages</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div className="card">
        {packages.length > 0 ? (
          <ul>
            {packages.map(pkg => (
              <li key={pkg.id}>
                <strong>{pkg.name}</strong>: {pkg.description}
              </li>
            ))}
          </ul>
        ) : (
          !error && <p>Loading packages...</p>
        )}
      </div>
    </>
  );
}

export default App;