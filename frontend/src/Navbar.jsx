import { Link, useNavigate } from 'react-router-dom';

function Navbar() {
  const navigate = useNavigate();
  const token = localStorage.getItem('token');

  const handleLogout = () => {
    localStorage.removeItem('token');
    // We reload the page to make sure the navbar updates correctly
    window.location.reload();
  };

  return (
    <nav style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
      <Link to="/">Home</Link>
      {token ? (
        <>
          <Link to="/my-bookings">My Bookings</Link>
          <button onClick={handleLogout}>Logout</button>
        </>
      ) : (
        <>
          <Link to="/login">Login</Link>
          <Link to="/register">Register</Link>
        </>
      )}
    </nav>
  );
}

export default Navbar;