import { BaseComponent } from '../utils/componentRegistry.js';

export class ActivityFeed extends BaseComponent {
  init() {
    this.render();
  }

  render() {
    this.element.innerHTML = `<ul class="activity-list"></ul>`;
  }
}
