import { ComponentRegistry } from './utils/componentRegistry.js';
import { ChartComponent } from './components/chartComponent.js';
import { DataTable } from './components/dataTable.js';
import { FormWizard } from './components/formWizard.js';
import { Modal } from './components/modal.js';
import { MetricCard } from './components/metricCard.js';
import { ActivityFeed } from './components/activityFeed.js';
import { QuickActions } from './components/quickActions.js';
import { CampaignManager } from './components/campaignManager.js';
import { CampaignWizard } from './components/campaignWizard.js';

const registry = new ComponentRegistry();

const componentMap = {
  ChartContainer: ChartComponent,
  DataTable: DataTable,
  FormWizard: FormWizard,
  Modal: Modal,
  MetricCard: MetricCard,
  ActivityFeed: ActivityFeed,
  QuickActions: QuickActions,
  CampaignManager: CampaignManager,
  CampaignWizard: CampaignWizard,
};

export function initApp() {
  document.querySelectorAll('[data-component]').forEach((el) => {
    const name = el.dataset.component;
    const Comp = componentMap[name];
    if (Comp) {
      registry.register(new Comp(el));
    }
  });
  registry.init();
}
