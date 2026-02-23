import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useRef } from 'react';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import ProductDetails from './pages/ProductDetails';
import Checkout from './pages/Checkout';
import Login from './pages/Login';
import Signup from './pages/Signup';
import Profile from './pages/Profile';
import Orders from './pages/Orders';
import AdminDashboard from './pages/Admin/AdminDashboard';
import ProductForm from './pages/Admin/ProductForm';
import ProtectedRoute from './components/ProtectedRoute';
import AdminRoute from './components/AdminRoute';
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
          <div className="d-flex flex-column min-vh-100" style={{ background: '#f1f5f9' }}>
            <Navbar onSearch={handleNavbarSearch} />
            <div className="flex-grow-1" style={{ paddingTop: '1rem' }}>
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
                <Route 
                  path="/orders" 
                  element={
                    <ProtectedRoute>
                      <Orders />
                    </ProtectedRoute>
                  } 
                />
                <Route 
                  path="/admin/dashboard" 
                  element={
                    <AdminRoute>
                      <AdminDashboard />
                    </AdminRoute>
                  } 
                />
                <Route 
                  path="/admin/products/new" 
                  element={
                    <AdminRoute>
                      <ProductForm />
                    </AdminRoute>
                  } 
                />
                <Route 
                  path="/admin/products/edit/:id" 
                  element={
                    <AdminRoute>
                      <ProductForm />
                    </AdminRoute>
                  } 
                />
              </Routes>
            </div>
            <footer className="bg-dark text-white py-4 mt-5">
              <div className="container">
                <div className="row">
                  <div className="col-md-4 mb-3 mb-md-0">
                    <h5 className="fw-bold mb-3">Smart Gadgets</h5>
                    <p className="text-white-50 mb-3">
                      Your trusted source for the latest smartphones in Kenya.
                    </p>
                    <div className="social-links">
                      <a href="#" className="social-icon" aria-label="Facebook">
                        <i className="bi bi-facebook"></i>
                      </a>
                      <a href="#" className="social-icon" aria-label="Twitter">
                        <i className="bi bi-twitter"></i>
                      </a>
                      <a href="#" className="social-icon" aria-label="Instagram">
                        <i className="bi bi-instagram"></i>
                      </a>
                      <a href="#" className="social-icon" aria-label="WhatsApp">
                        <i className="bi bi-whatsapp"></i>
                      </a>
                      <a href="#" className="social-icon" aria-label="TikTok">
                        <i className="bi bi-tiktok"></i>
                      </a>
                    </div>
                  </div>
                  <div className="col-md-4 mb-3 mb-md-0">
                    <h6 className="fw-bold mb-3">Quick Links</h6>
                    <ul className="list-unstyled">
                      <li className="mb-2">
                        <a href="/" className="text-white-50 text-decoration-none">Home</a>
                      </li>
                      <li className="mb-2">
                        <a href="/checkout" className="text-white-50 text-decoration-none">Cart</a>
                      </li>
                      <li className="mb-2">
                        <a href="/orders" className="text-white-50 text-decoration-none">My Orders</a>
                      </li>
                    </ul>
                  </div>
                  <div className="col-md-4">
                    <h6 className="fw-bold mb-3">Contact Us</h6>
                    <ul className="list-unstyled">
                      <li className="mb-2">
                        <i className="bi bi-telephone-fill me-2"></i>
                        <a href="tel:0759249875" className="text-white-50 text-decoration-none">
                          0759 249 875
                        </a>
                      </li>
                      <li className="mb-2">
                        <i className="bi bi-envelope-fill me-2"></i>
                        <a href="mailto:bivonmoriasi@gmail.com" className="text-white-50 text-decoration-none">
                          bivonmoriasi@gmail.com
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
                <hr className="my-3 bg-white opacity-25" />
                <div className="text-center">
                  <p className="mb-0 text-white-50">© 2026 Smart Gadgets. All rights reserved.</p>
                </div>
              </div>
            </footer>
          </div>
        </Router>
      </CartProvider>
    </AuthProvider>
  );
}

export default App;
