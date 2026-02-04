import React, { useEffect, useState } from 'react';
import api from '../services/api';
import { Product } from '../types';
import ProductCard from '../components/ProductCard';

const Home: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState<'All' | 'Phone' | 'Accessory'>('All');

  useEffect(() => {
    api.get('/products')
      .then(res => {
        setProducts(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  const filteredProducts = filter === 'All' 
    ? products 
    : products.filter(p => p.category === filter);

  if (loading) return <div className="text-center mt-5"><div className="spinner-border text-primary" role="status"></div></div>;

  return (
    <div>
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="fw-bold">Latest Arrivals</h2>
        <div className="btn-group">
          {['All', 'Phone', 'Accessory'].map(cat => (
            <button 
              key={cat}
              className={`btn ${filter === cat ? 'btn-primary' : 'btn-outline-primary'}`}
              onClick={() => setFilter(cat as any)}
            >
              {cat}
            </button>
          ))}
        </div>
      </div>
      
      <div className="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
        {filteredProducts.map(product => (
          <div className="col" key={product.id}>
            <ProductCard product={product} />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Home;
