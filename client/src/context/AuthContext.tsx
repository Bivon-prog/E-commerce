import React, { createContext, useContext, useState, useEffect } from 'react';
import api from '../services/api';

interface User {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
  phone?: string;
  role?: 'user' | 'admin';
}

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  signup: (userData: SignupData) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
}

interface SignupData {
  firstName: string;
  lastName: string;
  email: string;
  phone?: string;
  password: string;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  // Check if user is logged in on mount
  useEffect(() => {
    const checkAuth = async () => {
      const token = localStorage.getItem('authToken');
      const userData = localStorage.getItem('user');
      
      if (token && userData) {
        try {
          setUser(JSON.parse(userData));
          // Set default authorization header
          api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        } catch (error) {
          console.error('Failed to parse user data:', error);
          localStorage.removeItem('authToken');
          localStorage.removeItem('user');
        }
      }
      setLoading(false);
    };

    checkAuth();
  }, []);

  const login = async (email: string, password: string) => {
    try {
      // For demo purposes, we'll simulate a login
      // In production, this would call your backend API
      const response = await api.post('/auth/login', { email, password });
      
      const { token, user: userData } = response.data;
      
      // Store token and user data
      localStorage.setItem('authToken', token);
      localStorage.setItem('user', JSON.stringify(userData));
      
      // Set authorization header
      api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      
      setUser(userData);
    } catch (error) {
      // If backend not ready, use demo login
      if (email === 'demo@example.com' && password === 'password123') {
        const demoUser = {
          id: 'demo-user-1',
          email: 'demo@example.com',
          firstName: 'Demo',
          lastName: 'User',
          phone: '+254 700 000 000',
          role: 'user' as const
        };
        
        const demoToken = 'demo-token-' + Date.now();
        
        localStorage.setItem('authToken', demoToken);
        localStorage.setItem('user', JSON.stringify(demoUser));
        api.defaults.headers.common['Authorization'] = `Bearer ${demoToken}`;
        
        setUser(demoUser);
      } else if (email === 'admin@phoneplace.com' && password === 'admin123') {
        // Admin demo account
        const adminUser = {
          id: 'admin-user-1',
          email: 'admin@phoneplace.com',
          firstName: 'Admin',
          lastName: 'User',
          phone: '+254 700 000 001',
          role: 'admin' as const
        };
        
        const adminToken = 'admin-token-' + Date.now();
        
        localStorage.setItem('authToken', adminToken);
        localStorage.setItem('user', JSON.stringify(adminUser));
        api.defaults.headers.common['Authorization'] = `Bearer ${adminToken}`;
        
        setUser(adminUser);
      } else {
        throw error;
      }
    }
  };

  const signup = async (userData: SignupData) => {
    try {
      // For demo purposes, we'll simulate a signup
      // In production, this would call your backend API
      const response = await api.post('/auth/signup', userData);
      
      const { token, user: newUser } = response.data;
      
      // Store token and user data
      localStorage.setItem('authToken', token);
      localStorage.setItem('user', JSON.stringify(newUser));
      
      // Set authorization header
      api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      
      setUser(newUser);
    } catch (error) {
      // If backend not ready, use demo signup
      const newUser = {
        id: 'user-' + Date.now(),
        email: userData.email,
        firstName: userData.firstName,
        lastName: userData.lastName,
        phone: userData.phone
      };
      
      const token = 'token-' + Date.now();
      
      localStorage.setItem('authToken', token);
      localStorage.setItem('user', JSON.stringify(newUser));
      api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      
      setUser(newUser);
    }
  };

  const logout = () => {
    // Clear storage
    localStorage.removeItem('authToken');
    localStorage.removeItem('user');
    
    // Clear authorization header
    delete api.defaults.headers.common['Authorization'];
    
    setUser(null);
  };

  const value = {
    user,
    loading,
    login,
    signup,
    logout,
    isAuthenticated: !!user
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
