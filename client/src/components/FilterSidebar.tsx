import React, { useState, useEffect } from 'react';
import { FilterOptions } from '../types';
import api from '../services/api';

interface FilterSidebarProps {
  onFilterChange: (filters: any) => void;
  activeFilters: any;
}

const FilterSidebar: React.FC<FilterSidebarProps> = ({ onFilterChange, activeFilters }) => {
  const [filterOptions, setFilterOptions] = useState<FilterOptions | null>(null);
  const [loading, setLoading] = useState(true);
  const [expandedSections, setExpandedSections] = useState<Set<string>>(new Set(['brands', 'price_tiers']));

  useEffect(() => {
    api.get('/filter-options')
      .then(res => {
        setFilterOptions(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Failed to load filter options:', err);
        setLoading(false);
      });
  }, []);

  const toggleSection = (section: string) => {
    const newExpanded = new Set(expandedSections);
    if (newExpanded.has(section)) {
      newExpanded.delete(section);
    } else {
      newExpanded.add(section);
    }
    setExpandedSections(newExpanded);
  };

  const handleFilterChange = (filterType: string, value: string) => {
    const newFilters = { ...activeFilters };
    if (newFilters[filterType] === value) {
      delete newFilters[filterType];
    } else {
      newFilters[filterType] = value;
    }
    onFilterChange(newFilters);
  };

  const handlePriceRangeChange = (min: number, max: number) => {
    const newFilters = { ...activeFilters };
    if (min > (filterOptions?.price_range.min || 0)) {
      newFilters.min_price = min;
    } else {
      delete newFilters.min_price;
    }
    
    if (max < (filterOptions?.price_range.max || 0)) {
      newFilters.max_price = max;
    } else {
      delete newFilters.max_price;
    }
    
    onFilterChange(newFilters);
  };

  const clearAllFilters = () => {
    onFilterChange({});
  };

  const getActiveFilterCount = () => {
    return Object.keys(activeFilters).length;
  };

  if (loading) {
    return (
      <div className="card">
        <div className="card-body">
          <div className="text-center">
            <div className="spinner-border spinner-border-sm" role="status"></div>
            <p className="mt-2 mb-0">Loading filters...</p>
          </div>
        </div>
      </div>
    );
  }

  if (!filterOptions) {
    return (
      <div className="card">
        <div className="card-body">
          <p className="text-muted">Failed to load filters</p>
        </div>
      </div>
    );
  }

  const FilterSection: React.FC<{ title: string; items: string[]; filterKey: string; icon: string }> = 
    ({ title, items, filterKey, icon }) => {
      const isExpanded = expandedSections.has(filterKey);
      
      return (
        <div className="mb-3">
          <button
            className="btn btn-link p-0 text-start w-100 text-decoration-none d-flex justify-content-between align-items-center"
            onClick={() => toggleSection(filterKey)}
          >
            <span className="fw-semibold">
              {icon} {title}
              {activeFilters[filterKey] && <span className="badge bg-primary ms-2">1</span>}
            </span>
            <i className={`bi bi-chevron-${isExpanded ? 'up' : 'down'}`}></i>
          </button>
          
          {isExpanded && (
            <div className="mt-2">
              {items.map(item => (
                <div key={item} className="form-check">
                  <input
                    className="form-check-input"
                    type="radio"
                    name={filterKey}
                    id={`${filterKey}-${item}`}
                    checked={activeFilters[filterKey] === item}
                    onChange={() => handleFilterChange(filterKey, item)}
                  />
                  <label className="form-check-label small" htmlFor={`${filterKey}-${item}`}>
                    {item}
                  </label>
                </div>
              ))}
            </div>
          )}
        </div>
      );
    };

  return (
    <div className="card sticky-top" style={{ top: '20px' }}>
      <div className="card-header d-flex justify-content-between align-items-center">
        <h6 className="mb-0">🔍 Filters</h6>
        {getActiveFilterCount() > 0 && (
          <button 
            className="btn btn-sm btn-outline-secondary"
            onClick={clearAllFilters}
          >
            Clear All ({getActiveFilterCount()})
          </button>
        )}
      </div>
      
      <div className="card-body" style={{ maxHeight: '70vh', overflowY: 'auto' }}>
        {/* Brands */}
        <FilterSection
          title="Brands"
          items={filterOptions.brands}
          filterKey="brand"
          icon="🏷️"
        />

        {/* Price Tiers */}
        <FilterSection
          title="Price Tiers"
          items={filterOptions.price_tiers}
          filterKey="price_tier"
          icon="💰"
        />

        {/* Use Cases */}
        <FilterSection
          title="Use Cases"
          items={filterOptions.use_cases}
          filterKey="use_case"
          icon="🎯"
        />

        {/* Software Experience */}
        <FilterSection
          title="Software"
          items={filterOptions.software_experiences}
          filterKey="software_experience"
          icon="💻"
        />

        {/* Chipset Categories */}
        <FilterSection
          title="Processors"
          items={filterOptions.chipset_categories}
          filterKey="chipset_category"
          icon="🔧"
        />

        {/* Market Origins */}
        <FilterSection
          title="Market Origin"
          items={filterOptions.market_origins}
          filterKey="market_origin"
          icon="🌍"
        />

        {/* Target Demographics */}
        <FilterSection
          title="Target Users"
          items={filterOptions.target_demographics}
          filterKey="target_demographic"
          icon="👥"
        />

        {/* Price Range */}
        <div className="mb-3">
          <button
            className="btn btn-link p-0 text-start w-100 text-decoration-none d-flex justify-content-between align-items-center"
            onClick={() => toggleSection('price_range')}
          >
            <span className="fw-semibold">
              💵 Price Range
              {(activeFilters.min_price || activeFilters.max_price) && 
                <span className="badge bg-primary ms-2">1</span>
              }
            </span>
            <i className={`bi bi-chevron-${expandedSections.has('price_range') ? 'up' : 'down'}`}></i>
          </button>
          
          {expandedSections.has('price_range') && (
            <div className="mt-2">
              <div className="row g-2">
                <div className="col-6">
                  <label className="form-label small">Min Price</label>
                  <input
                    type="number"
                    className="form-control form-control-sm"
                    placeholder={`${Math.floor(filterOptions.price_range.min / 100).toLocaleString()}`}
                    value={activeFilters.min_price ? Math.floor(activeFilters.min_price / 100) : ''}
                    onChange={(e) => {
                      const value = parseInt(e.target.value) * 100;
                      if (!isNaN(value)) {
                        handlePriceRangeChange(value, activeFilters.max_price || filterOptions.price_range.max);
                      }
                    }}
                  />
                </div>
                <div className="col-6">
                  <label className="form-label small">Max Price</label>
                  <input
                    type="number"
                    className="form-control form-control-sm"
                    placeholder={`${Math.floor(filterOptions.price_range.max / 100).toLocaleString()}`}
                    value={activeFilters.max_price ? Math.floor(activeFilters.max_price / 100) : ''}
                    onChange={(e) => {
                      const value = parseInt(e.target.value) * 100;
                      if (!isNaN(value)) {
                        handlePriceRangeChange(activeFilters.min_price || filterOptions.price_range.min, value);
                      }
                    }}
                  />
                </div>
              </div>
              <small className="text-muted">
                Range: KES {Math.floor(filterOptions.price_range.min / 100).toLocaleString()} - 
                KES {Math.floor(filterOptions.price_range.max / 100).toLocaleString()}
              </small>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default FilterSidebar;