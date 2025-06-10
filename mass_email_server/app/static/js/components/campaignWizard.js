import { BaseComponent } from '../utils/componentRegistry.js';

export class CampaignWizard extends BaseComponent {
  init() {
    this.currentStep = 1;
    this.bindEvents();
  }

  bindEvents() {
    const nextBtn = this.element.querySelector('.btn--primary');
    const prevBtn = this.element.querySelector('.btn--secondary');
    if (nextBtn) nextBtn.addEventListener('click', () => this.next());
    if (prevBtn) prevBtn.addEventListener('click', () => this.prev());
  }

  showStep(step) {
    this.element.querySelectorAll('.step-panel').forEach((p) => p.classList.remove('active'));
    const panel = this.element.querySelector(`[data-step="${step}"]`);
    if (panel) panel.classList.add('active');
  }

  next() {
    this.currentStep = Math.min(5, this.currentStep + 1);
    this.showStep(this.currentStep);
  }

  prev() {
    this.currentStep = Math.max(1, this.currentStep - 1);
    this.showStep(this.currentStep);
  }
}
