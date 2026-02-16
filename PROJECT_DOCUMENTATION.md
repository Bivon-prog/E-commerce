# Smart Gadgets - E-Commerce Platform Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Features](#features)
5. [Setup & Installation](#setup--installation)
6. [Database Schema](#database-schema)
7. [API Endpoints](#api-endpoints)
8. [Frontend Architecture](#frontend-architecture)
9. [Authentication System](#authentication-system)
10. [Admin Panel](#admin-panel)
11. [Order Management](#order-management)
12. [Deployment](#deployment)

---

## Project Overview

Smart Gadgets is a modern, full-stack e-commerce platform for smartphones built with React, TypeScript, Django, and DataStax Astra DB (Cassandra). The platform features a responsive design, user authentication, shopping cart, order management, and a comprehensive admin panel.

**Live URLs:**
- Frontend: http://localhost:5173/
- Backend API: http://localhost:8080/api/v1/

---

## Technology Stack

### Frontend
- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **React Router** - Client-side routing
- **Bootstrap 5** - CSS framework
- **React Icons** - Icon library
- **Axios** - HTTP client

### Backend
- **Django 4.2.7** - Web framework
- **Django REST Framework** - API development
- **Python 3.x** - Programming language
- **CORS Headers** - Cross-origin resource sharing

### Database
- **DataStax Astra DB** - Cloud-native Cassandra database
- **AstraPy** - Python client for Astra Data API

### Development Tools
- **npm** - Frontend package manager
- **pip** - Python package manager
- **Git** - Version control

---

## Project Structure

```
E-commerce/
├── client/                          # Frontend React application
│   ├── dist/                        # Production build output
│   ├── node_modules/                # Frontend dependencies
│   ├── public/                      # Static assets
│   ├── src/
│   │   ├── components/              # Reusable React components
│   │   │   ├── AdminRoute.tsx       # Admin route protection
│   │   │   ├── FilterSidebar.tsx    # Product filtering sidebar
│   │   │   ├── HeroBanner.tsx       # Auto-rotating hero banner
│   │   │   ├── Navbar.tsx           # Navigation bar
│   │   │   ├── ProductCard.tsx      # Product display card
│   │   │   └── ProtectedRoute.tsx   # User route protection
│   │   ├── context/                 # React Context providers
│   │   │   ├── AuthContext.tsx      # Authentication state
│   │   │   └── CartContext.tsx      # Shopping cart state
│   │   ├── pages/                   # Page components
│   │   │   ├── Admin/               # Admin panel pages
│   │   │   │   ├── AdminDashboard.tsx  # Product management
│   │   │   │   └── ProductForm.tsx     # Add/Edit products
│   │   │   ├── Checkout.tsx         # Checkout page
│   │   │   ├── Home.tsx             # Homepage with products
│   │   │   ├── Login.tsx            # Login page
│   │   │   ├── Orders.tsx           # Order history
│   │   │   ├── ProductDetails.tsx   # Single product view
│   │   │   ├── Profile.tsx          # User profile
│   │   │   └── Signup.tsx           # Registration page
│   │   ├── services/                # API services
│   │   │   └── api.ts               # Axios configuration
│   │   ├── styles/                  # CSS styles
│   │   │   └── phoneplace.css       # Main stylesheet
│   │   ├── types/                   # TypeScript types
│   │   │   └── index.ts             # Type definitions
│   │   ├── App.tsx                  # Main app component
│   │   ├── main.tsx                 # App entry point
│   │   └── vite-env.d.ts            # Vite type definitions
│   ├── index.html                   # HTML template
│   ├── package.json                 # Frontend dependencies
│   ├── tsconfig.json                # TypeScript config
│   └── vite.config.ts               # Vite configuration
│
├── django-backend/                  # Backend Django application
│   ├── ecommerce/                   # Django project settings
│   │   ├── __init__.py
│   │   ├── asgi.py                  # ASGI configuration
│   │   ├── settings.py              # Django settings
│   │   ├── urls.py                  # Main URL routing
│   │   └── wsgi.py                  # WSGI configuration
│   ├── products/                    # Products app
│   │   ├── management/              # Django management commands
│   │   │   └── commands/
│   │   │       └── init_cassandra.py  # DB initialization
│   │   ├── astra_models.py          # Astra DB product models
│   │   ├── order_models.py          # Astra DB order models
│   │   ├── models.py                # Django models (legacy)
│   │   ├── serializers.py           # DRF serializers
│   │   ├── urls.py                  # API URL routing
│   │   └── views.py                 # API views
│   ├── .env                         # Environment variables
│   ├── .env.astra.example           # Example env file
│   ├── db.sqlite3                   # SQLite database (auth only)
│   ├── manage.py                    # Django management script
│   ├── populate_astra.py            # Database population script
│   ├── requirements.txt             # Python dependencies
│   └── update_single_image.py       # Image update utility
│
├── .gitignore                       # Git ignore rules
├── package.json                     # Root package.json
├── PROJECT_DOCUMENTATION.md         # This file
└── README.md                        # Project README

```

---

## Features

### 1. User Features
- **Product Browsing**: View 231+ smartphones with images, specs, and prices
- **Advanced Filtering**: Filter by brand, price tier, use case, form factor, chipset, etc.
- **Search**: Real-time search by name, brand, or specifications
- **Product Details**: Detailed product information with specifications
- **Shopping Cart**: Add/remove items, adjust quantities
- **Checkout**: Place orders with shipping details
- **Order History**: View past orders with full details
- **User Authentication**: Sign up, login, logout
- **User Profile**: View and manage account information

### 2. Admin Features
- **Product Management**: Full CRUD operations for products
- **Dashboard**: View statistics (total products, stock status, brands)
- **Product Search**: Search products in admin panel
- **Image Management**: Update product images
- **Stock Management**: Mark products as in/out of stock
- **Category Management**: Organize products by categories

### 3. Design Features
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Clean, professional design with gradients and animations
- **Hero Banner**: Auto-rotating banner showcasing premium phones
- **Collapsible Filters**: Organized filter sections
- **Sticky Sidebar**: Filters stay visible while scrolling
- **Loading States**: Spinners and loading indicators
- **Error Handling**: User-friendly error messages

---

## Setup & Installation

### Prerequisites
- Node.js 16+ and npm
- Python 3.8+
- DataStax Astra DB account (free tier available)

### 1. Clone Repository
```bash
git clone https://github.com/Bivon-prog/E-commerce.git
cd E-commerce
```

### 2. Backend Setup

```bash
cd django-backend

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.astra.example .env
# Edit .env with your Astra DB credentials

# Run migrations (for SQLite auth database)
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Start backend server
python manage.py runserver 8080
```

### 3. Frontend Setup

```bash
cd client

# Install dependencies
npm install

# Start development server
npm run dev
```

### 4. Access Application
- Frontend: http://localhost:5173/
- Backend API: http://localhost:8080/api/v1/
- Django Admin: http://localhost:8080/admin/

### Demo Accounts
- **Regular User**: demo@example.com / password123
- **Admin User**: admin@phoneplace.com / admin123

---

## Database Schema

### Products Collection (Astra DB)
```javascript
{
  _id: "uuid",                    // Unique product ID
  name: "string",                 // Product name
  brand: "string",                // Brand name (Samsung, Apple, etc.)
  category: "string",             // Product category
  price: number,                  // Price in cents (KES)
  description: "string",          // Product description
  images: ["url1", "url2"],       // Array of image URLs
  in_stock: boolean,              // Stock availability
  stock_quantity: number,         // Available quantity
  specs: {                        // Product specifications
    ram: "string",                // RAM size
    storage: "string",            // Storage capacity
    processor: "string",          // Processor model
    battery: "string",            // Battery capacity
    display: "string",            // Display specs
    camera: "string",             // Camera specs
    price_tier: "string",         // Budget/Mid-range/Flagship
    use_case: "string",           // Gaming/Photography/Business
    form_factor: "string",        // Standard/Compact/Foldable
    software_experience: "string", // Stock/Custom/Gaming
    chipset_category: "string",   // Snapdragon/MediaTek/Apple
    market_origin: "string",      // Global/China/India
    target_demographic: "string"  // Youth/Professional/Senior
  }
}
```

### Orders Collection (Astra DB)
```javascript
{
  _id: "uuid",                    // Unique order ID
  user_email: "string",           // Customer email
  items: [                        // Ordered items
    {
      id: "string",               // Product ID
      name: "string",             // Product name
      price: number,              // Price per unit (cents)
      quantity: number,           // Quantity ordered
      images: ["url"]             // Product images
    }
  ],
  shipping_details: {             // Shipping information
    name: "string",               // Customer name
    email: "string",              // Contact email
    address: "string"             // Delivery address
  },
  total: number,                  // Total amount (cents)
  status: "string",               // Order status (pending/completed)
  created_at: "ISO date string"   // Order timestamp
}
```

### Users (SQLite - Django Auth)
- Django's built-in User model
- Extended with custom fields in AuthContext
- Stores: email, password (hashed), first_name, last_name, role

---

## API Endpoints

### Base URL: `/api/v1/`

### Products
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/products` | Get all products with optional filters | No |
| POST | `/products` | Create new product | Admin |
| GET | `/products/:id` | Get single product | No |
| PUT | `/products/:id` | Update product | Admin |
| DELETE | `/products/:id` | Delete product | Admin |
| GET | `/filter-options` | Get available filter options | No |

### Orders
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/orders` | Create new order | No |
| GET | `/orders/user?email=` | Get user's orders | Yes |

### Health Check
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/health` | Check API status | No |

### Query Parameters for Products

**Filtering:**
- `brand` - Filter by brand name
- `category` - Filter by category
- `in_stock` - Filter by stock status (true/false)
- `price_tier` - Budget/Mid-range/Flagship
- `use_case` - Gaming/Photography/Business/etc.
- `form_factor` - Standard/Compact/Foldable
- `software_experience` - Stock/Custom/Gaming
- `chipset_category` - Snapdragon/MediaTek/Apple/etc.
- `market_origin` - Global/China/India
- `target_demographic` - Youth/Professional/Senior
- `min_price` - Minimum price (cents)
- `max_price` - Maximum price (cents)

**Example:**
```
GET /api/v1/products?brand=Samsung&price_tier=Flagship&in_stock=true
```

---

## Frontend Architecture

### State Management

#### 1. AuthContext
Manages user authentication state:
- User information (email, name, role)
- Login/logout functions
- Authentication status
- Token management

#### 2. CartContext
Manages shopping cart state:
- Cart items array
- Add/remove items
- Update quantities
- Calculate totals
- Persist to localStorage

### Routing Structure

```
/ (Home)
├── /product/:id (Product Details)
├── /checkout (Checkout)
├── /login (Login)
├── /signup (Signup)
├── /profile (Protected - User Profile)
├── /orders (Protected - Order History)
└── /admin
    ├── /dashboard (Admin - Product Management)
    ├── /products/new (Admin - Add Product)
    └── /products/edit/:id (Admin - Edit Product)
```

### Component Hierarchy

```
App
├── AuthProvider
│   └── CartProvider
│       └── Router
│           ├── Navbar
│           ├── Routes
│           │   ├── Home
│           │   │   ├── HeroBanner
│           │   │   ├── FilterSidebar
│           │   │   └── ProductCard (multiple)
│           │   ├── ProductDetails
│           │   ├── Checkout
│           │   ├── Login
│           │   ├── Signup
│           │   ├── ProtectedRoute
│           │   │   ├── Profile
│           │   │   └── Orders
│           │   └── AdminRoute
│           │       ├── AdminDashboard
│           │       └── ProductForm
│           └── Footer
```

---

## Authentication System

### User Roles
1. **Guest**: Can browse and add to cart
2. **User**: Can place orders and view order history
3. **Admin**: Full access to admin panel and product management

### Authentication Flow

1. **Signup**:
   - User fills registration form
   - Backend creates user account
   - Auto-login after signup
   - JWT token stored in localStorage

2. **Login**:
   - User enters credentials
   - Backend validates and returns JWT token
   - Token stored in localStorage
   - User redirected to homepage

3. **Protected Routes**:
   - ProtectedRoute: Requires authentication
   - AdminRoute: Requires admin role
   - Redirects to login if unauthorized

4. **Logout**:
   - Clear token from localStorage
   - Clear user state
   - Redirect to homepage

### Token Management
- JWT tokens stored in localStorage
- Automatically included in API requests via Axios interceptor
- Token expiration handled with auto-logout

---

## Admin Panel

### Access
- URL: `/admin/dashboard`
- Requires admin role
- Demo admin: admin@phoneplace.com / admin123

### Features

#### 1. Dashboard
- **Statistics Cards**:
  - Total products count
  - In stock count
  - Out of stock count
  - Total brands count
- **Product Table**:
  - Searchable product list
  - Product images
  - Stock status badges
  - Edit/Delete actions
- **Search**: Real-time product search

#### 2. Product Management
- **Add Product**:
  - All product fields
  - Multiple image URLs
  - Specifications
  - Stock status
- **Edit Product**:
  - Update any field
  - Change images
  - Update stock
- **Delete Product**:
  - Confirmation required
  - Permanent deletion

#### 3. Image Management
- Multiple images per product
- Add/remove image fields dynamically
- URL validation
- Image preview in product cards

---

## Order Management

### Order Placement Flow

1. **Add to Cart**:
   - User adds products to cart
   - Cart stored in localStorage
   - Cart badge shows item count

2. **Checkout**:
   - Review cart items
   - Enter shipping details
   - Email pre-filled for logged-in users
   - Calculate total

3. **Place Order**:
   - Submit order to backend
   - Order saved to Astra DB
   - Cart cleared
   - Success message displayed

4. **Order Confirmation**:
   - Order ID generated
   - Email confirmation (future feature)
   - Redirect to order history

### Order History

- **Access**: `/orders` (protected route)
- **Features**:
  - List all user orders
  - Order details (ID, date, total, status)
  - Item breakdown with images
  - Shipping information
  - Sorted by date (newest first)

### Order Status
- **Pending**: Order placed, awaiting processing
- **Processing**: Order being prepared (future)
- **Shipped**: Order dispatched (future)
- **Delivered**: Order completed (future)

---

## Deployment

### Frontend Deployment (Vercel/Netlify)

1. **Build Production**:
```bash
cd client
npm run build
```

2. **Deploy**:
- Upload `dist/` folder
- Set environment variables
- Configure build command: `npm run build`
- Set publish directory: `dist`

### Backend Deployment (Heroku/Railway)

1. **Prepare**:
```bash
# Add Procfile
echo "web: gunicorn ecommerce.wsgi" > Procfile

# Add gunicorn to requirements.txt
pip install gunicorn
pip freeze > requirements.txt
```

2. **Deploy**:
- Connect Git repository
- Set environment variables from `.env`
- Deploy from main branch

### Environment Variables

**Backend (.env)**:
```
USE_MOCK_DB=false
ASTRA_DB_ID=your-db-id
ASTRA_DB_REGION=your-region
ASTRA_DB_KEYSPACE=ecommerce
ASTRA_API_ENDPOINT=your-endpoint
ASTRA_TOKEN=your-token
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
```

**Frontend**:
```
VITE_API_URL=https://your-backend-url.com/api/v1
```

---

## Development Guidelines

### Code Style
- **Frontend**: ESLint + Prettier
- **Backend**: PEP 8 (Python style guide)
- **Naming**: camelCase (JS/TS), snake_case (Python)

### Git Workflow
1. Create feature branch
2. Make changes
3. Test thoroughly
4. Commit with descriptive message
5. Push and create pull request

### Testing
- Manual testing for all features
- Test user flows end-to-end
- Test on multiple devices/browsers
- Verify API responses

### Performance
- Lazy load images
- Minimize bundle size
- Cache API responses
- Optimize database queries

---

## Troubleshooting

### Common Issues

**1. Backend won't start**
- Check Python version (3.8+)
- Verify Astra DB credentials in `.env`
- Run `pip install -r requirements.txt`

**2. Frontend won't start**
- Check Node version (16+)
- Delete `node_modules` and run `npm install`
- Clear browser cache

**3. CORS errors**
- Verify CORS settings in Django settings
- Check API URL in frontend

**4. Images not loading**
- Check image URLs are valid
- Verify CORS on image hosts
- Use image proxy if needed

**5. Orders not saving**
- Check Astra DB connection
- Verify orders collection exists
- Check backend logs for errors

---

## Future Enhancements

### Planned Features
1. **Payment Integration**: Stripe/PayPal/M-Pesa
2. **Email Notifications**: Order confirmations
3. **Product Reviews**: User ratings and reviews
4. **Wishlist**: Save products for later
5. **Advanced Search**: Elasticsearch integration
6. **Inventory Management**: Stock tracking
7. **Shipping Integration**: Real-time shipping rates
8. **Analytics Dashboard**: Sales reports
9. **Multi-currency**: Support multiple currencies
10. **Mobile App**: React Native version

---

## Support & Contact

For issues, questions, or contributions:
- GitHub: https://github.com/Bivon-prog/E-commerce
- Email: support@smartgadgets.com (placeholder)

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- DataStax Astra DB for cloud database
- Bootstrap for UI components
- React community for excellent tools
- Django community for robust framework

---

**Last Updated**: February 16, 2026
**Version**: 1.0.0
**Author**: Bivon
