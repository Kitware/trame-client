import type { WSLinkSession } from "./types";

export default (session: WSLinkSession) => ({
  getArray(hash: string, binary = true) {
    return session
      .call("viewport.geometry.array.get", [hash, binary])
      .then((res: any) => {
        if (res.buffer) {
          return new Blob([res]);
        }
        return res;
      });
  },
  getViewState(viewId: string, newSubscription = false) {
    return session.call("viewport.geometry.view.get.state", [
      viewId,
      newSubscription,
    ]);
  },
  addViewObserver(viewId: string) {
    return session.call("viewport.geometry.view.observer.add", [viewId]);
  },
  removeViewObserver(viewId: string) {
    return session.call("viewport.geometry.view.observer.remove", [viewId]);
  },
  subscribeToViewChange(callback: (...args: any[]) => void) {
    return session.subscribe("viewport.geometry.view.subscription", callback);
  },
  unsubscribe(subscription: any) {
    return session.unsubscribe(subscription);
  },
});
