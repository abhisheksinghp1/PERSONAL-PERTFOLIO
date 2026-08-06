/**
 * Authentication Service
 * Handles all auth-related API calls
 */

import { apiPost, apiGet } from './api';

/**
 * Login with username and password
 */
export async function login(username, password) {
  const data = await apiPost('/api/auth/login', { username, password });
  if (data.access_token) {
    localStorage.setItem('token', data.access_token);
  }
  return data;
}

/**
 * Logout - clear local token
 */
export function logout() {
  localStorage.removeItem('token');
}

/**
 * Get current admin info
 */
export function getCurrentAdmin() {
  return apiGet('/api/auth/me');
}

/**
 * Request OTP for password change
 */
export function requestOTP() {
  return apiPost('/api/auth/request-otp', {});
}

/**
 * Change password with OTP
 */
export function changePassword(otp, newPassword) {
  return apiPost('/api/auth/change-password', {
    otp,
    new_password: newPassword,
  });
}

/**
 * Request password reset OTP (no auth required)
 */
export function forgotPasswordSend(method = 'email') {
  return apiPost('/api/auth/forgot-password/send', { method });
}

/**
 * Reset password with OTP (no auth required)
 */
export function forgotPasswordReset(otp, newPassword) {
  return apiPost('/api/auth/forgot-password/reset', {
    otp,
    new_password: newPassword,
  });
}

/**
 * Check if user is authenticated
 */
export function isAuthenticated() {
  return !!localStorage.getItem('token');
}

/**
 * Get stored token
 */
export function getToken() {
  return localStorage.getItem('token');
}
