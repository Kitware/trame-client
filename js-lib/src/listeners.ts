export class ListenerManager {
  name: string;
  nextId: number;
  listeners: Record<string, (...args: any[]) => void>;

  constructor(name: string) {
    this.name = name;
    this.nextId = 1;
    this.listeners = {};
  }

  on(fn: (...args: any[]) => void): () => void {
    const key = `${this.nextId++}`;
    this.listeners[key] = fn;
    const unsubscribe = () => delete this.listeners[key];
    return unsubscribe;
  }

  emit(...args: any[]): void {
    const listeners = Object.values(this.listeners);
    for (let i = 0; i < listeners.length; i++) {
      try {
        listeners[i](...args);
      } catch (error) {
        console.log(this.name, "on emit", error);
      }
    }
  }

  getListeners(): Array<(...args: any[]) => void> {
    return Object.values(this.listeners);
  }
}

interface Watcher {
  key: string;
  dependencies: string[];
  callback: (...args: any[]) => void;
}

export class WatcherManager {
  nextId: number;
  listeners: Record<string, Watcher>;

  constructor() {
    this.nextId = 1;
    this.listeners = {};
  }

  watch(
    dependencies: string[],
    callback: (...args: any[]) => void,
  ): () => void {
    const key = `${this.nextId++}`;
    this.listeners[key] = {
      key,
      dependencies,
      callback,
    };
    const unsubscribe = () => delete this.listeners[key];
    return unsubscribe;
  }

  notifyWatchers(changedKeys: string[], fullState: Record<string, any>): void {
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

  getWatchers(): Watcher[] {
    return Object.values(this.listeners);
  }
}
