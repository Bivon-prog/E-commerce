import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import api from '../services/api';
import { Product } from '../types';
import { useCart } from '../context/CartContext';
import { FaArrowLeft, FaChevronLeft, FaChevronRight } from 'react-icons/fa';
import '../components/ImageCarousel.css';

const ProductDetails: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [product, setProduct] = useState<Product | null>(null);
  const [loading, setLoading] = useState(true);
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const { addToCart } = useCart();

  useEffect(() => {
    api.get(`/products/${id}`)
      .then(res => {
        setProduct(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, [id]);

  if (loading) return <div className="text-center mt-5"><div className="spinner-border text-primary"></div></div>;
  if (!product) return <div className="alert alert-danger">Product not found</div>;

  // Convert price from cents to KES for display
  const displayPrice = (product.price / 100).toFixed(2);

  const nextImage = () => {
    setCurrentImageIndex((prev) => (prev + 1) % product.images.length);
  };

  const prevImage = () => {
    setCurrentImageIndex((prev) => (prev - 1 + product.images.length) % product.images.length);
  };

  return (
    <div>
      <Link to="/" className="btn btn-link text-decoration-none mb-3 ps-0"><FaArrowLeft /> Back to Shop</Link>
      <div className="card shadow-sm border-0 overflow-hidden">
        <div className="row g-0">
          <div className="col-md-6 bg-white d-flex flex-column align-items-center justify-content-center p-4">
            {/* Main Image Carousel */}
            <div className="image-carousel">
              <img 
                src={product.images[currentImageIndex]} 
                className="carousel-image" 
                alt={`${product.name} - Image ${currentImageIndex + 1}`}
              />
              
              {/* Image Counter */}
              {product.images.length > 1 && (
                <div className="image-indicator">
                  {currentImageIndex + 1} / {product.images.length}
                </div>
              )}
              
              {/* Navigation Arrows */}
              {product.images.length > 1 && (
                <>
                  <button 
                    className="carousel-nav-btn prev"
                    onClick={prevImage}
                    aria-label="Previous image"
                  >
                    <FaChevronLeft />
                  </button>
                  <button 
                    className="carousel-nav-btn next"
                    onClick={nextImage}
                    aria-label="Next image"
                  >
                    <FaChevronRight />
                  </button>
                </>
              )}
            </div>
            
            {/* Thumbnail Gallery */}
            {product.images.length > 1 && (
              <div className="thumbnail-gallery">
                {product.images.map((image, index) => (
                  <img
                    key={index}
                    src={image}
                    alt={`${product.name} - Thumbnail ${index + 1}`}
                    className={`thumbnail-image ${index === currentImageIndex ? 'active' : ''}`}
                    onClick={() => setCurrentImageIndex(index)}
                  />
                ))}
              </div>
            )}
          </div>
          <div className="col-md-6 p-4 d-flex flex-column">
            <h2 className="fw-bold">{product.name}</h2>
            <p className="text-muted fs-5">{product.brand}</p>
            <h3 className="text-primary fw-bold mb-4">KES {displayPrice}</h3>
            
            {!product.in_stock && (
              <div className="alert alert-warning mb-3">
                <strong>Out of Stock</strong> - This item is currently unavailable
              </div>
            )}
            
            <p className="lead">{product.description}</p>
            
            {product.specs && (
              <div className="mb-4">
                <h5 className="border-bottom pb-2">Specifications</h5>
                <ul className="list-unstyled">
                  {Object.entries(product.specs).map(([key, value]) => (
                    value && (
                      <li key={key} className="d-flex justify-content-between py-1 border-bottom border-light">
                        <span className="text-muted text-capitalize">{key.replace('_', ' ')}</span>
                        <span className="fw-medium">{value}</span>
                      </li>
                    )
                  ))}
                </ul>
              </div>
            )}

            <div className="mt-auto">
              <button 
                className="btn btn-primary btn-lg w-100" 
                onClick={() => addToCart(product)}
                disabled={!product.in_stock}
              >
                {product.in_stock ? 'Add to Cart' : 'Out of Stock'}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductDetails;
