class MessageChannelWebSocket {
  constructor(port) {
    console.log("create MessageChannelWebSocket");
    this._channel_port = port;
    this.onmessage = null;
    this.onclose = null;
    this.onerror = null;

    // Listen to channel messages
    this._channel_port.onmessage = (e) => {
      if (!this.onmessage) return;
      const { a, b, t } = e.data;

      if (a === "s") {
        this.onmessage({ data: b || t });
        return;
      }
      if (a === "c" && this.onclose) {
        this.onclose(e.data.c);
        return;
      }
      if (a === "e" && this.onerror) {
        this.onerror(e.data.e);
        return;
      }
    };
  }

  set onopen(callback) {
    // Auto open but allow current listeners registration to complete before triggering
    setTimeout(callback, 0);
  }

  send(data) {
    console.log("send", data);
    if (data.buffer) {
      // may need a copy
      if (data.buffer.byteLength !== data.length) {
        const tmp = new Uint8Array(data.length);
        tmp.set(data);
        self._channel_port.postMessage(
          {
            a: "s",
            b: tmp.buffer,
          },
          [tmp.buffer],
        );
        return;
      }
      self._channel_port.postMessage(
        {
          a: "s",
          b: data.buffer,
        },
        [data.buffer],
      );
      return;
    }
    self._channel_port.postMessage({
      a: "s",
      t: data,
    });
  }

  close() {
    self._channel_port.postMessage({ a: "c", c: "Closing from client" });
    self._channel_port.close();
  }
}

export function createMessageChannelWSFactory(port) {
  return () => new MessageChannelWebSocket(port);
}
