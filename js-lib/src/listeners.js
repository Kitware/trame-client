export class ListenerManager {
  constructor(name) {
    this.name = name;
    this.nextId = 1;
    this.listeners = {};
  }

  on(fn) {
    const key = `${this.nextId++}`;
    this.listeners[key] = fn;
    const unsubscribe = () => delete this.listeners[key];
    return unsubscribe;
  }

  emit(...args) {
    const listeners = Object.values(this.listeners);
    for (let i = 0; i < listeners.length; i++) {
      try {
        listeners[i](...args);
      } catch (error) {
        console.log(this.name, "on emit", error);
      }
    }
  }

  getListeners() {
    return Object.values(this.listeners);
  }
}

export class WatcherManager {
  constructor() {
    this.nextId = 1;
    this.listeners = {};
  }

  watch(dependencies, callback) {
    const key = `${this.nextId++}`;
    this.listeners[key] = {
      key,
      dependencies,
      callback,
    };
    const unsubscribe = () => delete this.listeners[key];
    return unsubscribe;
  }

  notifyWatchers(changedKeys, fullState) {
    const watchers = Object.values(this.listeners);
    const keys = new Set(changedKeys);

    for (let i = 0; i < watchers.length; i++) {
      const { dependencies, callback } = watchers[i];
      if (keys.intersection(new Set(dependencies)).size) {
        const args = dependencies.map((v) => fullState[v]);
        try {
          callback(...args);
        } catch (e) {
          console.error(`Watcher error with dependencies: ${dependencies}`, e);
        }
      }
    }
  }

  getWatchers() {
    return Object.values(this.listeners);
  }
}
