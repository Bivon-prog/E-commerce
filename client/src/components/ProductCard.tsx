import { Product } from '../types';
import { useCart } from '../context/CartContext';
import { Link } from 'react-router-dom';

interface ProductCardProps {
  product: Product;
}

const ProductCard: React.FC<ProductCardProps> = ({ product }) => {
  const { addToCart } = useCart();

  // Convert price from cents to KES for display
  const displayPrice = (product.price / 100).toFixed(2);

  // Get the primary image with fallback logic
  const getImageUrl = () => {
    if (product.images && product.images.length > 0) {
      return product.images[0];
    }
    // Fallback to old image_url field if it exists
    if ((product as any).image_url) {
      return (product as any).image_url;
    }
    // Final fallback to a placeholder
    return 'https://via.placeholder.com/400x300/f8f9fa/6c757d?text=No+Image';
  };

  return (
    <div className="card h-100 shadow-sm border-0">
      <img src={getImageUrl()} className="card-img-top p-3" alt={product.name} style={{ objectFit: 'contain', height: '200px' }} />
      <div className="card-body d-flex flex-column">
        <h5 className="card-title text-truncate">{product.name}</h5>
        <p className="card-text text-muted small">{product.brand}</p>
        {!product.in_stock && (
          <span className="badge bg-danger mb-2">Out of Stock</span>
        )}
        <div className="mt-auto d-flex justify-content-between align-items-center">
          <span className="fs-5 fw-bold">KES {displayPrice}</span>
          <div className="d-flex gap-2">
            <Link to={`/product/${product.id}`} className="btn btn-outline-primary btn-sm">Details</Link>
            <button 
              className="btn btn-primary btn-sm" 
              onClick={() => addToCart(product)}
              disabled={!product.in_stock}
            >
              Add
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
