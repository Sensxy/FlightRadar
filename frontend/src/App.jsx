import { useState, useEffect } from 'react';
import axios from 'axios';
import Navbar from './Navbar.jsx';
import './App.css';

function App() {
  const [packages, setPackages] = useState([]);
  const [error, setError] = useState('');
  const [searchTerm, setSearchTerm] = useState(''); // State for the search input

  useEffect(() => {
    // Define the API endpoint
    const url = 'http://127.0.0.1:5000/api/packages';
    
    // Pass the search term as a parameter
    axios.get(url, { params: { search: searchTerm } })
      .then(response => {
        setPackages(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the data!", error);
        setError('Failed to load packages.');
      });
  }, [searchTerm]); // <-- Re-run this effect whenever searchTerm changes

  return (
    <>
      <Navbar />
      <h1>FlightRadar Packages</h1>

      {/* Search Input */}
      <div className="search-bar">
        <input
          type="text"
          placeholder="Search for a package..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>

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
          !error && <p>No packages found.</p>
        )}
      </div>
    </>
  );
}

export default App;