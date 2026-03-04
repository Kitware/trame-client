export class ListenerManager {
  constructor(name: string);
  on(fn: (...args: any[]) => void): () => void;
  emit(...args: any[]): void;
  getListeners(): Array<(...args: any[]) => void>;
}

export class WatcherManager {
  constructor();
  watch(
    dependencies: string[],
    callback: (...args: any[]) => void
  ): () => void;
  notifyWatchers(changedKeys: string[], fullState: Record<string, any>): void;
  getWatchers(): Array<{
    key: string;
    dependencies: string[];
    callback: (...args: any[]) => void;
  }>;
}
