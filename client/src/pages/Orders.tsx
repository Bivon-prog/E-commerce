import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { FaShoppingCart, FaCheckCircle, FaBox } from 'react-icons/fa';
import { useAuth } from '../context/AuthContext';
import api from '../services/api';

interface OrderItem {
  id: string;
  name: string;
  price: number;
  quantity: number;
  images: string[];
}

interface Order {
  _id: string;
  items: OrderItem[];
  shipping_details: {
    name: string;
    email: string;
    address: string;
  };
  total: number;
  status: string;
  created_at: string;
}

const Orders = () => {
  const { user } = useAuth();
  const [orders, setOrders] = useState<Order[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {
      if (!user?.email) {
        setLoading(false);
        return;
      }
      
      const response = await api.get(`/orders/user?email=${encodeURIComponent(user.email)}`);
      setOrders(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching orders:', error);
      setLoading(false);
    }
  };

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  if (loading) {
    return (
      <div className="container mt-5 text-center">
        <div className="spinner-border text-primary" role="status"></div>
        <p className="mt-2">Loading orders...</p>
      </div>
    );
  }

  if (orders.length === 0) {
    return (
      <div className="container mt-5">
        <div className="row">
          <div className="col-md-8 offset-md-2">
            <div className="card shadow-sm">
              <div className="card-body text-center py-5">
                <FaShoppingCart className="text-muted display-1 mb-4" />
                <h2 className="mb-3">No Orders Yet</h2>
                <p className="text-muted mb-4">
                  You haven't placed any orders yet. Start shopping to see your order history here!
                </p>
                <Link to="/" className="btn btn-primary mt-3">
                  Start Shopping
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <h2 className="mb-4">My Orders</h2>
      
      {orders.map(order => (
        <div key={order._id} className="card shadow-sm mb-4">
          <div className="card-header bg-light">
            <div className="row align-items-center">
              <div className="col-md-3">
                <small className="text-muted">Order ID</small>
                <div className="fw-bold">{order._id.substring(0, 8)}</div>
              </div>
              <div className="col-md-3">
                <small className="text-muted">Date</small>
                <div>{formatDate(order.created_at)}</div>
              </div>
              <div className="col-md-3">
                <small className="text-muted">Total</small>
                <div className="fw-bold">KES {(order.total / 100).toFixed(2)}</div>
              </div>
              <div className="col-md-3">
                <span className="badge bg-warning text-dark">
                  {order.status.charAt(0).toUpperCase() + order.status.slice(1)}
                </span>
              </div>
            </div>
          </div>
          <div className="card-body">
            <h6 className="mb-3">Items ({order.items.length})</h6>
            <div className="list-group list-group-flush">
              {order.items.map((item, index) => (
                <div key={index} className="list-group-item d-flex align-items-center gap-3 px-0">
                  <img 
                    src={item.images[0]} 
                    alt={item.name} 
                    width="50" 
                    height="50" 
                    className="object-fit-contain rounded border"
                  />
                  <div className="flex-grow-1">
                    <div className="fw-semibold">{item.name}</div>
                    <small className="text-muted">
                      KES {(item.price / 100).toFixed(2)} x {item.quantity}
                    </small>
                  </div>
                  <div className="fw-bold">
                    KES {((item.price * item.quantity) / 100).toFixed(2)}
                  </div>
                </div>
              ))}
            </div>
            <div className="mt-3">
              <h6>Shipping Details</h6>
              <p className="mb-1"><strong>Name:</strong> {order.shipping_details.name}</p>
              <p className="mb-1"><strong>Email:</strong> {order.shipping_details.email}</p>
              <p className="mb-0"><strong>Address:</strong> {order.shipping_details.address}</p>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Orders;
