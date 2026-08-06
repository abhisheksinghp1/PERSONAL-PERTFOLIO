/**
 * Projects Service
 * Handles all projects-related API calls
 */

import { apiGet, apiPost, apiPatch, apiDelete } from './api';

/**
 * Get all projects
 */
export function getAllProjects() {
  return apiGet('/api/projects/');
}

/**
 * Create a new project (admin)
 */
export function createProject(projectData) {
  return apiPost('/api/projects/', projectData);
}

/**
 * Update a project (admin)
 */
export function updateProject(projectId, projectData) {
  return apiPatch(`/api/projects/${projectId}`, projectData);
}

/**
 * Delete a project (admin)
 */
export function deleteProject(projectId) {
  return apiDelete(`/api/projects/${projectId}`);
}
