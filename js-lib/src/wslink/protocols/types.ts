export interface WSLinkSession {
  call(
    method: string,
    args?: any[],
    kwargs?: Record<string, any>,
  ): Promise<any>;
  subscribe(topic: string, callback: (...args: any[]) => void): any;
  unsubscribe(subscription: any): any;
}
