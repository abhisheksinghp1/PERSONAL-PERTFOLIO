/**
 * Contact Service
 * Handles contact form and contact links API calls
 */

import { apiGet, apiPost, apiPut, apiPatch, apiDelete } from './api';

/**
 * Send contact form message
 */
export function sendMessage(messageData) {
  return apiPost('/api/contact/send', messageData);
}

/**
 * Get all contact messages (admin)
 */
export function getAllMessages() {
  return apiGet('/api/contact/messages');
}

/**
 * Get all contact links
 */
export function getAllContactLinks() {
  return apiGet('/api/contact-links/');
}

/**
 * Create contact link (admin)
 */
export function createContactLink(linkData) {
  return apiPost('/api/contact-links/', linkData);
}

/**
 * Update contact link (admin)
 */
export function updateContactLink(linkId, linkData) {
  return apiPut(`/api/contact-links/${linkId}`, linkData);
}

/**
 * Delete contact link (admin)
 */
export function deleteContactLink(linkId) {
  return apiDelete(`/api/contact-links/${linkId}`);
}

/**
 * Reorder contact links (admin)
 */
export function reorderContactLinks(items) {
  return apiPatch('/api/contact-links/reorder', items);
}
