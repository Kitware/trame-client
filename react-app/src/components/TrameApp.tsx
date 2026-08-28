// Application shell: waits for the connection + initial state, registers
// trame-template-* tags in the registry so templates can nest each other,
// wires busy/lifecycle/js_call plumbing. React port of vue3-app TrameApp.

import { useEffect, useState } from "react";
import registry from "../registry";
import type { TrameStateEvent } from "../types";
import TrameTemplate from "./TrameTemplate";
import { useTrame } from "../renderer/hooks";

function registerTemplateTag(stateKey: string) {
  const tag = `trame-template-${stateKey.toLowerCase().substring(16)}`
    .replaceAll("_", "-")
    .replaceAll("--", "-");
  if (!registry.has(tag)) {
    const NestedTemplate = (props: Record<string, unknown>) => (
      <TrameTemplate {...props} stateKey={stateKey} />
    );
    NestedTemplate.displayName = tag;
    registry.register(tag, NestedTemplate);
  }
}

export default function TrameApp({ useUrl = false }: { useUrl?: boolean }) {
  const trame = useTrame();
  const [ready, setReady] = useState(false);
  const [refreshTS, setRefreshTS] = useState(1);

  useEffect(() => {
    const subscriptions: (() => void)[] = [];

    const stateListener = ({ type, keys }: TrameStateEvent) => {
      if ((type === "dirty-state" || type === "new-keys") && keys) {
        for (let i = 0; i < keys.length; i++) {
          if (keys[i].startsWith("trame__template_")) {
            registerTemplateTag(keys[i]);
          }
        }
      } else if (type === "refresh") {
        setRefreshTS((v) => v + 1);
      } else if (type === "ready") {
        setReady(true);
        setRefreshTS((v) => v + 1);
      }
    };

    function onBusy(count: number) {
      if (trame.state) {
        trame.state.set("trame__busy", count);
      }
      if (count === 0) {
        trame.state.flush();
      }
    }

    function onConnect() {
      while (subscriptions.length) {
        subscriptions.pop()?.();
      }

      // Client handling
      subscriptions.push(trame.client.onBusyChange(onBusy).unsubscribe);

      // State handling
      trame.state.addListener(stateListener);
      subscriptions.push(() => trame.state.removeListener(stateListener));
      if (trame.state.ready) {
        const keys = trame.state.getAllKeys();
        for (let i = 0; i < keys.length; i++) {
          if (keys[i].startsWith("trame__template_")) {
            registerTemplateTag(keys[i]);
          }
        }
        setReady(true);
      }

      // js_call handling
      function execAction(action: any) {
        const { ref, type } = action;
        const elem = trame.refs[ref];

        if (elem && type === "method") {
          const { method, args } = action;
          elem[method](...args);
        }
        if (elem && type === "property") {
          const { property, value } = action;
          elem[property] = value;
        }
      }
      const wslinkSub = trame.client
        .getRemote()
        .Trame.subscribeToActions(([actions]: any[]) => actions.map(execAction));
      subscriptions.push(() =>
        trame?.client?.getRemote()?.Trame?.unsubscribe(wslinkSub),
      );

      // Attach lifecycles
      trame.client?.getRemote()?.Trame?.lifeCycleUpdate?.("client_connected");
      window.addEventListener("beforeunload", () => {
        trame.client?.getRemote()?.Trame?.lifeCycleUpdate("client_exited");
        trame.client?.getConnection()?.getSession()?.close();
      });
    }

    trame.addConnectListener(onConnect);
    return () => {
      trame.removeConnectListener(onConnect);
      trame.client?.getRemote()?.Trame?.lifeCycleUpdate?.("client_unmounted");
      while (subscriptions.length) {
        subscriptions.pop()?.();
      }
    };
  }, [trame]);

  if (!ready) return null;
  return <TrameTemplate key={refreshTS} useUrl={useUrl} />;
}
