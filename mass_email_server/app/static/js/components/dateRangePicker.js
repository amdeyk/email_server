import { BaseComponent } from '../utils/componentRegistry.js';

export class DateRangePicker extends BaseComponent {
  init() {
    this.element.querySelectorAll('button').forEach((btn) => {
      btn.addEventListener('click', () => {
        this.element.querySelectorAll('button').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });
  }
}
