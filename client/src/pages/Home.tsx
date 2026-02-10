import React, { useEffect, useState } from 'react';
import api from '../services/api';
import { Product } from '../types';
import ProductCard from '../components/ProductCard';
import FilterSidebar from '../components/FilterSidebar';

const Home: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [filteredProducts, setFilteredProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeFilters, setActiveFilters] = useState<any>({});
  const [showFilters, setShowFilters] = useState(false);

  // Fetch products with filters
  const fetchProducts = async (filters: any = {}) => {
    try {
      setLoading(true);
      const params = new URLSearchParams();
      
      // Add all active filters to params
      Object.entries(filters).forEach(([key, value]) => {
        if (value !== undefined && value !== null && value !== '') {
          params.append(key, value as string);
        }
      });

      const response = await api.get(`/products?${params.toString()}`);
      setProducts(response.data);
      setFilteredProducts(response.data);
      setLoading(false);
    } catch (err) {
      console.error('Failed to fetch products:', err);
      setLoading(false);
    }
  };

  // Initial load
  useEffect(() => {
    fetchProducts();
  }, []);

  // Handle filter changes
  const handleFilterChange = (newFilters: any) => {
    setActiveFilters(newFilters);
    fetchProducts(newFilters);
  };

  // Get category sections based on Phone Place Kenya style
  const getCategorySections = () => {
    const sections = [
      {
        title: "🔥 Gaming & Entertainment Deals - Flash Sales",
        products: filteredProducts.filter(p => p.specs?.use_case === 'Gaming').slice(0, 6),
        bgClass: "bg-danger"
      },
      {
        title: "💰 Pocket-Friendly Picks", 
        products: filteredProducts.filter(p => p.specs?.price_tier === 'Budget' || p.specs?.price_tier === 'Entry-Level').slice(0, 8),
        bgClass: "bg-success"
      },
      {
        title: "✨ See What's New",
        products: filteredProducts.slice(0, 10), // Latest products
        bgClass: "bg-info"
      },
      {
        title: "🏆 Experience High-End",
        products: filteredProducts.filter(p => p.specs?.price_tier === 'Premium Flagship' || p.specs?.price_tier === 'Ultra-Premium').slice(0, 6),
        bgClass: "bg-warning text-dark"
      },
      {
        title: "📱 This Week's Best-sellers",
        products: filteredProducts.filter(p => p.in_stock).slice(0, 8),
        bgClass: "bg-primary"
      }
    ];

    return sections.filter(section => section.products.length > 0);
  };

  if (loading) return (
    <div className="text-center mt-5">
      <div className="spinner-border text-primary" role="status"></div>
      <p className="mt-2">Loading amazing phones...</p>
    </div>
  );

  const categorySections = getCategorySections();

  return (
    <div className="container-fluid px-3">
      {/* Mobile Filter Backdrop */}
      {showFilters && (
        <div 
          className="filter-backdrop d-lg-none"
          onClick={() => setShowFilters(false)}
        ></div>
      )}

      <div className="row">
        {/* Filter Sidebar */}
        <div className={`col-lg-3 ${showFilters ? 'd-block filter-sidebar' : 'd-none d-lg-block'}`}>
          <div className="position-relative">
            {/* Mobile Close Button */}
            <button 
              className="btn btn-close position-absolute top-0 end-0 d-lg-none"
              onClick={() => setShowFilters(false)}
              style={{ zIndex: 1051 }}
            ></button>
            <FilterSidebar 
              onFilterChange={handleFilterChange}
              activeFilters={activeFilters}
            />
          </div>
        </div>

        {/* Main Content */}
        <div className="col-lg-9">
          {/* Header */}
          <div className="site-header rounded mb-4">
            <div className="d-flex justify-content-between align-items-center">
              <div>
                <h2 className="fw-bold mb-1">Phone Place Kenya</h2>
                <p className="mb-0 opacity-75">Latest Smartphones in Kenya</p>
              </div>
              <div className="d-flex gap-2">
                <button 
                  className="btn btn-light d-lg-none"
                  onClick={() => setShowFilters(!showFilters)}
                >
                  🔍 Filters {Object.keys(activeFilters).length > 0 && `(${Object.keys(activeFilters).length})`}
                </button>
                <div className="dropdown">
                  <button className="btn btn-light dropdown-toggle" type="button" data-bs-toggle="dropdown">
                    Sort by
                  </button>
                  <ul className="dropdown-menu">
                    <li><button className="dropdown-item" onClick={() => handleFilterChange({...activeFilters, sort: 'price_asc'})}>Price: Low to High</button></li>
                    <li><button className="dropdown-item" onClick={() => handleFilterChange({...activeFilters, sort: 'price_desc'})}>Price: High to Low</button></li>
                    <li><button className="dropdown-item" onClick={() => handleFilterChange({...activeFilters, sort: 'name'})}>Name A-Z</button></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          {/* Active Filters Display */}
          {Object.keys(activeFilters).length > 0 && (
            <div className="mb-4">
              <div className="d-flex flex-wrap gap-2 align-items-center">
                <span className="text-muted small fw-medium">Active filters:</span>
                {Object.entries(activeFilters).map(([key, value]) => (
                  <span key={key} className="badge bg-primary fs-6">
                    {key.replace('_', ' ')}: {value}
                    <button 
                      className="btn-close btn-close-white ms-2" 
                      style={{ fontSize: '0.6rem' }}
                      onClick={() => {
                        const newFilters = {...activeFilters};
                        delete newFilters[key];
                        handleFilterChange(newFilters);
                      }}
                    ></button>
                  </span>
                ))}
                <button 
                  className="btn btn-sm btn-outline-secondary"
                  onClick={() => handleFilterChange({})}
                >
                  Clear All
                </button>
              </div>
            </div>
          )}

          {/* Results Summary */}
          <div className="mb-4">
            <p className="text-muted mb-0">
              Showing <strong>{filteredProducts.length}</strong> product{filteredProducts.length !== 1 ? 's' : ''}
              {Object.keys(activeFilters).length > 0 && ' matching your filters'}
            </p>
          </div>

          {/* Category Sections (Phone Place Kenya Style) */}
          {Object.keys(activeFilters).length === 0 ? (
            // Show category sections when no filters are active
            <div>
              {categorySections.map((section, index) => (
                <div key={index} className="mb-5">
                  <div className={`category-section-header ${section.bgClass} rounded`}>
                    <div className="d-flex justify-content-between align-items-center">
                      <h4 className="fw-bold mb-0">{section.title}</h4>
                      <button className="btn btn-light btn-sm">
                        View All →
                      </button>
                    </div>
                  </div>
                  <div className="row row-cols-1 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 g-3 product-grid">
                    {section.products.map(product => (
                      <div className="col" key={product._id}>
                        <ProductCard product={product} />
                      </div>
                    ))}
                  </div>
                  {index < categorySections.length - 1 && <div className="section-divider"></div>}
                </div>
              ))}
            </div>
          ) : (
            // Show filtered results
            <div>
              <div className="row row-cols-1 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 g-3 product-grid">
                {filteredProducts.map(product => (
                  <div className="col" key={product._id}>
                    <ProductCard product={product} />
                  </div>
                ))}
              </div>
              
              {filteredProducts.length === 0 && (
                <div className="text-center py-5">
                  <div className="mb-3">
                    <i className="bi bi-search" style={{ fontSize: '3rem', color: '#6c757d' }}></i>
                  </div>
                  <h5>No products found</h5>
                  <p className="text-muted">Try adjusting your filters or search criteria</p>
                  <button 
                    className="btn btn-primary"
                    onClick={() => handleFilterChange({})}
                  >
                    Clear All Filters
                  </button>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Home;
