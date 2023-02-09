export function number(value, units = [], steps = 1000, fixed = 2) {
  if (value === null) {
    return null;
  }
  for (let i = 0; i < units.length; i++) {
    const step = Array.isArray(steps) ? steps[i] : steps;
    const unit = units[i];
    if (value > step) {
      value /= step;
    } else {
      return `${value.toFixed(fixed)} ${unit}`;
    }
  }
  return `${value.toFixed(fixed)} ${steps[steps.length - 1]}`;
}

export function bytes(v, fixed = 2) {
  return number(v, ['B', 'KB', 'MB', 'GB', 'TB', 'PB'], 1024, fixed);
}

export default {
  number,
  bytes,
};
