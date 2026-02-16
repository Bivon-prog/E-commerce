import { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import api from '../../services/api';

const ProductForm = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const isEdit = Boolean(id);

  const [formData, setFormData] = useState({
    name: '',
    brand: '',
    category: 'Smartphone',
    price: '',
    description: '',
    in_stock: true,
    images: [''],
    specs: {
      ram: '',
      storage: '',
      processor: '',
      battery: '',
      display: '',
      camera: '',
    }
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (isEdit) {
      fetchProduct();
    }
  }, [id]);

  const fetchProduct = async () => {
    try {
      const response = await api.get(`/products/${id}`);
      const product = response.data;
      setFormData({
        name: product.name || '',
        brand: product.brand || '',
        category: product.category || 'Smartphone',
        price: (product.price / 100).toString(),
        description: product.description || '',
        in_stock: product.in_stock !== false,
        images: product.images || [''],
        specs: {
          ram: product.specs?.ram || '',
          storage: product.specs?.storage || '',
          processor: product.specs?.processor || '',
          battery: product.specs?.battery || '',
          display: product.specs?.display || '',
          camera: product.specs?.camera || '',
        }
      });
    } catch (error) {
      console.error('Error fetching product:', error);
      setError('Failed to load product');
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value, type } = e.target;
    
    if (name.startsWith('specs.')) {
      const specName = name.split('.')[1];
      setFormData(prev => ({
        ...prev,
        specs: {
          ...prev.specs,
          [specName]: value
        }
      }));
    } else if (type === 'checkbox') {
      const checked = (e.target as HTMLInputElement).checked;
      setFormData(prev => ({ ...prev, [name]: checked }));
    } else {
      setFormData(prev => ({ ...prev, [name]: value }));
    }
  };

  const handleImageChange = (index: number, value: string) => {
    const newImages = [...formData.images];
    newImages[index] = value;
    setFormData(prev => ({ ...prev, images: newImages }));
  };

  const addImageField = () => {
    setFormData(prev => ({ ...prev, images: [...prev.images, ''] }));
  };

  const removeImageField = (index: number) => {
    setFormData(prev => ({
      ...prev,
      images: prev.images.filter((_, i) => i !== index)
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const productData = {
        ...formData,
        price: Math.round(parseFloat(formData.price) * 100),
        images: formData.images.filter(img => img.trim() !== ''),
      };

      if (isEdit) {
        await api.put(`/products/${id}`, productData);
        alert('Product updated successfully!');
      } else {
        await api.post('/products', productData);
        alert('Product created successfully!');
      }
      
      navigate('/admin/dashboard');
    } catch (error: any) {
      console.error('Error saving product:', error);
      setError(error.response?.data?.message || 'Failed to save product');
      setLoading(false);
    }
  };

  return (
    <div className="container mt-4">
      <div className="row">
        <div className="col-md-8 offset-md-2">
          <div className="card">
            <div className="card-header">
              <h4>{isEdit ? 'Edit Product' : 'Add New Product'}</h4>
            </div>
            <div className="card-body">
              {error && (
                <div className="alert alert-danger">{error}</div>
              )}

              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label className="form-label">Product Name *</label>
                  <input
                    type="text"
                    className="form-control"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-3">
                  <label className="form-label">Brand *</label>
                  <input
                    type="text"
                    className="form-control"
                    name="brand"
                    value={formData.brand}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-3">
                  <label className="form-label">Category *</label>
                  <input
                    type="text"
                    className="form-control"
                    name="category"
                    value={formData.category}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-3">
                  <label className="form-label">Price (KES) *</label>
                  <input
                    type="number"
                    className="form-control"
                    name="price"
                    value={formData.price}
                    onChange={handleChange}
                    step="0.01"
                    required
                  />
                </div>

                <div className="mb-3">
                  <label className="form-label">Description *</label>
                  <textarea
                    className="form-control"
                    name="description"
                    value={formData.description}
                    onChange={handleChange}
                    rows={3}
                    required
                  />
                </div>

                <div className="mb-3">
                  <div className="form-check">
                    <input
                      type="checkbox"
                      className="form-check-input"
                      name="in_stock"
                      checked={formData.in_stock}
                      onChange={handleChange}
                    />
                    <label className="form-check-label">In Stock</label>
                  </div>
                </div>

                <div className="mb-3">
                  <label className="form-label">Images</label>
                  {formData.images.map((image, index) => (
                    <div key={index} className="input-group mb-2">
                      <input
                        type="url"
                        className="form-control"
                        placeholder="Image URL"
                        value={image}
                        onChange={(e) => handleImageChange(index, e.target.value)}
                      />
                      {formData.images.length > 1 && (
                        <button
                          type="button"
                          className="btn btn-outline-danger"
                          onClick={() => removeImageField(index)}
                        >
                          Remove
                        </button>
                      )}
                    </div>
                  ))}
                  <button
                    type="button"
                    className="btn btn-sm btn-outline-secondary"
                    onClick={addImageField}
                  >
                    + Add Another Image
                  </button>
                </div>

                <hr />
                <h5>Specifications</h5>

                <div className="row">
                  <div className="col-md-6 mb-3">
                    <label className="form-label">RAM</label>
                    <input
                      type="text"
                      className="form-control"
                      name="specs.ram"
                      value={formData.specs.ram}
                      onChange={handleChange}
                      placeholder="e.g., 8GB"
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <label className="form-label">Storage</label>
                    <input
                      type="text"
                      className="form-control"
                      name="specs.storage"
                      value={formData.specs.storage}
                      onChange={handleChange}
                      placeholder="e.g., 128GB"
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <label className="form-label">Processor</label>
                    <input
                      type="text"
                      className="form-control"
                      name="specs.processor"
                      value={formData.specs.processor}
                      onChange={handleChange}
                      placeholder="e.g., Snapdragon 8 Gen 2"
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <label className="form-label">Battery</label>
                    <input
                      type="text"
                      className="form-control"
                      name="specs.battery"
                      value={formData.specs.battery}
                      onChange={handleChange}
                      placeholder="e.g., 5000mAh"
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <label className="form-label">Display</label>
                    <input
                      type="text"
                      className="form-control"
                      name="specs.display"
                      value={formData.specs.display}
                      onChange={handleChange}
                      placeholder='e.g., 6.7" AMOLED'
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <label className="form-label">Camera</label>
                    <input
                      type="text"
                      className="form-control"
                      name="specs.camera"
                      value={formData.specs.camera}
                      onChange={handleChange}
                      placeholder="e.g., 50MP + 12MP"
                    />
                  </div>
                </div>

                <div className="d-flex gap-2 mt-4">
                  <button
                    type="submit"
                    className="btn btn-primary"
                    disabled={loading}
                  >
                    {loading ? 'Saving...' : (isEdit ? 'Update Product' : 'Create Product')}
                  </button>
                  <button
                    type="button"
                    className="btn btn-secondary"
                    onClick={() => navigate('/admin/dashboard')}
                  >
                    Cancel
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductForm;
