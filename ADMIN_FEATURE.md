# Admin Panel Feature

## Overview
A complete admin panel has been added to Phone Place Kenya e-commerce platform, allowing administrators to manage products with full CRUD (Create, Read, Update, Delete) operations.

## Features

### 1. Admin Dashboard (`/admin/dashboard`)
- **Statistics Overview**
  - Total Products count
  - In Stock products count
  - Out of Stock products count
  - Total Inventory Value (KES)
  
- **Product Management Table**
  - View all products in a sortable table
  - Product image thumbnails
  - Product name and description
  - Brand badges
  - Price display
  - Stock status badges
  - Category information
  - Quick action buttons (Edit/Delete)

- **Quick Actions**
  - Add New Product button
  - Edit product (inline)
  - Delete product with confirmation

### 2. Add Product Page (`/admin/products/new`)
- **Basic Information**
  - Product Name (required)
  - Brand (required)
  - Category dropdown (Smartphones, Tablets, Accessories)
  - Price in KES (required)
  - Description textarea (required)
  - In Stock checkbox

- **Product Images**
  - Multiple image URL inputs
  - Add/Remove image fields dynamically
  - At least one image required
  - Image preview support

- **Specifications**
  - RAM
  - Storage
  - Display
  - Processor
  - Camera
  - Battery
  - Price Tier dropdown (Entry-Level to Ultra-Premium)
  - Use Case dropdown (General, Gaming, Camera, etc.)
  - Form Factor dropdown (Candy Bar, Foldable, etc.)

- **Form Validation**
  - Required field validation
  - Price validation (must be > 0)
  - Image URL validation
  - Real-time error messages

### 3. Edit Product Page (`/admin/products/edit/:id`)
- Same form as Add Product
- Pre-populated with existing product data
- Update button instead of Create button
- Loads product data on mount

### 4. Admin Authentication
- **Admin Role System**
  - User role: 'user' or 'admin'
  - Admin-only route protection
  - Access denied page for non-admins

- **Admin Demo Account**
  - Email: `admin@phoneplace.com`
  - Password: `admin123`
  - Full admin privileges

### 5. Admin Navigation
- **Admin Badge** in user dropdown
- **Admin Dashboard** link in dropdown menu
- Only visible to admin users
- Quick access from anywhere in the app

## Files Created

### Admin Pages
1. **client/src/pages/Admin/AdminDashboard.tsx** - Main admin dashboard
2. **client/src/pages/Admin/ProductForm.tsx** - Add/Edit product form

### Components
3. **client/src/components/AdminRoute.tsx** - Admin route protection

### Updated Files
4. **client/src/context/AuthContext.tsx** - Added admin role support
5. **client/src/components/Navbar.tsx** - Added admin menu link
6. **client/src/App.tsx** - Added admin routes
7. **client/src/pages/Login.tsx** - Added admin credentials display

## How to Use

### For Admins

#### Login as Admin
1. Go to login page
2. Use admin credentials:
   - Email: `admin@phoneplace.com`
   - Password: `admin123`
3. Click "Sign In"
4. You'll see "Admin" badge in your profile dropdown

#### Access Admin Dashboard
1. Click on your name in navbar
2. Select "Admin Dashboard"
3. Or navigate directly to `/admin/dashboard`

#### Add New Product
1. From Admin Dashboard, click "Add New Product"
2. Fill in all required fields:
   - Product Name
   - Brand
   - Category
   - Price (in KES)
   - Description
   - At least one image URL
3. Optionally fill in specifications
4. Check "In Stock" if available
5. Click "Create Product"
6. Product will be added to database

#### Edit Product
1. From Admin Dashboard, find the product
2. Click the Edit button (pencil icon)
3. Modify any fields
4. Click "Update Product"
5. Changes will be saved

#### Delete Product
1. From Admin Dashboard, find the product
2. Click the Delete button (trash icon)
3. Confirm deletion in popup
4. Product will be removed from database

### For Developers

#### Check Admin Status
```typescript
import { useAuth } from '../context/AuthContext';

const MyComponent = () => {
  const { user } = useAuth();
  
  if (user?.role === 'admin') {
    return <div>Admin content</div>;
  }
  
  return <div>Regular content</div>;
};
```

#### Protect Admin Routes
```typescript
import AdminRoute from './components/AdminRoute';

<Route 
  path="/admin/something" 
  element={
    <AdminRoute>
      <AdminPage />
    </AdminRoute>
  } 
/>
```

## API Endpoints Used

### Products API
- `GET /api/v1/products` - Get all products
- `GET /api/v1/products/:id` - Get single product
- `POST /api/v1/products` - Create new product
- `PUT /api/v1/products/:id` - Update product
- `DELETE /api/v1/products/:id` - Delete product

### Request/Response Format

#### Create Product (POST /products)
```json
{
  "name": "iPhone 15 Pro Max",
  "brand": "Apple",
  "category": "Smartphones",
  "price": 18999900,  // Price in cents
  "description": "Latest flagship from Apple",
  "in_stock": true,
  "images": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg"
  ],
  "specs": {
    "ram": "8GB",
    "storage": "256GB/512GB/1TB",
    "display": "6.7\" Super Retina XDR",
    "processor": "A17 Pro",
    "camera": "48MP Triple",
    "battery": "4422mAh",
    "price_tier": "Ultra-Premium",
    "use_case": "Camera & Photography",
    "form_factor": "Candy Bar"
  }
}
```

