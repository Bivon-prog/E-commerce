import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import ProductDetails from './pages/ProductDetails';
import Checkout from './pages/Checkout';
import { CartProvider } from './context/CartContext';

function App() {
  return (
    <CartProvider>
      <Router>
        <div className="d-flex flex-column min-vh-100">
          <Navbar />
          <div className="container mt-4 flex-grow-1">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/product/:id" element={<ProductDetails />} />
              <Route path="/checkout" element={<Checkout />} />
            </Routes>
          </div>
          <footer className="bg-dark text-white text-center py-3 mt-4">
            <p className="mb-0">© 2026 TechShop. All rights reserved.</p>
          </footer>
        </div>
      </Router>
    </CartProvider>
  );
}

export default App;
