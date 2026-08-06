/**
 * Validation Utilities
 * Common validation functions
 */

/**
 * Validate email format
 */
export function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Validate password strength
 * @param {string} password
 * @param {object} options - { minLength, requireUppercase, requireLowercase, requireNumbers, requireSpecial }
 */
export function isValidPassword(password, options = {}) {
  const {
    minLength = 6,
    requireUppercase = false,
    requireLowercase = false,
    requireNumbers = false,
    requireSpecial = false,
  } = options;

  if (password.length < minLength) {
    return { valid: false, message: `Password must be at least ${minLength} characters` };
  }

  if (requireUppercase && !/[A-Z]/.test(password)) {
    return { valid: false, message: 'Password must contain an uppercase letter' };
  }

  if (requireLowercase && !/[a-z]/.test(password)) {
    return { valid: false, message: 'Password must contain a lowercase letter' };
  }

  if (requireNumbers && !/\d/.test(password)) {
    return { valid: false, message: 'Password must contain a number' };
  }

  if (requireSpecial && !/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
    return { valid: false, message: 'Password must contain a special character' };
  }

  return { valid: true, message: 'Password is valid' };
}

/**
 * Validate URL format
 */
export function isValidURL(url) {
  try {
    new URL(url);
    return true;
  } catch {
    return false;
  }
}

/**
 * Validate phone number (basic)
 */
export function isValidPhone(phone) {
  const phoneRegex = /^[\d\s\-\+\(\)]+$/;
  return phoneRegex.test(phone) && phone.replace(/\D/g, '').length >= 10;
}

/**
 * Sanitize HTML to prevent XSS
 */
export function sanitizeHTML(html) {
  const div = document.createElement('div');
  div.textContent = html;
  return div.innerHTML;
}

/**
 * Validate file type
 */
export function isValidFileType(file, allowedTypes) {
  return allowedTypes.includes(file.type);
}

/**
 * Validate file size
 */
export function isValidFileSize(file, maxSizeMB) {
  const maxSizeBytes = maxSizeMB * 1024 * 1024;
  return file.size <= maxSizeBytes;
}

/**
 * Validate required fields in an object
 */
export function validateRequiredFields(obj, requiredFields) {
  const missing = [];
  
  for (const field of requiredFields) {
    if (!obj[field] || (typeof obj[field] === 'string' && obj[field].trim() === '')) {
      missing.push(field);
    }
  }
  
  if (missing.length > 0) {
    return {
      valid: false,
      missing,
      message: `Missing required fields: ${missing.join(', ')}`,
    };
  }
  
  return { valid: true, missing: [], message: 'All required fields present' };
}
