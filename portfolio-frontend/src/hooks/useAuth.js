/**
 * useAuth Hook
 * Custom hook for authentication state and actions
 */

import { useContext } from 'react';
import { AdminContext } from '../context/AdminContext';

export function useAuth() {
  const context = useContext(AdminContext);
  
  if (!context) {
    throw new Error('useAuth must be used within AdminProvider');
  }
  
  return context;
}
