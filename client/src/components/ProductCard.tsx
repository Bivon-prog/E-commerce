import { Product } from '../types';
import { useCart } from '../context/CartContext';
import { Link } from 'react-router-dom';

interface ProductCardProps {
  product: Product;
}

const ProductCard: React.FC<ProductCardProps> = ({ product }) => {
  const { addToCart } = useCart();

  // Convert price from cents to KES for display
  const displayPrice = (product.price / 100).toLocaleString('en-KE', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  });

  // Get the primary image with fallback logic
  const getImageUrl = () => {
    if (product.images && product.images.length > 0) {
      return product.images[0];
    }
    // Final fallback to a placeholder
    return 'https://via.placeholder.com/400x300/f8f9fa/6c757d?text=No+Image';
  };

  // Get price tier badge color
  const getPriceTierBadge = () => {
    const tier = product.specs?.price_tier;
    if (!tier) return null;
    
    let badgeClass = 'badge price-tier-badge ';
    switch (tier) {
      case 'Entry-Level':
        badgeClass += 'bg-success';
        break;
      case 'Budget':
        badgeClass += 'bg-info';
        break;
      case 'Mid-Range':
        badgeClass += 'bg-warning text-dark';
        break;
      case 'Flagship Killer':
        badgeClass += 'bg-primary';
        break;
      case 'Premium Flagship':
        badgeClass += 'bg-danger';
        break;
      case 'Ultra-Premium':
        badgeClass += 'bg-dark';
        break;
      default:
        badgeClass += 'bg-secondary';
    }
    
    return <span className={badgeClass}>{tier}</span>;
  };

  // Random offer badges for visual appeal (like Phone Place Kenya)
  const getOfferBadge = () => {
    const random = Math.random();
    if (random < 0.3) {
      return <span className="offer-badge">Offer</span>;
    } else if (random < 0.5) {
      return <span className="offer-badge hot-badge">Hot</span>;
    } else if (random < 0.7) {
      return <span className="offer-badge new-badge">New</span>;
    }
    return null;
  };

  return (
    <div className="card h-100 shadow-sm border-0 product-card">
      <div className="position-relative overflow-hidden">
        <img 
          src={getImageUrl()} 
          className="card-img-top" 
          alt={product.name}
        />
        
        {/* Offer Badge */}
        {getOfferBadge()}
        
        {/* Stock Status */}
        {!product.in_stock && (
          <div className="position-absolute top-0 start-0 m-2">
            <span className="badge bg-danger">Out of Stock</span>
          </div>
        )}
        
        {/* Gaming Badge */}
        {product.specs?.use_case === 'Gaming' && (
          <div className="position-absolute bottom-0 start-0 m-2">
            <span className="badge bg-success">🎮 Gaming</span>
          </div>
        )}
      </div>
      
      <div className="card-body d-flex flex-column">
        <div className="mb-2">
          {getPriceTierBadge()}
        </div>
        
        <h6 className="card-title text-truncate fw-bold mb-1">{product.name}</h6>
        <p className="card-text text-muted small mb-2">{product.brand}</p>
        
        {/* Key specs */}
        <div className="small text-muted mb-2">
          {product.specs?.ram && <span className="me-2">🧠 {product.specs.ram}</span>}
          {product.specs?.storage && <span className="me-2">💾 {product.specs.storage}</span>}
        </div>
        
        {/* Short description */}
        <p className="card-text small text-muted flex-grow-1" style={{ fontSize: '0.85rem', lineHeight: '1.3' }}>
          {product.description.length > 80 
            ? product.description.substring(0, 80) + '...' 
            : product.description
          }
        </p>
        
        <div className="mt-auto">
          <div className="d-flex justify-content-between align-items-center mb-3">
            <span className="fs-6 fw-bold text-primary">KES {displayPrice}</span>
            {product.specs?.chipset_category && (
              <small className="text-muted">{product.specs.chipset_category.split(' ')[0]}</small>
            )}
          </div>
          
          <div className="d-flex gap-2">
            <Link 
              to={`/product/${product._id}`} 
              className="btn btn-outline-primary btn-sm flex-fill"
            >
              View Details
            </Link>
            <button 
              className="btn btn-primary btn-sm flex-fill" 
              onClick={() => addToCart(product)}
              disabled={!product.in_stock}
            >
              {product.in_stock ? 'Add to Cart' : 'Out of Stock'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
