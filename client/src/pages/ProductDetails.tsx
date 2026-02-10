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
  const displayPrice = (product.price / 100).toLocaleString('en-KE', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  });

  const nextImage = () => {
    setCurrentImageIndex((prev) => (prev + 1) % product.images.length);
  };

  const prevImage = () => {
    setCurrentImageIndex((prev) => (prev - 1 + product.images.length) % product.images.length);
  };

  // Get category badge
  const getCategoryBadge = (category: string, value: string) => {
    const badges: { [key: string]: string } = {
      'Entry-Level': 'bg-success',
      'Budget': 'bg-info',
      'Mid-Range': 'bg-warning text-dark',
      'Flagship Killer': 'bg-primary',
      'Premium Flagship': 'bg-danger',
      'Ultra-Premium': 'bg-dark',
      'Gaming': 'bg-success',
      'Camera & Photography': 'bg-info',
      'Battery & Endurance': 'bg-warning text-dark',
      'Productivity & Business': 'bg-primary',
      'Fashion & Vlogging': 'bg-danger'
    };
    
    return badges[value] || 'bg-secondary';
  };

  return (
    <div className="container-fluid">
      <Link to="/" className="btn btn-link text-decoration-none mb-3 ps-0">
        <FaArrowLeft /> Back to Shop
      </Link>
      
      <div className="row">
        {/* Product Images */}
        <div className="col-lg-6">
          <div className="card shadow-sm border-0 overflow-hidden">
            <div className="bg-white d-flex flex-column align-items-center justify-content-center p-4">
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
          </div>
        </div>

        {/* Product Information */}
        <div className="col-lg-6">
          <div className="p-4">
            {/* Product Header */}
            <div className="mb-4">
              <div className="d-flex flex-wrap gap-2 mb-3">
                {product.specs?.price_tier && (
                  <span className={`badge ${getCategoryBadge('price', product.specs.price_tier)}`}>
                    {product.specs.price_tier}
                  </span>
                )}
                {product.specs?.use_case && (
                  <span className={`badge ${getCategoryBadge('use_case', product.specs.use_case)}`}>
                    {product.specs.use_case}
                  </span>
                )}
                {!product.in_stock && (
                  <span className="badge bg-danger">Out of Stock</span>
                )}
              </div>
              
              <h1 className="fw-bold mb-2">{product.name}</h1>
              <p className="text-muted fs-5 mb-3">{product.brand}</p>
              <h2 className="text-primary fw-bold mb-4">KES {displayPrice}</h2>
            </div>

            {/* Description */}
            <div className="mb-4">
              <h5 className="border-bottom pb-2 mb-3">Description</h5>
              <p className="lead">{product.description}</p>
            </div>

            {/* Key Specifications */}
            {product.specs && (
              <div className="mb-4">
                <h5 className="border-bottom pb-2 mb-3">Key Specifications</h5>
                <div className="row g-3">
                  {product.specs.screen_size && (
                    <div className="col-6">
                      <div className="d-flex align-items-center">
                        <span className="me-2">📱</span>
                        <div>
                          <small className="text-muted d-block">Screen</small>
                          <span className="fw-medium">{product.specs.screen_size}</span>
                        </div>
                      </div>
                    </div>
                  )}
                  {product.specs.ram && (
                    <div className="col-6">
                      <div className="d-flex align-items-center">
                        <span className="me-2">🧠</span>
                        <div>
                          <small className="text-muted d-block">RAM</small>
                          <span className="fw-medium">{product.specs.ram}</span>
                        </div>
                      </div>
                    </div>
                  )}
                  {product.specs.storage && (
                    <div className="col-6">
                      <div className="d-flex align-items-center">
                        <span className="me-2">💾</span>
                        <div>
                          <small className="text-muted d-block">Storage</small>
                          <span className="fw-medium">{product.specs.storage}</span>
                        </div>
                      </div>
                    </div>
                  )}
                  {product.specs.battery && (
                    <div className="col-6">
                      <div className="d-flex align-items-center">
                        <span className="me-2">🔋</span>
                        <div>
                          <small className="text-muted d-block">Battery</small>
                          <span className="fw-medium">{product.specs.battery}</span>
                        </div>
                      </div>
                    </div>
                  )}
                  {product.specs.camera && (
                    <div className="col-12">
                      <div className="d-flex align-items-center">
                        <span className="me-2">📸</span>
                        <div>
                          <small className="text-muted d-block">Camera</small>
                          <span className="fw-medium">{product.specs.camera}</span>
                        </div>
                      </div>
                    </div>
                  )}
                  {product.specs.processor && (
                    <div className="col-12">
                      <div className="d-flex align-items-center">
                        <span className="me-2">⚡</span>
                        <div>
                          <small className="text-muted d-block">Processor</small>
                          <span className="fw-medium">{product.specs.processor}</span>
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* Comprehensive Categories */}
            {product.specs && (
              <div className="mb-4">
                <h5 className="border-bottom pb-2 mb-3">Product Categories</h5>
                <div className="row g-3">
                  {product.specs.software_experience && (
                    <div className="col-12">
                      <div className="card bg-light border-0">
                        <div className="card-body py-2">
                          <small className="text-muted">Software Experience</small>
                          <div className="fw-medium">{product.specs.software_experience}</div>
                          {product.specs.software_description && (
                            <small className="text-muted">{product.specs.software_description}</small>
                          )}
                        </div>
                      </div>
                    </div>
                  )}
                  {product.specs.chipset_category && (
                    <div className="col-12">
                      <div className="card bg-light border-0">
                        <div className="card-body py-2">
                          <small className="text-muted">Chipset</small>
                          <div className="fw-medium">{product.specs.chipset_category}</div>
                          {product.specs.chipset_description && (
                            <small className="text-muted">{product.specs.chipset_description}</small>
                          )}
                        </div>
                      </div>
                    </div>
                  )}
                  {product.specs.target_demographic && (
                    <div className="col-12">
                      <div className="card bg-light border-0">
                        <div className="card-body py-2">
                          <small className="text-muted">Target Users</small>
                          <div className="fw-medium">{product.specs.target_demographic}</div>
                        </div>
                      </div>
                    </div>
                  )}
                  {product.specs.market_origin && (
                    <div className="col-12">
                      <div className="card bg-light border-0">
                        <div className="card-body py-2">
                          <small className="text-muted">Market Origin</small>
                          <div className="fw-medium">{product.specs.market_origin}</div>
                          {product.specs.origin_description && (
                            <small className="text-muted">{product.specs.origin_description}</small>
                          )}
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* Stock Status */}
            {!product.in_stock && (
              <div className="alert alert-warning mb-4">
                <strong>Out of Stock</strong> - This item is currently unavailable
              </div>
            )}

            {/* Add to Cart */}
            <div className="d-grid gap-2">
              <button 
                className="btn btn-primary btn-lg" 
                onClick={() => addToCart(product)}
                disabled={!product.in_stock}
              >
                {product.in_stock ? (
                  <>
                    <i className="bi bi-cart-plus me-2"></i>
                    Add to Cart - KES {displayPrice}
                  </>
                ) : (
                  'Out of Stock'
                )}
              </button>
              <button className="btn btn-outline-secondary">
                <i className="bi bi-heart me-2"></i>
                Add to Wishlist
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductDetails;
