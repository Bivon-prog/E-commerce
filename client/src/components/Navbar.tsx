import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useCart } from '../context/CartContext';
import { useAuth } from '../context/AuthContext';
import { FaShoppingCart, FaMobileAlt, FaSearch, FaUser, FaSignOutAlt } from 'react-icons/fa';
import { useState, useEffect } from 'react';

interface NavbarProps {
  onSearch?: (query: string) => void;
}

const Navbar: React.FC<NavbarProps> = ({ onSearch }) => {
  const { cart } = useCart();
  const { user, logout, isAuthenticated } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const itemCount = cart.reduce((acc, item) => acc + item.quantity, 0);
  const [searchQuery, setSearchQuery] = useState('');

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  // Clear search when navigating away from home
  useEffect(() => {
    if (location.pathname !== '/') {
      setSearchQuery('');
    }
  }, [location.pathname]);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (onSearch) {
      onSearch(searchQuery);
    }
    // Navigate to home if not already there
    if (location.pathname !== '/') {
      navigate('/');
    }
  };

  const handleSearchChange = (value: string) => {
    setSearchQuery(value);
    if (onSearch) {
      onSearch(value);
    }
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary shadow-sm">
      <div className="container">
        <Link className="navbar-brand d-flex align-items-center gap-2 fw-bold" to="/">
          <FaMobileAlt /> TechShop
        </Link>
        
        {/* Search Bar */}
        <form className="d-none d-md-flex mx-auto" style={{ width: '40%' }} onSubmit={handleSearch}>
          <div className="input-group">
            <input
              type="text"
              className="form-control"
              placeholder="Search phones by name, brand, or specs..."
              value={searchQuery}
              onChange={(e) => handleSearchChange(e.target.value)}
            />
            <button className="btn btn-light" type="submit">
              <FaSearch className="text-primary" />
            </button>
          </div>
        </form>

        <div className="ms-auto d-flex align-items-center gap-2">
          {/* Cart Button */}
          <Link to="/checkout" className="btn btn-light position-relative">
            <FaShoppingCart className="text-primary" />
            {itemCount > 0 && (
              <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                {itemCount}
              </span>
            )}
          </Link>

          {/* User Menu */}
          {isAuthenticated ? (
            <div className="dropdown">
              <button
                className="btn btn-light dropdown-toggle d-flex align-items-center gap-2"
                type="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                <FaUser />
                <span className="d-none d-md-inline">{user?.firstName}</span>
              </button>
              <ul className="dropdown-menu dropdown-menu-end">
                <li>
                  <div className="dropdown-item-text">
                    <div className="fw-semibold">{user?.firstName} {user?.lastName}</div>
                    <div className="small text-muted">{user?.email}</div>
                    {user?.role === 'admin' && (
                      <span className="badge bg-danger mt-1">Admin</span>
                    )}
                  </div>
                </li>
                <li><hr className="dropdown-divider" /></li>
                {user?.role === 'admin' && (
                  <>
                    <li>
                      <Link className="dropdown-item" to="/admin/dashboard">
                        <FaUser className="me-2" /> Admin Dashboard
                      </Link>
                    </li>
                    <li><hr className="dropdown-divider" /></li>
                  </>
                )}
                <li>
                  <Link className="dropdown-item" to="/profile">
                    <FaUser className="me-2" /> My Profile
                  </Link>
                </li>
                <li>
                  <Link className="dropdown-item" to="/orders">
                    <FaShoppingCart className="me-2" /> My Orders
                  </Link>
                </li>
                <li><hr className="dropdown-divider" /></li>
                <li>
                  <button className="dropdown-item text-danger" onClick={handleLogout}>
                    <FaSignOutAlt className="me-2" /> Logout
                  </button>
                </li>
              </ul>
            </div>
          ) : (
            <div className="d-flex gap-2">
              <Link to="/login" className="btn btn-outline-light">
                Sign In
              </Link>
              <Link to="/signup" className="btn btn-light">
                Sign Up
              </Link>
            </div>
          )}
        </div>
      </div>
      
      {/* Mobile Search Bar */}
      <div className="container d-md-none mt-2 pb-2">
        <form onSubmit={handleSearch}>
          <div className="input-group">
            <input
              type="text"
              className="form-control"
              placeholder="Search phones..."
              value={searchQuery}
              onChange={(e) => handleSearchChange(e.target.value)}
            />
            <button className="btn btn-light" type="submit">
              <FaSearch className="text-primary" />
            </button>
          </div>
        </form>
      </div>
    </nav>
  );
};

export default Navbar;
