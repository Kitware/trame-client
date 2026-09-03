// Instantiated once per `trame` instance (trame.refs is per-connection: a
// fresh Trame() on reconnect gets a fresh refs map).
export function createRefRegistry(trame) {
  const cache = new Map();
  return function getRefCallback(name) {
    if (!cache.has(name)) {
      cache.set(name, (el) => {
        if (el) trame.refs[name] = el;
        else {
          delete trame.refs[name];
          cache.delete(name);
        }
      });
    }
    return cache.get(name);
  };
}
