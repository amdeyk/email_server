import { BaseComponent } from '../utils/componentRegistry.js';

export class CampaignManager extends BaseComponent {
  init() {
    this.render();
  }

  render() {
    this.element.querySelector('.data-table').innerHTML = '<thead><tr><th>Name</th><th>Status</th></tr></thead><tbody></tbody>';
  }
}
