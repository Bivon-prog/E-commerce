import React, { useState, useEffect } from 'react';
import { Product } from '../types';

interface HeroBannerProps {
  products: Product[];
}

const HeroBanner: React.FC<HeroBannerProps> = ({ products }) => {
  const [currentSlide, setCurrentSlide] = useState(0);
  
  // Select featured products for banner (premium/flagship phones)
  const featuredProducts = products
    .filter(p => 
      p.specs?.price_tier === 'Premium Flagship' || 
      p.specs?.price_tier === 'Ultra-Premium' ||
      p.specs?.price_tier === 'Flagship Killer'
    )
    .slice(0, 5);

  // Auto-rotate slides every 2 seconds
  useEffect(() => {
    if (featuredProducts.length === 0) return;
    
    const interval = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % featuredProducts.length);
    }, 2000);

    return () => clearInterval(interval);
  }, [featuredProducts.length]);

  if (featuredProducts.length === 0) return null;

  const bannerGradients = [
    'linear-gradient(135deg, #1e40af 0%, #3b82f6 100%)',
    'linear-gradient(135deg, #7c3aed 0%, #a78bfa 100%)',
    'linear-gradient(135deg, #dc2626 0%, #f87171 100%)',
    'linear-gradient(135deg, #059669 0%, #34d399 100%)',
    'linear-gradient(135deg, #ea580c 0%, #fb923c 100%)',
  ];

  return (
    <div 
      className="hero-banner" 
      style={{ background: bannerGradients[currentSlide % bannerGradients.length] }}
    >
      {featuredProducts.map((product, index) => (
        <div
          key={product._id}
          className={`hero-banner-slide ${index === currentSlide ? 'active' : ''}`}
        >
          <div className="hero-banner-content">
            <h2>{product.name}</h2>
            <p>{product.description.substring(0, 100)}...</p>
            <div className="d-flex gap-3 align-items-center">
              <span className="fs-3 fw-bold">
                KES {(product.price / 100).toLocaleString()}
              </span>
              {product.specs?.price_tier && (
                <span className="badge bg-light text-dark px-3 py-2">
                  {product.specs.price_tier}
                </span>
              )}
            </div>
            <button className="btn btn-light btn-lg mt-3 px-4">
              Shop Now →
            </button>
          </div>
          <div className="hero-banner-image">
            <img 
              src={product.images?.[0] || 'https://via.placeholder.com/400x300'} 
              alt={product.name}
            />
          </div>
        </div>
      ))}
      
      {/* Slide Indicators */}
      <div className="hero-banner-indicators">
        {featuredProducts.map((_, index) => (
          <div
            key={index}
            className={`hero-banner-indicator ${index === currentSlide ? 'active' : ''}`}
            onClick={() => setCurrentSlide(index)}
          />
        ))}
      </div>
    </div>
  );
};

export default HeroBanner;
