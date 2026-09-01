import type { WSLinkSession } from "./types";

export default (session: WSLinkSession) => ({
  lifeCycleUpdate(phaseName: string) {
    return session.call("trame.lifecycle.update", [phaseName]);
  },
  sendError(message: string) {
    return session.call("trame.error.client", [message]);
  },
  getState() {
    return session.call("trame.state.get", []);
  },
  trigger(name: string, args: any[] = [], kwargs: Record<string, any> = {}) {
    return session.call("trame.trigger", [name, args, kwargs]);
  },
  updateState(changes: Array<{ key: string; value: any }>) {
    return session.call("trame.state.update", [changes]);
  },
  subscribeToStateUpdate(callback: (...args: any[]) => void) {
    return session.subscribe("trame.state.topic", callback);
  },
  subscribeToActions(callback: (...args: any[]) => void) {
    return session.subscribe("trame.actions.topic", callback);
  },
  unsubscribe(subscription: any) {
    return session.unsubscribe(subscription);
  },
});
