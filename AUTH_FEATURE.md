# Authentication System

## Overview
A complete authentication system has been added to Phone Place Kenya e-commerce platform with sign in, sign up, and user profile management.

## Features

### 1. Sign Up Page (`/signup`)
- **User Registration Form**
  - First Name & Last Name
  - Email Address (required)
  - Phone Number (optional)
  - Password with confirmation
  - Show/Hide password toggle
  - Terms & Conditions checkbox
  
- **Form Validation**
  - Email format validation
  - Password minimum length (6 characters)
  - Password match confirmation
  - Required field validation
  - Terms acceptance required

- **User Experience**
  - Clean, modern design
  - Responsive layout (mobile-friendly)
  - Loading states during submission
  - Error messages with dismissible alerts
  - Link to login page for existing users

### 2. Login Page (`/login`)
- **Login Form**
  - Email address
  - Password with show/hide toggle
  - Remember me checkbox
  - Forgot password link
  
- **Demo Credentials**
  - Email: `demo@example.com`
  - Password: `password123`
  
- **User Experience**
  - Clean, professional design
  - Responsive layout
  - Loading states
  - Error handling
  - Link to signup page

### 3. User Profile Page (`/profile`)
- **Protected Route** (requires authentication)
- **Profile Information Display**
  - User avatar placeholder
  - Full name
  - Email address
  - Phone number
  
- **Account Settings**
  - Edit profile button
  - Change password
  - Notification preferences
  - Delete account option

### 4. Navigation Bar Updates
- **Authenticated State**
  - User dropdown menu with name
  - Profile link
  - My Orders link
  - Logout button
  
- **Unauthenticated State**
  - Sign In button
  - Sign Up button

### 5. Authentication Context
- **Global State Management**
  - User authentication state
  - Login/Logout functionality
  - Signup functionality
  - Persistent sessions (localStorage)
  - Loading states

- **Protected Routes**
  - Automatic redirect to login for protected pages
  - Loading state during auth check

## Files Created

### Pages
1. **client/src/pages/Login.tsx** - Login page component
2. **client/src/pages/Signup.tsx** - Registration page component
3. **client/src/pages/Profile.tsx** - User profile page component

### Context
4. **client/src/context/AuthContext.tsx** - Authentication state management

### Components
5. **client/src/components/ProtectedRoute.tsx** - Route protection wrapper

### Updated Files
6. **client/src/components/Navbar.tsx** - Added user menu and auth buttons
7. **client/src/App.tsx** - Added auth routes and AuthProvider

## How to Use

### For Users

#### Sign Up
1. Click "Sign Up" button in navbar
2. Fill in registration form
3. Accept terms and conditions
4. Click "Create Account"
5. Automatically logged in and redirected to home

#### Login
1. Click "Sign In" button in navbar
2. Enter email and password
3. Optionally check "Remember me"
4. Click "Sign In"
5. Redirected to home page

#### Demo Login
- Use credentials: `demo@example.com` / `password123`

#### Access Profile
1. Click on your name in navbar (when logged in)
2. Select "My Profile" from dropdown
3. View and manage your profile information

#### Logout
1. Click on your name in navbar
2. Select "Logout" from dropdown

### For Developers

#### Check Authentication Status
```typescript
import { useAuth } from '../context/AuthContext';

const MyComponent = () => {
  const { user, isAuthenticated, loading } = useAuth();
  
  if (loading) return <div>Loading...</div>;
  if (!isAuthenticated) return <div>Please login</div>;
  
  return <div>Welcome {user?.firstName}!</div>;
};
```

#### Protect Routes
```typescript
import ProtectedRoute from './components/ProtectedRoute';

<Route 
  path="/protected" 
  element={
    <ProtectedRoute>
      <ProtectedPage />
    </ProtectedRoute>
  } 
/>
```

#### Login Programmatically
```typescript
import { useAuth } from '../context/AuthContext';

const { login } = useAuth();

try {
  await login(email, password);
  // Success - user is logged in
} catch (error) {
  // Handle error
}
```

## Technical Implementation

### Authentication Flow

1. **Sign Up**
   ```
   User fills form → Validation → API call → Store token → Update state → Redirect
   ```

2. **Login**
   ```
   User enters credentials → API call → Store token → Update state → Redirect
   ```

3. **Session Persistence**
   ```
   Page load → Check localStorage → Validate token → Restore user state
   ```

4. **Logout**
   ```
   User clicks logout → Clear localStorage → Clear state → Redirect to home
   ```

### State Management

```typescript
interface User {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
  phone?: string;
}

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  signup: (userData: SignupData) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
}
```

### Storage
- **Token**: Stored in `localStorage` as `authToken`
- **User Data**: Stored in `localStorage` as `user` (JSON string)
- **Auto-clear**: On logout or invalid session

## Security Features

1. **Password Protection**
   - Minimum 6 characters
   - Show/hide toggle for user convenience
   - Confirmation field on signup

2. **Form Validation**
   - Client-side validation before submission
   - Email format validation
   - Required field checks

3. **Protected Routes**
   - Automatic redirect to login
   - Loading states prevent flash of content

4. **Session Management**
   - Token-based authentication
   - Persistent sessions across page reloads
   - Clean logout with storage clearing

## Demo Mode

The authentication system works in demo mode without a backend:

- **Demo Login**: `demo@example.com` / `password123`
- **Demo Signup**: Any valid form data creates a demo account
- **Local Storage**: All data stored locally for demo purposes

## Backend Integration (Future)

To connect to a real backend:

1. Update API endpoints in `AuthContext.tsx`:
   - `/auth/login` - POST endpoint for login
   - `/auth/signup` - POST endpoint for registration
   - `/auth/verify` - GET endpoint to verify token

2. Expected API responses:
   ```typescript
   // Login/Signup response
   {
     token: string;
     user: {
       id: string;
       email: string;
       firstName: string;
       lastName: string;
       phone?: string;
     }
   }
   ```

3. Add token to API headers:
   ```typescript
   api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
   ```

## Styling

- **Design System**: Bootstrap 5
- **Icons**: React Icons (Font Awesome)
- **Color Scheme**: Primary blue theme
- **Responsive**: Mobile-first design
- **Accessibility**: Proper labels and ARIA attributes

## Future Enhancements

1. **Email Verification**
   - Send verification email on signup
   - Verify email before full access

2. **Password Reset**
   - Forgot password functionality
   - Email-based password reset

3. **Social Login**
   - Google OAuth
   - Facebook Login
   - Apple Sign In

4. **Two-Factor Authentication**
   - SMS verification
   - Authenticator app support

5. **Profile Editing**
   - Update user information
   - Change password
   - Upload profile picture

6. **Order History**
   - View past orders
   - Track current orders
   - Reorder functionality

## Testing Checklist

- [x] Sign up form validation works
- [x] Sign up creates new account
- [x] Login with valid credentials works
- [x] Login with invalid credentials shows error
- [x] Demo login works
- [x] User menu shows when logged in
- [x] Profile page accessible when logged in
- [x] Profile page redirects to login when not authenticated
- [x] Logout clears session
- [x] Session persists on page reload
- [x] Responsive design on mobile
- [x] Password show/hide toggle works
- [x] Form error messages display correctly

## Notes

- Authentication is fully functional in demo mode
- All user data is stored locally (no backend required for demo)
- Protected routes automatically redirect to login
- Session persists across page reloads
- Clean, professional UI matching the site design
