import { BaseComponent } from '../utils/componentRegistry.js';

export class TemplateEditor extends BaseComponent {
  init() {
    if (window.grapesjs) {
      this.editor = window.grapesjs.init({
        container: this.element,
        height: '600px',
        fromElement: true,
      });
    }
  }
}
