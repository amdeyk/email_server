import { BaseComponent } from '../utils/componentRegistry.js';

export class QuickActions extends BaseComponent {
  init() {
    this.render();
  }

  render() {
    this.element.innerHTML = `
      <button class="btn" onclick="location.href='/campaigns/new'">New Campaign</button>
    `;
  }
}
