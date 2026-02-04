import React, { useState } from 'react';
import { useCart } from '../context/CartContext';
import { FaTrash, FaCheckCircle } from 'react-icons/fa';
import api from '../services/api';
import { Link } from 'react-router-dom';

const Checkout: React.FC = () => {
  const { cart, removeFromCart, cartTotal, clearCart } = useCart();
  const [formData, setFormData] = useState({ name: '', address: '', email: '' });
  const [ordered, setOrdered] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      // Note: The Rust backend doesn't have an orders endpoint yet
      // This would need to be implemented in the Rust backend
      await api.post('/orders', { items: cart, shippingDetails: formData });
      setOrdered(true);
      clearCart();
    } catch (error) {
      alert('Failed to place order');
    }
  };

  if (ordered) {
    return (
      <div className="text-center mt-5">
        <FaCheckCircle className="text-success display-1 mb-3" />
        <h2>Thank You for Your Order!</h2>
        <p className="lead">We have received your order and are processing it.</p>
        <Link to="/" className="btn btn-primary mt-3">Continue Shopping</Link>
      </div>
    );
  }

  if (cart.length === 0) {
    return (
      <div className="text-center mt-5">
        <h3>Your cart is empty</h3>
        <Link to="/" className="btn btn-primary mt-3">Start Shopping</Link>
      </div>
    );
  }

  // Convert cart total from cents to KES for display
  const displayTotal = (cartTotal / 100).toFixed(2);

  return (
    <div className="row">
      <div className="col-md-8">
        <h4 className="mb-3">Shopping Cart</h4>
        <div className="list-group mb-4">
          {cart.map(item => {
            const itemPrice = (item.price / 100).toFixed(2);
            const itemTotal = ((item.price * item.quantity) / 100).toFixed(2);
            
            return (
              <div key={item.id} className="list-group-item d-flex justify-content-between align-items-center">
                <div className="d-flex align-items-center gap-3">
                  <img src={item.images[0]} alt={item.name} width="60" height="60" className="object-fit-contain rounded border" />
                  <div>
                    <h6 className="my-0">{item.name}</h6>
                    <small className="text-muted">KES {itemPrice} x {item.quantity}</small>
                  </div>
                </div>
                <div className="d-flex align-items-center gap-3">
                  <span className="fw-bold">KES {itemTotal}</span>
                  <button className="btn btn-outline-danger btn-sm" onClick={() => removeFromCart(item.id)}>
                    <FaTrash />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>
      
      <div className="col-md-4">
        <div className="card shadow-sm border-0 bg-light">
          <div className="card-body">
            <h4 className="card-title d-flex justify-content-between align-items-center mb-3">
              <span className="text-primary">Order Summary</span>
            </h4>
            <ul className="list-group mb-3">
              <li className="list-group-item d-flex justify-content-between">
                <span>Total (KES)</span>
                <strong>KES {displayTotal}</strong>
              </li>
            </ul>

            <h5 className="mb-3">Shipping Details</h5>
            <form onSubmit={handleSubmit}>
              <div className="mb-3">
                <label className="form-label">Full Name</label>
                <input 
                  type="text" 
                  className="form-control" 
                  required 
                  value={formData.name}
                  onChange={e => setFormData({...formData, name: e.target.value})}
                />
              </div>
              <div className="mb-3">
                <label className="form-label">Email</label>
                <input 
                  type="email" 
                  className="form-control" 
                  required
                  value={formData.email}
                  onChange={e => setFormData({...formData, email: e.target.value})}
                />
              </div>
              <div className="mb-3">
                <label className="form-label">Address</label>
                <textarea 
                  className="form-control" 
                  required
                  rows={2}
                  value={formData.address}
                  onChange={e => setFormData({...formData, address: e.target.value})}
                ></textarea>
              </div>
              <button className="w-100 btn btn-primary btn-lg" type="submit">Place Order</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Checkout;
