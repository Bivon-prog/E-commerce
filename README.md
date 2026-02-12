# Phone Place Kenya - E-Commerce Platform

A modern, full-stack e-commerce platform for smartphones built with React, TypeScript, Django, and Astra DB.

![Phone Place Kenya](https://img.shields.io/badge/Status-Active-success)
![React](https://img.shields.io/badge/React-18-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)

## 🚀 Features

### Core Features
- **Product Catalog**: 231+ smartphones from top brands (Samsung, Apple, OPPO, vivo, OnePlus, Realme, iQOO, Transsion)
- **Advanced Search**: Real-time search across product names, brands, and specifications
- **Smart Filtering**: Filter by brand, price tier, use case, form factor, and more
- **Product Details**: Comprehensive product information with image galleries
- **Shopping Cart**: Add to cart functionality with persistent storage
- **Responsive Design**: Mobile-first design that works on all devices

### User Features
- **User Authentication**: Sign up and login with secure authentication
- **User Profiles**: Manage personal information
- **Protected Routes**: Secure pages requiring authentication
- **Session Persistence**: Stay logged in across browser sessions

### Technical Features
- **RESTful API**: Django REST Framework backend
- **NoSQL Database**: Astra DB (DataStax Cassandra)
- **Hot Module Replacement**: Instant updates during development
- **TypeScript**: Type-safe frontend code
- **Bootstrap 5**: Modern, responsive UI components

## 📸 Screenshots

### Home Page
Browse through categorized sections of smartphones with beautiful product cards.

### Search & Filter
Powerful search and filtering capabilities to find the perfect phone.

### Product Details
Detailed product information with specifications and image galleries.

### User Authentication
Secure login and signup with form validation.

## 🛠️ Tech Stack

### Frontend
- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **React Router** - Client-side routing
- **Bootstrap 5** - CSS framework
- **React Icons** - Icon library
- **Axios** - HTTP client

### Backend
- **Django 4.2** - Web framework
- **Django REST Framework** - API framework
- **Python 3.x** - Programming language
- **Astra DB** - NoSQL database (DataStax Cassandra)

## 📦 Installation

### Prerequisites
- Node.js 16+ and npm
- Python 3.8+
- Astra DB account (free tier available)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/phone-place-kenya.git
cd phone-place-kenya
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd django-backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create .env file with your Astra DB credentials
# See .env.astra.example for reference

# Run migrations (if using Cassandra)
python manage.py init_cassandra

# Start the server
python manage.py runserver 8080
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd client

# Install dependencies
npm install

# Start development server
npm run dev
```

### 4. Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8080/api/v1

## 🔑 Demo Accounts

### Regular User
- **Email**: demo@example.com
- **Password**: password123

### Admin User
- **Email**: admin@phoneplace.com
- **Password**: admin123

## 📚 API Documentation

### Products Endpoints

```
GET    /api/v1/products              # Get all products
GET    /api/v1/products/:id          # Get single product
POST   /api/v1/products              # Create product (admin)
PUT    /api/v1/products/:id          # Update product (admin)
DELETE /api/v1/products/:id          # Delete product (admin)
GET    /api/v1/filter-options        # Get filter options
```

### Query Parameters
- `brand` - Filter by brand
- `category` - Filter by category
- `price_tier` - Filter by price tier
- `use_case` - Filter by use case
- `form_factor` - Filter by form factor
- `min_price` - Minimum price
- `max_price` - Maximum price

## 🗂️ Project Structure

```
phone-place-kenya/
├── client/                    # Frontend React application
│   ├── src/
│   │   ├── components/       # Reusable components
│   │   ├── pages/           # Page components
│   │   ├── context/         # React context providers
│   │   ├── services/        # API services
│   │   ├── types/           # TypeScript types
│   │   └── styles/          # CSS styles
│   ├── public/              # Static assets
│   └── package.json
│
├── django-backend/           # Backend Django application
│   ├── ecommerce/           # Django project settings
│   ├── products/            # Products app
│   │   ├── models.py        # Database models
│   │   ├── views.py         # API views
│   │   ├── serializers.py   # DRF serializers
│   │   └── urls.py          # URL routing
│   ├── manage.py
│   └── requirements.txt
│
├── README.md
└── .gitignore
```

## 🎯 Key Features Explained

### Search Functionality
Real-time search across:
- Product names
- Brand names
- Descriptions
- Processor specifications
- RAM and storage specs

### Filtering System
Comprehensive filtering by:
- **Brand**: Samsung, Apple, OPPO, vivo, OnePlus, Realme, iQOO, Transsion
- **Price Tier**: Entry-Level, Budget, Mid-Range, Flagship Killer, Premium, Ultra-Premium
- **Use Case**: General, Gaming, Camera & Photography, Battery & Endurance, Business
- **Form Factor**: Candy Bar, Foldable Book, Foldable Clamshell
- **Chipset Category**: Snapdragon, Dimensity, Apple Silicon
- **Market Origin**: American Giants, Korean Powerhouse, Chinese Powerhouses, African Innovators

### Authentication System
- JWT-based authentication (demo mode uses localStorage)
- Protected routes with automatic redirect
- Role-based access control (user/admin)
- Session persistence across page reloads

## 🔧 Configuration

### Astra DB Setup

1. Create a free account at [astra.datastax.com](https://astra.datastax.com)
2. Create a new database
3. Generate an application token
4. Copy credentials to `.env` file:

```env
ASTRA_TOKEN=your_token_here
ASTRA_API_ENDPOINT=your_endpoint_here
ASTRA_KEYSPACE=default_keyspace
```

### Environment Variables

**Backend (.env)**
```env
ASTRA_TOKEN=your_astra_token
ASTRA_API_ENDPOINT=your_astra_endpoint
ASTRA_KEYSPACE=default_keyspace
USE_MOCK_DB=false
```

**Frontend (optional)**
```env
VITE_API_URL=http://localhost:8080/api/v1
```

## 📱 Product Catalog

The platform includes 231+ smartphones from:

- **Samsung** (30+ models): Galaxy S, Z Fold, Z Flip, A series
- **Apple** (20+ models): iPhone 15, 14, 13, SE series
- **OPPO** (50+ models): Find N, Find X, Reno, A, F series
- **vivo** (50+ models): X Fold, X, V, Y, T series
- **OnePlus** (15+ models): Number series, Open, Nord
- **Realme** (40+ models): GT, Number, P, C, Narzo series
- **iQOO** (20+ models): Number, Neo, Z series
- **Transsion** (16+ models): Tecno, Infinix, itel brands

## 🚀 Deployment

### Frontend (Vercel/Netlify)
```bash
cd client
npm run build
# Deploy dist/ folder
```

### Backend (Heroku/Railway)
```bash
cd django-backend
# Add Procfile and runtime.txt
# Deploy using platform CLI
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Your Name** - Initial work

## 🙏 Acknowledgments

- Product data sourced from manufacturer specifications
- Images from Unsplash and manufacturer websites
- Built with love for the Kenyan market

## 📞 Support

For support, email support@phoneplaceKenya.com or open an issue in the repository.

## 🔮 Future Enhancements

- [ ] Payment integration (M-Pesa, Card payments)
- [ ] Order management system
- [ ] Email notifications
- [ ] Product reviews and ratings
- [ ] Wishlist functionality
- [ ] Admin dashboard for product management
- [ ] Inventory tracking
- [ ] Multi-language support
- [ ] PWA support
- [ ] Social media integration

## 📊 Project Status

This project is actively maintained and under development. New features are added regularly.

---

**Made with ❤️ in Kenya**
