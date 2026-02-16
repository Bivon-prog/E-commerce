import React, { useEffect, useState } from 'react';
import api from '../services/api';
import { Product } from '../types';
import ProductCard from '../components/ProductCard';
import FilterSidebar from '../components/FilterSidebar';
import HeroBanner from '../components/HeroBanner';

interface HomeProps {
  searchHandlerRef?: React.MutableRefObject<((query: string) => void) | null>;
}

const Home: React.FC<HomeProps> = ({ searchHandlerRef }) => {
  const [products, setProducts] = useState<Product[]>([]);
  const [filteredProducts, setFilteredProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeFilters, setActiveFilters] = useState<any>({});
  const [showFilters, setShowFilters] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');

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
      
      // Apply search filter if search query exists
      if (searchQuery.trim()) {
        const filtered = response.data.filter((product: Product) => {
          const query = searchQuery.toLowerCase();
          return (
            product.name.toLowerCase().includes(query) ||
            product.brand.toLowerCase().includes(query) ||
            product.description?.toLowerCase().includes(query) ||
            product.specs?.processor?.toLowerCase().includes(query) ||
            product.specs?.ram?.toLowerCase().includes(query) ||
            product.specs?.storage?.toLowerCase().includes(query)
          );
        });
        setFilteredProducts(filtered);
      } else {
        setFilteredProducts(response.data);
      }
      
      setLoading(false);
    } catch (err) {
      console.error('Failed to fetch products:', err);
      setLoading(false);
    }
  };

  // Handle search from navbar
  const handleSearch = (query: string) => {
    setSearchQuery(query);
    
    if (query.trim()) {
      const filtered = products.filter((product: Product) => {
        const searchTerm = query.toLowerCase();
        return (
          product.name.toLowerCase().includes(searchTerm) ||
          product.brand.toLowerCase().includes(searchTerm) ||
          product.description?.toLowerCase().includes(searchTerm) ||
          product.specs?.processor?.toLowerCase().includes(searchTerm) ||
          product.specs?.ram?.toLowerCase().includes(searchTerm) ||
          product.specs?.storage?.toLowerCase().includes(searchTerm)
        );
      });
      setFilteredProducts(filtered);
    } else {
      setFilteredProducts(products);
    }
  };

  // Initial load
  useEffect(() => {
    fetchProducts();
  }, []);

  // Register search handler
  useEffect(() => {
    if (searchHandlerRef) {
      searchHandlerRef.current = handleSearch;
    }
    return () => {
      if (searchHandlerRef) {
        searchHandlerRef.current = null;
      }
    };
  }, [searchHandlerRef, products]);

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

      {/* Hero Banner - Only show when no filters/search active */}
      {Object.keys(activeFilters).length === 0 && !searchQuery.trim() && (
        <div className="mb-4">
          <HeroBanner products={products} />
        </div>
      )}

      <div className="row">
        {/* Filter Sidebar */}
        <div className={`col-lg-3 ${showFilters ? 'd-block' : 'd-none d-lg-block'}`}>
          {showFilters && (
            <button 
              className="btn btn-close position-absolute top-0 end-0 d-lg-none"
              onClick={() => setShowFilters(false)}
              style={{ zIndex: 1051 }}
            ></button>
          )}
          <FilterSidebar 
            onFilterChange={handleFilterChange}
            activeFilters={activeFilters}
          />
        </div>

        {/* Main Content */}
        <div className="col-lg-9">
          {/* Header */}
          <div className="site-header rounded mb-4">
            <div className="d-flex justify-content-between align-items-center">
              <div>
                <h2 className="fw-bold mb-1">Smart Gadgets</h2>
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
          {(Object.keys(activeFilters).length > 0 || searchQuery.trim()) && (
            <div className="mb-4">
              <div className="d-flex flex-wrap gap-2 align-items-center">
                <span className="text-muted small fw-medium">Active filters:</span>
                {searchQuery.trim() && (
                  <span className="badge bg-info fs-6">
                    Search: {searchQuery}
                    <button 
                      className="btn-close btn-close-white ms-2" 
                      style={{ fontSize: '0.6rem' }}
                      onClick={() => handleSearch('')}
                    ></button>
                  </span>
                )}
                {Object.entries(activeFilters).map(([key, value]) => (
                  <span key={key} className="badge bg-primary fs-6">
                    {key.replace('_', ' ')}: {String(value)}
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
                  onClick={() => {
                    handleFilterChange({});
                    handleSearch('');
                  }}
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
              {searchQuery.trim() && ` matching "${searchQuery}"`}
              {Object.keys(activeFilters).length > 0 && !searchQuery.trim() && ' matching your filters'}
            </p>
          </div>

          {/* Category Sections (Phone Place Kenya Style) */}
          {Object.keys(activeFilters).length === 0 && !searchQuery.trim() ? (
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
            // Show filtered/search results
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
                  <p className="text-muted">
                    {searchQuery.trim() 
                      ? `No results for "${searchQuery}". Try different keywords.`
                      : 'Try adjusting your filters or search criteria'}
                  </p>
                  <button 
                    className="btn btn-primary"
                    onClick={() => {
                      handleFilterChange({});
                      handleSearch('');
                    }}
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
