import { BaseComponent } from '../utils/componentRegistry.js';

export class ChartComponent extends BaseComponent {
  init() {
    this.render();
  }

  render() {
    if (!window.Chart) {
      return;
    }
    const ctx = document.createElement('canvas');
    this.element.appendChild(ctx);
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        datasets: [
          {
            label: 'Emails Sent',
            data: [12, 19, 3, 5, 2],
            backgroundColor: 'rgba(54, 162, 235, 0.5)'
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    });
  }
}
