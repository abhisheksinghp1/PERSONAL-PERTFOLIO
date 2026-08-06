/**
 * Application Constants
 * Centralized configuration values
 */

// API Configuration
export const API_TIMEOUT = 30000; // 30 seconds

// File Upload Constraints
export const MAX_FILE_SIZE = {
  IMAGE: 5 * 1024 * 1024, // 5 MB
  VIDEO: 200 * 1024 * 1024, // 200 MB
  DOCUMENT: 50 * 1024 * 1024, // 50 MB
  PDF: 20 * 1024 * 1024, // 20 MB
};

export const ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/webp', 'image/gif'];
export const ALLOWED_VIDEO_TYPES = ['video/mp4', 'video/webm', 'video/ogg'];
export const ALLOWED_DOCUMENT_TYPES = [
  'application/pdf',
  'application/msword',
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  'application/vnd.ms-excel',
  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  'text/plain',
];

// Local Storage Keys
export const STORAGE_KEYS = {
  TOKEN: 'token',
  THEME: 'theme',
  USER: 'user',
  PREFERENCES: 'preferences',
};

// Toast Configuration
export const TOAST_DURATION = {
  SUCCESS: 3000,
  ERROR: 5000,
  INFO: 3000,
  WARNING: 4000,
};

// Pagination
export const DEFAULT_PAGE_SIZE = 10;

// Debounce Delays
export const DEBOUNCE_DELAY = {
  SEARCH: 300,
  INPUT: 500,
  RESIZE: 150,
};

// Animation Durations (ms)
export const ANIMATION_DURATION = {
  FAST: 150,
  NORMAL: 300,
  SLOW: 500,
};

// Breakpoints (pixels)
export const BREAKPOINTS = {
  MOBILE: 480,
  TABLET: 768,
  DESKTOP: 1024,
  WIDE: 1280,
};

// Social Media Links (example)
export const SOCIAL_LINKS = {
  GITHUB: 'https://github.com',
  LINKEDIN: 'https://linkedin.com',
  TWITTER: 'https://twitter.com',
  EMAIL: 'contact@example.com',
};

// Validation Rules
export const PASSWORD_MIN_LENGTH = 6;
export const OTP_LENGTH = 6;

// Route Paths
export const ROUTES = {
  HOME: '/',
  ABOUT: '/about',
  SKILLS: '/skills',
  PROJECTS: '/projects',
  CONTACT: '/contact',
  VAULT: '/vault',
  RESUME: '/resume',
  CERTIFICATIONS: '/certifications',
  ADMIN: '/admin',
};
