export class ComponentRegistry {
  constructor() {
    this.components = [];
  }

  register(component) {
    this.components.push(component);
  }

  init() {
    this.components.forEach((c) => c.init && c.init());
  }
}

export class BaseComponent {
  constructor(element, options = {}) {
    this.element = element;
    this.options = options;
  }

  init() {}
  render() {}
  destroy() {}
  bindEvents() {}
}
