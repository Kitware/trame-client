const VTK_EVENT_KEYS = [
  'type',
  'key',
  'keyCode',
  'controlKey',
  'altKey',
  'shiftKey',
  'position',
  'spinX',
  'spinY',
  'pixelX',
  'pixelY',
];

function event(e) {
  const result = {};
  for (let i = 0; i < VTK_EVENT_KEYS.length; i++) {
    const key = VTK_EVENT_KEYS[i];
    if (key in e) {
      result[key] = e[key];
    }
  }
  return result;
}

export default {
  event,
};
