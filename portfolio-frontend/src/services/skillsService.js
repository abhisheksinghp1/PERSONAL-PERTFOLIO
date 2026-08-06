/**
 * Skills Service
 * Handles all skills-related API calls
 */

import { apiGet, apiPost, apiPut, apiDelete, apiUpload } from './api';

/**
 * Get all skill categories with skills
 */
export function getAllSkills() {
  return apiGet('/api/skills/');
}

/**
 * Create a new skill category (admin)
 */
export function createCategory(categoryData) {
  return apiPost('/api/skills/categories', categoryData);
}

/**
 * Update a skill category (admin)
 */
export function updateCategory(categoryId, categoryData) {
  return apiPut(`/api/skills/categories/${categoryId}`, categoryData);
}

/**
 * Delete a skill category (admin)
 */
export function deleteCategory(categoryId) {
  return apiDelete(`/api/skills/categories/${categoryId}`);
}

/**
 * Create a new skill in a category (admin)
 */
export function createSkill(categoryId, skillData) {
  return apiPost(`/api/skills/categories/${categoryId}/skills`, skillData);
}

/**
 * Update a skill (admin)
 */
export function updateSkill(skillId, skillData) {
  return apiPut(`/api/skills/${skillId}`, skillData);
}

/**
 * Delete a skill (admin)
 */
export function deleteSkill(skillId) {
  return apiDelete(`/api/skills/${skillId}`);
}

/**
 * Upload skill image (admin)
 */
export function uploadSkillImage(skillId, file) {
  const formData = new FormData();
  formData.append('file', file);
  return apiUpload(`/api/skills/${skillId}/image`, formData);
}

/**
 * Remove skill image (admin)
 */
export function removeSkillImage(skillId) {
  return apiDelete(`/api/skills/${skillId}/image`);
}
