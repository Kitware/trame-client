import { State } from "./state";
import { Decorator } from "./decorators";
import { vtkWSLinkClient } from "@kitware/wslink/src/WsLinkClient";

export interface TrameConnectConfig {
  sessionManagerURL?: string;
  sessionURL?: string;
  application?: string;
  secret?: string;
  wsProxy?: any;
}

export class Trame {
  client: vtkWSLinkClient | null;
  state: State | null;
  config: TrameConnectConfig | null;
  refs: Record<string, any>;

  constructor(wsProxy?: any);
  isConnected(): boolean;
  connect(config?: TrameConnectConfig): Promise<TrameConnectConfig | undefined>;
  disconnect(): void;
  exit(timeout?: number): void;
  reconnect(): Promise<TrameConnectConfig | undefined>;
  onClose(fn: (...args: any[]) => void): () => void;
  onError(fn: (...args: any[]) => void): () => void;
  registerDecorator(decorator: Decorator): void;
  trigger(
    name: string,
    args?: any[],
    kwargs?: Record<string, any>
  ): Promise<any>;
}
