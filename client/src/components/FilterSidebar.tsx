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
  const [expandedSections, setExpandedSections] = useState<Set<string>>(new Set(['brand', 'price_tier']));

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
      <div className="filter-sidebar">
        <div className="text-center">
          <div className="spinner-border spinner-border-sm text-primary" role="status"></div>
          <p className="mt-2 mb-0 text-muted">Loading filters...</p>
        </div>
      </div>
    );
  }

  if (!filterOptions) {
    return (
      <div className="filter-sidebar">
        <p className="text-muted">Failed to load filters</p>
      </div>
    );
  }

  return (
    <div className="filter-sidebar">
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h5 className="mb-0">Filters</h5>
        {getActiveFilterCount() > 0 && (
          <button 
            className="btn btn-sm btn-outline-primary"
            onClick={clearAllFilters}
          >
            Clear All ({getActiveFilterCount()})
          </button>
        )}
      </div>
      
      {/* Brands */}
      <div className="filter-section">
        <div 
          className="filter-section-header"
          onClick={() => toggleSection('brand')}
          style={{ cursor: 'pointer' }}
        >
          <h6 className="mb-0 d-flex justify-content-between align-items-center">
            <span>Brands</span>
            <i className={`bi bi-chevron-${expandedSections.has('brand') ? 'up' : 'down'}`}></i>
          </h6>
        </div>
        {expandedSections.has('brand') && (
          <div className="filter-section-content">
            {filterOptions.brands.map(item => (
              <div key={item} className="form-check">
                <input
                  className="form-check-input"
                  type="radio"
                  name="brand"
                  id={`brand-${item}`}
                  checked={activeFilters.brand === item}
                  onChange={() => handleFilterChange('brand', item)}
                />
                <label className="form-check-label" htmlFor={`brand-${item}`}>
                  {item}
                </label>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Price Tiers */}
      <div className="filter-section">
        <div 
          className="filter-section-header"
          onClick={() => toggleSection('price_tier')}
          style={{ cursor: 'pointer' }}
        >
          <h6 className="mb-0 d-flex justify-content-between align-items-center">
            <span>Price Tiers</span>
            <i className={`bi bi-chevron-${expandedSections.has('price_tier') ? 'up' : 'down'}`}></i>
          </h6>
        </div>
        {expandedSections.has('price_tier') && (
          <div className="filter-section-content">
            {filterOptions.price_tiers.map(item => (
              <div key={item} className="form-check">
                <input
                  className="form-check-input"
                  type="radio"
                  name="price_tier"
                  id={`price_tier-${item}`}
                  checked={activeFilters.price_tier === item}
                  onChange={() => handleFilterChange('price_tier', item)}
                />
                <label className="form-check-label" htmlFor={`price_tier-${item}`}>
                  {item}
                </label>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Use Cases */}
      <div className="filter-section">
        <div 
          className="filter-section-header"
          onClick={() => toggleSection('use_case')}
          style={{ cursor: 'pointer' }}
        >
          <h6 className="mb-0 d-flex justify-content-between align-items-center">
            <span>Use Cases</span>
            <i className={`bi bi-chevron-${expandedSections.has('use_case') ? 'up' : 'down'}`}></i>
          </h6>
        </div>
        {expandedSections.has('use_case') && (
          <div className="filter-section-content">
            {filterOptions.use_cases.map(item => (
              <div key={item} className="form-check">
                <input
                  className="form-check-input"
                  type="radio"
                  name="use_case"
                  id={`use_case-${item}`}
                  checked={activeFilters.use_case === item}
                  onChange={() => handleFilterChange('use_case', item)}
                />
                <label className="form-check-label" htmlFor={`use_case-${item}`}>
                  {item}
                </label>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Software Experience */}
      <div className="filter-section">
        <div 
          className="filter-section-header"
          onClick={() => toggleSection('software_experience')}
          style={{ cursor: 'pointer' }}
        >
          <h6 className="mb-0 d-flex justify-content-between align-items-center">
            <span>Software</span>
            <i className={`bi bi-chevron-${expandedSections.has('software_experience') ? 'up' : 'down'}`}></i>
          </h6>
        </div>
        {expandedSections.has('software_experience') && (
          <div className="filter-section-content">
            {filterOptions.software_experiences.map(item => (
              <div key={item} className="form-check">
                <input
                  className="form-check-input"
                  type="radio"
                  name="software_experience"
                  id={`software_experience-${item}`}
                  checked={activeFilters.software_experience === item}
                  onChange={() => handleFilterChange('software_experience', item)}
                />
                <label className="form-check-label" htmlFor={`software_experience-${item}`}>
                  {item}
                </label>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Chipset Categories */}
      <div className="filter-section">
        <div 
          className="filter-section-header"
          onClick={() => toggleSection('chipset_category')}
          style={{ cursor: 'pointer' }}
        >
          <h6 className="mb-0 d-flex justify-content-between align-items-center">
            <span>Processors</span>
            <i className={`bi bi-chevron-${expandedSections.has('chipset_category') ? 'up' : 'down'}`}></i>
          </h6>
        </div>
        {expandedSections.has('chipset_category') && (
          <div className="filter-section-content">
            {filterOptions.chipset_categories.map(item => (
              <div key={item} className="form-check">
                <input
                  className="form-check-input"
                  type="radio"
                  name="chipset_category"
                  id={`chipset_category-${item}`}
                  checked={activeFilters.chipset_category === item}
                  onChange={() => handleFilterChange('chipset_category', item)}
                />
                <label className="form-check-label" htmlFor={`chipset_category-${item}`}>
                  {item}
                </label>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Market Origins */}
      <div className="filter-section">
        <div 
          className="filter-section-header"
          onClick={() => toggleSection('market_origin')}
          style={{ cursor: 'pointer' }}
        >
          <h6 className="mb-0 d-flex justify-content-between align-items-center">
            <span>Market Origin</span>
            <i className={`bi bi-chevron-${expandedSections.has('market_origin') ? 'up' : 'down'}`}></i>
          </h6>
        </div>
        {expandedSections.has('market_origin') && (
          <div className="filter-section-content">
            {filterOptions.market_origins.map(item => (
              <div key={item} className="form-check">
                <input
                  className="form-check-input"
                  type="radio"
                  name="market_origin"
                  id={`market_origin-${item}`}
                  checked={activeFilters.market_origin === item}
                  onChange={() => handleFilterChange('market_origin', item)}
                />
                <label className="form-check-label" htmlFor={`market_origin-${item}`}>
                  {item}
                </label>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Target Demographics */}
      <div className="filter-section">
        <div 
          className="filter-section-header"
          onClick={() => toggleSection('target_demographic')}
          style={{ cursor: 'pointer' }}
        >
          <h6 className="mb-0 d-flex justify-content-between align-items-center">
            <span>Target Users</span>
            <i className={`bi bi-chevron-${expandedSections.has('target_demographic') ? 'up' : 'down'}`}></i>
          </h6>
        </div>
        {expandedSections.has('target_demographic') && (
          <div className="filter-section-content">
            {filterOptions.target_demographics.map(item => (
              <div key={item} className="form-check">
                <input
                  className="form-check-input"
                  type="radio"
                  name="target_demographic"
                  id={`target_demographic-${item}`}
                  checked={activeFilters.target_demographic === item}
                  onChange={() => handleFilterChange('target_demographic', item)}
                />
                <label className="form-check-label" htmlFor={`target_demographic-${item}`}>
                  {item}
                </label>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Price Range */}
      <div className="filter-section">
        <div 
          className="filter-section-header"
          onClick={() => toggleSection('price_range')}
          style={{ cursor: 'pointer' }}
        >
          <h6 className="mb-0 d-flex justify-content-between align-items-center">
            <span>Price Range</span>
            <i className={`bi bi-chevron-${expandedSections.has('price_range') ? 'up' : 'down'}`}></i>
          </h6>
        </div>
        {expandedSections.has('price_range') && (
          <div className="filter-section-content">
            <div className="row g-2 mb-2">
              <div className="col-6">
                <label className="form-label small">Min (KES)</label>
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
                <label className="form-label small">Max (KES)</label>
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
            <small className="text-muted d-block">
              Range: KES {Math.floor(filterOptions.price_range.min / 100).toLocaleString()} - 
              KES {Math.floor(filterOptions.price_range.max / 100).toLocaleString()}
            </small>
          </div>
        )}
      </div>
    </div>
  );
};

export default FilterSidebar;