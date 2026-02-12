import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useRef } from 'react';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import ProductDetails from './pages/ProductDetails';
import Checkout from './pages/Checkout';
import Login from './pages/Login';
import Signup from './pages/Signup';
import Profile from './pages/Profile';
import ProtectedRoute from './components/ProtectedRoute';
import { CartProvider } from './context/CartContext';
import { AuthProvider } from './context/AuthContext';
import './styles/phoneplace.css';

function App() {
  const homeSearchHandlerRef = useRef<((query: string) => void) | null>(null);

  const handleNavbarSearch = (query: string) => {
    if (homeSearchHandlerRef.current) {
      homeSearchHandlerRef.current(query);
    }
  };

  return (
    <AuthProvider>
      <CartProvider>
        <Router>
          <div className="d-flex flex-column min-vh-100">
            <Navbar onSearch={handleNavbarSearch} />
            <div className="container-fluid mt-4 flex-grow-1">
              <Routes>
                <Route path="/" element={<Home searchHandlerRef={homeSearchHandlerRef} />} />
                <Route path="/product/:id" element={<ProductDetails />} />
                <Route path="/checkout" element={<Checkout />} />
                <Route path="/login" element={<Login />} />
                <Route path="/signup" element={<Signup />} />
                <Route 
                  path="/profile" 
                  element={
                    <ProtectedRoute>
                      <Profile />
                    </ProtectedRoute>
                  } 
                />
              </Routes>
            </div>
            <footer className="bg-dark text-white text-center py-3 mt-4">
              <p className="mb-0">© 2026 Phone Place Kenya. All rights reserved.</p>
            </footer>
          </div>
        </Router>
      </CartProvider>
    </AuthProvider>
  );
}

export default App;
