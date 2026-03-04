export interface StateChangeEvent {
  type: "dirty-state" | "new-keys";
  keys: string[];
}

export class State {
  constructor(client: any, oldState?: State);
  loadState(): Promise<void>;
  canDirty(name: string): boolean;
  dirty(...keys: string[]): void;
  set(key: string, value: any): Promise<void>;
  get(): Record<string, any>;
  get(key: string): any;
  getAllKeys(): string[];
  update(obj: Record<string, any>): Promise<void>;
  onChange(fn: (event: StateChangeEvent) => void): () => void;
  watch(keys: string[], fn: (...values: any[]) => void): () => void;
  flush(...keys: (string | string[])[]): Promise<void>;
  delete(): void;
}
