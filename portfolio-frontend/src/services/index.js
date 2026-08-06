/**
 * Service Layer - Central export
 * Import all services from here for convenience
 */

export * from './api';
export * from './authService';
export * from './contactService';
export * from './projectsService';
export * from './skillsService';

// Re-export commonly used functions for convenience
export { API_BASE_URL } from './api';
