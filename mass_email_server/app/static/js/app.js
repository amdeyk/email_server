import { ComponentRegistry } from './utils/componentRegistry.js';

const registry = new ComponentRegistry();

export function initApp() {
  registry.init();
}
