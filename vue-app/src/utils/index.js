import vtk from './vtk';

function download(filename, content, type = 'application/octet-stream') {
  const blob = new Blob([content], { type });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement('a');
  anchor.setAttribute('href', url);
  anchor.setAttribute('download', filename);
  document.body.appendChild(anchor);
  anchor.click();
  document.body.removeChild(anchor);
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function get(path, obj = window) {
  let current = obj;
  const steps = path.split('.');
  for (let i = 0; i < steps.length; i++) {
    current = current[steps[i]];
  }
  return current;
}

function safe(obj) {
  try {
    JSON.stringify(obj);
    return obj;
  } catch (e) {
    // We need to look into object
  }

  const safeObj = {};
  const keys = Object.keys(obj);
  for (let i = 0; i < keys.length; i++) {
    const key = keys[i];
    const value = obj[key];
    if (Array.isArray(value)) {
      safeObj[key] = value.map(safe);
    } else {
      try {
        JSON.stringify(value);
        safeObj[key] = value;
      } catch (e) {
        continue;
      }
    }
  }
  return safeObj;
}

export default {
  download,
  get,
  safe,
  vtk,
};