#### Update Product (PUT /products/:id)
Same format as create

#### Delete Product (DELETE /products/:id)
No body required, returns success message

## Security Features

### 1. Role-Based Access Control
- Only users with `role: 'admin'` can access admin pages
- Non-admin users see "Access Denied" message
- Automatic redirect to login for unauthenticated users

### 2. Route Protection
- AdminRoute component wraps all admin pages
- Checks authentication status
- Checks admin role
- Shows loading state during auth check

### 3. Confirmation Dialogs
- Delete operations require confirmation
- Prevents accidental deletions
- Shows product name in confirmation

### 4. Form Validation
- Client-side validation before submission
- Required field checks
- Data type validation
- Error messages for invalid data

## UI/UX Features

### 1. Dashboard Statistics
- Color-coded stat cards
- Icons for visual clarity
- Real-time calculations
- Responsive grid layout

### 2. Product Table
- Sortable columns
- Image thumbnails with fallback
- Status badges (In Stock/Out of Stock)
- Hover effects
- Responsive design

### 3. Product Form
- Clean, organized layout
- Grouped sections (Basic Info, Images, Specs)
- Dynamic image fields (add/remove)
- Dropdown selects for categories
- Loading states during submission
- Success/Error alerts

### 4. Navigation
- Admin badge in dropdown
- Quick access to dashboard
- Breadcrumb-style navigation
- Cancel buttons to go back

## Styling

- **Design System**: Bootstrap 5
- **Icons**: React Icons (Font Awesome)
- **Color Scheme**: 
  - Primary: Blue (#0d6efd)
  - Success: Green (In Stock)
  - Danger: Red (Out of Stock, Delete)
  - Warning: Yellow (Total Value)
- **Cards**: Shadow-sm for depth
- **Tables**: Hover effects, striped rows
- **Forms**: Proper spacing, clear labels

## Demo Accounts

### Admin Account
- **Email**: `admin@phoneplace.com`
- **Password**: `admin123`
- **Role**: admin
- **Permissions**: Full CRUD access

### Regular User Account
- **Email**: `demo@example.com`
- **Password**: `password123`
- **Role**: user
- **Permissions**: No admin access

## Testing Checklist

- [x] Admin can login with admin credentials
- [x] Admin sees "Admin" badge in dropdown
- [x] Admin can access dashboard
- [x] Dashboard shows correct statistics
- [x] Dashboard displays all products
- [x] Admin can add new product
- [x] Form validation works correctly
- [x] Admin can edit existing product
- [x] Edit form pre-populates with data
- [x] Admin can delete product
- [x] Delete confirmation dialog appears
- [x] Non-admin users cannot access admin pages
- [x] Access denied message shows for non-admins
- [x] Unauthenticated users redirect to login
- [x] Image fields can be added/removed
- [x] All form fields save correctly
- [x] Success/Error messages display properly

## Future Enhancements

### 1. Bulk Operations
- Select multiple products
- Bulk delete
- Bulk update (price, stock status)
- Export to CSV

### 2. Advanced Filtering
- Filter by brand
- Filter by price range
- Filter by stock status
- Search products in dashboard

### 3. Image Upload
- Direct image upload (not just URLs)
- Image compression
- Multiple image upload
- Drag and drop interface

### 4. Product Analytics
- View count tracking
- Sales statistics
- Popular products
- Revenue charts

### 5. Inventory Management
- Stock quantity tracking
- Low stock alerts
- Reorder notifications
- Stock history

### 6. Order Management
- View all orders
- Update order status
- Customer management
- Order analytics

### 7. User Management
- View all users
- Promote/demote admins
- Ban/unban users
- User activity logs

### 8. Settings
- Site configuration
- Email templates
- Payment settings
- Shipping options

## Troubleshooting

### Issue: Cannot access admin dashboard
**Solution**: Make sure you're logged in with admin credentials (`admin@phoneplace.com` / `admin123`)

### Issue: Product not saving
**Solution**: Check all required fields are filled and image URLs are valid

### Issue: Delete not working
**Solution**: Ensure backend API is running and product ID is correct

### Issue: Images not displaying
**Solution**: Verify image URLs are accessible and use HTTPS

### Issue: Form validation errors
**Solution**: Check that price is greater than 0 and at least one image URL is provided

## Notes

- Admin panel is fully functional with demo backend
- All CRUD operations work with the Django backend
- Product data persists in Astra database
- Admin role is stored in localStorage for demo mode
- In production, implement proper JWT-based role verification

## Backend Integration

The admin panel integrates with existing Django REST API:
- Uses same `/api/v1/products` endpoints
- No additional backend changes needed
- Works with Astra DB, Cassandra, or mock database
- Supports all existing product fields and specs

---

**Status**: ✅ Fully Functional  
**Access**: Admin credentials required  
**Ready**: Yes - Login as admin to start managing products!
