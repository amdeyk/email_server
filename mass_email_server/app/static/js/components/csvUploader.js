import { BaseComponent } from '../utils/componentRegistry.js';

export class CSVUploader extends BaseComponent {
  init() {
    this.bindEvents();
  }

  bindEvents() {
    const input = this.element.querySelector('.upload-input');
    this.element.addEventListener('click', () => input.click());
  }
}
