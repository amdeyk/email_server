import { BaseComponent } from '../utils/componentRegistry.js';

export class MetricCard extends BaseComponent {
  init() {
    this.render();
  }

  render() {
    this.element.innerHTML = `
      <div class="metric">
        <h3>Total Campaigns</h3>
        <span class="metric-value" id="total-campaigns">0</span>
      </div>
      <div class="metric">
        <h3>Emails Sent Today</h3>
        <span class="metric-value" id="emails-sent">0</span>
      </div>
      <div class="metric">
        <h3>Delivery Rate</h3>
        <span class="metric-value" id="delivery-rate">0%</span>
      </div>`;
  }
}
